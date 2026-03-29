from demand_agent import DemandAgent
from inventory_agent import InventoryAgent
from vendor_agent import VendorAgent
from transport_agent import TransportAgent

demand_agent = DemandAgent()
inventory_agent = InventoryAgent()
vendor_agent = VendorAgent()
transport_agent = TransportAgent()

sample_input = {
    "store_id": 1,
    "product_id": 101,
    "price": 100,
    "promotion": 1,
    "sales_store": 50,
    "day_of_week": 2,
    "month": 5,
    "week_of_year": 20,
    "sales_7day_avg": 45,
    "sales_30day_avg": 48,
    "demand_growth": 0.1,
    "log_freight_cost": 3.2,
    "vendor_score": 0.8,
    "inventory_proxy": 20
}

prediction = demand_agent.predict(sample_input).item()
sample_input["sales"] = prediction
decision = inventory_agent.decide(sample_input)

vendors = [
    {"name": "Vendor A", "customer_rating": 4.5, "freight_cost": 100, "delivery_time": 3},
    {"name": "Vendor B", "customer_rating": 4.0, "freight_cost": 90, "delivery_time": 5},
    {"name": "Vendor C", "customer_rating": 4.8, "freight_cost": 110, "delivery_time": 2}
]

transport_options = [
    {"mode": "Truck", "cost": 50, "delivery_time": 3},
    {"mode": "Air", "cost": 120, "delivery_time": 1},
    {"mode": "Ship", "cost": 40, "delivery_time": 7}
]

best_vendor = vendor_agent.select_vendor(vendors)
best_transport = transport_agent.select_transport(transport_options)

print(f"Predicted Demand: {prediction:.2f}")
print(f"Required Stock: {decision['required_stock']:.2f}")
print(f"Order Quantity: {decision['order_quantity']:.2f}")
print(f"Best Vendor: {best_vendor['name']}")
print(f"Best Transport Mode: {best_transport['mode']}")