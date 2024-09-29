import streamlit as st
import json
import os
import time

# Constants
DATA_FILE = 'revenue.json'


# Functions to load and save revenue data
def load_revenue():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        return {
            "Clean Water Initiative": 0,
            "Education for All": 0,
            "Healthcare Access": 0
        }


def save_revenue(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)


# Simple user database
users = {
    "Tejaswi": "Amatya",
    "user2": "password2"
}

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''
if 'revenue' not in st.session_state:
    st.session_state.revenue = load_revenue()

# Page Configuration
st.set_page_config(
    page_title="Charity Donation App",
    page_icon="🔒",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f5f5f5;
    }
    .login-header {
        font-size: 36px;
        font-weight: bold;
        color: #4B0082;
        text-align: center;
    }
    .welcome-text {
        font-size: 16px;
        color: #707070;
        text-align: center;
        margin-bottom: 10px;
    }
    .forgot-password {
        text-align: center;
        margin-bottom: 20px;
    }
    .forgot-password a {
        color: #E993E9;
        text-decoration: none;
        font-size: 14px;
    }
    .login-button {
        background: linear-gradient(90deg, #E993E9, #FF75D8);
        color: white;
        padding: 10px;
        border: none;
        border-radius: 25px;
        width: 100%;
        cursor: pointer;
        font-size: 18px;
        font-weight: bold;
    }
    .login-button:hover {
        background: linear-gradient(90deg, #FF75D8, #E993E9);
    }
    </style>
    """, unsafe_allow_html=True)

# Title
if not st.session_state.logged_in:
    st.markdown("<h1 class='login-header'>Login</h1>", unsafe_allow_html=True)

    # Welcome text
    st.markdown("""
        <div class='welcome-text'>
            Welcome back! Login to access the Sweet Marketplace.
        </div>
        <div class='forgot-password'>
            Did you <a href='#'>forget your password?</a>
        </div>
        """, unsafe_allow_html=True)

    # Login Form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button('Continue', key='login_button')

    # Handle Login Logic
    if login_button:
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password.")
else:
    # Main App Page
    st.title("Charity Donation App")
    st.sidebar.write(f"Logged in as: {st.session_state.username}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.success("Logged out.")

    # Main App
    col1, col2 = st.columns(2)

    with col1:
        st.header("📺 Watch an Ad")
        st.video("https://www.youtube.com/watch?v=J4Zwc6UzxAg&ab_channel=TUCWStudios%7CCatWarriorPlayzlegacy")

        if st.button("Watch Ad to Donate"):
            with st.spinner('Watching ad...'):
                progress = st.progress(0)
                for i in range(1, 101):
                    time.sleep(0.02)
                    progress.progress(i)
            st.success("Ad finished! Thank you for your support.")

    with col2:
        st.header("💰 Organizations and Funds Raised")
        for org, amount in st.session_state.revenue.items():
            st.write(f"**{org}**: ${amount}")

        st.write("### Donate Directly")
        selected_org = st.selectbox("Choose an organization:", list(st.session_state.revenue.keys()))
        donate_amount = st.number_input("Donation amount:", min_value=1, step=1)

        if st.button("Donate"):
            st.session_state.revenue[selected_org] += donate_amount
            save_revenue(st.session_state.revenue)
            st.success(f"Thank you for donating ${donate_amount} to {selected_org}!")
