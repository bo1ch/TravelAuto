from app.admin import Admin
from selenium import webdriver


class Application:

    def __init__(self, env: str = 'STAGE'):
        self.driver = webdriver.Chrome()
        self.env = env

        self.admin = Admin(self.driver, env)
        self.website = ''
