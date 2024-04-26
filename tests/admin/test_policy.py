from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from app import Application
from app.admin.pom.searcher import Searcher


#Проверка на полиси(Все есть)
# def test_system():
#     app = Application()
#     admin_page = app.admin.login_page
#     admin_page.creds('role_system@test.test', 'role_system@test.test', admin_page)
#     admin_page.check_tab_main_reports(False)
# #Проверка на полиси()
#
# def test_manager():
#     app = Application()
#     admin_page = app.admin.login_page
#     creds('role_manager@test.test', 'role_manager@test.test', admin_page)
#     admin_page.check_tab_main_reports()

#Проверка на полиси(Новости и связи)
# def test_redactor():
#     app = Application()
#     admin_page = app.admin.login_page
#     admin_page.creds('role_redactor@test.test', 'role_redactor@test.test')
#     Searcher().check_by_link_text(admin_page, True, 'LOCATOR_TAB_SETTINGS', 'Настройки')
#
