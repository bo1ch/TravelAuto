from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

locators = {
        'LOCATOR_LOGIN_FIELD' : 'FieldText__input',
        'LOCATOR_PASSWORD_FIELD' : 'FieldPassword__input',
        'LOCATOR_SUBMIT_BTN' : 'Modal__submit',
        'LOCATOR_SIDEBAR_TOGGLE_BTN' : 'Sidebar__toggle',
        'LOCATOR_TAB_MAIN_REPORT' : 'Основной отчет',
        'LOCATOR_TAB_LANDINGS' : 'Лендинги',
        'LOCATOR_TAB_HANDWORK' : 'Ручное Управление',
        'LOCATOR_TAB_SETTINGS' : 'Настройки'
    }
class  Searcher:

    def check_by_link_text(self, page, findable, locator, name='Имя не известно'):
        try:
            page.driver.find_element(By.LINK_TEXT, locators[locator])
        except NoSuchElementException:
            if findable:
                print(f'Элемент с текстом ссылки {name} - не найден, а должен был')
            else:
                print(f'Элемент с текстом ссылки {name} - не найден, как и надо было')
            return False
        if findable:
            print(f'Элемент с текстом ссылки {name} - найден, как и надо было')
        else:
            print(f'Элемент с текстом ссылки {name} - найден, хотя не должен был')
        return True

    def check_by_class_name(self, page, findable, locator, name='Имя не известно'):
        try:
            page.driver.find_element(By.CLASS_NAME, locators[locator])
        except NoSuchElementException:
            if findable:
                print(f'Элемент с названием класса {name} - не найден, а должен был')
            else:
                print(f'Элемент с названием класса {name} - не найден, как и надо было')
            return False
        if findable:
            print(f'Элемент с названием класса {name} - найден, как и надо было')
        else:
            print(f'Элемент с названием класса {name} - найден, хотя не должен был')
        return True

    def get_by_class_name(self, page, locator):
        return page.driver.find_element(By.CLASS_NAME, locators[locator])
