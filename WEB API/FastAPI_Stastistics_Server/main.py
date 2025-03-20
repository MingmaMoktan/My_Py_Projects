from fastapi import FastAPI, Form
from statistics import median

app = FastAPI()

@app.post("/api/factorial")
async def factorial(number: int = Form(...)):
    try:
        if number < 0:
            raise ValueError("Number should be greater than or equal to 0.")
        elif number==0:
            return {
            "status": 1,
            "parameter": number,
            "action": "factorial",
            "result": "1"
        }
        
        result = 1
        for i in range(1, number + 1):
            result *= i

        return {
            "status": 1,
            "parameter": number,
            "action": "factorial",
            "result": result
        }
    
    except Exception as e:
        return {
            "status":0,
            "message": str(e)
        }


@app.post("/api/median")
async def calculate_median(numbers: list[float] = Form(...)):
    try:
        if not numbers:
            raise ValueError("Median can be calculated only for a non-empty list of numerical data.")
        else:
            result = median(numbers)  
            return {
                "status": 1,
                "parameter": numbers,
                "action": "median",
                "result": result
            }
    except Exception as e:
        return {
            "status": 0,
            "message": str(e)
        }
