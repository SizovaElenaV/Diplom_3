import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage

from data import UrlPageData, LocatorData


class TestMainFunctional:

    @allure.title('Проверка успешной работы кнопки Конструктор')
    def test_konstrukt_button(self, driver):
        driver.get(UrlPageData.LOGIN_URL)
        main_page = MainPage(driver)
        main_page.click_konstrukt_button()
        assert main_page.get_current_url() == UrlPageData.INDEX_URL

    @allure.title('Проверка успешной работы кнопки Лента')
    def test_order_feed_button(self, driver):
        driver.get(UrlPageData.INDEX_URL)
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert main_page.get_current_url() == UrlPageData.FEED_URL

    @allure.title('Проверка успешной работы попапа')
    def test_flur_bulka_detailed(self, driver):
        driver.get(UrlPageData.INDEX_URL)
        main_page = MainPage(driver)
        main_page.click_flur_bulka()
        assert 'Детали ингредиента' in main_page.get_page_source()

    @allure.title('Проверка успешного закрытия попапа')
    def test_close_bulka_detailed(self, driver):
        driver.get(UrlPageData.INDEX_URL)
        main_page = MainPage(driver)
        main_page.click_flur_bulka()
        main_page.close_flur_bulka_popup()
        assert LocatorData.OPENED_POPUP_CLASSNAME not in main_page.get_page_source()

    @allure.title('Проверка калькуляции ингредииентов')
    def test_ingredient_count(self, driver):
        driver.get(UrlPageData.INDEX_URL)
        main_page = MainPage(driver)
        main_page.drag_and_drop_space_sauce()
        assert main_page.get_space_sauce_count() == '1'

    @allure.title('Проверка создания заказа')
    def test_logged_in_order(self, driver, login_data):
        login_page = LoginPage(driver)
        login_page.set_local(login_data)
        driver.get(UrlPageData.INDEX_URL)
        main_page = MainPage(driver)
        main_page.drag_and_drop_space_sauce()
        main_page.click_order_button()
        assert 'Ваш заказ начали готовить' in main_page.get_page_source()
