import joblib
import pandas as pd
import os

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(script_dir, "..", "models")

# Load models with paths relative to script location
model = joblib.load(os.path.join(models_dir, "catboost_model.pkl"))
scaler = joblib.load(os.path.join(models_dir, "scaler.pkl"))
feature_names = joblib.load(os.path.join(models_dir, "feature_names.pkl"))

def predict_bio_oil(sample_df):
    sample_encoded = pd.get_dummies(sample_df)
    sample_encoded = sample_encoded.reindex(
    columns=feature_names,
    fill_value=0
)
    prediction = model.predict(sample_encoded)

    return prediction[0]

sample = pd.DataFrame({
    "Biomass species": ["rice husk"],
    "Moisture": [8.2],
    "Ash": [6.5],
    "Volatile_Matter": [72.0],
    "Fixed_Carbon": [14.5],
    "Carbon": [46.8],
    "Hydrogen": [6.0],
    "Oxygen": [44.0],
    "Nitrogen": [1.2],
    "Particle_Size": [0.5],
    "Temperature": [500],
    "Heating_Rate": [20],
    "Flow_Rate": [100],
    "Biochar_Yield": [30],
    "Gas_Yield": [28]
})

predicted_yield = predict_bio_oil(sample)

print(f"Predicted Bio-Oil Yield: {predicted_yield:.2f}%")
