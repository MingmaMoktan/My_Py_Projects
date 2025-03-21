from fastapi import FastAPI, Form
import json
from statistics import median, variance, pstdev

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
            "result": 1
        }
        
        result = 1
        for i in range(1, number + 1):
            result = result*i

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
async def calculate_median(numbers: str = Form(...)):
    try:
        # I used AI to generate this part of logic and copied same for variance and pstdev.
        numbers_list = json.loads(numbers)
        if not isinstance(numbers_list, list) or not all(isinstance(x, (int, float)) for x in numbers_list):
            raise ValueError("Input must be a list of numbers.")

        result = median(numbers_list)
        return {
            "status": 1,
            "parameter": numbers_list,
            "action": "median",
            "result": result
        }
    except Exception as e:
        return {
            "status": 0,
            "message": str(e)
        }

@app.post("/api/variance")
async def calculate_variance(numbers: str = Form (...)):
    try:
        numbers_list = json.loads(numbers)
        if not isinstance(numbers_list, list) or not all(isinstance(x, (int, float)) for x in numbers_list):
            raise ValueError("Input must be a list of numbers.")

        result = variance(numbers_list)
        return {
            "status": 1,
            "parameter": numbers_list,
            "action": "variance",
            "result": result
        }
    except Exception as e:
        return {
            "status": 0,
            "message": str(e)
        }
    
@app.post("/api/pstdev")
async def calculate_pstdev(numbers: str = Form (...)):
    try:
        numbers_list = json.loads(numbers)
        if not isinstance(numbers_list, list) or not all(isinstance(x, (int, float)) for x in numbers_list):
            raise ValueError("Input must be a list of numbers.")

        result = pstdev(numbers_list)
        return {
            "status": 1,
            "parameter": numbers_list,
            "action": "pstdev",
            "result": result
        }
    except Exception as e:
        return {
            "status": 0,
            "message": str(e)
        }