import streamlit as st
from flights_utils import load_data
from Home_Stats import show_home
from Route_Finder import show_route_finder
from Global_Analysis import show_global

st.set_page_config(page_title="Airline Performance Analytics", layout="wide")

df = load_data()

st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to:", ["Home & Stats", "Route Finder", "Global Analysis"])

st.sidebar.divider()

with st.sidebar.expander("📊 View System Snapshot"):
    st.metric("Total Sample Size", f"{len(df)//1000}K")
    if "DELAY_DUE_WEATHER" in df.columns:
        w_val = df[df["DELAY_DUE_WEATHER"] > 0].shape[0]
        st.metric("Environmental Latency", f"{w_val/1000:.1f}K")

st.sidebar.divider()

if page == "Home & Stats":
    show_home(df)
elif page == "Route Finder":
    show_route_finder(df)
elif page == "Global Analysis":
    show_global(df)
