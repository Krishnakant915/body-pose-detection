import streamlit as st
import exercise_counter   # our pose detection code
import about              # our about page

st.set_page_config(page_title="Body Pose Detection", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])

# Home Page
if page == "Home":
    st.title("🏋 Body Pose Detection - Exercise Counter")
    st.write("Choose an exercise below and start the live detection.")

    exercise = st.radio("Select Exercise:", ["squat", "pushup"])

    st.info("👉 Press the button below to start detection. "
            "A new webcam window will open. Press *Q* to quit.")

    if st.button("Start Detection"):
        exercise_counter.run_exercise_detection(exercise)

# About Page
elif page == "About":
 about.show()