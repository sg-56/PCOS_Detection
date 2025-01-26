from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, conint, constr,Field
from typing import Optional, Literal
from fastapi.middleware.cors import CORSMiddleware
from typing_extensions import Annotated
import pickle
import pandas as pd

app = FastAPI()

# origins = [
#     "http://localhost:8501",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MODEL_PATH = './artifacts/model.pkl'
PREPROCESSOR_PATH = './artifacts/preprocessor.pkl'
def load_preproccesor():
    with open(PREPROCESSOR_PATH, 'rb') as file:
        preprocessor = pickle.load(file)
    return preprocessor


def load_model():
    with open(MODEL_PATH, 'rb') as file:
        model = pickle.load(file)
    return model

app = FastAPI()

# Define the data model using Pydantic for validation
class PCOSData(BaseModel):
    Country: Literal['Madagascar', 'Vietnam', 'Somalia', 'Malawi', 'France', 'Rwanda', 'Tanzania', 'United States', 'Italy', 'Australia', 'India', 'Argentina', 'Morocco', 'Zambia', 'Romania', 'Sudan', 'Benin', 'Burkina Faso', 'Nepal', 'Mali', 'Malaysia', 'Chile', 'Mozambique', 'Ivory Coast', 'Taiwan', 'Nigeria', 'Zimbabwe', 'Uzbekistan', 'Germany', 'Indonesia', 'Egypt', 'Russia', 'Chad', 'Peru', 'Bangladesh', 'Iraq', 'Canada', 'Cameroon', 'Brazil', 'North Korea', 'Kazakhstan', 'Uganda', 'Guinea', 'Yemen', 'Saudi Arabia', 'South Korea', 'Afghanistan', 'Spain', 'Ghana', 'Guatemala', 'China', 'Japan', 'Pakistan', 'Kenya', 'Ethiopia', 'South Africa', 'Poland', 'Colombia', 'Burundi', 'Venezuela', 'Philippines', 'Ukraine', 'Ecuador', 'Sri Lanka', 'Cambodia', 'Niger', 'Thailand', 'Netherlands', 'Iran', 'Senegal', 'Turkey', 'United Kingdom', 'Syria', 'Algeria', 'Myanmar', 'Angola', 'Mexico']
    Age: Annotated[int, Field(strict=True, gt=10,lt=100)]  # Age between 10 and 100
    BMI: Literal["Underweight", "Normal", "Overweight", "Obese"]
    Menstrual_Regularity: Literal["Regular", "Irregular"]
    Hirsutism: Literal["Yes", "No"]
    Acne_Severity: Literal["Mild", "Moderate", "Severe","NA"]
    Family_History_of_PCOS: Literal["Yes", "No"]
    Insulin_Resistance: Literal["Yes", "No"]
    Lifestyle_Score: Annotated[int, Field(strict=True, gt=0,lt=10)]  # Lifestyle Score between 1 and 10
    Stress_Levels: Literal["Low", "Medium", "High"]
    Urban_Rural: Literal["Urban", "Rural"]
    Socioeconomic_Status: Literal["Low", "Middle", "High"]
    Awareness_of_PCOS: Literal["Yes", "No"]
    Fertility_Concerns: Literal["Yes", "No"]
    Ethnicity: Literal["Hispanic", "Caucasian", "African", "Asian", "Other"]


@app.get('/')
async def root():
    return {"message": "Welcome to the PCOS prediction API"}

@app.post('/predict')
async def submit_data(data:PCOSData):
    try:
        # Parse and validate the incoming JSON data
        data = {
            'Country': data.Country,
            'Age': data.Age,
            'BMI': data.BMI,
            'Menstrual_Regularity': data.Menstrual_Regularity,
            'Hirsutism': data.Hirsutism,
            'Acne_Severity': data.Acne_Severity,
            'Family_History_of_PCOS': data.Family_History_of_PCOS,
            'Insulin_Resistance': data.Insulin_Resistance,
            'Lifestyle_Score': data.Lifestyle_Score,
            'Stress_Levels': data.Stress_Levels,
            'Urban/Rural': data.Urban_Rural,
            'Socioeconomic_Status': data.Socioeconomic_Status,
            'Awareness_of_PCOS': data.Awareness_of_PCOS,
            'Fertility_Concerns': data.Fertility_Concerns,
            'Ethnicity': data.Ethnicity
        }
        data = pd.DataFrame([data])
        preprocess = load_preproccesor()
        model = load_model()
        # Preprocess the data
        preprocessed_data = preprocess.transform(data)
        # Make prediction
        prediction = model.predict(preprocessed_data)
        # print(prediction[0])
        return {"status": "success", "result": prediction[0]}, 200
    
    except ValidationError as e:
        # If validation fails, return the error details
        return {"status": "error", "message": "Validation failed", "errors": e.errors()}, 400

if __name__ == '__main__':
    app.run(debug=True)
