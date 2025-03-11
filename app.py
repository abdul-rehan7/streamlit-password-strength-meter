import streamlit as st
import re

# Function to check password strength
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
        return "🟢 Strong 💪", "#28a745"
    elif score == 3:
        return "🟠 Medium ⚖️", "#ff9800"
    else:
        return "🔴 Weak ⚠️", "#ff4d4d"

# Set up page config
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

# Custom styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #141E30, #243B55);
        color: white;
    }
    .stTextInput input {
        background-color: #1e293b;
        color: white;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title with gradient text effect
st.markdown(
    "<h1 style='text-align: center; background: -webkit-linear-gradient(left, #ff416c, #ff4b2b); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🔐 Password Strength Meter</h1>", 
    unsafe_allow_html=True
)

# Password input
password = st.text_input("🔑 Enter your password", type="password", help="Use a mix of letters, numbers, and symbols.")

# Check strength and display result
if password:
    strength, color = check_password_strength(password)
    st.markdown(f"<h3 style='color:{color}; text-align: center;'>{strength}</h3>", unsafe_allow_html=True)
