import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ResetPage(BasePage):
    mail_input = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"]')
    reset_submit_button = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx '
                                     'button_button_size_medium__3zxIa"]')

    @allure.step('Заполнить поле емеила')
    def set_email_field(self, mail):
        self.send_keys(self.mail_input, mail)

    @allure.step('Нажать енопку сброса пароля')
    def click_reset_button(self):
        self.click(self.reset_submit_button)

    @allure.step('Заполнить форму сброса пароля')
    def fill_reset_form(self, mail):
        self.set_email_field(mail)
        self.click_reset_button()
