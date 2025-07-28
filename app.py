
import streamlit as st
from recommender import WorkoutRecommender

# Load recommender
recommender = WorkoutRecommender("workouts.csv")

st.set_page_config(page_title="FitHub AI", page_icon="🏋️")
st.title("🏋️ FitHub AI – Personalized Fitness Coach")
st.markdown("Get a personalized workout plan based on your fitness goal!")

# User input
user_goal = st.text_input("Describe your goal (e.g., 'I want to lose weight', 'build muscle')")

if st.button("Get Recommendation"):
    if user_goal.strip():
        plan = recommender.recommend(user_goal)
        st.success("💪 Here's a plan for you!")
        st.markdown(f"**Workout:** {plan['workout']}")
        st.markdown(f"**Goal:** {plan['goal'].capitalize()}")
        st.markdown(f"**Duration:** {plan['duration']}")
        st.markdown(f"**Equipment:** {plan['equipment']}")
        st.markdown(f"**Difficulty:** {plan['difficulty']}")
    else:
        st.warning("Please enter your goal to get a recommendation.")
