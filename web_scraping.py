
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common import exceptions as SE

import time

from database_connection import update_coure

PATH = "D:\Program Files (x86)\chromedriver\chromedriver.exe"

def get_scores_from_afeka(username, password, email):
    driver = webdriver.Chrome(PATH)

    driver.get("https://yedion.afeka.ac.il/")

    user_name_input = driver.find_element(By.ID, "input_1")
    user_name_input.send_keys(username)

    password_input = driver.find_element(By.ID, "input_2")
    password_input.send_keys(password)

    driver.find_element(By.XPATH, "//input[@type = 'submit' and @value = 'כניסה']").send_keys(Keys.ENTER)

    time.sleep(5)

    driver.find_element(By.LINK_TEXT, "רשימת ציונים").click()

    time.sleep(5)

    choos_year_ddr = Select(driver.find_element(By.ID, "R1C1"))
    choos_year_ddr.select_by_value('-1')

    choos_year_ddr = Select(driver.find_element(By.ID, "R1C2"))
    choos_year_ddr.select_by_value('0')

    driver.find_element(By.LINK_TEXT, "ביצוע").click()

    time.sleep(5)

    exist = True
    counter = 1
    idStr = "MyFather"
    try:
        curr_element = driver.find_element(By.ID, idStr + str(counter))
    except SE.NoSuchElement:
        exist = False
    while(exist):
        under_element = curr_element.find_elements(By.XPATH, ".//*")
        course_name = under_element[1].get_attribute('textContent').strip()
        course_type = under_element[3].get_attribute('textContent').strip()
        score = under_element[6].get_attribute('textContent').strip().split(":")[1].strip()
        print("course: " + course_name + " " + course_type + " score: " + score)
        update_coure(username, course_name, course_type, score)

        counter += 1
        try:
            curr_element = driver.find_element(By.ID, idStr + str(counter))
        except SE.NoSuchElementException:
            exist = False


    driver.quit()


