import streamlit as st
import time
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo
from PIL import Image
import os
import random

def main():
    st.set_page_config(page_title="Art Gallery", page_icon="🎨", layout="wide")
    
    # Custom Styling
    st.markdown("""
        <style>
            @keyframes fadeIn {
                from {opacity: 0;}
                to {opacity: 1;}
            }
            .fade-in {
                animation: fadeIn 2s ease-in;
            }
            .stTextInput > div > div > input, .stButton > button {
                font-size: 18px;
                padding: 10px;
                border-radius: 8px;
            }
            .stButton > button {
                background-color: #4CAF50;
                color: white;
            }
            .stButton > button:hover {
                background-color: #45a049;
            }
            .gallery-section {
                text-align: center;
                font-size: 22px;
                font-weight: bold;
                margin-top: 20px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # App Logo
    add_logo("https://upload.wikimedia.org/wikipedia/commons/a/a6/Arts_Council_England_logo.png", height=80)
    
    st.title("🎨 Welcome to the Art Gallery")
    st.markdown("<p class='fade-in' style='font-size:20px;'>Experience the beauty of art like never before</p>", unsafe_allow_html=True)
    
    # Authentication
    option = st.radio("Select an option:", ("Sign In", "Sign Up"))
    email = st.text_input("📧 Email Address", placeholder="Enter your email")
    password = st.text_input("🔑 Password", placeholder="Enter your password", type="password")
    remember_me = st.checkbox("Remember Me")
    
    if st.button("Proceed"):
        if email and password:
            if option == "Sign In":
                st.success("✅ Logged in successfully!")
                time.sleep(1)
                switch_page("Gallery")  # Navigating to the gallery
            else:
                st.success("✅ Account created successfully!")
        else:
            st.error("⚠️ Please fill all fields!")

    # Art Gallery
    st.markdown("---")
    st.markdown("<p class='gallery-section'>🖼️ Explore Our Stunning Art Collection</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    image_folder = "art_images"  # Change to your actual image folder
    
    if os.path.exists(image_folder):
        images = os.listdir(image_folder)
        random.shuffle(images)
        for index, img in enumerate(images):
            image_path = os.path.join(image_folder, img)
            image = Image.open(image_path)
            if index % 3 == 0:
                with col1:
                    st.image(image, use_column_width=True)
            elif index % 3 == 1:
                with col2:
                    st.image(image, use_column_width=True)
            else:
                with col3:
                    st.image(image, use_column_width=True)
    else:
        st.warning("No images found! Please add some artwork to the gallery.")
    
    # Additional Features
    st.markdown("---")
    st.subheader("✨ Featured Artists")
    featured_artists = ["🎭 Leonardo da Vinci", "🖌️ Vincent van Gogh", "🎨 Frida Kahlo", "🖼️ Pablo Picasso", "🌅 Claude Monet"]
    for artist in featured_artists:
        st.write(artist)
    
    st.markdown("---")
    st.subheader("📢 Upcoming Events")
    events = [
        "🗓️ Modern Art Exhibition - March 15, 2025",
        "🏆 Annual Painting Contest - April 10, 2025",
        "🎤 Artist Talk: Future of Digital Art - May 20, 2025",
        "🎭 Live Sketching Workshop - June 5, 2025",
        "🖼️ Abstract Art Masterclass - July 12, 2025"
    ]
    for event in events:
        st.write(event)
    
    st.markdown("---")
    st.subheader("🖌️ Art Blog & News")
    st.write("🎨 The Impact of Digital Art in the Modern Era")
    st.write("🖌️ How to Master Watercolor Painting")
    st.write("📸 Photography as an Art Form")
    st.write("🎭 Exploring the World of Surrealism")
    
    st.markdown("---")
    st.caption("© 2025 Art Gallery. All Rights Reserved.")
    
if __name__ == "__main__":
    main()
