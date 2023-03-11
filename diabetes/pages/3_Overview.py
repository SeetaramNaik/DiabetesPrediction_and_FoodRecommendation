import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np


html_temp = """
<div style="background-color:#748c08;padding:1.5px">
<h1 style="color:white;text-align:center;">Overview of Diabetes 📃</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)


st.title('What is diabetes?')
st.subheader('In this section:')
st.markdown(" 👉:blue[What are the different types of diabetes?]") 
st.markdown(" 👉:blue[How common is diabetes?]") 
st.markdown(" 👉:blue[Who is more likely to develop type 2 diabetes?]")
st.markdown(" 👉:blue[What health problems can people with diabetes develop?]") 
st.markdown(' ')
st.markdown('Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. **:blue[Insulin]**, a **:blue[hormone]** made by the **:blue[pancreas]**, helps glucose from food get into your cells to be used for energy. Sometimes your body doesn’t make enough—or any—insulin or doesn’t use insulin well. Glucose then stays in your blood and doesn’t reach your cells.')
st.markdown(' ')
st.markdown('Over time, having too much glucose in your blood can cause health problems. Although diabetes has no cure, you can take steps to manage your diabetes and stay healthy.')
st.markdown(' ')
st.markdown('Sometimes people call diabetes “a touch of sugar” or “borderline diabetes.” These terms suggest that someone doesn’t really have diabetes or has a less serious case, but every case of diabetes is serious.')

image = Image.open('../images/diabetes.png')

st.image(image, caption='India is often referred to as the "Diabetes Capital of the World", as it accounts for 17%percent of the total number of diabetes patients in the world. There are currently close to 80 million people with diabetes in India and this number is expected to increase to 135 million by 2045.')

st.title("What are the different types of diabetes?")
st.markdown(' ')
st.markdown('The most common types of diabetes are:')
st.markdown('-> Type 1 diabetes')
st.markdown('-> Type 2 diabetes')
st.markdown('-> Gestational diabetes')

st.subheader('a) Type 1 Diabetes')
# st.markdown(' ')
st.markdown('If you have type 1 diabetes, your body does not make insulin. Your immune system attacks and destroys the cells in your pancreas that make insulin. Type 1 diabetes is usually diagnosed in children and young adults, although it can appear at any age. People with type 1 diabetes need to take insulin every day to stay alive.')

st.subheader('b) Type 2 Diabetes')
# st.markdown(' ')
st.markdown('If you have type 2 diabetes, your body does not make or use insulin well. You can develop type 2 diabetes at any age, even during childhood. However, this type of diabetes occurs most often in middle-aged and older people. Type 2 is the most common type of diabetes.')

st.subheader('c) Gestational Diabetes')
# st.markdown(' ')
st.markdown('Gestational diabetes develops in some women when they are pregnant. Most of the time, this type of diabetes goes away after the baby is born. However, if you’ve had gestational diabetes, you have a greater chance of developing type 2 diabetes later in life. Sometimes diabetes diagnosed during pregnancy is actually type 2 diabetes.')

st.subheader('c) other types of Diabetes')
st.markdown('Less common types include monogenic diabetes, which is an inherited form of diabetes, and cystic fibrosis-related diabetes.')
st.markdown(' ')

st.title('How common is Diabetes?')
st.markdown('The rate of diabetes diagnoses is increasing around the world, including in India. India has the second-highest total population in the world at more than 1.3 billion people. The International Diabetes Federation estimated that **:red[72.9 million adults]** in India were living with diabetes in 2017. A 2017 study also found that diabetes prevalenceTrusted Source was higher in urban areas.')

# import matplotlib.pyplot as plt

# # Create sample data
# data = {
#     'category': ['A', 'B', 'C', 'D'],
#     'value': [10, 20, 30, 40],
#     'color': ['red', 'green', 'blue', 'orange']
# }

# # Create horizontal bar chart using matplotlib
# fig, ax = plt.subplots()
# ax.barh(data['category'], data['value'], color=data['color'])

# # Set chart title and axis labels
# ax.set_title('My Horizontal Bar Chart')
# ax.set_xlabel('Value')
# ax.set_ylabel('Category')

# # Display chart using Streamlit
# st.pyplot(fig)


import matplotlib.pyplot as plt

# # Define data
# categories = ['B', 'C', 'D','Diabetic retinopathy treatment can regain normal vision']
# values = [10, 20, 30, 40]
# colors = ['#FF5733', '#FFC300', '#DAF7A6', '#C70039']

# # Create figure and axis objects
# fig, ax = plt.subplots()

# # Create bar chart
# ax.barh(categories, values, color=colors)

# # Set chart title and axis labels
# ax.set_title('My Bar Chart')
# ax.set_xlabel('Category')
# ax.set_ylabel('Value')

# # Display chart using Streamlit
# st.pyplot(fig)




# Define data
# categories = ['Diabetes is more among rich people',
#               'Diabetes can be cured by proper diet control',
#               'Diabetics are more likely to develop\n eye problems than non-diabetics',
#               'All diabetics should have a periodic\n eye examination once in a year',
#               'Diabetes can cause blindness',
#               'Diabetic retinopathy can be\n cured with laser treatment',
#               'Diabetes retinopathy treatment \ncan regain normal vision']
# values1 = [80, 80, 30, 40,60,40,10]
# values2 = [10, 30, 10, 50,10,20,20]
# values3 = [20, 30, 10, 50,10,20,30]
# values4 = [30, 0, 0, 0, 0, 0, 40]
# values5 = [30, 0, 0, 0, 0, 0, 50]

# colors1 = ['red', 'blue', 'green', 'yellow','purple']
# # colors1 = ['#FF5733', '#FFC300', '#DAF7A6', '#C70039']
# colors2 = ['#3366CC', '#DC3912', '#FF9900', '#109618']
# colors3 = ['pink', '#3366CC', '#FF9900', '#109618']
# colors4 = [ 'grey','#3366CC', '#DC3912', '#109618']
# colors5 = ['skyblue', '#FFC300', '#DAF7A6', '#C70039']

# # Create figure and axis objects
# fig, ax = plt.subplots()

# # Create horizontal bar chart for each color and stack them
# ax.barh(categories, values1, color=colors1)
# ax.barh(categories, values2, color=colors2, left=values1)
# ax.barh(categories, values3, color=colors3, left=values2)
# ax.barh(categories, values4, color=colors4, left=values3)
# ax.barh(categories, values5, color=colors5, left=values4)

# # Set chart title and axis labels
# ax.set_title('My Bar Chat')
# ax.set_xlabel('Value')
# ax.set_ylabel('Category')

# # Display chart using Streamlit
# st.pyplot(fig)


# st.markdown('🟥: gdg ')
# st.markdown('🟦: dfd')
# st.markdown('🟩: dff')
# st.markdown('🟨: sdf')
# st.markdown('🟪: fds')



import altair as alt

# Get the data from the user



# uploaded_file = st.file_uploader("Choose a file")

# # Read the data into a pandas DataFrame
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     # Convert year column to datetime type
#     df['year'] = pd.to_datetime(df['year'], format='%Y')

#     # Create a line chart using Altair
#     chart = alt.Chart(df).mark_line().encode(
#         x=alt.X('year', axis=alt.Axis(title='Year')),
#         y=alt.Y('population_diabetes', axis=alt.Axis(title='Population Diabetes')),
#         tooltip=[alt.Tooltip('year', format='%Y'), alt.Tooltip('population_diabetes', format=',')]
#     ).properties(
#         width=700,
#         height=400
#     )

#     # Show the chart in Streamlit
#     st.altair_chart(chart, use_container_width=True)



df = pd.read_csv('../data/analysis.csv')

# Convert year column to datetime type
df['year'] = pd.to_datetime(df['year'], format='%Y')

# Create a line chart using Altair
chart = alt.Chart(df).mark_line().encode(
x=alt.X('year', axis=alt.Axis(title='Year')),
y=alt.Y('population_diabetes', axis=alt.Axis(title='Population Diabetes')),
tooltip=[alt.Tooltip('year', format='%Y'), alt.Tooltip('population_diabetes', format=',')]
).properties(
width=700,
height=400
)

# Show the chart in Streamlit
st.altair_chart(chart, use_container_width=True)
# st.markdown('<center>**:red[Diabetes report of India 2000-2045]**</center>', unsafe_allow_html=True)
st.markdown("<center><span style='color:green'>Diabetes report of India 2000-2045</span></center>", unsafe_allow_html=True)

st.markdown(' ')
st.title('Who is more likely to develop type 2 diabetes?')
st.markdown('You are more likely to develop type 2 diabetes if you are age 45 or older, have a family history of diabetes, or are overweight. Physical inactivity, race, and certain health problems such as high blood pressure also affect your chance of developing type 2 diabetes. You are also more likely to develop type 2 diabetes if you have prediabetes or had gestational diabetes when you were pregnant. Learn more about risk factors for type 2 diabetes.')



st.title('What health problems can people with diabetes develop?')
st.markdown('Over time, high blood glucose leads to problems such as')
st.markdown('🔴 Heart disease')
st.markdown('🔴 Stroke')
st.markdown('🔴 Kidney disease')
st.markdown('🔴 Eye problems')
st.markdown('🔴 Dental disease')
st.markdown('🔴 Nerve damage')
st.markdown('🔴 Foot problems')






