import streamlit as st

st.title("Health Suggestion App")
st.subheader("Youar AI Agents That Solves Your Health Issue !")

if st.button("Send"):
    st.success("Message Sent !")

insurence = st.checkbox("Want To Claim Insurence")
if insurence:
    st.write("Insurence Selected")

    insurenceType = st.radio("Select Insurence Type" , ["Health", "Dental", "Vision", "Life"])
    if insurenceType:
        st.write("You Selected : ", insurenceType)  

location = st.selectbox("Select Your Location  ", ["Vadodara", "Surat", "Ahmedavad" , "Rajkot"])
if location:
    st.write("Your Location Is : ", location)


money = st.slider("Select Your Budget", 1000, 100000, 20000)
if money:
    st.write("Your budget is : ", money)


rate = st.number_input("Enter Your Health Issue Rate", min_value=0, max_value=10, step=1)
if rate:
    st.write("Your Health Issue Rate Is : ", rate)


name = st.text_input("Enter Your Name ")
if name:
    st.write(f"Welcome {name}, Your insurence is approved !")



dob = st.date_input("Enter Hospital Admit Date ")
if dob:
    st.write("Your Hospital Admit Date is : ", dob)