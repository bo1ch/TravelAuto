from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from app import Application
from Scripts import create_news
from app.admin.pom.searcher import Searcher

import pytest
import subprocess

@pytest.fixture(autouse=True)
def script():
    subprocess.run(['python', 'C:\\TravelAuto\\Scripts\\create_news.py'])

def get_result():
    return {"AbsoluteUrl"}
def test_Create_News():
    app = Application()
    login_page = app.admin.login_page
    login_page.enter_login('role_system@test.test')
    login_page.enter_password('role_system@test.test')
    login_page.submit()

    sleep(20)

def test_verstka_news():
    webdriver.get('AbsoluteUrl')




