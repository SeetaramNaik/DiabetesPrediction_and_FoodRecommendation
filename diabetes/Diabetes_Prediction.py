import streamlit as st
import Login_and_Registration
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import pdfkit
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition


pickle_in = open('logisticRegr.pkl', 'rb')
classifier = pickle.load(pickle_in)

# st.set_page_config(page_title = "Diabetes Prediction")
st.set_page_config(layout="wide")




def Diabetes_Predict():
    # st.button('LOGOUT')
    # Display user data
    # st.write(st.session_state["user_data"])
    username=st.session_state["user_data"][0]
    # st.subheader(f"Welcome!!! {username} ")
    html_temp = """
    <div style="background-color:tomato;padding:1.5px">
    <h1 style="color:white;text-align:center;">Diabetes Prediction System 💉</h1>
    </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
 
    msg= f"""
       <div style="background-color:#666565;padding:3px;display:flex;align-items:center;justify-content:center;border-radius:10px;">
       <h3 style="margin:auto;text-align:center;"> Logged in as \t <span> {username}</span><h5>
       
       </div><br>
    """
   
    # st.sidebar.header(f'Welcome!!! {username}')
    # st.sidebar.markdown(msg,unsafe_allow_html=True)
    
    if st.sidebar.button('LOGOUT🔁'):
    # Clear user data from session state
        # st.session_state.pop("user_data", None)
        # Login_and_Registration.loginAndRegister()
        Login_and_Registration.loginAndRegister()
        st.session_state.logged_in = False
        st.session_state['user_data'] = None
        
        st.success('Logged out successfully.')
        return True
        

        # st.stop()
    
    st.sidebar.header('Diabetes Prediction System')
    name = st.text_input("Enter your Name:",value=username)
    pregnancy = st.number_input("No. of times pregnant:",step=1.)
    glucose = st.number_input("Plasma Glucose Concentration :",step=10.)
    bp =  st.number_input("Diastolic blood pressure (mm Hg):",step=10.)
    skin = st.number_input("Triceps skin fold thickness (mm):",step=5.)
    insulin = st.number_input("2-Hour serum insulin (mu U/ml):",step=10.)
    bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):",step=10.)
    dpf = st.number_input("Diabetes Pedigree Function:",step=0.1)
    age = st.number_input("Age:",step=5.)
    submit = st.button('Predict 🔍')
    if submit:
        prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        # html = f"""
        #         <html>
        #             <body>
        #                 <h1>Diabetic Prediction Form</h1>
        #                 <p><strong>Name:</strong> {name}</p>
        #                 <p><strong>Age:</strong> {age}</p>
        #                 <p><strong>Pregnancy:</strong> {glucose}</p>
        #                 <p><strong>Blood Pressure:</strong> {bp}</p>
        #                 <p><strong>Skin fold thickness:</strong> {skin}</p>
        #                 <p><strong>2-hour serun Insulin:</strong> {insulin}</p>
        #                 <p><strong>Body mass index:</strong> {bmi}</p>
        #                 <p><strong>Pedigree function:</strong> {dpf}</p>
        #             </body>
        #         </html>
        #         """
        # # Convert the HTML content to a PDF file
        # pdfkit.from_string(html, "form.pdf")

        # # Create a SendGrid message and attach the PDF file
        # message = Mail(
        #     from_email="19c16@sdmit.in",
        #     to_emails="cturuby@gmail.com",
        #     subject="Diabetic Prediction Form",
        #     html_content="Please find attached the PDF file with your form data.")
        # with open("form.pdf", "rb") as f:
        #     data = f.read()
        # attachment = Attachment(
        #     FileContent(data),
        #     FileName("form.pdf"),
        #     FileType("application/pdf"),
        #     Disposition("attachment")
        # )
        # message.attachment = attachment

        #  # Send the email using SendGrid
        # try:
        #     # sg = SendGridAPIClient("YOUR_API_KEY")
        #     sg=SendGridAPIClient('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')
        #     response = sg.send(message)
        #     st.success("Form submitted successfully. Check your email for the PDF file.")
        # except Exception as e:
        #     st.error("Failed to send the email. Please try again later.")
        #     st.write(str(e))


        #Printing the result
        if prediction == 0:
            st.success(name.upper()+'!!! You are not diabetic 😃')
        else:
            st.warning(name.upper()+'... we are really sorry to say, but it seems like you are Diabetic. ☹️')




