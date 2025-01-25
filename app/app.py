from flask import Flask, render_template


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


@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Process the contact form data (e.g., save to database, send email)
    return f"Thanks for your message, {name}!"


if __name__ == '__main__':
    app.run(debug=True)
