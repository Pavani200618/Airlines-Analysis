import streamlit as st
import plotly.express as px

def show_global(df):
    # Top Heading
    st.title("📊 Global Performance Trends")

    col1, col2 = st.columns(2)

    with col1:
        avg_delay_chart = df.groupby("AIRLINE")["DEP_DELAY"].mean().reset_index()
        fig1 = px.bar(
            avg_delay_chart,
            x="AIRLINE",
            y="DEP_DELAY",
            title="Avg Delay by Airline",
            color="DEP_DELAY",
            color_continuous_scale="Blues_r"  # Dark blue to light blue gradient
        )
        fig1.update_layout(
            template="plotly_dark",
            height=400,
            margin=dict(l=10, r=10, t=50, b=10),
            yaxis_title=None, # Removes DEP_DELAY text from the side
            xaxis_title="AIRLINE"
        )
        st.plotly_chart(fig1, width="stretch")

    with col2:
        risk_chart = (df.groupby("AIRLINE")["IS_HIGH_RISK"].mean() * 100).reset_index()
        fig2 = px.bar(
            risk_chart,
            x="AIRLINE",
            y="IS_HIGH_RISK",
            title="Delay Risk Probability (%)",
            color="IS_HIGH_RISK",
            color_continuous_scale="Blues_r"
        )
        fig2.update_layout(
            template="plotly_dark",
            height=400,
            margin=dict(l=10, r=10, t=50, b=10),
            yaxis_title=None, # Removes IS_HIGH_RISK text from the side
            xaxis_title="AIRLINE"
        )
        st.plotly_chart(fig2, width="stretch")