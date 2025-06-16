import streamlit as st
from caption_generator import generate_captions
from image_analysis import get_image_context

st.set_page_config(page_title="InstaCaptionPro", page_icon="📸")
st.title("📸 InstaCaptionPro - AI Caption Generator")

image = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])

style = st.selectbox("Choose Caption Style", ["Funny", "Emotional", "Motivational", "Romantic", "Trending"])

if st.button("Generate Captions"):
    if image:
        with open("temp.jpg", "wb") as f:
            f.write(image.read())

        with st.spinner("Analyzing image..."):
            context = get_image_context("temp.jpg")
            captions = generate_captions(context, style)

        st.subheader("📢 Captions:")
        st.write(captions)
    else:
        st.warning("Please upload an image first.")
