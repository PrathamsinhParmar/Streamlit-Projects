import streamlit as st

st.sidebar.title("Voter Details ")
name = st.sidebar.text_input("Enter Your Name ")
age = st.sidebar.number_input("Enter Your Age ", min_value=18 , max_value=80, step=1 )
gender = st.sidebar.radio("Gender", ["Male", "Female", "Other"])
location = st.sidebar.selectbox("Select Your Location ", ["Karjan", "Miyagam", "Sarsavani", "Karamdi", "Anastu", "Shinor"])



st.title("Vote For Your Leader ")
col1 , col2, col3 = st.columns(3)


with col1:
    st.header("BJP")
    st.subheader("Satish Nishdiya")
    st.image("https://images.bhaskarassets.com/web2images/960/2023/02/21/sathish_1676963719.jpg" , width=200)
    if st.button("Vote BJP" , key = "bjp"):
        st.success(f"Thank you for voting for BJP, {name if name else "User"}!")
        vote = "BJP"

with col2:
    st.header("Congress")
    st.subheader("Akshay Patel")
    st.image("https://tse1.mm.bing.net/th/id/OIP.RSL_xrJA0h4JgkT4ELTC4AHaE8?pid=Api&P=0&h=180" , width=200)
    if st.button("Vote Congress", key="congress"):
        st.success(f"Thank you for voting for Congress, {name if name else "User"}!")
        vote = "Congress"

with col3:
    st.header("AAP")
    st.subheader("Arvind Kejriwal")
    st.image("https://tse2.mm.bing.net/th/id/OIP.Xosstq8WKQ5CUKTtrChmXQHaEc?pid=Api&P=0&h=180" , width=200)
    if st.button("Vote APP", key="app"):
        st.success(f"Thank you for voting for APP, {name if name else "User"}")
        vote = "APP"

if name: 
    st.write(f"Welcome, {name}")


with st.expander("Voteing Guidelines "):
    st.write("""
    1. You must be a registered voter to cast your vote.
    2. Voting is confidential. Your choice will not be shared with anyone.
    3. You can only vote once. Multiple votes will be discarded.
    4. Please provide accurate information when registering.
    5. If you encounter any issues, contact support.
    """)    


with st.expander("Voter Information", expanded=True):
    st.write(f"Name: {name if name else 'Voter'}")
    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")
    st.write(f"Location: {location}")
    st.write(f"You voted for: {vote if 'vote' in locals() else 'No vote cast yet'}")