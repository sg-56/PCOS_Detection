
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
│   ├── EDA.ipynb            # Exploratory Data Analysis (EDA)
│   └── Model_Building.ipynb # Model selection and tuning
└── train.py                 # Script to train the model
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
uv run train.py
```

### 4. Start the Backend Server 🚀

Once the model is trained, run `server.py` to launch the backend server:

```bash
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
docker-compose up --build
```

This will build and start both the frontend and backend services. You can access the services at:

- **Backend**: [http://localhost:8000](http://localhost:8000)
- **Frontend**: [http://localhost:8501](http://localhost:8501)

---

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


## Files with Dependencies 📦

- **pyproject.toml**: The Python project configuration file that lists all the dependencies. 📝


## Dockerfile 🐳

Dockerfiles for both **backend** and **frontend** are included in their respective directories. These are used to create containers for the backend and frontend services.

---

## Deployment 🚀

The model is deployed as a web service! 🎉 Once it’s running, you can interact with it by sending HTTP requests to the endpoint where the model is hosted. 🌍

- **URL to the deployed service**: [<deployment_url>](<deployment_url>) 🌐

Let’s make PCOS prediction smarter and faster! 💡

