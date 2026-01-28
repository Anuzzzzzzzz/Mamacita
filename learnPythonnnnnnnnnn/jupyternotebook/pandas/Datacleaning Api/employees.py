from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

# load the cleaned CSV
df = pd.read_csv("cleaned_employees.csv")

# POST input schema
class Employee(BaseModel):
    name: str
    age: int
    salary: int
    department: str
    join_date: str

@app.get("/")
def home():
    return {"message": "API running"}

# get employees
@app.get("/employees")
def get_employees():
    # replace NaN with empty string so JSON works
    return df.fillna("").to_dict(orient="records")

# POST new employee
@app.post("/employees")
def add_employee(emp: Employee):
    global df

    # this prevents duplicates name
    if emp.name in df["name"].values:
        return {"message": "Employee already exists!"}

    # create a new row dictionary including the next ID
    # we do this because the CSV already has 'id' for each employee
    new_row = {
        "id": int(df["id"].max()) + 1,  # next ID
        "name": emp.name,
        "age": emp.age,
        "salary": emp.salary,
        "department": emp.department,
        "join_date": emp.join_date
    }

    # add the new row to the DataFrame
    df.loc[len(df)] = new_row

    # save the updated DataFrame back to CSV
    df.to_csv("cleaned_employees.csv", index=False)

    return new_row
