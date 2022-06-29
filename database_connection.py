from collections import UserList
import os
import pymongo
from dotenv import load_dotenv

from email_sender import send_new_score

load_dotenv()
con_str = os.getenv("DB_LINK")

mongo_client = pymongo.MongoClient(con_str, connect=False)

users_db = mongo_client.Users

def get_all_users():
    users_collaction = users_db.Users
    return users_collaction.find()

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
        if(score.isnumeric() and found_course["Score"] != score):
            send_new_score(email, course_model)
        courses_collaction.replace_one(found_course, course_model)
    
    else:
        courses_collaction.insert_one(course_model)