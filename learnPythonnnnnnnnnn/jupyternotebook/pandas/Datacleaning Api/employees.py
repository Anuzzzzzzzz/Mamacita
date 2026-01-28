from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()
df = pd.read_csv("cleaned_employees.csv")

class Employee(BaseModel):
    name: str
    age: int
    salary: int
    department: str
    join_date: str

@app.get("/")
def home():
    return {"message": "Employee API running"}

@app.get("/employees")
def get_employees():
    return df.fillna("").to_dict(orient="records")

@app.post("/employees")
def add_employee(emp: Employee):
    global df

    # fill unknowns if left empty
    dept = emp.department if emp.department.strip() != "" else "Unknown"
    date = emp.join_date if emp.join_date.strip() != "" else "Unknown"

    # prevent duplicates
    if emp.name in df["name"].values:
        return {"message": "Employee already exists!"}
    # add new row with next id
    df.loc[len(df)] = [int(df["id"].max()) + 1, emp.name, emp.age, emp.salary, dept, date]

    df.to_csv("cleaned_employees.csv", index=False)

    return {"id": int(df["id"].max()), "name": emp.name, "age": emp.age, "salary": emp.salary,
            "department": dept, "join_date": date}
