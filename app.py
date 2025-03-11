import streamlit as st
import re

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 4:
        return "Strong", "green"
    elif score == 3:
        return "Medium", "orange"
    else:
        return "Weak", "red"

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    strength, color = check_password_strength(password)
    st.markdown(f"### Strength: <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)
