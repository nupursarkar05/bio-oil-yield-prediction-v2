from fastapi import FastAPI
import pandas as pd
import joblib
from pathlib import Path

from schema import PredictionInput

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR/"models"/"catboost_model.pkl")
feature_names = joblib.load(BASE_DIR/"models"/"feature_names.pkl")

app = FastAPI(
    title="Bio-Oil Yield Prediction API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message":"Bio-Oil Yield Prediction API",
        "status":"running"
    }


@app.post("/predict")
def predict(data: PredictionInput):

    input_dict={}

    for feature in feature_names:

        if feature=="Moisture":
            input_dict[feature]=data.Moisture

        elif feature=="Ash":
            input_dict[feature]=data.Ash

        elif feature=="Volatile_Matter":
            input_dict[feature]=data.Volatile_Matter

        elif feature=="Fixed_Carbon":
            input_dict[feature]=data.Fixed_Carbon

        elif feature=="Carbon":
            input_dict[feature]=data.Carbon

        elif feature=="Hydrogen":
            input_dict[feature]=data.Hydrogen

        elif feature=="Oxygen":
            input_dict[feature]=data.Oxygen

        elif feature=="Nitrogen":
            input_dict[feature]=data.Nitrogen

        elif feature=="Particle_Size":
            input_dict[feature]=data.Particle_Size

        elif feature=="Temperature":
            input_dict[feature]=data.Temperature

        elif feature=="Heating_Rate":
            input_dict[feature]=data.Heating_Rate

        elif feature=="Flow_Rate":
            input_dict[feature]=data.Flow_Rate

        elif feature=="Biochar_Yield":
            input_dict[feature]=data.Biochar_Yield

        elif feature=="Gas_Yield":
            input_dict[feature]=data.Gas_Yield

        elif feature.startswith("Biomass species_"):

            input_dict[feature]=1 if feature==f"Biomass species_{data.Biomass_species}" else 0

        else:
            input_dict[feature]=0

    df=pd.DataFrame([input_dict])

    prediction=model.predict(df)[0]

    return {
        "Predicted_Bio_Oil_Yield": round(float(prediction),2)
    }