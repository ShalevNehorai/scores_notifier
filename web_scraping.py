
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common import exceptions as SE

import time

from database_connection import update_coure
import log

PATH = "D:\Program Files (x86)\chromedriver\chromedriver.exe"

def get_scores_from_afeka(username, password, email):
    driver = webdriver.Chrome(PATH)

    driver.get("https://yedion.afeka.ac.il/")

    user_name_input = driver.find_element(By.ID, "input_1")
    user_name_input.send_keys(username)

    password_input = driver.find_element(By.ID, "input_2")
    password_input.send_keys(password)

    driver.find_element(By.XPATH, "//input[@type = 'submit' and @value = 'כניסה']").send_keys(Keys.ENTER)


    try:
        grade_list_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "רשימת ציונים")))
        grade_list_btn.click()

    except:
        log.write_error(e, "the element רשימת ציונים didnt load")
        driver.quit()
        return
    
    try:
        choos_year_ddr = Select(WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "R1C1"))))
        #choos_year_ddr = Select(driver.find_element(By.ID, "R1C1"))
        choos_year_ddr.select_by_value('-1')

        choos_year_ddr = Select(driver.find_element(By.ID, "R1C2"))
        choos_year_ddr.select_by_value('0')

        driver.find_element(By.LINK_TEXT, "ביצוע").click()
    except:
        log.write_error(e, "the element of year selection didnt load")
        driver.quit()
        return

    time.sleep(3)

    exist = True
    counter = 1
    idStr = "MyFather"
    try:
        curr_element = driver.find_element(By.ID, idStr + str(counter))
    except SE.NoSuchElement:
        exist = False
    
    while(exist):
        try:
            under_element = curr_element.find_elements(By.XPATH, ".//*")
            course_name = under_element[1].get_attribute('textContent').strip()
            course_nz = under_element[2].get_attribute('textContent').strip()
            course_type = under_element[3].get_attribute('textContent').strip()
            score = under_element[6].get_attribute('textContent').split(":")[1].split("(")[0].strip()
            update_coure(username, course_name, course_nz, course_type, score, email)
        except Exception as e:
            log.write_error(e, "Course tile have something missing")

        counter += 1
        try:
            curr_element = driver.find_element(By.ID, idStr + str(counter))
        except SE.NoSuchElementException:
            exist = False


    driver.quit()


