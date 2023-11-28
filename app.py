import pickle
import streamlit as st
import streamlit_option_menu 
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('models/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('models/parkinsons_model.sav', 'rb'))

# streamlit init/body

st.set_page_config(page_title='Pulse - ML-powered healthcare',page_icon='assets/applogo.png')

tc1, tc2=st.columns(2)

with tc1:
    st.image('assets/applogo.png')
with tc2:
    st.header("Pulse: A ML-based disease prediction app.")


st.divider()

# sidebar
with st.sidebar:
    sd1,sd2,sd3,sd4=st.columns(4)
    with sd2:
        st.image('assets/applogo.png',width=60)
    with sd3:
        st.header('Pulse')
    sel = option_menu('Our tools:',
                          
                          ['Home',
                            'Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                            menu_icon=['activity'],
                          icons=['house'],
                          default_index=0)


if (sel== 'Home'):
    st.write("Welcome to our machine-learning based disease prediction system - Pulse! Our system is designed to help you identify potential health risks and take proactive measures to prevent them. By leveraging the power of machine learning algorithms, we can accurately predict the likelihood of various diseases based on your symptoms, medical history, and lifestyle. Our system is easy to use and provides quick and reliable results that you can trust. Whether you’re looking to stay healthy or manage an existing condition, our disease prediction web-app is here to help you.")
    
# Diabetes prediction
if (sel == 'Diabetes Prediction'):

    st.title('Diabetes Assessment:\n')
    st.caption("This is the diabetes prediction assessment which relies on a public database. It uses several arguments and determines an outcome based on a trained machine-learning model.\n")

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies',step=1)
        
    with col2:
        Glucose = st.number_input('Glucose Level')
    
    with col3:
        BloodPressure = st.number_input('Blood Pressure')
    
    with col4:
        SkinThickness = st.number_input('Skin Thickness Value')
    
    with col1:
        Insulin = st.number_input('Insulin Level')
    
    with col2:
        BMI = st.number_input('BMI value')
    
    with col3:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value')
    
    with col4:
        Age = st.number_input('Age',step=1)
    
    st.caption("Please note: The prediction generated was presented via machine learning and therefore can be inaccurate; Remember to seek clinical assistance if you suspect you are at risk.")
    
    diab_diagnosis = ''
    
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart disease prediction
if (sel == 'Heart Disease Prediction'):

    st.title('Heart Disease Assessment:')
    st.caption("This is the heart disease prediction assessment which relies on a public database. It uses several arguments and determines an outcome based on a trained machine-learning model.\n")

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        age = st.number_input('Age',step=1)
        
    with col2:
        sex=0
        opt1 = st.selectbox('Sex',
                            ('Male','Female'))
        if opt1=='Male':
            sex=1
        
    with col3:
        cp = st.number_input('Chest Pain types',step=1)
        
    with col4:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col1:
        chol = st.number_input('Serum Cholesterol')
        
    with col2:
        fbs = st.number_input('Fasting Blood Sugar')
        
    with col3:
        restecg = st.number_input('Resting ECG')
        
    with col4:
        thalach = st.number_input('Maximum Heart Rate')
        
    with col1:
        exang = st.number_input('Exercise Angina')
        
    with col2:
        oldpeak = st.number_input('Exercise-induced ST depression')
        
    with col3:
        slope = st.number_input('Slope of ST')
        
    heart_diagnosis = ''
    
    st.caption("Please note: The prediction generated was presented via machine learning and therefore can be inaccurate; Remember to seek clinical assistance if you suspect you are at risk.")

    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's prediction
if (sel == "Parkinsons Prediction"):

    st.title("Parkinson's Disease Assessment:")
    st.caption("This is the Parkinsons disease prediction assessment which relies on a public database. It uses several arguments and determines an outcome based on a trained machine-learning model.\n")

    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP [Fo(Hz)]')
        
    with col2:
        fhi = st.number_input('MDVP [Fhi(Hz)]')
        
    with col3:
        flo = st.number_input('MDVP [Flo(Hz)]')
        
    with col4:
        Jitter_percent = st.number_input('MDVP [Jitter(%)]')
        
    with col5:
        Jitter_Abs = st.number_input('MDVP [Jitter(Abs)]')
        
    with col1:
        RAP = st.number_input('MDVP [RAP]')
        
    with col2:
        PPQ = st.number_input('MDVP [PPQ]')
        
    with col3:
        DDP = st.number_input('Jitter [DDP]')
        
    with col4:
        Shimmer = st.number_input('MDVP[Shimmer]')
        
    with col5:
        Shimmer_dB = st.number_input('MDVP[Shimmer(dB)]')
        
    with col1:
        APQ3 = st.number_input('Shimmer[APQ3]')
        
    with col2:
        APQ5 = st.number_input('Shimmer[APQ5]')
        
    with col3:
        APQ = st.number_input('MDVP[APQ]')
        
    with col4:
        DDA = st.number_input('Shimmer[DDA]')
        
    with col5:
        NHR = st.number_input('NHR')
        
    with col1:
        HNR = st.number_input('HNR')
        
    with col2:
        RPDE = st.number_input('RPDE')
        
    with col3:
        DFA = st.number_input('DFA')
        
    with col4:
        spread1 = st.number_input('Spread 1')
        
    with col5:
        spread2 = st.number_input('Spread 2')
        
    with col1:
        D2 = st.number_input('D2')
        
    with col2:
        PPE = st.number_input('PPE')
        
    st.caption("Please note: The prediction generated was presented via machine learning and therefore can be inaccurate; Remember to seek clinical assistance if you suspect you are at risk.")


    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)