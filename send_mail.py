from email import message
import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '954f90bdd507f5'
    password = '445d139bf96c01'
    message=f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>dealer: {dealer}</li><li>rating: {rating}</li><li>comments: {comments}</li></ul>"

    sender_email = 'lexus@lexus.com'
    receiver_email = 'leshem@xiang.com'

    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())