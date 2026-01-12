from fastapi import FastAPI

app = FastAPI()

@app.post("/calculate-salary")
async def calculate_salary(hours: int, hourly_rate: float):
    gross = hours * hourly_rate
    net_salary = gross * 0.9 if gross > 5000 else gross * 0.95
    return {"net_salary": net_salary}


