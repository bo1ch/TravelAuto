from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def find_by_link_text(page, findable, locator, name='Имя не известно'):
    try:
        page.driver.find_element(By.LINK_TEXT, locator)
    except NoSuchElementException:
        if findable:
            print(f'Элемент с тексто ссылки {name} - не найден, а должен был')
        else:
            print(f'Элемент с тексто ссылки {name} - не найден, как и надо было')
        return False
    if findable:
        print(f'Элемент с тексто ссылки {name} - найден, как и надо было')
    else:
        print(f'Элемент с тексто ссылки {name} - найден, хотя не должен был')
    return True

def find_by_class_name(page, findable, locator, name='Имя не известно'):
    try:
        page.driver.find_element(By.CLASS_NAME, locator)
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