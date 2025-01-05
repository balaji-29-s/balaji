import os
import joblib
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Prediction of Disease Outbreaks", layout="wide", page_icon="🧑‍⚕️")

# Load the saved models
heart_disease_model = joblib.load('heart_disease_model.pkl')
parkinsons_model = joblib.load('parkinsons_model.pkl')

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Prediction of Disease Outbreaks System',
        ['Heart Disease Prediction', "Parkinson's Prediction"],
        menu_icon='hospital-fill',
        icons=['heart', 'person'],
        default_index=0
    )

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Input fields for heart disease prediction
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.selectbox('Sex (0 = Female, 1 = Male)', [0, 1])
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)', [0, 1])
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.selectbox('Exercise Induced Angina (1 = Yes, 0 = No)', [0, 1])
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Number of major vessels colored by fluoroscopy')
    with col1:
        thal = st.text_input('Thalassemia (0 = Normal, 1 = Fixed defect, 2 = Reversible defect)')

    # Prediction button
    if st.button('Heart Disease Test Result'):
        try:
            # Convert inputs to float
            user_input = [float(age), float(sex), float(cp), float(trestbps), float(chol),
                          float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak),
                          float(slope), float(ca), float(thal)]

            # Make prediction
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                st.success('The person is having heart disease')
            else:
                st.success('The person does not have any heart disease')
        except Exception as e:
            st.error(f"Error in input: {e}")

# Parkinson's Prediction Page
if selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    # Input fields for Parkinson's disease prediction
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        rap = st.text_input('MDVP:RAP')
    with col2:
        ppq = st.text_input('MDVP:PPQ')
    with col3:
        ddp = st.text_input('Jitter:DDP')
    with col4:
        shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        apq3 = st.text_input('Shimmer:APQ3')
    with col2:
        apq5 = st.text_input('Shimmer:APQ5')
    with col3:
        apq = st.text_input('MDVP:APQ')
    with col4:
        dda = st.text_input('Shimmer:DDA')
    with col5:
        nhr = st.text_input('NHR')
    with col1:
        hnr = st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        d2 = st.text_input('D2')
    with col2:
        ppe = st.text_input('PPE')

    # Prediction button
    if st.button("Parkinson's Test Result"):
        try:
            # Convert inputs to float
            user_input = [float(fo), float(fhi), float(flo), float(jitter_percent), float(jitter_abs),
                          float(rap), float(ppq), float(ddp), float(shimmer), float(shimmer_db),
                          float(apq3), float(apq5), float(apq), float(dda), float(nhr),
                          float(hnr), float(rpde), float(dfa), float(spread1), float(spread2),
                          float(d2), float(ppe)]

            # Make prediction
            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                st.success("The person has Parkinson's disease")
            else:
                st.success("The person does not have Parkinson's disease")
        except Exception as e:
            st.error(f"Error in input: {e}")