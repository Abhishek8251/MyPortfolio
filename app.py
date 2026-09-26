import streamlit as st

st.set_page_config(
    page_title="Abhishek Singh | Portfolio",
    page_icon="💻",
    layout="wide"
)

st.title("Hi, I'm Abhishek Singh 👋")

st.subheader("B.Tech CSE Student | Python Developer")

st.write(
    "I am a B.Tech Computer Science student interested in "
    "software development, Python, and building practical projects."
)

st.button("Download Resume")

st.header("About Me")

st.write("""
I am a final-year B.Tech Computer Science student
with an interest in Python development, software engineering,
and problem solving.

I enjoy building practical projects and continuously
improving my technical skills.
""")

st.header("Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Programming")
    st.write("Python")
    st.write("C++")
    st.write("Java")

with col2:
    st.subheader("Database")
    st.write("MySQL")
    st.write("SQL")

with col3:
    st.subheader("Tools")
    st.write("Git")
    st.write("GitHub")
    st.write("VS Code")
    st.write("Streamlit")

    st.header("Projects")

st.subheader("1. File Management System")
st.write("""
A Python Streamlit application for managing files
through a simple web interface.
""")

st.subheader("2. Management App")
st.write("""
A Streamlit-based management application designed
to manage and organize information efficiently.
""")

st.subheader("3. Cybersecurity Threat Detector")
st.write("""
A planned project focused on detecting potential
cybersecurity threats using machine learning concepts.
""")

st.header("Education")

st.subheader("B.Tech — Computer Science & Engineering")

st.write("Final Year Student")
st.write("Expected Graduation: 2027")



st.header("My Resume")

with open("assets/Abhishek_Resume.pdf", "rb") as file:
    resume = file.read()

st.download_button(
    label="📄 Download My Resume",
    data=resume,
    file_name="Abhishek_Resume.pdf",
    mime="application/pdf"
)

st.header("Contact Me")

st.write("📧 Email: as7374532@gmail.com")
st.write("💼 LinkedIn: www.linkedin.com/in/abhishek-singh-3a14312a6")
st.write("🐙 Github: https://github.com/Abhishek8251 ")