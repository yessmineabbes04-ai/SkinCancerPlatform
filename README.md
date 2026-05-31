# SkinAI - Skin Cancer Detection Platform

![SkinAI Banner](https://img.shields.io/badge/SkinAI-Medical_Platform-0ea5e9?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

SkinAI is a modern, responsive, and secure web platform designed to assist in the preliminary classification of skin lesions (Benign vs. Malignant) using Deep Learning (VGG16 Convolutional Neural Network). 

**Author:** Abbes Yassmine

---

## ✨ Key Features

- **🔒 Secure Authentication:** User registration, login, and encrypted session management.
- **📊 Professional Dashboard:** High-level overview of analysis statistics (total, benign, malignant).
- **🤖 AI-Powered Diagnosis:** Seamless integration with a pre-trained Keras/TensorFlow VGG16 model for image classification.
- **📁 Patient Records Management:** Maintain a persistent database of patient analyses, including demographic data (name, age) and visual history.
- **🌓 Dark / Light Mode:** A premium, fully responsive user interface built from scratch with custom CSS and Phosphor Icons.
- **🛠 Graceful Fallback:** If the heavy AI model is missing or the environment is unsupported, the app falls back to a simulated inference mode for demonstration purposes.

---

## 📸 Platform Screenshots

*(Note: Add your actual screenshots to the `screenshots/` folder to display them here)*

### 1. Dashboard & Statistics
![Dashboard Overview](screenshots/dashboard.png)
*The main hub displaying analysis statistics and recent patient activity.*

### 2. New Analysis / Image Upload
![New Analysis](screenshots/predict.png)
*The modern drag-and-drop interface for patient data entry and lesion image upload.*

### 3. AI Prediction Result
![Analysis Result](screenshots/result.png)
*Detailed AI confidence score and diagnosis breakdown.*

### 4. Patient Records
![Patient Records](screenshots/patients.png)
*Complete tabular history of all analyses performed on the platform.*

---

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.9+ (64-bit required for TensorFlow)**
- Git

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/skin_cancer_app.git
cd skin_cancer_app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add the AI Model
Download your pre-trained `vgg16_malignant_benign.h5` model (approx. 130MB) and place it inside the `model/` directory:
```
skin_cancer_app/
└── model/
    └── vgg16_malignant_benign.h5
```
> *If you skip this step, the app will gracefully use a "mock prediction" fallback so you can still test the UI and database!*

### 4. Run the application
```bash
python app.py
```
The platform will be live at `http://127.0.0.1:5000`.

---

## 🏗️ Architecture & Technologies

- **Frontend:** HTML5, Custom CSS3 (CSS Variables for Theming), Vanilla JavaScript, Phosphor Icons.
- **Backend:** Python, Flask, Werkzeug, SQLite3.
- **Machine Learning:** TensorFlow, Keras, NumPy.

### Project Structure
```text
SKIN_CANCER_APP/
│
├── backend/                  # Application logic
│   ├── api.py                # API endpoints
│   ├── auth.py               # Authentication logic
│   ├── db.py                 # SQLite database handlers
│   └── model_service.py      # AI Inference & fallback handlers
│
├── model/                    # ML Models directory
│   └── vgg16_malignant_benign.h5 
│
├── static/                   # Static assets
│   ├── css/style.css         # Premium stylesheet
│   ├── js/                   # Frontend logic
│   └── uploads/              # User-uploaded images
│
├── templates/                # Jinja2 HTML templates
│   ├── base.html             # Master layout
│   ├── login.html            
│   ├── register.html         
│   ├── dashboard.html        # Main stats view
│   ├── predict.html          # Upload form
│   ├── result.html           # Diagnosis view
│   └── patients.html         # Records table
│
├── app.py                    # Flask Entry Point
└── database.db               # Auto-generated SQLite Database
```

---

## ⚠️ Medical Disclaimer
This platform is an educational and conceptual project. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified dermatologist or physician for clinical decisions.

---
*Developed with ❤️ by Abbes Yassmine.*
