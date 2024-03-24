from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from app import Application

LOCATOR_LOGIN_FIELD = 'FieldText__input'
LOCATOR_PASSWORD_FIELD = 'FieldPassword__input'
LOCATOR_SUBMIT_BTN = 'Modal__submit'
LOCATOR_SIDEBAR_TOGGLE_BTN = 'Sidebar__toggle'

def test_login():
    app = Application()
    login_page = app.admin.login_page
    login_page.enter_login('test1')
    login_page.enter_password('test2')
    login_page.submit()

    sleep(10)

def test_login_success():
    # Проверка успешного входа путем сравнения текущего URL с URL страницы входа
    app = Application()
    login_page = app.admin.login_page
    login_page.enter_login('role_system@test.test')
    login_page.enter_password('role_system@test.test')
    login_page.submit()

    sleep(3)

    assert login_page.driver.current_url != 'https://admin.travelwise.click/login'


