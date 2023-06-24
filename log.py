from datetime import datetime


PATH = "timestemps.txt"

def write_log(msg):
    file = open(PATH, "a+", encoding="utf-8")
    file.write(msg + "\n")
    file.close()

def write_timestep_user(username):
    msg = str(datetime.now()) + " " + username
    write_log(msg)

def write_sent_mail(title):
    msg = "send mail:" + title
    write_log(msg)

def write_error(e : Exception, additional_msg):
    write_log(str(e) + "\n\t" + additional_msg)
