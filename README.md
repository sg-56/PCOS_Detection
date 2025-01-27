
# 🚺 PCOS Prediction Model 🧬

## Description 🌟

Welcome to the **PCOS Prediction Model**! 🎉 This project uses machine learning magic ✨ to predict the likelihood of Polycystic Ovary Syndrome (PCOS) based on different input features. It’s designed to help healthcare professionals make better, faster diagnoses. 🩺 And guess what? The model is deployed as a web service for seamless interaction! 🚀

## Problem 😟

PCOS is a hormonal disorder that affects women of reproductive age and can lead to infertility, weight gain, and other health issues. Early prediction of PCOS can make a huge difference in managing symptoms and preventing long-term complications. 💪 This project focuses on using machine learning to predict the risk of PCOS based on a dataset with key features. 📊


## Dataset
The data used to train and test the model is in the `data` folder. You can download it from here:

- [PCOS Prediction Dataset](https://www.kaggle.com/code/vengadeshwaran58/pcos-dataset-exploration-and-prediction) 📥


## Repository Structure 📂

Here’s the structure of the repository to help you navigate:

```
├── .gitignore               # Git ignore file to exclude unnecessary files
├── .python-version          # Python version management file
├── README.md                # This README file
├── backend                  # Backend service code and model
│   ├── Dockerfile           # Dockerfile for backend container
│   ├── README.md            # Backend README with details
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
    ├── EDA.ipynb            # Exploratory Data Analysis (EDA)
    └── train.py                 # Script to train the model
    └── Model_Building.ipynb # Model selection and tuning

```

## Instructions to Run the Project 💻

⚠️ **Warning**: The git repo has been configured with docker-compose since I wanted to run frontend and backend seperately.If you want to run locally u have to change the api_url of the /frontend/app.py from http://fastapi:8000/predict to "http://localhost:8000/predict"

### 1. Clone the Repository 💾

First, get the code by cloning the repository to your local machine. Run the following command:

```bash
git clone [https://github.com/sg-56/PCOS_Detection]
cd PCOS_Detection/
```

### 2. Set Up the Environment 🛠️

We’ll use **`uv`**, a fast and modern Python package installer, to set up the environment. Here's how:

1. **Install `uv`** (if not already installed):  
   You can install `uv` using `pip` or `curl`:

   ```bash
   pip install uv
   ```

   or:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
    For more info see here : [https://docs.astral.sh/uv/getting-started/installation/]
## Running the Backend Service 🖥️

The backend handles the machine learning model and serves predictions via an API. Here's how you can run it separately.

### 1. Navigate to the `backend/` directory

```bash
cd backend
uv init 
```

### 2. Install Dependencies

- **Using `uv`**:  
  Install the dependencies with `uv`:

  ```bash
    uv pip install -r pyproject.toml --all-extras
  ```

### 3. Train the Model (First Time Only) 🔥

Run `train.py` to train the model and save it for later use.

```bash
cd ../notebooks
uv run train.py
```

### 4. Start the Backend Server 🚀

Once the model is trained, run `server.py` to launch the backend server:

```bash
cd ../backend
uv run fastapi run server.py
```

The backend service will start and be available on `http://localhost:5000/predict`. You can now access the model via API endpoints.

---

## Running the Frontend Service 🌐

The frontend is a simple web app that allows you to interact with the model. Here's how you can run it separately.

### 1. Navigate to the `frontend/` directory

```bash
cd frontend
```

### 2. Install Dependencies

- **Using `uv`**:  
  Install the dependencies with `uv`:

  ```bash
    uv pip install -r pyproject.toml --all-extras
  ```

### 3. Start the Frontend Application 🚀

Run the following command to launch the frontend service:

```bash
uv run streamlit run app.py
```

The frontend service will start, and you can access the web interface via `http://localhost:8501` to interact with the model.

---

## Running Both Backend and Frontend Together with Docker 🐳

If you prefer to run both services together, you can use `docker-compose`. This will set up both the backend and frontend in Docker containers, making it easy to run the whole application at once.

## Please note : I encourage you to use docker-compose as the first option since all the files have been configured to run with docker

### 1. Use Docker Compose
** Please note if you are running using docker-compose then change the api_url in the /frontend/app.py from "http:localhost:8000/predict" to "http:fastapi:8000/predict" ** 
- The above step is very important for the docker compose to work

In the root directory, run:
```bash
docker-compose up --build or sudo docker-compose --build (if you're on linux)
```

This will build and start both the frontend and backend services. You can access the services at:

- **Backend**: [http://localhost:8000](http://localhost:8000)
- **Frontend**: [http://localhost:8501](http://localhost:8501)

---

## Data 📊


Files in `data/`:

- `cleaned_data.csv`: Data that's ready to go for training.
- `pcos_prediction_dataset.csv`: The raw dataset, ready for exploration.
- 
#### Key Findings
    Numerical Summary:
        Age: Mean = 31.98 years; ranges from 15 to 49 years.
        Lifestyle Score: Mean = 5.51 (scale 1–10).
        Undiagnosed PCOS Likelihood: Mean = 0.15 (ranges from 0.05 to 0.25).

    Diagnosis Distribution:
        89.5% of participants were not diagnosed with PCOS.
        10.5% were diagnosed with PCOS.

    BMI Distribution:
        50.1% have a Normal BMI.
        30.0% are Overweight, 14.9% are Obese, and 4.9% are Underweight.

    Menstrual Regularity:
        Among participants with Irregular Menstrual Cycles, 10.6% were diagnosed with PCOS.
        For those with Regular Menstrual Cycles, only 10.4% were diagnosed.

    Hirsutism:
        15.0% of participants with Hirsutism were diagnosed with PCOS, compared to 10.5% without it.

    Correlations:
        Weak correlations exist between Age, Lifestyle Score, and Undiagnosed PCOS Likelihood, indicating that other factors (likely categorical ones) play a stronger role in PCOS diagnosis.

## Notebook 📓

We’ve provided some Jupyter notebooks to walk you through the entire process:

- **EDA.ipynb**: Dive into Exploratory Data Analysis (EDA) and visualize the data. 📊
- **Model_Building.ipynb**: Follow the journey of selecting and tuning the best model for PCOS prediction. 🤖

These notebooks show how we prepare the data, analyze feature importance, and choose the perfect model. 🏆

## Scripts 📝

- **train.py**: 
  - Loads the dataset, prepares it for training, and fits a machine learning model.
  - Saves the trained model and preprocessor as `.pkl` files so you can use them later.


## Files with Dependencies 📦

- **pyproject.toml**: The Python project configuration file that lists all the dependencies. 📝


## Dockerfile 🐳

Dockerfiles for both **backend** and **frontend** are included in their respective directories. These are used to create containers for the backend and frontend services.

---

## Deployment 🚀

The model is deployed as a web service! 🎉 Once it’s running, you can interact with it by sending HTTP requests to the endpoint where the model is hosted. 🌍

- **URL to the deployed service**: [https://pcosdetection.streamlit.app/] 🌐
- Steps to deploy to Streamlit Cloud
  - Login/Signup for streamlit cloud from here [https://share.streamlit.io/]
  - Click on Create APP -> Deploy app from Github -> fill the form with details such github repo link -> select branch -> select path
  - Select App file
  - That's it your app will be launched (Please note i have modified the files the files to faciliate streamlit deployment that can be found in streamlit branch of this repo)
  - WARNING - U need to have requirements.txt for streamlit cloud , please generate with this command "uv pip compile pyproject.toml -o requirements.txt"

Let’s make PCOS prediction smarter and faster! 💡


