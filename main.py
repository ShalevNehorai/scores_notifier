import os
from datetime import datetime
from dotenv import load_dotenv
from database_connection import get_all_users
from encryption import decrypt

from web_scraping import get_scores_from_afeka
#try:

users = get_all_users()

for user in users:
    if user["Active"]:
        print(user["username"])
        password = decrypt(user["password"])
        get_scores_from_afeka(user["username"], password, user["email"])
    with open('timestemps.txt', 'a+') as file:
        file.write(str(datetime.now()) + " ")
        file.write(user['username'] + '\n')
        file.close()

"""
except Exception as e:
    with open('timestemps.txt', 'a+') as file:
            file.write(str(datetime.now()) + " ")
            file.write("error", e)
            file.close()"""