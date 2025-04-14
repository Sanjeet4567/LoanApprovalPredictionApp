# Loan Prediction App

This project is a **Loan Prediction App** built using **Flask** and a machine learning model. The app predicts whether a loan application will be **Accepted** or **Rejected** based on user inputs like income, loan amount, CIBIL score, etc.

## Features
- **Interactive Web Interface**: Built using **Flask** to allow users to input data and receive predictions.
- **Loan Status Prediction**: Predicts whether a loan is accepted or rejected based on user-provided data.
- **Machine Learning Model**: A trained machine learning model is used to classify loan applications.

## Technologies Used
- **Flask**: A lightweight web framework for building the backend.
- **Scikit-learn**: For implementing machine learning models.
- **Pandas and NumPy**: For data processing and manipulation.

## Setup Instructions

Follow the steps below to set up and run the project:

### Prerequisites
- Python 3.7 or above
- Virtual environment (optional but recommended)

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Sanjeet4567/LoanApproval.git
cd LoanApproval
```
### 2. Create a Virtual Environment (Optional but Recommended)
It's a good practice to create a virtual environment to keep dependencies isolated:
```bash
python3 -m venv venv
```
#### Activate the virtual environment:
- On Windows :
    ```bash
    .\venv\Scripts\activate
    ```
- On macOS/Linux :
    ```bash
    source venv/bin/activate
    ```
### 3. Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```
or use the `setup.py` file
```bash
python setup.py install
```
The `requirements.txt` file should include the following (or similar):

```plain
flask
scikit-learn
pandas
numpy
xgboost
-e.
```
### 4. Run the Flask App
To start the Flask app, run the following command:
```bash
python application.py
```
This will start the Flask server, and it will provide a local URL, usually http://127.0.0.1:5000/. Open this URL in your browser to interact with the app.
### 5. Prediction Flow
- Step 1: Enter the details such as number of dependents, income, loan amount, loan term, CIBIL score, etc., in the input fields.

- Step 2: Click the "Submit" button.

- Step 3: View the loan prediction status, either "Accepted" or "Rejected", displayed on the screen.

### 6. Modify and Update
You can modify the app by editing the application.py file or adding more features, as per your requirements.

### 7. Deactivate the Virtual Environment
Once you're done, you can deactivate the virtual environment:
```bash
deactivate
```

### Contributing
If you'd like to contribute to this project, feel free to fork the repository, make your changes, and create a pull request. Contributions, issues, and suggestions are welcome!

### License
This project is open-source and available under the MIT License.

### Contact
For any inquiries or issues, please feel free to contact me at sanjeetraj0440@gmail.com.