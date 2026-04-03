# SupplyMind

SupplyMind is an intelligent multi-agent supply chain optimization system that leverages machine learning models to make data-driven decisions across demand forecasting, inventory management, vendor selection, and transportation logistics.

## Features

- **Demand Forecasting Agent**: Predicts product demand using trained ML models based on historical data, pricing, promotions, and seasonal factors.
- **Inventory Management Agent**: Determines optimal stock levels and order quantities to minimize costs while meeting demand.
- **Vendor Selection Agent**: Evaluates and selects the best vendors based on ratings, costs, and delivery times.
- **Transport Optimization Agent**: Chooses the most efficient transportation options considering cost and delivery time.
- **MCP Orchestration**: Uses Model Context Protocol (MCP) for agent coordination and state management.
- **Event Streaming**: Real-time event publishing and subscription for dashboard and analytics integration.

## Architecture

The system consists of:
- **Agents**: Specialized AI agents for each supply chain domain
- **MCP Components**: Context store, state manager, message bus for agent communication
- **Streaming Layer**: Event broker for real-time data flow
- **ML Models**: Pre-trained models for predictions and decisions

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd supplymind-original-project
   ```

2. Install dependencies:
   ```bash
   pip install pandas scikit-learn xgboost joblib
   ```

3. Ensure model files are present (best_model.pkl, best_inventory_model.pkl, etc.)

## Usage

### Running the Main Orchestration

Execute the main MCP orchestration script:

```bash
python run_mcp.py
```

This will:
- Generate a demand forecast
- Make inventory decisions
- Select optimal vendor and transport
- Display the complete supply chain optimization results

### Training Models

Train the ML models using the provided scripts:

```bash
python run_training.py
```

Individual model training:
- `python train_model.py` - Demand forecasting model
- `python train_inventory_model.py` - Inventory optimization model
- `python train_vendor_model.py` - Vendor selection model
- `python train_transport_model.py` - Transport optimization model

### Testing Agents

Run agent tests:

```bash
python test_agent.py
```

### Evaluation

Evaluate model performance:

```bash
python evaluate.py
```

## Data

The system uses `supplymind_unified_dataset.csv` containing historical supply chain data for training and evaluation.

## Project Structure

```
├── demand_agent.py          # Demand forecasting agent
├── inventory_agent.py       # Inventory management agent
├── vendor_agent.py          # Vendor selection agent
├── transport_agent.py       # Transport optimization agent
├── run_mcp.py               # Main orchestration script
├── run_training.py          # Model training orchestration
├── train_*.py               # Individual model training scripts
├── evaluate.py              # Model evaluation
├── test_agent.py            # Agent testing
├── mcp/                     # Model Context Protocol components
│   ├── agent_registry.py
│   ├── context_store.py
│   ├── message_bus.py
│   ├── schemas.py
│   └── state_manager.py
├── streaming/               # Event streaming components
│   ├── event_broker.py
│   └── __init__.py
├── ML part/                 # Additional ML components
└── supplymind_unified_dataset.csv  # Training dataset
```

## Requirements

- Python 3.7+
- pandas
- scikit-learn
- xgboost
- joblib

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

