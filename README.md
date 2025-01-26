# 🛠️ Project Name: PCOS Health Check Web Application

## 📖 Overview
Welcome to the **PCOS Health Check Web Application**, where we aim to help individuals assess the possibility of Polycystic Ovary Syndrome (PCOS) through an engaging questionnaire and advanced data processing. This repository contains everything from data preparation and machine learning model building to a fully functional REST API service.

---

## 🎯 Potential Use Cases

1. **Early Detection**: Identify individuals who might be at risk of PCOS and encourage them to seek medical advice.
2. **Health Awareness**: Increase awareness of PCOS symptoms and lifestyle changes that can mitigate risks.
3. **Healthcare Insights**: Provide actionable insights for medical practitioners and researchers.

---

## 📂 Repository Structure

```
.
├── .gitignore             # Ignored files and folders
├── .python-version        # Python version used for the project
├── README.md              # You're reading it now!
├── app.py                 # Streamlit app for user interaction
├── backend/               # Backend for model training and REST API
│   ├── Dockerfile         # Dockerfile for containerizing the backend
│   ├── README.md          # Backend-specific documentation
│   ├── artifacts/         # Model and preprocessor files
│   │   ├── model.pkl      # Trained ML model
│   │   └── preprocessor.pkl # Preprocessing pipeline
│   ├── data/              # Dataset and processed data
│   │   ├── cleaned_data.csv
│   │   └── pcos_prediction_dataset.csv
│   ├── main.py            # REST API server script
│   ├── notebooks/         # Jupyter notebooks for EDA and modeling
│   │   ├── EDA.ipynb      # Exploratory Data Analysis
│   │   └── Model_Building.ipynb # Model development
│   ├── pyproject.toml     # Python project metadata
│   ├── requirements.txt   # Backend dependencies
│   └── train.py           # Model training script
├── pyproject.toml         # Python project metadata for the app
└── uv.lock                # Dependency lock file
```

---

## 🧩 Components

### 1. **README.md**
This file provides a comprehensive guide to the project, including usage instructions and details about each component.

### 2. **app.py**
A Streamlit-based frontend application that:
- Collects user responses through an interactive questionnaire.
- Sends data to a REST API for prediction.
- Displays results and motivational messages based on predictions.

### 3. **backend/**
Contains the backend components, including:
- **Model Training**: Scripts for preprocessing and training the ML model.
- **REST API**: A Flask-based API for serving predictions.
- **Artifacts**: Stored trained model and preprocessing pipeline.

### 4. **Data/**
Stores raw and processed datasets for training and analysis.

### 5. **Notebooks/**
Jupyter notebooks for:
- Exploratory Data Analysis (EDA).
- Feature engineering and model development.

### 6. **Dependencies**
All required Python libraries are listed in `requirements.txt` or `pyproject.toml` for easy environment setup.

### 7. **Dockerfile**
A Dockerfile for containerizing the backend service, ensuring consistency across different environments.

---

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd PCOS-Health-Check
   ```

2. **Set up the environment**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Start the backend server**:
   ```bash
   cd backend
   python main.py
   ```

5. **Optional: Run with Docker**:
   ```bash
   docker build -t pcos-backend ./backend
   docker run -p 5000:5000 pcos-backend
   ```

---

## 🌟 Deployment

The app can be deployed using services like Heroku, AWS, or Docker. Detailed deployment instructions are provided in the `backend/README.md` file.

---

## 📊 Example Data Workflow

1. User data is collected via the Streamlit app.
2. Data is sent to the REST API for prediction.
3. The REST API processes the data and returns a prediction (e.g., likelihood of PCOS).
4. The app displays personalized feedback and motivational messages.

---

## 🎉 Features

- **Interactive Questionnaire**: Engages users with an intuitive UI.
- **ML-Powered Predictions**: Backend uses a trained model for predictions.
- **Motivational Messaging**: Provides encouragement regardless of the prediction.
- **Data Insights**: Supports healthcare awareness and decision-making.

---

## 🛠️ Contributing

We welcome contributions to improve the app. Feel free to:
- Submit bug reports or feature requests.
- Fork the repository and create pull requests.

---

## 📜 License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

## 🤝 Acknowledgments
- **Streamlit**: For the excellent framework.
- **Flask**: For the robust REST API.
- **PCOS Community**: For inspiring this initiative.

---

## ⚠️ Disclaimer
This app is not a substitute for professional medical advice. Always consult a healthcare provider for medical concerns.

