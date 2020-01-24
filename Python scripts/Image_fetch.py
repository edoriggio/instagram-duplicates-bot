# Copyright  2020  Edoardo Riggio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import json
import base64
from time import sleep
# Selenium modules
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Selenium driver init
op = Options()
op.headless = True
# driver = webdriver.Firefox(options = op)
driver = webdriver.Firefox()
driver.implicitly_wait(20)

# Variables
insta_url = 'https://www.instagram.com/'

# Function for reading and writing data froma a JSON file
def read_write_to_json(file: str, data: dict = {}, readwrite: str = 'r'):
    if readwrite == 'r':
        with open(file, 'r') as file_to_read:
            return json.load(file_to_read)
    elif readwrite == 'w':
        with open(file, 'w') as file_to_write:
            json.dump(data, file_to_write)
    else:
        raise Exception("readwrite must be either 'r' or 'w'")

def login_to_instagram():
    if not check_if_registered():
        register_new_user()

    json_data = read_write_to_json(json_file)
    username = json_data['username']
    password = json_data['password']

    driver.get(insta_url)
    driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
    driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
    driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    sleep(4)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

def register_new_user():
    username = input('Write down your Instagram username:\n>> ')
    password = (input('Write down your instagram password:\n>> '))

    read_write_to_json(json_file, {'username': username, 'password': password}, 'w')

def check_if_registered():
    with open(json_file, 'r') as file_to_read:
        if json.load(file_to_read) == {}:
            return False
        else:
            return True

login_to_instagram()