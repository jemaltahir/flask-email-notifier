import smtplib
import os
from flask import Flask, request, render_template, redirect, url_for
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

smtp_server = 'smtp.pouta.csc.fi'
port = 25
def send_email(subject, body, to):
    sender = os.getenv('SENDER_EMAIL')
    message = f"From: {sender}\nTo: {to}\nSubject: {subject}\n\n{body}"
    try:
        smtpObj = smtplib.SMTP(smtp_server, port)
        smtpObj.sendmail(sender, [to], message)
        smtpObj.quit()
        app.logger.info(f"Successfully sent email to {to}")
    except Exception as e:
        app.logger.error(f"Error: unable to send email to {to}. {e}")

@app.route('/')
def index():
    app.logger.info("Rendering form.html")
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    app.logger.info("Received form submission")
    try:
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
            
            app.logger.info(f"Form data: {name}, {email}, {message}")
            
            subject = "New Form Submission"
            body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            
            receiver_email = os.getenv('RECEIVER_EMAIL')
            send_email(subject, body, receiver_email)
            
            return redirect(url_for('index'))
    except Exception as e:
        app.logger.error(f"Error in form submission: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0')