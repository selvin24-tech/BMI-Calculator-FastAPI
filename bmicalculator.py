from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="BMI Calculator API",
    description="Professional BMI Calculator using FastAPI",
    version="1.0"
)


# ----------------------------
# Request Model
# ----------------------------

class BMIRequest(BaseModel):
    name: str = Field(..., example="Selvin")
    age: int = Field(..., ge=5, le=120, example=35)
    gender: str = Field(..., example="Male")
    weight: float = Field(..., gt=0, example=84)
    height: float = Field(..., gt=0, example=5.9)
    activity_level: str = Field(
        ...,
        example="Moderately Active"
    )


# ----------------------------
# Home API
# ----------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to the BMI Calculator API",
        "developer": "Selvin",
        "version": "1.0",
        "usage": "Use POST /bmi"
    }


# ----------------------------
# Helper Functions
# ----------------------------

def convert_height(height):
    feet = int(height)
    inches = round((height - feet) * 10)

    total_inches = feet * 12 + inches

    meter = total_inches * 0.0254

    return feet, inches, meter


def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


def motivation():

    return [
        "Take care of your body. It is the only place you have to live.",
        "Health is the greatest wealth.",
        "Small daily improvements create stunning long-term results.",
        "Exercise is a celebration of what your body can do.",
        "Consistency beats perfection."
    ]


def exercise_plan(category):

    plans = {

        "Underweight": [
            "Strength training 3 times/week",
            "Increase healthy calorie intake",
            "Eat protein-rich foods"
        ],

        "Normal": [
            "Walk 30 minutes daily",
            "Strength training twice/week",
            "Stretch every day"
        ],

        "Overweight": [
            "Walk 45 minutes daily",
            "Strength training 3 times/week",
            "Reduce sugary foods",
            "Cardio 4 days/week"
        ],

        "Obese": [
            "Start with 20-30 minute walks",
            "Consult a fitness coach",
            "Increase activity gradually",
            "Low-impact cardio"
        ]

    }

    return plans[category]


def diet_plan(category):

    diets = {

        "Underweight": [
            "Milk",
            "Eggs",
            "Chicken",
            "Nuts",
            "Rice"
        ],

        "Normal": [
            "Balanced Diet",
            "Vegetables",
            "Fruits",
            "Lean Protein",
            "Whole Grains"
        ],

        "Overweight": [
            "High Protein",
            "Green Vegetables",
            "Less Sugar",
            "Less Junk Food",
            "Drink 3L Water"
        ],

        "Obese": [
            "Consult Dietitian",
            "Low Sugar",
            "High Fiber",
            "Protein Rich Foods",
            "Drink Plenty of Water"
        ]

    }

    return diets[category]

# ----------------------------
# BMI API Endpoint
# ----------------------------

@app.post("/bmi")
def calculate_bmi(data: BMIRequest):

    feet, inches, height_m = convert_height(data.height)

    bmi = data.weight / (height_m ** 2)

    category = bmi_category(bmi)

    healthy_min = round(18.5 * (height_m ** 2), 1)
    healthy_max = round(24.9 * (height_m ** 2), 1)

    if data.weight < healthy_min:
        weight_status = f"Gain {round(healthy_min-data.weight,1)} kg"
    elif data.weight > healthy_max:
        weight_status = f"Lose {round(data.weight-healthy_max,1)} kg"
    else:
        weight_status = "Healthy Weight"

    # Water Intake
    water = round(data.weight * 0.035, 1)

    # Calories
    if category == "Underweight":
        calories = 2800
    elif category == "Normal":
        calories = 2300
    elif category == "Overweight":
        calories = 2000
    else:
        calories = 1800

    return {

        "person": {
            "name": data.name,
            "age": data.age,
            "gender": data.gender
        },

        "body": {
            "height": f"{feet} ft {inches} in",
            "weight": data.weight,
            "bmi": round(bmi, 1),
            "category": category
        },

        "healthy_weight": {
            "minimum": healthy_min,
            "maximum": healthy_max,
            "status": weight_status
        },

        "daily_health": {
            "recommended_water_liters": water,
            "recommended_calories": calories
        },

        "exercise_plan": exercise_plan(category),

        "diet_plan": diet_plan(category),

        "motivation": motivation()
    }