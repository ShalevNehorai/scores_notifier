import os
from datetime import datetime
from dotenv import load_dotenv
from database_connection import get_all_users
from encryption import decrypt
from log import write_error, write_timestep_user

from web_scraping import get_scores_from_afeka
#try:

users = get_all_users()

for user in users:
    if user["Active"]:
        write_timestep_user(user['username'])
        try:
            password = decrypt(user["password"])
        except TypeError as e:
            write_error(e, "password of user " + user['username'] + " not encrypted correctly")
            continue
        get_scores_from_afeka(user["username"], password, user["email"])
    
        

"""
except Exception as e:
    with open('timestemps.txt', 'a+') as file:
            file.write(str(datetime.now()) + " ")
            file.write("error", e)
            file.close()"""