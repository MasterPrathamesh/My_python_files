import streamlit as st
import numpy as np
import pandas as pd
import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the trained model (EfficientFormer)
# Assuming the model is saved as "efficientformer_model.pth"
def load_model():
    model = torch.load("efficientformer_model.pth", map_location=torch.device('cpu'))
    model.eval()
    return model

# Define image transformation
def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

# Class labels
class_labels = ['Cataract', 'Diabetic Retinopathy', 'Glaucoma', 'Normal']

# Streamlit UI
st.set_page_config(page_title="Eye Disease Prediction", layout="wide")
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Upload & Predict", "Data Visualization", "Model Performance"])

# Load model
model = load_model()

if menu == "Home":
    st.title("👁️ Eye Disease Prediction using AI")
    st.markdown("""
    ### Welcome to the Eye Disease Prediction App!
    - Upload an eye image to predict the disease.
    - Explore dataset insights and model performance.
    - Developed using **EfficientFormer** & **Streamlit**.
    """)
    st.image("eye_disease_banner.jpg", use_column_width=True)

elif menu == "Upload & Predict":
    st.title("📤 Upload Eye Image & Get Prediction")
    uploaded_file = st.file_uploader("Upload an Eye Image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        processed_image = preprocess_image(image)
        with torch.no_grad():
            output = model(processed_image)
            predicted_class = torch.argmax(output, dim=1).item()
        
        st.write(f"### Prediction: {class_labels[predicted_class]}")
        
elif menu == "Data Visualization":
    st.title("📊 Data Analysis & Visualization")
    df = pd.read_csv("/content/drive/MyDrive/skin_disease/filtered_metadata.csv")
    
    st.write("### Dataset Sample")
    st.dataframe(df.head())
    
    st.write("### Distribution of Eye Diseases")
    plt.figure(figsize=(10, 5))
    sns.countplot(x='disease', data=df, palette='coolwarm')
    st.pyplot(plt)

elif menu == "Model Performance":
    st.title("📈 Model Performance Metrics")
    st.write("Accuracy, Loss Curves & Confusion Matrix")
    
    # Load performance metrics
    metrics = np.load("model_metrics.npz")
    accuracy = metrics['accuracy']
    loss = metrics['loss']
    cm = metrics['confusion_matrix']
    
    # Display Accuracy & Loss Curves
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].plot(accuracy, label="Accuracy")
    ax[0].set_title("Model Accuracy")
    ax[0].legend()
    ax[1].plot(loss, label="Loss", color='red')
    ax[1].set_title("Model Loss")
    ax[1].legend()
    st.pyplot(fig)
    
    # Display Confusion Matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap="Blues", xticklabels=class_labels, yticklabels=class_labels, fmt="d")
    st.pyplot(plt)

st.sidebar.markdown("---")
st.sidebar.info("Developed by Prathamesh Deshmukh")
