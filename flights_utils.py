@st.cache_data
def load_data():
    file_id = "19h0lEG2PouEG7sSM7MR6ARHncmYaIT6x"
    data_url = f'https://drive.google.com/uc?id={file_id}'
    
    df = pd.read_csv(data_url, nrows=70000)

    # DEBUG: This will show you the real column names in the Streamlit logs
    print("Columns found in file:", df.columns.tolist())

    # Make columns uppercase to avoid case-sensitivity issues
    df.columns = [c.upper() for c in df.columns]

    if "DEP_DELAY" not in df.columns:
        st.error(f"Column 'DEP_DELAY' not found. Available columns: {df.columns.tolist()}")
        st.stop()

    df = df.dropna(subset=["DEP_DELAY"])
    # ... rest of your code ...
