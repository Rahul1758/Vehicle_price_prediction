import app1
import app2
import streamlit as st
PAGES = {
    "Random Forest": app1,
    "XGBoost": app2
}
st.title('Select a ML model for Prediction')
st.sidebar.title('ML Model')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
