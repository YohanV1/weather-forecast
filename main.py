import streamlit as st
import plotly.express as px
from backend import get_data
from datetime import date

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
        dates = [lst['dt_txt'] for lst in filtered_data]
        if option == "Temperature":
            temperatures = [lst['main']['temp'] for lst in filtered_data]
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

            img_label = [date(day=int(dates[i][8:10]),
                       month=int(dates[i][5:7]),
                       year=int(dates[i][0:4])).
                  strftime(f'%a, %b %d {dates[i][11:-3]}')
                         for i in range(days*8)]

            st.image(img_paths, width=115, caption=img_label)

    except KeyError:
        st.write("You entered a place that does not exist!")

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                footer:after{
                visibility: visible;
                content: 'Made by Yohan Vinu';
                display:block;
                position:relative;
                color:grey
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
