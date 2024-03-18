import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title='Resume Scorer', initial_sidebar_state="collapsed", layout="wide")

page_style = """
<style>
    /* Default style */
    .container {
        max-width: 1000px; /* Adjust maximum width for larger screens */
    }

    /* Media query for smaller screens */
    @media only screen and (max-width: 768px) {
        .container {
            max-width: 90%; /* Adjust maximum width for smaller screens */
        }
    }
</style>
"""

# Apply CSS style to the Streamlit app
st.markdown(page_style, unsafe_allow_html=True)

def space(n):
    for i in range(n):
        st.markdown(" ")

c1, c2, c3, c4= st.columns([2,0.2,4,2.5])
def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)


with c1:
    space(6)
    st.image("logo.png",width=290)
    

with c3:
    space(5)
    st.markdown("<h1 style='text-align: center; color: white ; '>Get your Resume score in less than a minute!</h1>", unsafe_allow_html=True)
# Second column
with c4:
    c1,c2 = st.columns([0.6,3])
    with c2:
        lottie_home = load_lottiefile("lottie_files/a.json")
        st_lottie(lottie_home,
                speed=0.7,
                reverse=False,
                loop=True,
                quality="low",
                height=None,
                width=360,
                key=None)

# Form fields
c1,c2 = st.columns([4,7])
with c1:
    st.markdown("<h1 style='text-align: left; color: white ; '><b>Improve your resume and LinkedIn Profile</b></h1>", unsafe_allow_html=True)
    space(2)
    st.markdown("<h5 style = 'text-align: left; color: white ;'><b>Designed by top recruiters, our AI-powered platform instantly gives you tailored feedback on your resume and LinkedIn profile.</b></h5>", unsafe_allow_html = True)
    space(1)
    st.markdown("<h5 style = 'text-align: left; color: white ;'><b>Land 5x more interviews, opportunities and job offers.</b></h5>", unsafe_allow_html = True)
    space(1)
    a1, a2 = st.columns([3,2])
    with a1:
        with st.container():
            button_style = """
            <style>
                .stButton>button {
                    background-color: #4CAF50; 
                    color: white;
                }
            </style>
            """
            st.markdown(button_style, unsafe_allow_html=True)
            if st.button("Get Started for free >>"):
                st.write("Button clicked!")
    with a2:
        with st.container():
            st.markdown(button_style, unsafe_allow_html=True)
            if st.button("See preview >>"):
                st.write("Button clicked!")
    lottie_home1 = load_lottiefile("lottie_files/b.json")
    st_lottie(lottie_home1,
              speed=0.7,
              reverse=False,
              loop=True,
              quality="low",
              height=None,
              width=550,
              key=None)
with c2:
    st.image('sketch.png',width=1200)
space(3)
st.markdown("---")
space(2)
st.markdown("<h1 style = 'text-align: center; color: white ;'><b>Your personal resume & LinkedIn coach</b></h1>", unsafe_allow_html = True)
space(2)
st.markdown("<h5 style = 'text-align: center; color: white ;'><b>Join over 1 million experienced professionals, graduates and students who have used Resume Worded's </b></h5>", unsafe_allow_html = True)
st.markdown("<h5 style = 'text-align: center; color: white ;'><b>toolkit to get ahead in their careers. </b></h5>", unsafe_allow_html = True)

space(2)
c1,c2,c3= st.columns([2.5,4,2.5])

with st.container():
    tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10,tab11,tab12,tab13,tab14,tab15,tab16,tab17,tab18,tab19,tab20,tab21,tab22,tab23,tab24,tab25,tab26,tab27,tab28,tab29,tab30,tab31,tab32,tab33,tab34,tab35,tab36,tab37,tab38,tab39,tab40,tab41,tab42,tab43,tab44,tab45,tab46,tab47,tab48,tab49,tab50,tab51,tab52,tab53,tab54= st.tabs(["         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","INSTANT RESUME REVIEW","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ", "RESUME SAMPLES","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ", "RESUME TARGETTING","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ", "LINKEDIN OPTIMIZATION"])
    with tab18:
        space(5)
        c1,c2,c3 = st.columns([5,0.5,5])
        with c1:
            st.video("IRR.mp4")
        with c3:
            space(6)
            st.markdown("<h3 style = 'text-align: center; color: white ;'><b>Get expert feedback on your resume, instantly.</b></h3>", unsafe_allow_html = True)
            st.markdown("<h5 style = 'text-align: center; color: white ;'><b>Score My Resume scores your resume on key criteria recruiters and hiring managers look for. Upload your resume and in just 30 seconds, you'll get actionable steps to revamp your resume and land more interviews.</b></h5>", unsafe_allow_html = True)
            space(1)
            c1,c2,c3 = st.columns([3,3,2])
            with c2:
                st.markdown(button_style, unsafe_allow_html=True)
                if st.button("Upload resume >>"):
                    st.write("Button clicked!")

    with tab30:
        space(5)
        c1,c2,c3 = st.columns([5,0.5,5])
        with c1:
            st.video("RS.mp4")
        with c3:
            space(6)
            st.markdown("<h3 style = 'text-align: center; color: white ;'><b>Examples from top resumes</b></h3>", unsafe_allow_html = True)
            st.markdown("<h5 style = 'text-align: center; color: white ;'><b>Successful job applicants have already spent hours crafting the perfect resume lines that got them interviews at top-tier companies. Find a line similar to your own experience, tweak it and use it in your resume.</b></h5>", unsafe_allow_html = True)
            space(1)
            c1,c2,c3 = st.columns([1.2,2,0.4])
            with c2:
                st.markdown(button_style, unsafe_allow_html=True)
                if st.button("See resume samples >>"):
                    st.write("Button clicked!")
    
    with tab42:
        space(5)
        c1,c2,c3 = st.columns([5,0.5,5])
        with c1:
            st.image("RT.png")
        with c3:
            space(6)
            st.markdown("<h3 style = 'text-align: center; color: white ;'><b>Target your resume to a job, instantly.</b></h3>", unsafe_allow_html = True)
            st.markdown("<h5 style = 'text-align: center; color: white ;'><b>Our free AI-powered platform analyzes the job description and identifies important keywords and skills missing from your resume. Learn how to tailor your resume to a specific job and land more interviews.</b></h5>", unsafe_allow_html = True)
            space(1)
            c1,c2,c3 = st.columns([1.2,2,0.4])
            with c2:
                st.markdown(button_style, unsafe_allow_html=True)
                if st.button("Target your resume >>"):
                    st.write("Button clicked!")
    
    with tab54:
        space(5)
        c1,c2,c3 = st.columns([5,0.5,5])
        with c1:
            st.image("LO.png")
        with c3:
            space(6)
            st.markdown("<h3 style = 'text-align: center; color: white ;'><b>Get found by the right people on LinkedIn</b></h3>", unsafe_allow_html = True)
            st.markdown("<h5 style = 'text-align: center; color: white ;'><b>Instantly get tailored feedback on how to optimize your LinkedIn profile, for free. Generate 5x more jobs, leads and opportunities.</b></h5>", unsafe_allow_html = True)
            space(1)
            c1,c2,c3 = st.columns([1,2,0.4])
            with c2:
                st.markdown(button_style, unsafe_allow_html=True)
                if st.button("Optimize LinkedIn profile >>"):
                    st.write("Button clicked!")


space(10)
c1,c2 = st.columns([4.4,2])
with c2:
    st.text("Credits: Text, Images and videos sourced from https://resumeworded.com")
    st.text("For project purpose only")
