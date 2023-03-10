import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

pickle_in = open('logisticRegr.pkl', 'rb')
classifier = pickle.load(pickle_in)

# st.set_page_config(page_title = "Diabetes Prediction")
st.set_page_config(layout="wide")


html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Diabetes Prediction System 🩺</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)
with st.sidebar:
    st.experimental_memo()

st.sidebar.header('Diabetes Prediction')
select = st.sidebar.selectbox('Select Form', ['Form 1'], key='1')
if not st.sidebar.checkbox("Hide", False, key='2'):
    # st.title('Diabetes Prediction')
    name = st.text_input("Enter your Name:")
    pregnancy = st.number_input("No. of times pregnant:")
    glucose = st.number_input("Plasma Glucose Concentration :")
    bp =  st.number_input("Diastolic blood pressure (mm Hg):")
    skin = st.number_input("Triceps skin fold thickness (mm):")
    insulin = st.number_input("2-Hour serum insulin (mu U/ml):")
    bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):")
    dpf = st.number_input("Diabetes Pedigree Function:")
    age = st.number_input("Age:")
submit = st.button('Predict 🔍')
if submit:
        prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        if prediction == 0:
            st.success(name.upper()+'!!! You are not diabetic 😃')
        else:
            st.warning(name.upper()+'... we are really sorry to say, but it seems like you are Diabetic. ☹️')