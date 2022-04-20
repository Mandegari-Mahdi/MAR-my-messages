# import requirements
from multiprocessing.connection import wait
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initialization
user_username = input("Enter your 'sess' id: ")
user_pass = input("Enter your pass: ")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# ATTENTION: for work well in your case, Download "chromedriver.exe" and replace your PATH with mine below.
#                          |---------------------CHANGE THIS---------------------|
driver = webdriver.Chrome(r"C:/Users/mahdi/Desktop/chrome driver/chromedriver.exe", options=options)
driver.get("https://sess.sku.ac.ir")

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="edId"]')))

# get user info to sign in:
user = driver.find_element_by_xpath('//*[@id="edId"]')
user.send_keys(user_username)
passw = driver.find_element_by_xpath('//*[@id="edPass"]')
passw.send_keys(user_pass)
passw.send_keys(Keys.ENTER)

# wait to load page:
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ParentForm"]/div[4]/section/div[1]/section/div/div[2]/section/div[1]/div[1]/div[1]/div[2]')))

# enter to 'omoor amoozeshi' page:
enter_button = driver.find_element_by_xpath('//*[@id="ParentForm"]/div[4]/section/div[1]/section/div/div[2]/section/div[1]/div[1]/div[1]/div[2]')
enter_button.click()

# wait to load 'omoor amoozeshi' page:
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="Banner1_edMsg"]')))

# enter to 'payam ha' page:
messages_button = driver.find_element_by_xpath('//*[@id="Banner1_edMsg"]')
messages_button.click()

wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="Form1"]/table/tbody/tr[2]/td[1]/table/tbody/tr[5]/td[2]')))

# enter to 'payam haye khande nashode' page:
unread_button = driver.find_element_by_xpath('//*[@id="Form1"]/table/tbody/tr[2]/td[1]/table/tbody/tr[5]/td[2]')
unread_button.click()

# read each message and return to previous page:
while len(driver.find_elements(By.XPATH, '//*[@id="edList"]/tbody/tr[2]/td[2]')) != 0:

    first_message = driver.find_element_by_xpath('//*[@id="edList"]/tbody/tr[2]/td[2]')
    first_message.click()

    back_button = driver.find_element_by_xpath('//*[@id="edReturn"]')
    back_button.click()
    
    refresh_button = driver.find_element_by_xpath('//*[@id="Form1"]/table/tbody/tr[2]/td[1]/table/tbody/tr[13]/td[2]')
    refresh_button.click()

print("\n\nALL MESSAGES READ SUCCESSFULLY.")