import streamlit as st
import plotly.express as px

def show_home(df):
    st.title("✈️ Airline On-Time Performance")

    # Compact Data Processing
    unreliable = (
        df.groupby(["ORIGIN", "DEST"])["DEP_DELAY"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    unreliable["Route"] = unreliable["ORIGIN"] + " ➔ " + unreliable["DEST"]

    # Simple Violet Bar Chart
    fig = px.bar(
        unreliable,
        x="DEP_DELAY",
        y="Route",
        orientation='h',
        color_discrete_sequence=["#8A2BE2"] # Violet
    )

    # Tight Layout for Screenshot
    fig.update_layout(
        title="Top 10 Routes by Average Latency (Mins)",
        yaxis={"categoryorder": "total ascending"},
        xaxis_title="Avg Delay (min)",
        yaxis_title=None,
        margin=dict(l=0, r=10, t=30, b=0), # Removes white space
        height=350, # Short height to fit on screen
        template="plotly_white"
    )

    # Use "stretch" to stop the warning errors
    st.plotly_chart(fig, width="stretch")