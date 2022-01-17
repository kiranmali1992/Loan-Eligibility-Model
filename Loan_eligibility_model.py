import pickle
import streamlit as st
import numpy as np


#loading the model

loaded_model = pickle.load(open("trained_logistic_model.sav","rb"))


def Prediction(input_value):

    #convert it into array
    input_value = np.array(input_value).reshape(1,-1)

    Prediction = loaded_model.predict(input_value)
    
    if(Prediction[0] == 1):
      return "You are eligible for loan"
    else:
      return "Sorry you are not eligible for loan"
      
def main():
    input_data = []

    st.markdown(f'<h1 style="color:#faca2b;font-size:40px;">{"Wellcome to Loan Eligibility Prediction Model"}</h1>', unsafe_allow_html=True)
    image = Image.open('C:/Users/Kiran/Desktop/Jupyter_ notebook/ML_project/loan.jpg')

    st.image(image,width = 700)
    

    st.markdown(f'<h1 style="color:#0066cc;font-size:20px;">{"Please Enter your Detail"}</h1>', unsafe_allow_html=True)

#1......................
    gender = st.selectbox("Gender",("Male","Female"))


    if gender == "Male":
        input_data.append(1)
    else:
        input_data.append(0)
#2........................

    
    
    Married = st.selectbox("Married",("yes","No"))

    if Married == "yes":
        input_data.append(1)
    else:
        input_data.append(0)
#3....................

    Dependent = st.text_input("Dependent")
    input_data.append(Dependent)
    
#............................
    Education = st.selectbox("Education",("Graduate","Undergraduate"))
    
    if Education == "Graduate":
      input_data.append(0)
    else:
        input_data.append(1)
        
#4..........................

    Self_employed = st.selectbox("Self Employed" ,("yes","No"))
    

    if Self_employed == "yes":
        input_data.append(1)
    else:
        input_data.append(0)
#5.................

    Income = st.text_input("Income (Monthly)")
    input_data.append(Income)
#6....................

    Coapplicant_income = st.text_input("Coapplicant Income")

    input_data.append(Coapplicant_income)
#7..........................
    Loan_amount = st.text_input("Loan Amount (Monthly)")
    input_data.append(Loan_amount)
#8..................

    loan_amount_term = st.text_input("Loan Amount Term")
    input_data.append(loan_amount_term)

#........................
    
    Crediatial_history = st.selectbox("Credit History",(1,0))
    input_data.append(Crediatial_history)
#10............................

    Property = st.selectbox("Property",("Rural","SemiRural","Urban"))
    if Property == "Rural":
        input_data.append(0)
    elif Property == "Semi-Urban":
        input_data.append(1)
    else:
        input_data.append(2)

    
    #Code for prediction
    check = ""

    #Creating Button
    if st.button("Check"):
        check = Prediction(input_data)
        
    st.success(check)
        

if __name__ == "__main__":
    main()


    

    
    
    











        
        
    





        
