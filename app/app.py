from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the JobApp-Tracker!"


@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Process the contact form data (e.g., save to database, send email)
    return f"Thanks for your message, {name}!"


if __name__ == '__main__':
    app.run(debug=True)
