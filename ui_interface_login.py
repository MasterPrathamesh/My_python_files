import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo

def main():
    st.set_page_config(page_title="Login Page", page_icon="🔑", layout="centered")
    
    # Custom Styling
    st.markdown("""
        <style>
            .stTextInput > div > div > input {
                font-size: 18px;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            .stButton > button {
                background-color: #4CAF50;
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 8px;
            }
            .stButton > button:hover {
                background-color: #45a049;
            }
            .welcome-text {
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 20px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # App Logo (Optional)
    add_logo("https://upload.wikimedia.org/wikipedia/commons/a/ab/Android_O_Preview_Logo.png", height=80)
    
    st.title("🔐 Welcome to Secure App")
    st.markdown("<p class='welcome-text'>Your Security, Our Priority</p>", unsafe_allow_html=True)
    
    # Toggle between login and sign-up
    option = st.radio("Select an option:", ("Sign In", "Sign Up"))
    
    # User Input Fields
    email = st.text_input("📧 Email Address", placeholder="Enter your email")
    phone = st.text_input("📞 Phone Number", placeholder="Enter your phone number")
    password = st.text_input("🔑 Password", placeholder="Enter your password", type="password")
    show_password = st.checkbox("Show Password")
    remember_me = st.checkbox("Remember Me")
    
    if show_password:
        st.write(f"Your Password: {password}")
    
    if st.button("Proceed"):
        if email and phone and password:
            if option == "Sign In":
                st.success("✅ Logged in successfully!")
                switch_page("Home")  # If you have a home page to navigate to
            else:
                st.success("✅ Account created successfully!")
        else:
            st.error("⚠️ Please fill all the fields!")
    
    # Additional Components
    st.markdown("---")
    st.subheader("Why Choose Us?")
    st.write("✔️ Secure Login System")
    st.write("✔️ Easy and Fast Authentication")
    st.write("✔️ User-Friendly Interface")
    
    st.markdown("---")
    st.caption("© 2025 Secure App. All Rights Reserved.")
    
if __name__ == "__main__":
    main()
