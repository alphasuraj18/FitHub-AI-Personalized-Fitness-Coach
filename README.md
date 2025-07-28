# 🏋️ FitHub AI – Personalized Fitness Coach

**FitHub AI** is an AI-powered web app that recommends **personalized workout plans** based on your fitness goals using **Natural Language Processing** and **Machine Learning**.

<img width="1919" height="986" alt="Screenshot 2025-07-28 113619" src="https://github.com/user-attachments/assets/dd713a37-4bf1-42d0-8c50-52871bedab89" />

---

## 🚀 How to Run
```bash Install Dependencies
pip install -r requirements.txt
```
```bash Run the App
streamlit run app.py
```
---
## 🚀 Demo

Run the app locally and try entering goals like:
- "I want to lose weight"
- "I want to build muscle"
- "Improve flexibility"

It will suggest a personalized workout based on your input!

---
<img width="1919" height="1010" alt="Screenshot 2025-07-28 114330" src="https://github.com/user-attachments/assets/afb87283-68ad-4c4d-b579-58b5b090d062" />

---


## 🎯 Features

- 🧠 **NLP-based goal detection** using TF-IDF + cosine similarity
- 💪 Personalized **workout recommendations**
- 🖥️ **Streamlit UI** with clean dark mode
- 📦 Fully local and lightweight
- 🔜 Easy to extend with diet plans, posture detection, or user login

---

## 🧠 How It Works

1. User enters a fitness goal in plain English
2. Input is vectorized using `TF-IDF`
3. Compared with stored workout goals using `cosine similarity`
4. Best matching workout is recommended

---
## 📂 Folder Structure

fithub-ai/
* app.py # Main Streamlit app
*  recommender.py # NLP + ML recommendation logic
* workouts.csv # Dataset of fitness plans
* requirements.txt # Python dependencies
* README.md # This file

---
## Future Scope
🥗 Add diet recommendations

📈 Track user progress

📷 Posture correction via webcam (OpenCV)

☁️ Deploy to Streamlit Cloud / HuggingFace Spaces




