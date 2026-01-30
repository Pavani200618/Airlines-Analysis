import streamlit as st

def show_route_finder(df):
    st.title("🔍 Passenger Route Search")

    col1, col2 = st.columns(2)

    with col1:
        origin = st.selectbox("From (Origin):", sorted(df["ORIGIN"].unique()))

    with col2:
        valid_dests = sorted(df[df["ORIGIN"] == origin]["DEST"].unique())
        dest = st.selectbox("To (Destination):", valid_dests)

    search_results = df[(df["ORIGIN"] == origin) & (df["DEST"] == dest)]

    if not search_results.empty:
        st.subheader(f"Flights Found: {origin} ➔ {dest}")

        display_df = (
            search_results.groupby("AIRLINE")[["DEP_DELAY", "RISK_SCORE"]]
            .mean()
            .reset_index()
        )

        display_df.columns = ["Airline Name", "Avg Delay (Mins)", "Delay Risk (%)"]

        st.table(display_df)

        best = display_df.sort_values("Delay Risk (%)").iloc[0]

        st.success(
            f"✅ Recommended: **{best['Airline Name']}** (Risk: {best['Delay Risk (%)']:.1f}%)"
        )
    else:
        st.error("No flights found for this specific route.")
