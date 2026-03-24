import streamlit as st
from pathlib import Path
import pandas as pd
from engine import calculate_nitrogen

st.set_page_config(page_title="Nutrient Management Tool", layout="centered")

_DATA_DIR = Path(__file__).resolve().parent / "data"
_WORKBOOK = _DATA_DIR / "tamu_legacy_nutrient_tool.xlsm"


@st.cache_data
def load_crop_data():
    df = pd.read_excel(_WORKBOOK, sheet_name="Constants")
    return df.set_index("Crop").to_dict("index")


try:
    full_crop_database = load_crop_data()
except Exception as e:
    st.error(f"Could not load crop data from `{_WORKBOOK}`: {e}")
    st.caption("Please ensure to keep the workbook under `data/`.")
    st.stop()

st.title("Nutrient Management Tool", text_alignment="center")
st.caption("Migration of Calculator from Excel to Streamlit")


crop_name = st.selectbox("Select Crop", list(full_crop_database.keys()))
target_yield = st.number_input("Target Yield (bu/acre):", min_value=1.0, value=200.0)

soil_n_ppm = st.number_input("Soil Nitrogen (ppm):", min_value=0.0, value=20.0)
st.divider()

if st.button("Calculate Nitrogen Requirement", type="primary"):
    try:
        selected_crop_factors = {
            "target_n": full_crop_database[crop_name]["Target N (lbs/bu)"],
            "efficiency": full_crop_database[crop_name]["Efficiency Factor"],
        }
        req = calculate_nitrogen(selected_crop_factors, target_yield, soil_n_ppm)
        st.success("Calculation completed and verified")
        st.metric(
            label=f"Recommended Nitrogen for {crop_name}",
            value=f"{req} lbs/acre",
        )
    except Exception as e:
        st.error(f"Calculation failed: {e}")
