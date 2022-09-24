import streamlit as st
from PIL import Image

def About_diamond():

    st.title("All about Diamonds : ")
    image = Image.open('diamond_info.png')
    st.image(image, caption='diamond_info')


    image = Image.open('diamond_info1.png')
    st.image(image, caption='diamond_info1')


    image = Image.open('diamond_info2.png')
    st.image(image, caption='diamond_info2')


    image = Image.open('diamond_info3.png')
    st.image(image, caption='diamond_info3')

    st.title("color : ")
    image = Image.open('color.png')
    st.image(image, caption='color')

    st.title("cut : ")
    image = Image.open('cut.png')
    st.image(image, caption='cut')