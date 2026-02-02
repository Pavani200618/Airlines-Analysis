import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    # Converted Google Drive View link to Direct Download link
    file_id = "19h0lEG2PouEG7sSM7MR6ARHncmYaIT6x"
    data_url = f'https://drive.google.com/uc?id={file_id}'
    
    # Load data from URL
    df = pd.read_csv(data_url, nrows=70000)

    df = df.dropna(subset=["DEP_DELAY"])
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
