import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------
# Page Config
# ------------------------------

st.set_page_config(
    page_title="Bio-Oil Yield Prediction",
    page_icon="🌿",
    layout="wide"
)

# ------------------------------
# Load Model
# ------------------------------

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "catboost_model.pkl")
feature_names = joblib.load(BASE_DIR / "models" / "feature_names.pkl")

# ------------------------------
# Title
# ------------------------------

st.title("🌿 Bio-Oil Yield Prediction")
st.write("Predict bio-oil yield obtained from biomass pyrolysis using Machine Learning.")

# ------------------------------
# Sidebar
# ------------------------------

st.sidebar.header("About")

st.sidebar.info(
"""
This application predicts the **Bio-Oil Yield**
obtained from biomass pyrolysis using a trained
CatBoost Machine Learning model.
"""
)

st.sidebar.success("Model: CatBoost")

st.sidebar.metric(
label="R² Score",
value="95.89%"
)

# ------------------------------
# Biomass List
# ------------------------------

species_list = sorted([
"almond shell",
"bamboo",
"banana peel",
"corncob",
"cotton stalk",
"grape pomace",
"microalgae",
"miscanthus",
"olive pomace",
"pine sawdust",
"rice husk",
"rice straw",
"sawdust",
"spirulina",
"sunflower",
"tobacco residues",
"tomato peel",
"wheat straw",
"wheat stalk"
])

# ------------------------------
# Layout
# ------------------------------

left, right = st.columns(2)

with left:

    biomass = st.selectbox(
        "Biomass Species",
        species_list
    )

    moisture = st.number_input(
        "Moisture (%)",
        0.0,
        30.0,
        5.0
    )

    ash = st.number_input(
        "Ash (%)",
        0.0,
        50.0,
        5.0
    )

    vm = st.number_input(
        "Volatile Matter (%)",
        0.0,
        100.0,
        70.0
    )

    fc = st.number_input(
        "Fixed Carbon (%)",
        0.0,
        100.0,
        15.0
    )

    carbon = st.number_input(
        "Carbon (%)",
        0.0,
        100.0,
        45.0
    )

    hydrogen = st.number_input(
        "Hydrogen (%)",
        0.0,
        25.0,
        6.0
    )

    oxygen = st.number_input(
        "Oxygen (%)",
        0.0,
        100.0,
        44.0
    )

with right:

    nitrogen = st.number_input(
        "Nitrogen (%)",
        0.0,
        25.0,
        1.5
    )

    particle = st.number_input(
        "Particle Size (mm)",
        0.1,
        200.0,
        0.5
    )

    temp = st.number_input(
        "Temperature (°C)",
        300,
        900,
        500
    )

    hr = st.number_input(
        "Heating Rate",
        0,
        700,
        20
    )

    fr = st.number_input(
        "Flow Rate",
        0,
        10000,
        100
    )

    biochar = st.number_input(
        "Biochar Yield (%)",
        0.0,
        100.0,
        30.0
    )

    gas = st.number_input(
        "Gas Yield (%)",
        0.0,
        100.0,
        30.0
    )

# ------------------------------
# Create Feature Vector
# ------------------------------

input_dict = {}

for feature in feature_names:

    if feature == "Moisture":
        input_dict[feature] = moisture

    elif feature == "Ash":
        input_dict[feature] = ash

    elif feature == "Volatile_Matter":
        input_dict[feature] = vm

    elif feature == "Fixed_Carbon":
        input_dict[feature] = fc

    elif feature == "Carbon":
        input_dict[feature] = carbon

    elif feature == "Hydrogen":
        input_dict[feature] = hydrogen

    elif feature == "Oxygen":
        input_dict[feature] = oxygen

    elif feature == "Nitrogen":
        input_dict[feature] = nitrogen

    elif feature == "Particle_Size":
        input_dict[feature] = particle

    elif feature == "Temperature":
        input_dict[feature] = temp

    elif feature == "Heating_Rate":
        input_dict[feature] = hr

    elif feature == "Flow_Rate":
        input_dict[feature] = fr

    elif feature == "Biochar_Yield":
        input_dict[feature] = biochar

    elif feature == "Gas_Yield":
        input_dict[feature] = gas

    elif feature.startswith("Biomass species_"):

        if feature == f"Biomass species_{biomass}":
            input_dict[feature] = 1
        else:
            input_dict[feature] = 0

    else:
        input_dict[feature] = 0

input_df = pd.DataFrame([input_dict])

# ------------------------------
# Prediction
# ------------------------------

if st.button("Predict Bio-Oil Yield"):

    prediction = model.predict(input_df)[0]

    st.success(
        f"Predicted Bio-Oil Yield = {prediction:.2f}%"
    )

    st.progress(min(prediction/100,1.0))

    st.subheader("Prediction Summary")

    st.dataframe(input_df)

    # Feature Importance

    if hasattr(model,"feature_importances_"):

        importance = model.feature_importances_

        fi = pd.DataFrame({
            "Feature":feature_names,
            "Importance":importance
        })

        fi = fi.sort_values(
            "Importance",
            ascending=False
        ).head(10)

        st.subheader("Top 10 Important Features")

        fig,ax = plt.subplots(figsize=(8,5))

        ax.barh(
            fi["Feature"],
            fi["Importance"]
        )

        ax.invert_yaxis()

        st.pyplot(fig)

    csv = input_df.copy()

    csv["Predicted Bio_Oil_Yield"] = prediction

    csv = csv.to_csv(index=False)

    st.download_button(
        "Download Prediction",
        csv,
        "prediction.csv",
        "text/csv"
    )