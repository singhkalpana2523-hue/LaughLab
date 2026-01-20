# LaughLab – AI Powered Meme & Poster Generator

LaughLab is a Streamlit-based AI application that allows users to create memes and posters quickly using intelligent, context-aware caption generation. The application is designed to simplify creative content creation for students by combining image processing and AI-driven text generation in a user-friendly interface.

---

## 🔍 Problem Statement
Students often need creative content such as memes, motivational posters, study posters, or event posters for academic and social purposes. Existing tools are either complex, time-consuming, or require graphic design skills. There is a need for a simple AI-powered solution that can automatically generate relevant captions and visually appealing content without technical expertise.

---

## 💡 Proposed Solution
LaughLab provides an AI-assisted platform where users can:
- Choose a content type (Meme, Motivational Poster, Study Poster, Event Poster)
- Enter a topic
- Select a predefined template
- Generate context-aware captions using AI logic
- Preview and download the generated output instantly

This approach reduces manual effort and makes creative content generation accessible to all users.

---

## 🧠 System Development Approach
- The application is developed using Python and Streamlit.
- Image rendering and text overlay are handled using the Pillow (PIL) library.
- AI captions are generated using rule-based contextual logic based on user input and content type.
- The application is deployed on Streamlit Cloud for easy public access.

---

## 🛠️ Technology Stack
- **Programming Language:** Python  
- **Framework:** Streamlit  
- **Image Processing:** Pillow (PIL)  
- **HTTP Requests:** Requests  
- **Deployment:** Streamlit Cloud  
- **Version Control:** GitHub  

---

## ⚙️ Algorithm Overview
1. User selects the type of content.
2. User enters a topic.
3. A suitable template is selected.
4. The system generates a context-aware caption.
5. Caption is rendered onto the image.
6. Final output is displayed and available for download.

---

## 🚀 Deployment
The application is deployed using Streamlit Cloud.

🔗 **Live Application:**  
👉 https://laughlab-hkuzfxxy4wrvj2bbfr7yry.streamlit.app/

---

## 📂 How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py

