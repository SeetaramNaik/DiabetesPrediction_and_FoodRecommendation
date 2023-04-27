
import streamlit as st
import pickle

pickle_in = open('E:/FinalYearProject/diabetes/pages/randomForest.pkl', 'rb')
classifier = pickle.load(pickle_in)

# Define the questions and answer options
questions = ["Gender", "Polyuria (Excessive passage of Urine)", "Polydipsia (Excessive thirst)", "Sudden weight loss", "Weakness", "Polyphagia (Feeling of extreme, insatiable hunger)", "Visual blurring", "Itching", "Irritability", "Delayed healing", "Partial paresis (Weakening of a muscle)", "Muscle stiffness", "Alopecia (Baldness)", "Obesity (Excessive amount of body fat)"]
options = {
    "Gender": ["Male", "Female"],
    "Polyuria (Excessive passage of Urine)": ["Yes", "No"],
    "Polydipsia (Excessive thirst)": ["Yes", "No"],
    "Sudden weight loss": ["Yes", "No"],
    "Weakness": ["Yes", "No"],
    "Polyphagia (Feeling of extreme, insatiable hunger)": ["Yes", "No"],
    "Visual blurring": ["Yes", "No"],
    "Itching": ["Yes", "No"],
    "Irritability": ["Yes", "No"],
    "Delayed healing": ["Yes", "No"],
    "Partial paresis (Weakening of a muscle)": ["Yes", "No"],
    "Muscle stiffness": ["Yes", "No"],
    "Alopecia (Baldness)": ["Yes", "No"],
    "Obesity (Excessive amount of body fat)": ["Yes", "No"]
}

# Create the form using Streamlit
# st.title("Predict DIABETES with some simple questions")
html_temp = """
                    <div style="margin-top:30px;background-color:#f5de31;color:#000;padding:1.5px;border-radius:20px;">
                    <h3 style="color:#000;text-align:center;">Predict <span style="color:red;font-size:35px;">DIABETES</span> with some "Simple Questions"</h3>
                    </div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)
Age = st.number_input("Enter your age:",step=10.0)

# Define variables to store the selected options
selected_options = []

# Display the form using Streamlit
i=0
for question in questions:
    st.subheader(question)
    option = st.radio("", options[question],key=i)
    selected_options.append(option)
    i=i+1

# Run the ML model when the user clicks the "Submit" button
if st.button("Submit"):
    # Convert selected_options to a list of integers (age is already an integer)
    selected_options = [Age] + [1 if option == "Yes" else 0 for option in selected_options]
    prediction = classifier.predict([selected_options])

    prediction = classifier.predict([selected_options])[0]
    proba = classifier.predict_proba([selected_options])[0][1] * 100

    if prediction == 0:
        html_temp = """
                    <div style="margin-top:30px;background-color:#748c08;padding:1.5px;border-radius:20px;">
                    <h4 style="color:white;text-align:center;">You are not diabetic 😃</h4>
                    </div><br>"""
        st.markdown(html_temp,unsafe_allow_html=True)
    else:
        html_temp = """
                    <div style="background-color:#ad0f03;padding:1.5px;border-radius:20px;">
                    <h4 style="color:white;text-align:center;">We are really sorry to say, but it seems like you are Diabetic. ☹️</h4>
                    </div><br>"""
        st.markdown(html_temp,unsafe_allow_html=True)

      # Display the probability of being positive
    st.header(f"Probability of being positive:  **:red[{proba:.2f}%]**")
    

#     html_code ="""
# <!DOCTYPE html>
# <html>
# <head>
#   <title>My App</title>
#   <style>
#     .gauge {
#   width: 100%;
#   max-width: 250px;
#   font-family: 'Roboto', sans-serif;
#   font-size: 32px;
#   color: #004033;
# }

# .gauge__body {
#   width: 100%;
#   height: 0;
#   padding-bottom: 50%;
#   background: #b4c0be;
#   position: relative;
#   border-top-left-radius: 100% 200%;
#   border-top-right-radius: 100% 200%;
#   overflow: hidden;
# }

# .gauge__fill {
#   position: absolute;
#   top: 100%;
#   left: 0;
#   width: inherit;
#   height: 100%;
#   background: #009578;
#   transform-origin: center top;
#   transform: rotate(0.25turn);
#   transition: transform 0.2s ease-out;
# }

# .gauge__cover {
#   width: 75%;
#   height: 150%;
#   background: #ffffff;
#   border-radius: 50%;
#   position: absolute;
#   top: 25%;
#   left: 50%;
#   transform: translateX(-50%);

#   /* Text */
#   display: flex;
#   align-items: center;
#   justify-content: center;
#   padding-bottom: 25%;
#   box-sizing: border-box;
# }

#   </style>
# </head>
# <body>
#   <div class="gauge">
#   <div class="gauge__body">
#     <div class="gauge__fill"></div>
#     <div class="gauge__cover"></div>
#   </div>
# </div>
#   <script>
#     const gaugeElement = document.querySelector(".gauge");

#     function setGaugeValue(gauge, value) {
#         if(value < 0 || value > 1) {
#         return;
#         }

#         gauge.querySelector(".gauge__fill").style.transform = `rotate(${value / 2}turn)`;
#         gauge.querySelector(".gauge__cover").textContent = `${Math.round(value * 100)}%`;
# }

# setGaugeValue(gaugeElement, 0.4);

#   </script>
# </body>
# </html>
# """
#     st.html(html_code)



import pandas as pd
import numpy as np

# Define the threshold values for each attribute
age_threshold = 40
bmi_threshold = 30
sex_threshold = 0
family_history_threshold = 0
physical_activity_threshold = 150
diastolic_pressure = 130
systolic_pressure = 80

# Function to predict diabetes based on threshold values
def predict_diabetes(row):
    if row['age'] > age_threshold and row['BMI'] > bmi_threshold and row['sex'] > sex_threshold and row['FamilyHistory'] > family_history_threshold and row['physical_activity'] < physical_activity_threshold and row['systolic_pressure'] > systolic_pressure and row['diastolic_pressure'] > diastolic_pressure :
        return "High Risk"
    else:
        return "Low Risk"
    
html_temp = """
                    <div style="margin-top:30px;background-color:#f5de31;color:#000;padding:1.5px;border-radius:20px;">
                    <h2 style="color:#000;text-align:center;">Form 2</h2>
                    </div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)  
    
age = st.number_input("Enter age:",step=5.)
bmi = st.number_input("Enter BMI (Body mass index):",step=5.)
gender_map = {"Male": 0, "Female": 1}
# Create a selection menu for gender and convert to binary
gender = st.selectbox("Select gender", list(gender_map.keys()))
gender_binary = gender_map[gender]
fh = {"No": 0, "Yes": 1}
family_history = st.selectbox("Do you have any Family History of Diabetes?", list(fh.keys()))
family_history_binary= fh[family_history]
physical_activity = st.number_input("Enter physical activity level (in minutes per week): ",step=10.)
diastolic_pressure = st.number_input("Enter blood pressure history (1st Number):",step=10.)
systolic_pressure = st.number_input("Enter blood pressure history (2nd Number):",step=10.)

submit = st.button('Predict 🔍')

data = {'age': age, 'BMI': bmi, 'sex': gender_binary, 'FamilyHistory': family_history_binary, 'physical_activity': physical_activity, 'diastolic_pressure': diastolic_pressure, 'systolic_pressure': systolic_pressure }
data = pd.DataFrame(data, index=[0]) # Convert dictionary to dataframe

if submit:
    prediction = predict_diabetes(data.iloc[0])
    #if prediction=="High Risk":
    st.header(f"Probability of being positive:  **:red[{prediction}]**")





