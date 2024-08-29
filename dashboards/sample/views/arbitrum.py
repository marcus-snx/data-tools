import streamlit as st
from datetime import datetime
from dashboards.utils.charts import chart_bars

st.markdown("# Arbitrum")

def fetch_data():
    logging.info("Fetching Arbitrum data!")
    return st.session_state.api.get_volume(
        chain="base_mainnet", start_date=datetime(2024, 6, 1), end_date=datetime(2024, 7, 1)
    )

data = fetch_data()

st.write(data)

chart = chart_bars(data, x_col="ts", y_cols="volume", title="Daily Perps Volume")
st.plotly_chart(chart)
