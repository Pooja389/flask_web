from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField
from wtforms.validators import DataRequired, Email,Length
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message="Email is required."),
        Email(message="Invalid email address. Please include '@' and  '.'")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Password is required."),
        Length(min=8, message="Password must be at least 8 characters long.")
    ])

app = Flask(__name__)
app.secret_key = "poojasaini"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():

        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "12345678":

            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    return render_template('login.html', form=login_form)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/denied")
def denied():
    return render_template("denied.html")
if __name__ == '__main__':
    app.run(debug=True)
