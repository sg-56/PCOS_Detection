
# 🚺 PCOS Prediction Model 🧬

## Description 🌟

Welcome to the **PCOS Prediction Model**! 🎉 This project uses machine learning magic ✨ to predict the likelihood of Polycystic Ovary Syndrome (PCOS) based on different input features. It’s designed to help healthcare professionals make better, faster diagnoses. 🩺 And guess what? The model is deployed as a web service for seamless interaction! 🚀

## Problem 😟

PCOS is a hormonal disorder that affects women of reproductive age and can lead to infertility, weight gain, and other health issues. Early prediction of PCOS can make a huge difference in managing symptoms and preventing long-term complications. 💪 This project focuses on using machine learning to predict the risk of PCOS based on a dataset with key features. 📊

## Repository Structure 📂

Here’s the structure of the repository to help you navigate:

```
├── .gitignore               # Git ignore file to exclude unnecessary files
├── .python-version          # Python version management file
├── README.md                # This README file
├── backend                  # Backend service code and model
│   ├── Dockerfile           # Dockerfile for backend container
│   ├── artifacts            # Trained model and preprocessor
│   │   ├── model.pkl        # Saved machine learning model
│   │   └── preprocessor.pkl # Preprocessor used during training
│   ├── pyproject.toml       # Python project dependencies for backend
│   └── server.py            # Backend server script
├── data                     # Dataset files
│   ├── cleaned_data.csv     # Cleaned data ready for model training
│   └── pcos_prediction_dataset.csv # Raw dataset
├── docker-compose.yml       # Configuration for multi-container Docker setup
├── frontend                 # Frontend service code
│   ├── Dockerfile           # Dockerfile for frontend container
│   ├── app.py               # Frontend application script
│   └── pyproject.toml       # Python project dependencies for frontend
├── notebooks                # Jupyter notebooks for analysis
│   ├── EDA.ipynb            # Exploratory Data Analysis (EDA)
│   └── Model_Building.ipynb # Model selection and tuning
└── train.py                 # Script to train the model
```

## Instructions to Run the Project 💻

### 1. Clone the Repository 💾

First, get the code by cloning the repository to your local machine. Run the following command:

```bash
git clone ["https://github.com/sg-56/PCOS_Detection"]
cd 
```

### 2. Set Up the Environment 🛠️

- **Using Pipenv**:  
  Install the required dependencies with Pipenv. 🎉

  ```bash
  pipenv install
  pipenv shell
  ```

- **Using Conda or Virtual Environment**:  
  Or, create a virtual environment and install dependencies from `pyproject.toml` or `requirements.txt`.

### 3. Run the Application 🚀

- **Train the Model**:  
  Now, it's time to train the model! Run `train.py` to get started:

  ```bash
  python train.py
  ```

- **Serve the Model**:  
  Once the model is trained and saved, run `predict.py` to launch the web service and start serving predictions.

  ```bash
  python predict.py
  ```

### 4. Access the Web Service 🌐

Once the service is running, open your browser and navigate to the specified URL (e.g., `http://localhost:5000`). You’re good to go! 🖥️

## Data 📊

The data used to train and test the model is in the `data` folder. You can download it from here:

- [PCOS Prediction Dataset](<dataset_download_url>) 📥

Files in `data/`:

- `cleaned_data.csv`: Data that's ready to go for training.
- `pcos_prediction_dataset.csv`: The raw dataset, ready for exploration.

## Notebook 📓

We’ve provided some Jupyter notebooks to walk you through the entire process:

- **EDA.ipynb**: Dive into Exploratory Data Analysis (EDA) and visualize the data. 📊
- **Model_Building.ipynb**: Follow the journey of selecting and tuning the best model for PCOS prediction. 🤖

These notebooks show how we prepare the data, analyze feature importance, and choose the perfect model. 🏆

## Scripts 📝

- **train.py**: 
  - Loads the dataset, prepares it for training, and fits a machine learning model.
  - Saves the trained model and preprocessor as `.pkl` files so you can use them later.

- **predict.py**:
  - Loads the saved model and preprocessor.
  - Deploys the model as a web service using Flask for real-time predictions.

## Files with Dependencies 📦

- **pyproject.toml**: The Python project configuration file that lists all the dependencies. 📝
- You can also use `requirements.txt` or `Pipenv` if you prefer! 💼

## Dockerfile 🐳

Dockerfiles for both **backend** and **frontend** are included in their respective directories. These are used to create containers for the backend and frontend services.

### To build and run the Docker containers 🚢:

```bash
docker-compose up --build
```

This will set up both the backend and frontend in Docker containers. Dockerize your life! 🐋

## Deployment 🚀

The model is deployed as a web service! 🎉 Once it’s running, you can interact with it by sending HTTP requests to the endpoint where the model is hosted. 🌍

- **URL to the deployed service**: [<deployment_url>](<deployment_url>) 🌐
- **Video demonstration**: [Check out this demo](<demo_link>) 🎥

Let’s make PCOS prediction smarter and faster! 💡
