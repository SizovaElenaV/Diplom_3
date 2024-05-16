from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def execute_script_without_element(self, script):
        return self.driver.execute_script(script)

    def execute_script(self, script, locator):
        return self.driver.execute_script(script, self.find_element(locator))

    def js_click(self, locator):
        return self.execute_script("arguments[0].click()", locator)

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def get_text(self, locator):
        return self.find_element(locator).text

    def send_keys(self, locator, data):
        self.find_element(locator).send_keys(data)

    def click(self, locator):
        self.find_element(locator).click()

    @staticmethod
    def click_element(elem):
        elem.click()

    def get_current_url(self):
        return self.driver.current_url

    def switch(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def windows_count(self):
        return len(self.driver.window_handles)

    def wait_untill_url_to_be(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    def wait_until_text_change(self, locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))

    def get_page_source(self):
        return self.driver.page_source

    def drag_and_drop_elem(self, source_locator, target_locator):
        action = ActionChains(self.driver)
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        action.drag_and_drop(source, target).perform()
