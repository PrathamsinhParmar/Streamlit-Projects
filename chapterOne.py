import streamlit as st

st.title("Hello, My First Streamlit App")
st.subheader("Prathamsinh Parmar")
st.write("Drs. Kiran & Pallavi Patel Global University")
st.text("KPGU")


language = st.selectbox("Select your Favourite language : ", ["Python" , "Java" , "JavaScript" , "C" , "C++", "NULL"])

st.write(f"Your favourite language is {language}")

if(language != "NULL"):
    st.success("Language Selected !")    # Gives message in green(.success) box
else:
    st.error("Error Occured !")    # Gives message in red(.error) box