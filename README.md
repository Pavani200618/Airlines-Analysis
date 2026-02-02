# ✈️ Airlines Performance Analysis Dashboard

**🚀 LIVE APP:** [View Interactive Dashboard](https://pavani200618-airlines-analysis-app-pjimon.streamlit.app/)  
*(Hosted via Streamlit Cloud for real-time data processing)*

---

## 🛠 Project Architecture & Deployment
Due to GitHub's file size limitations (100MB) and the dataset being **586MB**, this project uses a high-performance cloud pipeline:

* **Frontend:** [Streamlit Cloud](https://streamlit.io/cloud) - Powers the interactive UI and Python backend.
* **Data Storage:** [Dropbox](https://www.dropbox.com/) - External hosting to bypass GitHub's storage constraints.
* **Version Control:** [GitHub](https://github.com/) - Hosts the logic and code structure.

---

## 📂 Dataset & Local Setup
If you wish to run this analysis on your local machine, follow the instructions below.

### 1. Download the Dataset
The dataset contains over 70,000 flight records. 
* **[Download Flights.csv (Direct Download)](https://www.dropbox.com/scl/fi/xkdcenlz9qdwdzmfy1gik/flights.csv.csv?rlkey=s0hsv38sh9m1vzggq1h412b83&st=c9w05fs2&dl=1)**

### 2. Installation
Install the necessary Python libraries:
```bash
pip install streamlit pandas plotly
