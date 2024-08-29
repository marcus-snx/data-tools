# path setup
import streamlit as st
from api.internal_api import SynthetixAPI, get_db_config
import logging

st.set_page_config(
    page_title="Synthetix Dashboards",
    page_icon=f"dashboards/static/favicon.ico",
    layout="wide",
)

# set the API
def load_api():
    logging.error("Loading API in main")
    return SynthetixAPI(db_config=get_db_config(streamlit=True))

st.session_state.api = load_api()


hide_footer = """
    <style>
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_footer, unsafe_allow_html=True)

# pages
home = st.Page("views/home.py", title="Home")
arbitrum = st.Page("views/arbitrum.py", title="Arbitrum")
base = st.Page("views/base.py", title="Base")

# navigation
pages = {
    "": [home],
    "Chains": [arbitrum, base],
}
nav = st.navigation(pages)
nav.run()
