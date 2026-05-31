# 🩺 SkinAI — Advanced Skin Cancer Detection Platform

This is a NEW and IMPROVED modern web application for classifying skin lesion images as **Benign** or **Malignant** using a Deep Learning model (VGG16).

## ✨ New Features & Improvements over original

1. **Modern Medical UI/UX**: Completely redesigned with a clean white/blue medical theme, utilizing CSS variables.
2. **True Dark Mode**: Fully functioning dark mode toggle.
3. **Decoupled Architecture**: Frontend is a pure HTML/JS Single Page Application that communicates asynchronously with a Flask REST API (`/api/predict`).
4. **Enhanced UX Animations**: Added beautiful loading states, animated confidence bars, and modern Phosphor icons.
5. **Session History**: Visually track all scans performed during the current session without page reloads.
6. **Graceful Fallback Model**: The application can run *immediately* without needing the 130MB `.h5` model file. It uses a mock API delay and response to demonstrate UI capabilities, and will automatically switch to the real AI once the model file is provided.
7. **AI Explainability**: Includes a section explaining what the CNN is looking for (asymmetry, border irregularity, etc.).

## 📁 Project Structure

```
skin_cancer_app/
│
├── model/
│   └── vgg16_malignant_benign.h5   # Place your Keras model here (Optional for demo)
│
├── backend/
│   ├── api.py                      # Flask RESTful routes
│   └── model_service.py            # TensorFlow inference logic & mock fallback
│
├── static/
│   ├── css/style.css               # Modern styling and theming variables
│   ├── js/main.js                  # Frontend logic (drag-drop, API fetch)
│   └── uploads/                    # User uploaded images
│
├── templates/
│   └── index.html                  # Main Single Page Application structure
│
├── app.py                          # Flask application entry point
├── requirements.txt                # Python dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd skin_cancer_app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Add the actual AI Model**:
   If you have the pre-trained `vgg16_malignant_benign.h5` model, place it inside the `model/` directory. If you do NOT add it, the app will gracefully fall back to a mock prediction so you can still test the UI!

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open in browser**:
   Navigate to `http://127.0.0.1:5000`

## 🧠 Technology Stack

- **Backend**: Python, Flask, Werkzeug
- **AI/ML**: TensorFlow, Keras, NumPy, Pillow
- **Frontend**: HTML5, Vanilla JavaScript (ES6+), CSS3 (Flexbox/Grid, CSS Variables)
- **Icons**: Phosphor Icons

## ⚠️ Medical Disclaimer
This application is for **educational and demonstration purposes only**. It is **not** a medical device.
