import streamlit as st
import re
import string
import random

st.set_page_config(page_title="Password Strength checker")
st.title("🔓Password Strength checker")
st.markdown("""
## Welcome to Password strength checker
""")

password =st.text_input("Enter your password", type="password")
feedback =[]
score=0
reject_passwords=["password123","hello342","123456789"]

if password:
    if password.lower() in reject_passwords:
        feedback.append("❌This password can't be used - it's in the list of commonly used passwords")
        score = 0
    else:
        if len(password) >=8:
            score+=1
        else:
            feedback.append("❌Password should be atleast 8 characters long.")

        if re.search(r'[A-Z]',password ) and re.search(r'[a-z]', password):
            score +=1
        else:
            feedback.append("❌Password should contain both upper and lower case characters.")

        if re.search(r'[0-9]', password):
            score+=1
        else:
            feedback.append("❌Password should contain atleast one digit.")

        if re.search(r'[!@#$%&]', password):
            score+=1
        else:
            feedback.append("❌Password should contain atleast one special characters(!@#$%&).")

        if score==4:
            feedback.append("✅Your password is strong enough")
        
        elif score==3:
            feedback.append("Your password is medium strenght. It could be more strong")
        
        else:
            special_chars = "!@#$%&"
            characters = string.ascii_letters + string.digits + special_chars
            passwordGive = "".join(random.choice(characters) for _ in range(8))
            feedback.append(f"Your password is weak. Please make it strong. Create password like {passwordGive}")
        
        
        
        

    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please enter password to get started.")
