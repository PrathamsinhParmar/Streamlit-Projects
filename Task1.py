import streamlit as st

currentDate = st.date_input("Current Date :")

userDob = st.date_input("Enter Your Date Of Birth : ")

userAge = (currentDate - userDob).days // 365
st.write(f"Your Age is : {userAge} Years")