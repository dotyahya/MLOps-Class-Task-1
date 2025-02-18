from flask import Flask

app = Flask(__name__)

@app.route('/')
def display_welcome_message():
    return "Deploying Flask App on Vercel!"
