from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import joblib
import json
import os
import pandas as pd
from datetime import datetime, timedelta

app = FastAPI(title="AgriPrice Forecast API")

# Setup directories
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# History management
HISTORY_FILE = "history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(entry):
    history = load_history()
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

# Load model and metadata
def get_model():
    results = joblib.load('models/model.pkl')
    metadata = joblib.load('models/metadata.pkl')
    return results, metadata

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    history = load_history()
    return templates.TemplateResponse(
        request=request, name="index.html", context={"history": history}
    )

@app.post("/predict")
async def predict_price(request: Request, horizon: int = Form(12)):
    results, metadata = get_model()
    
    # Forecast
    forecast = results.get_forecast(steps=horizon)
    mean_forecast = forecast.summary_frame()["mean"]
    
    # Process dates for forecast
    last_date = datetime.strptime(metadata['last_date'], "%Y-%m-%d")
    forecast_dates = [(last_date + timedelta(days=30*i)).strftime("%Y-%m-%d") for i in range(1, horizon + 1)]
    
    # New prediction entry
    prediction_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "horizon": horizon,
        "forecast": [{"date": d, "price": round(p, 2)} for d, p in zip(forecast_dates, mean_forecast)]
    }
    
    save_history(prediction_data)
    
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "history": load_history(),
            "latest_forecast": prediction_data
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
