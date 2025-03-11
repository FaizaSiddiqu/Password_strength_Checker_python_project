import re                              # importing regular expression module (regax)
import streamlit as st

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.title("🔐Password Strength Checker")
st.markdown("""
## Welcome to the ultimate password strength checker!🔍
 Use the simple tool to check the strength of your password and get suggestions on how to make it stronger.
            we will give you helpful tips to create a **Strong Password** 🔒""")

password = st.text_input("Enter Your Password", type="password")

# Function to check the strength of the password
feedback = []

score = 0

if password:
    if len(password) >= 8:
      score +=1
    else :
        feedback.append("❌Password should be at least 8 characters long.")           # append() methods adds an element to the end of the list
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score +=1
    else:
        feedback.append("❌Password should contain both uppercase and lowercase letters.")   
        
    if re.search(r'\d', password):
        score +=1
    else:
        feedback.append('❌Password should contain at least one number.') 
        
    if re.search(r'[!@#$%^&]', password):
        score +=1
    else:
        feedback.append('❌Password should contain at least one special character (!@#$%^&).')
    if score == 4:
        feedback.append("✅Your password is strong!🎉")
    elif score == 3:
        feedback.append("🔶Your password is medium strength.")
    else:
        feedback.append("🔴Your password is weak. Please make it stronger.")
    
    if feedback :
        st.markdown("## Suggestions to make your password stronger:")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter a password to get started.")