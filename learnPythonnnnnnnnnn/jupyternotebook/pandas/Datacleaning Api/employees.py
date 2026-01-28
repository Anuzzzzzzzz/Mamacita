from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# Load cleaned dataset
df_cleaned = pd.read_csv("cleaned_employees.csv")

# Schemas
class Item(BaseModel):
    name: str
    age: int
    salary: int

# Root endpoint
@app.get("/")
def root():
    return {"status": "Employee API running"}

# GET all employees
@app.get("/employees")
def get_employees():
    return df_cleaned.to_dict(orient="records")

# POST new employee
@app.post(
    "/employees",
    response_model=Item,
    tags=["employees"],
)
def create_employee(employee: Item):
    global df_cleaned  # ensure we modify the global DataFrame

    # Append new employee to DataFrame
    df_cleaned = pd.concat([df_cleaned, pd.DataFrame([employee.dict()])], ignore_index=True)

    # Save updated DataFrame back to CSV
    df_cleaned.to_csv("cleaned_employees.csv", index=False)

    return employee
