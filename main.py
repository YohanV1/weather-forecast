import streamlit as st
import plotly.express as px
from backend import get_data
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

d, t = get_data(place, days, option)

figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperature (C)"})
st.plotly_chart(figure)