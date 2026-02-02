import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    file_id = "19h0lEG2PouEG7sSM7MR6ARHncmYaIT6x"
    data_url = f'https://drive.google.com/uc?id={file_id}'
    
    # Load data
    df = pd.read_csv(data_url, nrows=70000)

    # FIX: Clean column names (Remove spaces and make Uppercase)
    df.columns = [str(c).strip().upper() for c in df.columns]

    # Verify if column exists after cleaning
    if "DEP_DELAY" not in df.columns:
        st.error(f"Error: 'DEP_DELAY' not found. Columns in your file: {df.columns.tolist()}")
        st.stop()

    df = df.dropna(subset=["DEP_DELAY"])

    # Feature Engineering
    df["IS_HIGH_RISK"] = df["DEP_DELAY"] > 15
    df["RISK_SCORE"] = df["IS_HIGH_RISK"].astype(int) * 100

    delay_cols = [
        "DELAY_DUE_CARRIER", "DELAY_DUE_WEATHER", "DELAY_DUE_NAS",
        "DELAY_DUE_SECURITY", "DELAY_DUE_LATE_AIRCRAFT",
    ]
    
    existing_cols = [c for c in delay_cols if c in df.columns]
    if existing_cols:
        df["TOTAL_DELAY"] = df[existing_cols].sum(axis=1)

    return df
