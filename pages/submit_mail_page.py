import allure

from locators.submit_mail_locators import SubmitMailLocators
from pages.base_page import BasePage


class SubmitMailPage(BasePage):
    locators = SubmitMailLocators

    @allure.step('Подсветить пароль')
    def click_highlight_password_button(self):
        self.click(self.locators.highlight_password_icon)

    @allure.step('Проверить подсвечен ли пароль')
    def is_password_highlighted(self):
        return 'text' == self.find_element(self.locators.password_field).get_attribute('type')
