import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    restore_password_button = (By.XPATH, "//a[@href='/forgot-password']")
    email_field = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default']/input")
    password_field = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"]/div/div/input[@type="password"]')
    submit_button = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx '
                               'button_button_size_medium__3zxIa"]')

    @allure.step('Нажатие на конпку сброса пароля')
    def reset_password_button_click(self):
        self.click(self.restore_password_button)

    @allure.step('Заполнение емеила')
    def set_email(self, email):
        self.send_keys(self.email_field, email)

    @allure.step('Заполнение пароля')
    def set_password(self, password):
        self.send_keys(self.password_field, password)

    @allure.step('Клик подтверждения формы')
    def click_submit_button(self):
        self.click(self.submit_button)

    @allure.step('Логин юзера')
    def login_user(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_submit_button()

    @allure.step('Обновление токенов')
    def set_local(self, data):
        self.execute_script_without_element(f"window.localStorage.setItem('accessToken','{data['accessToken']}');")
        self.execute_script_without_element(f"window.localStorage.setItem('refreshToken','{data['refreshToken']}');")
