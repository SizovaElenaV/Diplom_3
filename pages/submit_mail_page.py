import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SubmitMailPage(BasePage):
    highlight_password_icon = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    password_field = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"]/div/div/input')

    @allure.step('Подсветить пароль')
    def click_highlight_password_button(self):
        self.click(self.highlight_password_icon)

    @allure.step('Проверить подсвечен ли пароль')
    def is_password_highlighted(self):
        return 'text' == self.find_element(self.password_field).get_attribute('type')
