import streamlit as st

st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days.")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
if days == 1:
    subheader_title = f"{option} for the next day in {place}"
else:
    subheader_title = f"{option} for the next {days} days " \
                      f"in {place}"

st.subheader(subheader_title)