from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from app import Application

#Проверка на полиси(Все есть)
def test_system():
    app = Application()
    admin_page = app.admin.login_page
    admin_page.enter_login('role_system@test.test')
    admin_page.enter_password('role_system@test.test')
    admin_page.submit()
    sleep(5)
    admin_page.open_side_menu()
    sleep(10)
#Проверка на полиси()

def test_manager():
    app = Application()
    admin_page = app.admin.admin_page
    admin_page.enter_login('role_manager@test.test')
    admin_page.enter_password('role_manager@test.test')
    admin_page.open_side_menu()

    sleep(10)

#Проверка на полиси(Новости и связи)
def test_redactor():
    app = Application()
    admin_page = app.admin.login_page
    admin_page.enter_login('role_redactor@test.test')
    admin_page.enter_password('role_redactor@test.test')
    admin_page.submit()
    sleep(2)
    admin_page.open_side_menu()
    sleep(2)
    admin_page.check_tab_main_reports()
