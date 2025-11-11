import streamlit as st

def show():
    st.title("ℹ About This Project")
    st.markdown("""
    ## Body Pose Detection Mini Project  

    This project demonstrates *real-time human pose detection* using  
    - *Python* 🐍  
    - *MediaPipe* 🤖  
    - *OpenCV* 🎥  
    - *Streamlit* 🌐  

    ### Features
    - Detects *Squats* and *Push-ups* using webcam  
    - Counts repetitions automatically  
    - Uses *angles between joints* (Knee for squats, Elbow for pushups)  
    - Live feedback with pose landmarks  

    ### Future Scope
    - Add more exercises (Jumping Jacks, Yoga Poses, etc.)  
    - Save workout stats for progress tracking  
    - Mobile/web deployment  

    🚀 Great project for Fitness tracking!
    """)