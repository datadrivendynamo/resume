import streamlit as st
from docx import Document
import time

st.set_page_config(page_title='Resume Scorer', initial_sidebar_state="collapsed", layout="wide")
def space(n):
    for i in range(n):
        st.markdown(" ")
def read_docx(file):
    doc = Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)
c1,c2,c3 = st.columns([2,3,2])
with c2:
    st.markdown("<h2 style='text-align: center; color: white ; '><b>Upload your Resume</b></h2>", unsafe_allow_html=True)
    resume= st.file_uploader("",type=".docx")
    if resume is not None:
        with st.spinner('Uploading resume...'):
            time.sleep(4)
        st.success("Resume uploaded successfully")
