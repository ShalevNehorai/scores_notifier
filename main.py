import os
from dotenv import load_dotenv

from web_scraping import get_scores_from_afeka

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

get_scores_from_afeka(username, password, "")