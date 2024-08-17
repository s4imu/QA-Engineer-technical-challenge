import time

import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def type(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self,locator):
        self.find_element(locator).click()

    def check_if_element_exists(self, locator):
        assert self.find_element(locator).is_displayed(), f"Element '{locator}' not found!!!"

    def check_element_text(self, locator):
        self.wait_element_appears(locator)
        return self.find_element(locator).text

    def page_redirect_check(self, expected_title):
        gotten_title = self.check_element_text(self.page_title)
        assert gotten_title == expected_title, f"Expected text: '{expected_title}' Gotten text: '{gotten_title}'"

    def wait_element_appears(self, locator, timeout=10):
        return WebDriverWait(self.driver,  timeout).until(EC.presence_of_element_located(locator))

    def wait_element_disappear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    def wait_resolve_captcha(self, timeout=10):
        self.driver.execute_script("alert('Clique no Botão OK para fechar esse Alerta e Preencha Corretamente o CAPTCHA em 10 segundos');")
        return time.sleep(timeout)

    def element_exists_check(self, locator):
        assert self.find_element(locator), f"Element {locator} exists but was not found!!!"

    def element_not_exist_check(self, locator):
        assert len(self.find_elements(locator)) == 0, f"Element {locator} was found even was not supposed!!!"

    def double_click(self, locator):
        element = self.wait_element_appears(locator)
        ActionChains(self.driver).double_click(element).perform()

    def right_button_click(self, locator):
        element = self.wait_element_appears(locator)
        ActionChains(self.driver).context_click(element).perform()

    def keyboard_key_press(self, locator, key):
        element = self.find_element(locator)
        if key == "ENTER":
            element.send_keys(Keys.ENTER)
        elif key == "SPACE":
            element.send_keys(Keys.SPACE)
        elif key == "BACKSPACE":
            element.send_keys(Keys.BACKSPACE)

    def select_option(self, locator, option):
        dropdown = Select(self.find_element(locator))
        return dropdown.select_by_value(option)
