import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import joblib
import os

def run_pipeline():
    print("🚀 Starting Data Pipeline...")
    
    # 1. Load Data
    if not os.path.exists('price_data.csv'):
        print("❌ Error: price_data.csv not found.")
        return False
        
    df = pd.read_csv('price_data.csv')
    
    # 2. Data Cleaning (Matching your notebook logic)
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)
    df.set_index('date', inplace=True)
    df = df.interpolate(method='time')
    
    print("🧹 Data Cleaned & Interpolated.")

    # 3. Model Training (SARIMA)
    # Using the optimized parameters from your analysis
    # order=(1,1,1), seasonal_order=(1,1,1,12)
    model = SARIMAX(df['avg_monthly_price'], 
                    order=(1, 1, 1), 
                    seasonal_order=(1, 1, 1, 12),
                    enforce_stationarity=False,
                    enforce_invertibility=False)
    
    results = model.fit(disp=False)
    print("🧠 Model Training Complete.")

    # 4. Save Model & Metadata
    if not os.path.exists('models'):
        os.makedirs('models')
        
    joblib.dump(results, 'models/model.pkl')
    
    metadata = {
        'last_date': df.index[-1].strftime('%Y-%m-%d'),
        'last_price': float(df['avg_monthly_price'].iloc[-1])
    }
    joblib.dump(metadata, 'models/metadata.pkl')
    print("💾 Model and Metadata saved successfully.")
    return True

if __name__ == "__main__":
    run_pipeline()
