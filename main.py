import os
from dotenv import load_dotenv
from database_connection import get_all_users

from web_scraping import get_scores_from_afeka

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

users = get_all_users()

for user in users:
    get_scores_from_afeka(user["username"], user["password"], user["email"])