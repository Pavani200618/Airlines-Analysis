import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    # Your Dropbox link
    dropbox_link = "https://www.dropbox.com/scl/fi/xkdcenlz9qdwdzmfy1gik/flights.csv.csv?rlkey=s0hsv38sh9m1vzggq1h412b83&st=c9w05fs2&dl=0"
    
    # Converts the link to a direct download link
    data_url = dropbox_link.replace("dl=0", "dl=1")
    
    try:
        # Load 70,000 rows as requested
        df = pd.read_csv(data_url, nrows=70000)
    except Exception as e:
        st.error(f"Failed to download data: {e}")
        st.stop()

    # Clean column names (Fixes the DEP_DELAY error)
    df.columns = [str(c).strip().upper() for c in df.columns]

    if "DEP_DELAY" not in df.columns:
        st.error(f"Column 'DEP_DELAY' not found. Available: {df.columns.tolist()}")
        st.stop()

    # Data Processing
    df = df.dropna(subset=["DEP_DELAY"])
    df["IS_HIGH_RISK"] = df["DEP_DELAY"] > 15
    df["RISK_SCORE"] = df["IS_HIGH_RISK"].astype(int) * 100

    delay_cols = ["DELAY_DUE_CARRIER", "DELAY_DUE_WEATHER", "DELAY_DUE_NAS", "DELAY_DUE_SECURITY", "DELAY_DUE_LATE_AIRCRAFT"]
    existing_cols = [c for c in delay_cols if c in df.columns]
    
    if existing_cols:
        df["TOTAL_DELAY"] = df[existing_cols].sum(axis=1)

    return df
