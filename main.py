import os
from datetime import datetime
from dotenv import load_dotenv
from database_connection import get_all_users

from web_scraping import get_scores_from_afeka
try:
    load_dotenv()

    users = get_all_users()

    for user in users:
        if user["Active"]:
            get_scores_from_afeka(user["username"], user["password"], user["email"])
        with open('timestemps.txt', 'a+') as file:
            file.write(str(datetime.now()) + " ")
            file.write(user['username'] + '\n')
            file.close()

except Exception as e:
    with open('timestemps.txt', 'a+') as file:
            file.write(str(datetime.now()) + " ")
            file.write("error", e)
            file.close()