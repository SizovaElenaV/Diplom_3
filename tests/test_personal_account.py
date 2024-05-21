import allure

from data import UrlPageData


from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage


class TestPersonalAccount:

    @allure.title('Проверка кнопки личного кабинета')
    def test_personal_account_button(self, driver):
        driver.get(UrlPageData.INDEX_URL)
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        assert main_page.get_current_url() == UrlPageData.LOGIN_URL

    @allure.title('Проверка истории заказов')
    def test_order_history(self, driver, login_data):
        login_page = LoginPage(driver)
        login_page.set_local(login_data)
        driver.get(UrlPageData.ACCOUNT_URL)
        profile_page = ProfilePage(driver)
        profile_page.click_history_button()

        assert profile_page.get_current_url() == UrlPageData.ORDER_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта')
    def test_quit_account(self, driver, login_data):
        login_page = LoginPage(driver)
        login_page.set_local(login_data)
        driver.get(UrlPageData.ACCOUNT_URL)

        profile_page = ProfilePage(driver)

        profile_page.click_quit_button()
        assert profile_page.get_current_url() == UrlPageData.LOGIN_URL
