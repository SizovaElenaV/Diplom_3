import allure

from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginLocators

    @allure.step('Нажатие на конпку сброса пароля')
    def reset_password_button_click(self):
        self.click(self.locators.restore_password_button)

    @allure.step('Заполнение емеила')
    def set_email(self, email):
        self.send_keys(self.locators.email_field, email)

    @allure.step('Заполнение пароля')
    def set_password(self, password):
        self.send_keys(self.locators.password_field, password)

    @allure.step('Клик подтверждения формы')
    def click_submit_button(self):
        self.click(self.locators.submit_button)

    @allure.step('Логин юзера')
    def login_user(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_submit_button()

    @allure.step('Обновление токенов')
    def set_local(self, data):
        self.execute_script_without_element(f"window.localStorage.setItem('accessToken','{data['accessToken']}');")
        self.execute_script_without_element(f"window.localStorage.setItem('refreshToken','{data['refreshToken']}');")
