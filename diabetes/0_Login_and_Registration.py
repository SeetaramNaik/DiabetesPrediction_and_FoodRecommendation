import streamlit as st
import pandas as pd
import hashlib
import Diabetes_Prediction

# Define a function to read the user data from the CSV file
def read_data():
    data = pd.read_csv("../data/user_data.csv")
    return data

# Define a function to write the user data to the CSV file
def write_data(data):
    data.to_csv("../data/user_data.csv", index=False)

# Create a function to simulate a login check
def simulate_login(username, password):
    if username == "example_user" and password == "example_password":
        return True
    else:
        return False
    
# Function to hash the password using SHA-256 algorithm
def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

# Create a Streamlit app
def loginAndRegister():
    st.title("Login and Register Form")

    # Create a menu with two options: Login and Register
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Select an option", menu)

    # Read the user data from the CSV file
    data = read_data()

    # Define variables for the user inputs
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # If the user selects "Register"
    if choice == "Register":
        # st.title('Register Form')
        confirm_password = st.text_input("Confirm Password", type="password")
        if st.button("Register"):
            # Check if the username is already in use
            if username in list(data["Username"]):
                st.warning("Username already exists. Please choose a different username.")
            # Check if the password and confirm password fields match
            elif password != confirm_password:
                st.warning("Passwords do not match. Please try again.")
            # If the username is new and the passwords match, add the user data to the CSV file
            else:
                hashed_password = hash_password(password)
                new_data = pd.DataFrame({"Username": [username], "Password": [hashed_password]})
                data = pd.concat([data, new_data], axis=0).reset_index(drop=True)
                write_data(data)
                st.success("Registration successful. Please log in.")
    
    # If the user selects "Login"
    elif choice == "Login":
        # st.title('Login Form')
        if st.button("Login"):
            # Check if the username and password are valid
            hashed_password = hash_password(password)
            if (username in list(data["Username"])) and (hashed_password == list(data[data["Username"]==username]["Password"])[0]):
                st.success("Logged in successfully.")
                Diabetes_Prediction.Diabetes_Predict()
                
            
            else:
                st.warning("Incorrect username or password. Please try again.")


loginAndRegister()

