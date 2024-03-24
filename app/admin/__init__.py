from app.admin.pom.login import LoginPage


class Admin:

    def __init__(self, driver, env: str = 'STAGE'):
        self.driver = driver
        self.env = env

        if self.env == 'PRODUCTION':
            self.base_url = 'https://admin.travelwiseway.com'
        else:
            self.base_url = 'https://admin.travelwise.click'

        self.login_page = LoginPage(driver=driver, host=self.base_url)