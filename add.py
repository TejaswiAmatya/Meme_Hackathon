import streamlit as st
import json
import os
import time

DATA_FILE = 'revenue.json'


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
if 'revenue' not in st.session_state:
    st.session_state.revenue = load_revenue()
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''

st.title("Charity Donation App")

# Login Section
if not st.session_state.logged_in:
    st.header("🔒 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password.")
else:
    st.sidebar.write(f"Logged in as: {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.success("Logged out.")

    # Main App
    col1, col2 = st.columns(2)

    with col1:
        st.header("📺 Watch an Ad")

        # Embed YouTube video in an iframe
        st.video("https://www.youtube.com/watch?v=s7LS5lh0dLQ&ab_channel=LF12")

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
