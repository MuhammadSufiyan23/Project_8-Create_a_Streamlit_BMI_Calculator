# PROJECT: 8
# BMI CLACULATOR PROJECT        

import streamlit as st
import time  

st.set_page_config(page_title="BMI Calculator", page_icon="🤩", layout="centered")
st.title("🧮 BMI Calculator")
st.markdown(""" 
## 📏 Apna Body Mass Index (BMI) Calculate Karen  
Nechay Apna **⚖️ Weight Aur 📏 Height** Enter Karen:
""")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("⚖️ Weight (Kg):", min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("📏 Height (m):", min_value=0.5, format="%.2f")

if weight and height:  
    bmi = weight / (height ** 2)
    
    time.sleep(1)  
    
    st.subheader("📊 Apka BMI Hai:")
    st.metric(label="💪 BMI", value=f"{bmi:.2f}")

    if bmi < 18.5:
        st.error("⚠️ Underweight 😟")
    elif 18.5 <= bmi <= 24.9:
        st.success("✅ Normal Weight 😃")    
    elif 25 <= bmi < 29.9:
        st.warning("⚠️ Overweight 🤔")
    else:
        st.error("🚨 Obesity 😞")

else:
    st.info("ℹ️ Please enter a valid weight and height.")  
