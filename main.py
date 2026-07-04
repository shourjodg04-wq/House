import streamlit as st
import numpy as np
import joblib
#uploading the model
model = joblib.load("rf.pkl")
st.title("House Price Prediction")
st.markdown("---")
bedroom = st.number_input("Enter the number of bedroom", min_value = 0)
bathroom = st.number_input("Enter the number of bathroom", min_value = 0)
living_area = st.number_input("Enter the size of living area", min_value = 2000)
condition_of_house = st.number_input("Enter the condition of the house", min_value = 0)
schools = st.number_input("Enter the number of schools nearby", min_value = 0) 

X = [[bedroom, bathroom, living_area, condition_of_house, schools]]

pred = st.button("Predict Price")
if pred == True:
   n = np.array(X)
   price = int(model.predict(n)[0])
   st.write(f"House Price = {price}")
else:
    st.write("Please Predict")

#if pred == True:
    #np_array=np.array(X)
    #price=int(model.predict(np_array)[0])
    #st.write(f"House price={price}")