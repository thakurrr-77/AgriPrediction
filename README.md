# 🌾 Way2Agribusiness Price Forecasting Dashboard

A production-ready price forecasting platform for agribusiness, leveraging a SARIMA (Seasonal Autoregressive Integrated Moving Average) time-series model.

## 🚀 Overview
This project provides a complete pipeline from raw historical price data to an interactive, real-time dashboard. It handles missing value interpolation, outlier analysis, model training, and provides a premium web interface for viewing forecasts and history.

## 🛠️ Tech Stack
- **Core Modeling**: Python, Statsmodels (SARIMA), Pandas
- **Backend API**: FastAPI
- **Frontend**: Jinja2, CSS3 (Glassmorphism), Chart.js
- **Environment**: Pip (requirements.txt)

## 📁 Project Structure
- `forecasting_model.ipynb`: Exploration, cleaning, and model validation.
- `pipeline.py`: Automated "Clean -> Train -> Save" production pipeline.
- `main.py`: FastAPI server logic and history management.
- `templates/`: HTML dashboard with interactive visualizations.
- `static/`: Modern glassmorphism UI styles.
- `models/`: Serialized model and metadata artifacts.
- `history.json`: Persistent prediction session logs.

## ⚡ Quick Start

### 1. Installation
Install all required modules:
```powershell
pip install -r requirements.txt
```

### 2. Update & Retrain (New Data)
Whenever you update `price_data.csv`, run the pipeline to refresh the model:
```powershell
python pipeline.py
```

### 3. Launch Dashboard
Start the production server:
```powershell
python main.py
```
Visit **[http://127.0.0.1:8000](http://127.0.0.1:8000)** to view your agribusiness trends!

## 📊 Dashboard Features
- **Forecast Window**: Dynamically input how many months (1-24) you want to predict.
- **Interactive Charts**: Responsive time-series data visualization powered by Chart.js.
- **Session History**: Track past predictions and identify market highs/lows.
- **Premium UI**: Dark mode glassmorphism design with a state-of-the-art "Outfit" typography.

---
**Developed for Way2Agribusiness Forecasting Challenge**
