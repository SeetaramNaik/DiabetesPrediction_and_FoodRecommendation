
import streamlit as st
import pandas as pd


html_temp = """
<div style="background-color:#f2b016;padding:1.5px">
<h1 style="color:white;text-align:center;">Food Recommendation System 🥗</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

# New code for food recommendation


# Load data
foods_df = pd.read_csv('../data/food_dataset.csv')

def check_veg(row):
    if "veg" in row["Veg_Non"].lower():
        return "veg"
    elif "non-veg" in row["Veg_Non"].lower():
        return "non-veg"
    else:
        return "unknown"

# Define function to filter food based on nutrient, disease, and food type
def filter_food(nutrient, disease):
    filtered_food = foods_df[(foods_df['Nutrient'].str.contains(nutrient)) & 
                             (foods_df['Disease'].str.contains(disease)) 
                            #  (foods_df['Veg_Non'].str.contains(food_type))
                            ]
    
    return filtered_food

# Define Streamlit app



# st.title('Food Recommendation System 🥗')
st.success('Welcome! Please provide your preferences for nutrient and disease to receive food recommendations.')

    
    # User input for nutrient, disease, and food type
nutrient = st.selectbox('Select the Nutrient to focus on:', ['fiber', 'vitamin_a', 'calcium', 'magnesium', 'sodium',
       'vitamin_c', 'protien', 'vitamin_e', 'iron', 'selenium',
       'carbohydrates', 'chloride', 'potassium', 'vitamin_d', 'manganese',
       'phosphorus', 'iodine'])
disease = st.selectbox('Choose the Disease:',['diabeties','cancer', 'obesity','hypertension','goitre','anemia','pregnancy',
        'rickets','scurvy','kidney_disease','heart_disease','eye_disease'])
# food_type = st.selectbox('veg', ['veg', 'non-veg'])
    
    # Filter food based on user input
# filtered_food = filter_food(nutrient, disease, food_type)

filtered_food = filter_food(nutrient, disease)

#Testing code
# df=pd.DataFrame(filter_food)
hide=['Meal_Id','Price']
df=filtered_food.drop(columns=hide)


if st.button('FIND FOOD 🔍'):
    if filtered_food.empty:
        st.write('Sorry, no food recommendations found.')
    else:
        st.write('Here are some food recommendations for you:')
        # st.write(filtered_food)
        st.write(df)


    # Display filtered food