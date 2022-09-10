import os
from dotenv import load_dotenv
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from log import write_sent_mail

load_dotenv()
sender = os.getenv("SENDEREMAIL")
password = os.getenv("EMAILPASSWORD")

def send_email(email, title, msg):
    email_string = MIMEMultipart()
    email_string["From"] = sender
    email_string["To"] = email
    email_string["Subject"] = title
    email_string.attach(MIMEText(msg, "plain"))
    
    #context = ssl.create_default_context()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, email, email_string.as_string())
    print("sending to" , email, "the msg", title)
    write_sent_mail(title)

    server.close()

def send_new_score(email, course_model):
    title = "הקבל ציון חדש ב" + course_model["Type"] +  " בקורס: " + course_model["Name"]
    msg = "בהצלחה במועד ב."
    send_email(email, title, msg)
    
"""
course_model = {
        "Name": "20373 מעגלים אלקטרוניים אנלוגיים1 ",
        "Nz": 'נ"ז  / ש"ס  / מועד 1',
        "Type": "בחינה",
        "Score": 100
    }

to_email = "Shalev336n@gmail.com"
send_new_score(to_email, course_model)
"""