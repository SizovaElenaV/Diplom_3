import allure
from selenium import webdriver

from pages.login_page import LoginPage
from pages.reset_page import ResetPage
from pages.submit_mail_page import SubmitMailPage


class TestPasswordReset:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title('Проверка удачного ресета пароля')
    def test_success_reset_button_redirect(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/login')
        login_page = LoginPage(self.driver)

        login_page.reset_password_button_click()
        assert login_page.get_current_url() == 'https://stellarburgers.nomoreparties.site/forgot-password'

    @allure.title('Проверка удачного ресета формы')
    def test_success_reset_form(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        reset_page = ResetPage(self.driver)

        reset_page.fill_reset_form('adssa@mail.ru')

        assert reset_page.get_current_url() == 'https://stellarburgers.nomoreparties.site/reset-password'

    @allure.title('Проверка подсветки пароля')
    def test_is_password_highlighted(self):
        reset_page = ResetPage(self.driver)
        reset_page.click_reset_button()
        submit_mail_page = SubmitMailPage(self.driver)
        submit_mail_page.click_highlight_password_button()
        assert submit_mail_page.is_password_highlighted()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

