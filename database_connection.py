from collections import UserList
import os
import pymongo
from dotenv import load_dotenv

load_dotenv()
con_str = os.getenv("DB_LINK")

mongo_client = pymongo.MongoClient(con_str)

users_db = mongo_client.Users
users_collaction = users_db.Users

def get_all_users():
    return users_collaction.find()

def update_coure(user_name, course_name, type, score):
    course_collaction_name = user_name + "-Curses"
    courses_collaction = users_db[course_collaction_name]

    course_model = {
        "Name": course_name,
        "Type": type,
        "Score": score
    }

    courses_collaction.insert_one(course_model)