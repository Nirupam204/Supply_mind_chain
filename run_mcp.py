from demand_agent import DemandAgent
from inventory_agent import InventoryAgent
from vendor_agent import VendorAgent
from transport_agent import TransportAgent

from mcp.context_store import ContextStore
from mcp.state_manager import StateManager
from mcp.message_bus import MessageBus
from mcp.schemas import Decision

from streaming.event_broker import EventBroker

demand_agent = DemandAgent()
inventory_agent = InventoryAgent()
vendor_agent = VendorAgent()
transport_agent = TransportAgent()

context = ContextStore()
state_manager = StateManager()
bus = MessageBus()
broker = EventBroker()

demand_input = {
    "store_id": 1,
    "product_id": 101,
    "price": 100,
    "promotion": 1,
    "sales_store": 50,
    "day_of_week": 2,
    "month": 5,
    "week_of_year": 20
}

def dashboard_consumer(event):
    print(f"\n[DASHBOARD STREAM] {event['topic']} received")

def analytics_consumer(event):
    print(f"[ANALYTICS STREAM] event_id: {event['event_id']}")

broker.subscribe("demand_updates", dashboard_consumer)
broker.subscribe("inventory_updates", analytics_consumer)

forecast = demand_agent.predict(demand_input)
forecast = round(float(forecast), 2)

context.set("demand_forecast", forecast)

broker.publish(
    topic="demand_updates",
    producer="demand_agent",
    data={"forecast": forecast}
)


inventory_input = {
    "sales": forecast,
    "sales_7day_avg": round(forecast * 0.9, 2),
    "sales_30day_avg": round(forecast * 0.85, 2),
    "demand_growth": 0.12,
    "inventory_proxy": 20
}

inventory_result = inventory_agent.decide(inventory_input)
context.set("inventory_decision", inventory_result)

broker.publish(
    topic="inventory_updates",
    producer="inventory_agent",
    data=inventory_result
)

vendors = [
    {
        "vendor_id": 1,
        "customer_rating": 4.7,
        "freight_cost": 120,
        "delivery_time": 2
    },
    {
        "vendor_id": 2,
        "customer_rating": 4.2,
        "freight_cost": 100,
        "delivery_time": 3
    }
]

vendor_result = vendor_agent.select_vendor(vendors)
context.set("vendor_decision", vendor_result)


transport_options = [
    {
        "transport_id": 1,
        "cost": 60,
        "delivery_time": 5
    },
    {
        "transport_id": 2,
        "cost": 80,
        "delivery_time": 3
    }
]

transport_result = transport_agent.select_transport(transport_options)
context.set("transport_decision", transport_result)


decision = Decision(
    agent="final_decision_engine",
    action="Supply chain optimization completed",
    confidence=0.97
)

state_manager.update_state(decision.__dict__)

bus.publish({
    "event": "SUPPLY_CHAIN_UPDATED",
    "data": context.get_all()
})


full_context = context.get_all()
latest_state = state_manager.get_latest()
events = bus.consume()


print("\n" + "=" * 60)
print("SUPPLYMIND - MCP ORCHESTRATION OUTPUT")
print("=" * 60)

print(f"\nDemand Forecast        : {float(full_context['demand_forecast']):.2f}")

inventory = full_context["inventory_decision"]
print(f"Required Stock         : {float(inventory['required_stock']):.2f}")
print(f"Order Quantity         : {float(inventory['order_quantity']):.2f}")

vendor = full_context["vendor_decision"]
print(f"\nSelected Vendor ID     : {int(vendor['vendor_id'])}")
print(f"Vendor Rating          : {float(vendor['customer_rating']):.1f}")
print(f"Vendor Cost            : {float(vendor['freight_cost']):.2f}")
print(f"Vendor Delivery Time   : {float(vendor['delivery_time']):.1f} days")

transport = full_context["transport_decision"]
print(f"\nTransport ID           : {int(transport['transport_id'])}")
print(f"Transport Cost         : {float(transport['freight_cost']):.2f}")
print(f"Delivery ETA           : {float(transport['delivery_time']):.1f} hours")

print(f"\nFinal Decision         : {latest_state['action']}")
print(f"Confidence Score       : {float(latest_state['confidence']):.2f}")

print(f"\nEvents Published       : {len(events)}")
print("=" * 60)