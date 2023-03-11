

# Import necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px

# Load the diabetes dataset
df = pd.read_csv("../data/countrywise_data.csv")

# Create a Streamlit app
# st.title("Diabetes Map Chart of the world")
html_temp = """
<div style="background-color:#440270;padding:1.5px">
<h1 style="color:white;text-align:center;">Diabetes Map chart of the world🌎 </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

st.subheader('Diabetes estimates (20-79 y)')

# Create a selectbox for the user to choose the year
year = st.selectbox("Select a Year", ["2000", "2011", "2021", "2030", "2045"])

# Create a choropleth map chart using Plotly Express
fig = px.choropleth(df, locations="Country/Territory", locationmode="country names",
                    color=year, hover_name="Country/Territory", range_color=[0, 20],
                    title=f"Diabetes Prevalence by Country in {year}", width=800, height=600,template = "plotly_dark")
fig.update_layout(geo=dict(showframe=False, showcoastlines=False, projection_type="equirectangular"))

# Display the map chart in Streamlit
st.plotly_chart(fig)

st.markdown("<center><span style='color:yellow'>Diabetes report of all the countries 2000-2045</span></center>", unsafe_allow_html=True)


st.markdown(' ')
st.markdown('According to the International Diabetes Federation, an estimated 463 million people worldwide had diabetes in 2019, representing 9.3% of the global adult population. This figure is expected to rise to 700 million by 2045.')
st.markdown('The prevalence of diabetes varies widely by region, with the highest rates found in low- and middle-income countries. In 2019, the countries with the highest prevalence of diabetes were Tokelau (25.4%), Nauru (24.3%), and Mauritius (22.8%), while the countries with the lowest prevalence were Papua New Guinea (2.8%), Tanzania (2.9%), and Ethiopia (3.1%).')

