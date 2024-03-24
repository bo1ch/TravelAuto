from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage: #Объявление класса
    path = '/login' #Путь
#Поиск полей ввода на странице
    LOCATOR_LOGIN_FIELD = 'FieldText__input'
    LOCATOR_PASSWORD_FIELD = 'FieldPassword__input'
    LOCATOR_SUBMIT_BTN = 'Modal__submit'
    LOCATOR_SIDEBAR_TOGGLE_BTN = 'Sidebar__toggle'
    LOCATOR_TAB_MAIN_REPORT = 'Основной отчет'
    LOCATOR_TAB_LANDINGS = 'Лендинги'
    LOCATOR_TAB_HANDWORK = 'Ручное Управление'
    LOCATOR_TAB_SETTINGS = 'Настройки'


    def __init__(self, driver, host: str): #Объявляет метод __init__, который принимает аргументы self(обращаеться сам к себе(только к себе)) driver(браузер), host(адрес хоста)
        self.driver: WebDriver = driver
        self.url = host + self.path
        self.driver.get(self.url)
#Отправка данных в поля ввода
    def enter_login(self, text: str):
        field = self.driver.find_element(By.CLASS_NAME, self.LOCATOR_LOGIN_FIELD)
        field.send_keys(text)

    def enter_password(self, text: str):
        field = self.driver.find_element(By.CLASS_NAME, self.LOCATOR_PASSWORD_FIELD)
        field.send_keys(text)

    def submit(self):
        btn = self.driver.find_element(By.CLASS_NAME, self.LOCATOR_SUBMIT_BTN)
        btn.click()

    def open_side_menu(self):
        btn = self.driver.find_element(By.CLASS_NAME, self.LOCATOR_SIDEBAR_TOGGLE_BTN)
        btn.click()

    def check_tab_main_reports(self):
        check = self.driver.find_element(By.LINK_TEXT, self.LOCATOR_TAB_MAIN_REPORT)
        check
        # if len(check) == 0:
        #     print("Нету = хорошо".format(self.LOCATOR_TAB_MAIN_REPORT))
        # else:
        #     assert False, "Элемент есть = плохо".format(self.LOCATOR_TAB_MAIN_REPORT)

    def check_tab_landings(self):
        check = self.driver.find_element(By.LINK_TEXT, self.LOCATOR_TAB_LANDINGS)
        assert check

    def check_tab_handwork(self):
        check = self.driver.find_element(By.LINK_TEXT, self.LOCATOR_TAB_HANDWORK)
        assert check

    def check_tab_settings(self):
        check = self.driver.find_element(By.LINK_TEXT, self.LOCATOR_TAB_SETTINGS)
        assert check
