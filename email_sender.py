def send_email(email, msg):
    print("sending to" , email, "the msg", msg)

def send_new_score(email, course_model):
    print("new score in " , course_model["Name"], course_model["Type"], "is ", course_model["Score"])