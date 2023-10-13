from fastapi import FastAPI, HTTPException
from joblib import load
import pandas as pd
import numpy as np
from fastapi.responses import JSONResponse
from starlette.responses import JSONResponse



app = FastAPI()

# Define the full path to the joblib file, including the directory structure
#file_path_predictive = 'C:/Users/saumy/OneDrive/Desktop/Semester-3/AdvMLA/AdvMLA_AT2/models/predictive'
#file_path_forecasting = 'C:/Users/saumy/OneDrive/Desktop/Semester-3/AdvMLA/AdvMLA_AT2/models/forecasting'

# Load the lgbm model
lgbm_pipe = ('../models/predictive/lgbm_pipe.joblib')
#lgbm_pipe = load('C:/Users/saumy/OneDrive/Desktop/Semester-3/AdvMLA/AdvMLA_AT2/models/forecasting/models/predictive/lgbm_pipe.joblib')
# Load the SARIMA model
SARIMA_model = ('../models/forecasting/SARIMA_model.joblib')
#SARIMA_model = load('C:/Users/saumy/OneDrive/Desktop/Semester-3/AdvMLA/AdvMLA_AT2/models/forecasting/SARIMA_model.joblib')
@app.get('/health', status_code=200)
def sales_check():
    return 'Ready to predict and forecast!'

# Endpoint to display project information
@app.get("/")
def project_info():
    return {
        "Project Description": "This API provides access to sales revenue prediction and forecasting for a retail business.",
        "Endpoints": [
            {
                "Endpoint": "/sales/national/",
                "Description": "Returns next 7 days sales volume forecast for an input date.",
                "Method": "GET"
            },
            {
                "Endpoint": "/sales/stores/items/",
                "Description": "Returns predicted sales volume for an input item, store, and date.",
                "Method": "GET"
            }
        ],
        "Expected Input Parameters": [
            "For /sales/national/: date (date)",
            "For /sales/stores/items/: store_id (int), item_id (int), input_date (date)"
        ],
        "Output Format": "JSON",
        "Github Repo": "https://github.com/bhutanisaumya/AdvMLA_AT2"
    }

# Endpoint for health check
@app.get("/sales/")
def sales_check():
    return "Welcome to the Sales Forecasting API!"

# endpoint for /sales/national/
@app.get("/sales/national/")
def national_sales(date: str):
    try:
        # Convert the input date string to a datetime object
        input_date = pd.to_datetime(date, format='%Y-%m-%d')

        # Generate a date range for the next 7 days
        forecast_dates = pd.date_range(start=input_date, periods=7, freq='D')

        # Predict sales for the next 7 days using the SARIMA model
        forecast = SARIMA_model.get_forecast(steps=7)
        forecast_values = forecast.predicted_mean

        # Create a dictionary to store the forecasted values
        forecast_data = {
            "Input Date": input_date.strftime('%Y-%m-%d'),
            "Forecasted Dates": forecast_dates.strftime('%Y-%m-%d').tolist(),
            "Forecasted Sales": forecast_values.tolist()
        }

        return forecast_data

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input date format: {str(e)}")



# endpoint for /sales/stores/items/
@app.get("/sales/stores/items/")
def store_item_sales(
    store_id: str,
    item_id: int, 
    date: str):
    # Replace with your sales forecasting logic
    # Convert the 'date' column to datetime
    # Convert the 'input_date' column to datetime
    date = pd.to_datetime(date, format='%Y-%m-%d')
    date_df = pd.DataFrame({'date': [date]})

    # Extract month, day of the week, and year into separate columns
    date_df['month'] = date_df['date'].dt.month
    date_df['day_of_week'] = date_df['date'].dt.day_name()
    date_df['year'] = date_df['date'].dt.year

    # Create a DataFrame from the response_data dictionary
    response_data = {
        'store_id': [store_id],
        'item_id': [item_id],
        'month': date_df['month'].tolist(),
        'day_of_week': date_df['day_of_week'].tolist(),
        'year': date_df['year'].tolist()
    }

    response_df = pd.DataFrame(response_data)

    # Your sales forecasting logic here
    obs = response_df  # Use response_df as input to your model
    pred = lgbm_pipe.predict(obs)

    # Return the prediction as JSON response
    response_data['prediction'] = pred.tolist()
    return JSONResponse(content=response_data)
