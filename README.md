# PCOS Health Check Web Application

## Overview
The **PCOS Health Check** is an interactive web application built using **Streamlit**. It allows users to complete a questionnaire to assess the possibility of having PCOS (Polycystic Ovary Syndrome) and provides motivating, supportive feedback based on their responses. The app also sends user data to a REST API for further analysis and receives responses to guide users.

---

## Features
- **Interactive Questionnaire**: Collects user data, including demographics, health, and lifestyle information.
- **Dynamic Progress Bar**: Visual representation of progress through the questionnaire.
- **API Integration**: Sends user responses to a REST API and processes the server's response.
- **Motivating Feedback**: Provides encouraging messages, regardless of the user's PCOS likelihood.
- **Data Persistence**: Saves user responses locally to a CSV file for further analysis.
- **Responsive Design**: Fun animations, emojis, and clean UI to create an engaging experience.

---

## Tech Stack
- **Frontend**: Streamlit for building the web interface.
- **Backend Integration**: REST API for processing user responses.

---

## Installation

### Prerequisites
- Python 3.10 or above installed on your system.
- A virtual environment (optional but recommended).

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd repo
   ```
2. Create a virtual environment (optional):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## API Integration
The app sends user responses to a REST API and processes the response to display motivating feedback.

### Example API Workflow
1. User data is collected via the form.
2. The data is sent to the API:
   ```python
   import requests
   response = requests.post(api_url, json=data)
   ```
3. The API responds with a JSON object containing the result (e.g., `Result`).
4. Based on the result, the app displays a personalized motivational message.

---

## File Structure
```
.
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

---

## Usage
1. Open the application in your web browser.
2. Fill out the questionnaire with accurate details about your health and lifestyle.
3. Submit your responses to see the results and motivational feedback.
4. Your data will be saved locally and processed by the API.

---

## Example Screenshots
### Home Page
![Home Page](https://via.placeholder.com/800x400.png?text=Home+Page+Screenshot)

### Questionnaire
![Questionnaire](https://via.placeholder.com/800x400.png?text=Questionnaire+Screenshot)

### Results
![Results](https://via.placeholder.com/800x400.png?text=Results+Screenshot)

---

## Contributing
We welcome contributions to improve the app! Feel free to:
- Submit bug reports or feature requests.
- Fork the repository and make pull requests.

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Acknowledgments
- Streamlit for the amazing web app framework.
- The PCOS community for inspiring this initiative.
- All contributors who helped develop this app.

---

## Disclaimer
This application is not a substitute for professional medical advice. Always consult a healthcare provider for medical concerns.

