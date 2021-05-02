from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

mail_sender = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'email@xyz.com'
app.config['MAIL_PASSWORD'] = '*********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail_sender = Mail(app)

@app.route("/")
def index():
    msg = Message('Hello from abhishek', sender = 'email@xyz.com',recipients=['recipient1@gmail.com','test2@yahoo.com'])
    msg.body = "I am extremely delited to share with you that this mail has been sent using flask and python. I am very glad that I have figured out the way to send emails using python. this so cooool!!!!!!"
    mail_sender.send(msg)
    return "Message sucessfully sent!"


if __name__ == '__main__':
    app.run(debug = True)
