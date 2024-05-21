import allure

from locators.reset_locators import ResetLocators
from pages.base_page import BasePage


class ResetPage(BasePage):
    locators = ResetLocators

    @allure.step('Заполнить поле емеила')
    def set_email_field(self, mail):
        self.send_keys(self.locators.mail_input, mail)

    @allure.step('Нажать енопку сброса пароля')
    def click_reset_button(self):
        self.click(self.locators.reset_submit_button)

    @allure.step('Заполнить форму сброса пароля')
    def fill_reset_form(self, mail):
        self.set_email_field(mail)
        self.click_reset_button()
