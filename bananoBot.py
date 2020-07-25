# Generated by Selenium IDE
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class BananoBot():
    def quit(self):
        self.driver.quit()
  
    def mine(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        self.driver.get("https://powerplant.banano.cc/")
        self.driver.find_element(By.CSS_SELECTOR, "p > input:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "p > input:nth-child(1)").send_keys("ban_3s73baf6c9zxjpha8bff5rdthq6gam5bo13k7swdwmg7bikazz99tnd3pi4m")
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(13)").click()
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > input:nth-child(1)").click()
        print("Ok !")