import pandas as pd
import streamlit as st
import pickle

model = pickle.load(open('weight_predictor_model.pkl', 'rb'))

# ------------------------------------------- GUI: starts from here ----------------------------------
# title
st.title('Weight Predictor')
st.divider()

# taking user input
# height
height = st.number_input(
    "Height",
    placeholder="Your height in cm",
    value=None
)

# physical appearance
bmi_class = st.selectbox(
    "Physical Appearnace",
    (
        "Severe Thinness",
        "Moderate Thinness",
        "Mild Thinness",
        "Normal",
        "Overweight",
        "Obese class I",
        "Obese class II",
        "Obese class III"
    ),
    key='Normal'
)
if bmi_class.startswith('Obese'):
    if 'III' in bmi_class:
        bmi_class = bmi_class.replace('III', '3')
    elif 'II' in bmi_class:
        bmi_class = bmi_class.replace('II', '2')
    else:
        bmi_class = bmi_class.replace('I', '1')
    
bmi_class = bmi_class.replace(' ','_').lower()
        
# gender
gender_input = st.radio(
    "Gender",
    ["Male","Female"]
)
gender = 'M' if gender_input == "Male" else 'F'


def predict_my_weight():
    if height == None:
        st.warning("Your height is missing.")
        return
    data = {
        "gender":[gender],
        "height_cm":[height],
        "bmi_class":[bmi_class]
    }

    df = pd.DataFrame(data, index=[1])
    prediction = model.predict(df)

    st.divider()
    st.info(f"Your weight is: {round(prediction[0], 2)} kg")

# button
st.button(
    "Predict my weight",
    on_click=predict_my_weight
)

# ------------------- GUI ends here ---------------------

