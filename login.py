from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def login_with_selenium(username, password):
    # Open Instagram login page
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    # Fill in login info
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Send login form
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # Extract cookies and user agent
    cookies = driver.get_cookies()
    user_agent = driver.execute_script("return navigator.userAgent;")

    # Return driver, cookies, and user agent
    return driver, cookies, user_agent
