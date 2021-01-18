import streamlit as st
import numpy as np
import joblib 
import pickle

model1= pickle.load(open('RF.pkl', 'rb'))
model2=joblib.load('XGB.dat')

def main():
    st.title('Vehicle Price Prediction App')
    st.write('''This app has been made using STREAMLIT framework to predict the Selling price of your Vehicle based on the inputs. Let's Start!''')
    st.header('Please choose a model for Prediction')
    page=st.sidebar.selectbox('ML Models',['Random Forest','XGBoost'])
    
    if page=='Random Forest':
        
        html_temp = """
         <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Vehicle Selling-Price prediction app</h2>
        </div>
        """
        st.markdown(html_temp,unsafe_allow_html=True)
        Year = st.text_input("Year of Vehicle Bought","e.g 2021")
        Present_Price = st.text_input("Showroom price of the Vehicle (in lakhs)","e.g 5.29")
        Kms_Driven = st.text_input("Kms_driven","e.g 3000")
        Fuel_type = st.selectbox("Fuel type",['Petrol','Diesel','CNG'])
        Seller_type = st.selectbox("Seller type",['Individual','Dealer'])
        Transmission = st.selectbox("Transmission type",['Manual','Automatic'])
        result=""
        if st.button("Predict"):
            result=Price_prediction_RF(Present_Price,Kms_Driven,Year,Fuel_type,Seller_type,Transmission)
        st.success('You should sell the vehicle in {} lakhs'.format(result))
    else:
        html_temp = """
         <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Vehicle Selling-Price prediction app</h2>
        </div>
        """
        st.markdown(html_temp,unsafe_allow_html=True)    
        Year = st.text_input("Year of Vehicle Bought","e.g 2021")
        Present_Price = st.text_input("Showroom price of the Vehicle (in lakhs)","e.g 5.29")
        Kms_Driven = st.text_input("Kms_driven","e.g 3000")
        Fuel_type = st.selectbox("Fuel type",['Petrol','Diesel','CNG'])
        Seller_type = st.selectbox("Seller type",['Individual','Dealer'])
        Transmission = st.selectbox("Transmission type",['Manual','Automatic'])
        result=""
        if st.button("Predict"):
            result=Price_prediction_XGB(Present_Price,Kms_Driven,Year,Fuel_type,Seller_type,Transmission)
        st.success('You should sell the vehicle in {} lakhs'.format(result))

@st.cache
def Price_prediction_RF(Present_Price,Kms_Driven,Year,Fuel_type,Seller_type,Transmission):
    Vehicle_Age=2020-int(Year)
    if (Fuel_type=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    elif (Fuel_type=='Diesel'):
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0
    if (Seller_type=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0
    if (Transmission=='Manual'):
        Transmission_Manual=1
    else:
        Transmission_Manual=0
    prediction=model1.predict([[Present_Price,Kms_Driven,Vehicle_Age,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
    output=round(prediction[0],3)
    print(output)
    return output

@st.cache
def Price_prediction_XGB(Present_Price,Kms_Driven,Year,Fuel_type,Seller_type,Transmission):
    Vehicle_Age=2020-int(Year)
    if (Fuel_type=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    elif (Fuel_type=='Diesel'):
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0
    if (Seller_type=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0
    if (Transmission=='Manual'):
        Transmission_Manual=1
    else:
        Transmission_Manual=0
    a=[Present_Price,Kms_Driven,Vehicle_Age,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]
    prediction=model2.predict(np.array(a).reshape(1,-1))
    output=np.round(prediction[0],3)
    print(output)
    return output

if __name__=='__main__':
    main()