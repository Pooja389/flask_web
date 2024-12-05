# flask_web
This uses flask wtf for login form and prevent unaurhoriaed access
# Flask Login Application

A simple Flask web application that allows users to log in with an email and password. It validates the input fields and provides feedback based on the login credentials.

This app uses **Flask**, **Flask-WTF** for form handling, and **Flask-Bootstrap** for styling.

## Features

- Email and password validation using **Flask-WTF** and **WTForms**.
- **Bootstrap 5** for responsive design and layout.
- Redirects to a success page for valid credentials and a denied page for incorrect ones.

## Requirements

- Python 3.x
- Flask
- Flask-WTF
- Flask-Bootstrap

### To install the required packages, run:

```bash
python -m pip install -r requirements.txt
```
## installation

**clone the repo**
```bash
git clone https://github.com/Pooja389/flask_web.git
cd wtf
```
**create and activate virtual environment**
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

**install dependencies**
```bash
pip install -r requirements.txt
```
**Run the application**
```bash
python main.py
