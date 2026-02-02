# ✈️ Airlines Performance & Delinquency Risk Analysis

## Overview
This project is an interactive dashboard analyzing airline flight data (70,000+ records) to identify delay patterns and risk factors. Unlike static analysis, this project uses a live Python backend to calculate performance metrics in real-time.

**🚀 [Click Here to View the Live Interactive App](https://airlines-analysis-pavani.streamlit.app/)**

## Key Risk Factors Analyzed
Based on industry standards for customer delinquency, this tool evaluates:
* **Payment History** and **Credit Utilization Rate**
* **Debt-to-Income (DTI) Ratio**
* **Employment and Income Stability**
* **Recent Credit Activity** and **Demographic Trends**

## Project Architecture
* **Frontend:** Streamlit (hosted on Streamlit Cloud)
* **Data Hosting:** Dropbox (handles the 586MB dataset bypass)
* **Analysis Engine:** Python (Pandas, Plotly)

## Files
* `app.py` — Main application entry point and navigation.
* `flights_utils.py` — Data pipeline connecting to Dropbox and cleaning the CSV.
* `Route_Finder.py` / `Global_Analysis.py` — Page-specific analysis logic.

## Dataset
The dataset (586MB) is streamed directly from Dropbox to the app, so no local download is required to view the results.
