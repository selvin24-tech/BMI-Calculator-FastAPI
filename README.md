# 🧮 BMI Calculator API

A FastAPI-based REST API that calculates Body Mass Index (BMI) and provides personalized health recommendations.

## 🚀 Features

- BMI Calculation
- Healthy Weight Range
- Daily Water Intake Recommendation
- Daily Calorie Recommendation
- Exercise Suggestions
- Diet Plan
- Motivation Quotes
- JSON Request & Response
- Tested with Postman

## 🛠 Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Postman
- Git & GitHub

## ▶️ Run the Project

```bash
uvicorn bmicalculator:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

## 📌 API Endpoint

### POST `/bmi`

## 📥 Sample Request

```json
{
    "name": "Selvin",
    "age": 35,
    "gender": "Male",
    "weight": 84,
    "height": 5.9,
    "activity_level": "Moderately Active"
}
```

## 📤 Sample Response

```json
{
    "person": {
        "name": "Selvin",
        "age": 35,
        "gender": "Male"
    },
    "body": {
        "height": "5 ft 9 in",
        "weight": 84,
        "bmi": 27.3,
        "category": "Overweight"
    }
}
```

## 👨‍💻 Author

**Selvin I**

Healthcare Operations Professional | Learning Python, FastAPI & Generative AI

GitHub: https://github.com/selvin24-tegit add README.md
git commit -m "Improve README documentation"
git push

# BMI Calculator API

A REST API built using FastAPI that calculates Body Mass Index (BMI) and provides health recommendations.

## Features

- FastAPI
- POST API
- JSON Request & Response
- BMI Calculation
- Healthy Weight Range
- Diet Suggestions
- Exercise Recommendations
- Motivation Quotes

## Technologies

- Python
- FastAPI
- Uvicorn
- Pydantic
- Postman

## Run

```bash
uvicorn bmicalculator:app --reload
```
