import pickle
import streamlit as st
f1=open("model_heart.pkl","rb") # File open command
model=pickle.load(f1)
f1.close()
st.title("Heart Disease Prediction")
st.markdown("""
This app predicts whether a person is likely to have **heart disease** based on several medical parameters.
Please enter the values below and click **Detect the Heart Disease**.
""")
age=st.text_input("enter age")
sex_option = st.radio("Select Gender: ", ('Male', 'Female'))
sex = 1 if sex_option == 'Male' else 0
cp_option = st.radio(
    "Select Chest Pain Type:",
    options=["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"]
)
cp_dict = {
    "Typical angina": 0,
    "Atypical angina": 1,
    "Non-anginal pain": 2,
    "Asymptomatic": 3
}
cp = cp_dict[cp_option]
rbp=st.text_input("enter resting blood pressure (mm Hg)")
chol=st.text_input("enter cholestrol (mg/dl)")
fbs_option = st.radio(
    "Is Fasting Blood Sugar > 120 mg/dl?",
    options=["Yes", "No"]
)
fbs = 1 if fbs_option == "Yes" else 0
ecg_option = st.radio(
    "Resting ECG Results",
    options=[
        "Normal",
        "ST-T wave abnormality",
        "Left ventricular hypertrophy"
    ]
)
ecg = {
    "Normal": 0,
    "ST-T wave abnormality": 1,
    "Left ventricular hypertrophy": 2
}[ecg_option]
mhr=st.text_input("enter maximum heart rate (BPM)")
eia = st.radio("Exercise Induced Angina", ["Yes", "No"])
eia = 1 if eia == "Yes" else 0
std=st.text_input("enter ST depression induced by exercise compared to rest(0.0-6.2)")
sts_option = st.radio("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
sts = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}[sts_option]
nmv_option = st.radio("Number of Major Vessels Colored by Fluoroscopy", ["0", "1", "2", "3"])
nmv = int(nmv_option)
thalium_option = st.radio("Thalassemia Type", ["Fixed Defect", "Normal", "Reversible Defect"])
thalium = {"Fixed Defect": 1, "Normal": 2, "Reversible Defect": 3}[thalium_option]
if st.button("detect the heart disease"):
    disease=model.predict([[int(age),int(sex),int(cp),int(rbp),int(chol),int(fbs),int(ecg),int(mhr),int(eia),float(std),int(sts),int(nmv),int(thalium)]])[0]
    if disease == 1:
        st.error("Heart Disease Detected! Please consult a doctor.")
        st.snow()
        st.markdown("[👉 Click here to learn more about heart health](https://www.cdc.gov/heartdisease/about.htm)")
    else:
        st.success("No Heart Disease Detected! You seem to be healthy.")
        st.balloons()
