import allure
from selenium import webdriver

from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage


class TestPersonalAccount:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title('Проверка кнопки личного кабинета')
    def test_personal_account_button(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/')
        main_page = MainPage(self.driver)
        main_page.click_personal_account_button()
        assert main_page.get_current_url() == 'https://stellarburgers.nomoreparties.site/login'

    @allure.title('Проверка истории заказов')
    def test_order_history(self, login_data):
        login_page = LoginPage(self.driver)
        login_page.set_local(login_data)
        self.driver.get('https://stellarburgers.nomoreparties.site/account')
        profile_page = ProfilePage(self.driver)
        profile_page.click_history_button()

        assert profile_page.get_current_url() == 'https://stellarburgers.nomoreparties.site/account/order-history'

    @allure.title('Проверка выхода из аккаунта')
    def test_quit_account(self, login_data):
        login_page = LoginPage(self.driver)
        login_page.set_local(login_data)
        self.driver.get('https://stellarburgers.nomoreparties.site/account')

        profile_page = ProfilePage(self.driver)

        profile_page.click_quit_button()
        assert profile_page.get_current_url() == 'https://stellarburgers.nomoreparties.site/login'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
