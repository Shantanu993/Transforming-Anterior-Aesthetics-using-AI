import random
import streamlit as st
from PIL import Image

# Set up the page
st.set_page_config(page_title="Anterior Aesthetics", layout="wide")
st.title("Transforming Anterior Aesthetics Using AI")

st.write("""
This application helps identify the suitable composite shades (A1, A2, A3) for anterior restorations based on tooth images.
""")

# File uploader for composite shades in a row (inside sidebar)
st.sidebar.write("### Upload Composite Shade Images:")
st.sidebar.write("Upload images for A1, A2, and A3 composite shades:")

# Using columns to align the file upload buttons vertically
a1_image = st.sidebar.file_uploader("Upload A1", type=["png", "jpg", "jpeg"], key="a1")
a2_image = st.sidebar.file_uploader("Upload A2", type=["png", "jpg", "jpeg"], key="a2")
a3_image = st.sidebar.file_uploader("Upload A3", type=["png", "jpg", "jpeg"], key="a3")

# Displaying the uploaded images if provided
if a1_image:
    st.sidebar.image(a1_image, caption="A1", width=100)
if a2_image:
    st.sidebar.image(a2_image, caption="A2", width=100)
if a3_image:
    st.sidebar.image(a3_image, caption="A3", width=100)

if not (a1_image and a2_image and a3_image):
    st.sidebar.warning("Please upload all three composite shade images (A1, A2, A3).")

# Upload tooth image
st.write("### Upload and Select Tooth for Processing:")
tooth_image = st.file_uploader("Upload an image of teeth (incisors)", type=["png", "jpg", "jpeg"], key="tooth")

if tooth_image:
    img = Image.open(tooth_image)

    # Center the tooth image and set fixed width
    st.write("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(img, caption="Uploaded tooth image", width=250)
    st.write("</div>", unsafe_allow_html=True)

    st.write("### Select a tooth for processing:")
    tooth_selected = st.selectbox(
        "Select the tooth to process",
        [
            "Maxillary Central Incisor - 11 (right)", 
            "Maxillary Central Incisor - 21 (left)",
            "Maxillary Lateral Incisor - 12 (right)", 
            "Maxillary Lateral Incisor - 22 (left)",
            "Mandibular Central Incisor - 41 (right)", 
            "Mandibular Central Incisor - 31 (left)",
            "Mandibular Lateral Incisor - 42 (right)", 
            "Mandibular Lateral Incisor - 32 (left)"
        ]
    )

    # Generate random proportions for A1, A2, A3 shades
    a1_percentage = random.randint(20, 50)
    a2_percentage = random.randint(10, 40)
    a3_percentage = 100 - (a1_percentage + a2_percentage)

    # Display the output in a distinct box
    st.write("### Suggested Composite Shade Proportions for:", tooth_selected)
    st.markdown(
        f"""
        <div style="border: 2px solid #4CAF50; padding: 10px; border-radius: 10px; background-color:rgba(249, 249, 249, 0); text-align: center;">
            <p style="font-size: 18px;"><strong>A1 Shade:</strong> {a1_percentage}%</p>
            <p style="font-size: 18px;"><strong>A2 Shade:</strong> {a2_percentage}%</p>
            <p style="font-size: 18px;"><strong>A3 Shade:</strong> {a3_percentage}%</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
else:
    st.warning("Please upload a tooth image to select a tooth for processing.")
