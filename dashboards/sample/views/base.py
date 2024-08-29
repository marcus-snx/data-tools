import streamlit as st
from datetime import datetime
import logging

st.markdown("# Base")

def fetch_data():
    logging.info("Fetching Base data!")
    return st.session_state.api.get_volume(
        chain="base_mainnet", start_date=datetime(2024, 6, 1), end_date=datetime(2024, 7, 1)
    )

data = fetch_data()

st.write(data)
