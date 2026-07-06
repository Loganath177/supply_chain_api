from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI(
    title="Sample Customer API",
    description="API to serve customer data from a CSV file",
    version="1.0"
)

CSV_FILE = "customers.csv"


@app.get("/")
def home():
    return {
        "message": "Customer API is running",
        "status": "success"
    }


@app.get("/customers")
def get_customers():
    try:
        # Read CSV
        df = pd.read_csv(CSV_FILE)

        # Replace NaN with empty string
        df = df.fillna("")

        # Convert DataFrame to JSON
        return df.to_dict(orient="records")

    except FileNotFoundError:
        return {
            "status": "error",
            "message": f"{CSV_FILE} not found."
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
