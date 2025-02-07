from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html',
                           error='404 Not Found',
                           message='The page you are \
                           looking for does not exist.'), 404


@app.route('/apply', methods=['POST'])
def apply():
    company = request.form['company']
    position = request.form['position']
    resume = request.files['resume']  # Save the resume file if needed
    # Simulate saving the job application
    # (you can save to a database or a file)
    print(f"Job Application Submitted: {company} - {position}")
    return redirect(url_for('home'))  # Redirect back to home after submission


@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Simulate sending the message (you can integrate email functionality)
    print(f"Message from {name} ({email}): {message}")
    return redirect(url_for('home'))  # Redirect back to home after submission


if __name__ == '__main__':
    app.run(debug=True)
