from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep

from app.admin import my_searcher
from app.admin.pom.searcher import Searcher


class LoginPage: #Объявление класса
    path = '/login' #Путь

#Поиск полей ввода на странице
    def __init__(self, driver, host: str): #Объявляет метод __init__, который принимает аргументы self(обращаеться сам к себе(только к себе)) driver(браузер), host(адрес хоста)
        self.driver: WebDriver = driver
        self.url = host + self.path
        self.driver.get(self.url)

#Отправка данных в поля ввода
    def enter_login(self, text: str):
        field = Searcher.get_by_class_name(page=self, locator='LOCATOR_LOGIN_FIELD')
        field.send_keys(text)

    def enter_password(self, text: str):
        field = Searcher.get_by_class_name(page=self, locator='LOCATOR_PASSWORD_FIELD')
        field.send_keys(text)

    def submit(self):
        btn = Searcher.get_by_class_name(page=self, locator='LOCATOR_SUBMIT_BTN')
        btn.click()

    def open_side_menu(self):
        temp=self
        btn = my_searcher.get_by_class_name(temp, 'LOCATOR_SIDEBAR_TOGGLE_BTN')
        btn.click()

    def creds(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.submit()
        sleep(1)
        self.open_side_menu()
        sleep(1)