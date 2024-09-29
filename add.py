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
if 'ad_watched' not in st.session_state:
    st.session_state.ad_watched = False

# Page Configuration
st.set_page_config(
    page_title="Charity Donation App",
    page_icon="🔒",
    layout="wide"
)


# Login Page
if not st.session_state.logged_in:
    st.markdown("<h1 class='login-header'>Login</h1>", unsafe_allow_html=True)

    st.markdown("""
        <div class='welcome-text'>
            Welcome back! Please log in to access the Charity Donation App.
        </div>
        <div class='forgot-password'>
            Did you <a href='#'>forget your password?</a>
        </div>
        """, unsafe_allow_html=True)

    # Create a form for login
    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        # Submit button for the form
        login_button = st.form_submit_button('Log In')

        if login_button:  # Check if the button was clicked
            if username in users and users[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success(f"Welcome, {username}!")
                st.experimental_rerun()  # Refresh to show the main app page
            else:
                st.error("Invalid username or password.")

else:
    # Main App Page
    st.title("Charity Donation App")
    st.sidebar.write(f"Logged in as: {st.session_state.username}")
    
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.session_state.ad_watched = False  # Reset the ad watched state
        st.success("Logged out.")
        st.experimental_rerun()  # Refresh to show the login page

    # Main App Container
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    # Create two columns for side-by-side layout
    col1, col2 = st.columns(2)

    col1, spacer, col2 = st.columns([3, 0.25, 1])

    with col1:
        # First Column: Watch an Ad
        st.header("📺 Watch an Ad")
        
        if st.button("Watch Ad to Donate"):
            st.session_state.ad_watched = False  # Reset for a new session
            st.video("https://www.youtube.com/watch?v=J4Zwc6UzxAg&ab_channel=TUCWStudios%7CCatWarriorPlayzlegacy")

            # Simulate waiting for the video to be watched
            time.sleep(10)  # Wait for 10 seconds to simulate watching the full video
            st.session_state.ad_watched = True  # Set the ad watched state
            st.success("Ad finished! Thank you for your support.")

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        # Second Column: Organizations and Funds Raised
        st.header("💰 Organizations and Funds Raised")
        for org, amount in st.session_state.revenue.items():
            st.write(f"**{org}**: ${amount}")

        st.write("### Donate Directly")
        selected_org = st.selectbox("Choose an organization:", list(st.session_state.revenue.keys()))
        donate_amount = st.number_input("Donation amount:", min_value=1, step=1)

        if st.session_state.ad_watched:  # Allow donation only after watching the ad
            if st.button("Donate"):
                st.session_state.revenue[selected_org] += donate_amount
                save_revenue(st.session_state.revenue)
                st.success(f"Thank you for donating ${donate_amount} to {selected_org}!")
        else:
            st.warning("Please watch the ad to enable donations.")

    st.markdown("</div>", unsafe_allow_html=True)




# Custom CSS for styling
st.markdown("""
    <style>
    body {
        font-family: 'Times New Roman', sans-serif;
        color: #333333; /* Darker text for better readability */
    }
    .login-header {
        font-size: 36px;
        font-weight: bold;
        color: #B660CD;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .welcome-text {
        font-size: 18px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    .forgot-password {
        text-align: center;
        margin-bottom: 20px;
    }
    .forgot-password a {
        color: #B660CD;
        text-decoration: none;
        font-size: 14px;
    }
    .login-button {
        background: linear-gradient(90deg, #E993E9, #FF75D8); /* Button gradient unchanged */
        color: white;
        padding: 15px;
        border: none;
        border-radius: 5px;  /* Rounded corners */
        width: 100%;  /* Full width */
        cursor: pointer;
        font-size: 18px;
        font-weight: bold;
        text-align: center;  /* Centered text */
        display: block;  /* Block element for full width */
        margin-top: 10px;  /* Space above the button */
    }
    # .login-button:hover {
    #     background: #FFFFFF;
    # }
    .main-container {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
        border-bottom: solid;
    }
    .section {
        margin-bottom: 40px;  /* Space between sections */
        padding: 120px;  /* Space inside the sections */
        border-radius: 8px;  /* Rounded corners for sections */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
        background-color: white;
    }
            
    h1 {
             margin-bottom: 10px;
        }
    h2 {
        color: #B660CD; /* Changed to specified color */
    }
    # .ad-container {
    #     text-align: center; /* Centered ad section */
    #     margin-bottom: 20px; /* Space below the ad section */
    # }
    </style>
    """, unsafe_allow_html=True)
