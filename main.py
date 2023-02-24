import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days.")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))


if place:
    if days == 1:
        subheader_title = f"{option} for the next day in {place}"
    else:
        subheader_title = f"{option} for the next {days} days " \
                          f"in {place}"

    st.subheader(subheader_title)

    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [lst['main']['temp']-273.15 for lst in filtered_data]
            dates = [lst['dt_txt'] for lst in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates",
                                                              "y": "Temperature (C)"})
            st.plotly_chart(figure)
        else:
            sky_condition = [lst['weather'][0]['main'] for lst in
                             filtered_data]
            images = {'Clear': "images/clear.png",
                      'Clouds': "images/cloud.png",
                      'Rain': "images/rain.png", 'Snow': "images/snow.png"}
            img_paths = [images[state] for state in sky_condition]
            st.image(img_paths, width=115)

    except KeyError:
        st.write("You entered a place that does not exist!")

