import base64
import streamlit as st


st.title("Lutadores 🥋")
st.write("Bem-vindo à página dos lutadores!")



def img_to_bytes(img_path):
    img_bytes = None
    with open(img_path, "rb") as f:
        img_bytes = f.read()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

image_path = "fotos/Akira.png"
st.markdown(
    f'<a href="Akira"><img src="data:fotos/Akira.png;base64,{img_to_bytes(image_path)}" width="50"></a>',
    unsafe_allow_html=True
)