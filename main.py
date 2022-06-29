import os
from dotenv import load_dotenv
from database_connection import get_all_users

from web_scraping import get_scores_from_afeka

load_dotenv()

users = get_all_users()

for user in users:
    if user["Active"]:
        get_scores_from_afeka(user["username"], user["password"], user["email"])