import pandas as pd

# 1. LOAD DATA FROM CLOUD
file_id = "19h0lEG2PouEG7sSM7MR6ARHncmYaIT6x"
data_url = f'https://drive.google.com/uc?id={file_id}'

df = pd.read_csv(data_url, nrows=5000)
df = df.dropna(subset=['DEP_DELAY'])
# ... (rest of your analysis code remains the same)
