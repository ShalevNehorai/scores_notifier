from collections import UserList
import os
import pymongo
from dotenv import load_dotenv

from email_sender import send_new_score

load_dotenv()
con_str = os.getenv("DB_LINK")

mongo_client = pymongo.MongoClient(con_str, connect=False)

users_db = mongo_client.Users
users_collaction = users_db.Users

def get_all_users():
    #user_model={
    #    "username": "username",
    #    "email": "email",
    #    "password": b'Z0FBQUFBQml3WGFrWFZNdndfYmJHa2M2dUplNVctVVJ6cF9DQngzbFQxN21ZZDR2Q2t5TUVLUi1oV2YyUVBvU2VCdzZpdk1HMnU3...',
    #    "Active": True
    #}
    #return [user_model]

    return users_collaction.find()

def add_user(username, password, email):
    user_model={
        "username": username,
        "email": email,
        "password": password,
        "Active": True
    }
    #TODO check if username exists

    users_collaction.insert_one(user_model)


def update_coure(user_name, course_name, course_nz, type, score, email):
    course_collaction_name = user_name + "-Curses"
    courses_collaction = users_db[course_collaction_name]

    found_course = courses_collaction.find_one({
        "Name": course_name, "Nz": course_nz, "Type": type
    })

    course_model = {
        "Name": course_name,
        "Nz": course_nz,
        "Type": type,
        "Score": score
    }
    
    if found_course is not None:
        if score.isnumeric():
            course_model["Score"] = [score]
            scoresLst = found_course['Score']
            if not isinstance(scoresLst, list):
                send_new_score(email, course_model)
                courses_collaction.replace_one(found_course, course_model)
            elif score not in scoresLst:
                send_new_score(email, course_model)
                course_model["Score"].extend(scoresLst)
                
                courses_collaction.replace_one(found_course, course_model)
        
    else:
        if score.isnumeric():
            course_model["Score"] = [score]
        courses_collaction.insert_one(course_model)