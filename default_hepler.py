
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import csv
import os
from selenium.common.exceptions import ElementNotInteractableException

from selenium.common.exceptions import NoSuchElementException, TimeoutException

import undetected_chromedriver as uc

def init_driver():
    options = uc.ChromeOptions()
    # Add your desired options here
    driver = uc.Chrome(options=options)
    return driver

def slow_type(element, text):
    """Teebet aaleha el function hethi to get the most human like typing for bots take good care of it"""
    i = 0
    for character in text:
        i += 1
        if i % 3 == 0:
            delay = random.uniform(0.3, 0.4)
        if i % 3 == 1:
            delay = random.uniform(0.1, 0.2)
        if i % 3 == 2:
            delay = random.uniform(0.2, 0.3)
        if i % 5 == 4:
            delay = random.uniform(0.1, 0.3)
            element.send_keys(random.choice(string.ascii_letters))
            delay = random.uniform(0.1, 0.3)
            element.send_keys(Keys.BACK_SPACE)
        element.send_keys(character)
        time.sleep(delay)