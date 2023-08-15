# Run using uvicorn api:app --port 8081

from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
def read_root():
    formatted_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "name": "dopo3",
        "date": formatted_datetime
    }
