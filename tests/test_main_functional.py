import allure
from selenium import webdriver

from pages.login_page import LoginPage
from pages.main_page import MainPage

from data import OPENED_POPUP_CLASSNAME


class TestMainFunctional:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title('Проверка успешной работы кнопки Конструктор')
    def test_konstrukt_button(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/login')
        main_page = MainPage(self.driver)
        main_page.click_konstrukt_button()
        assert main_page.get_current_url() == 'https://stellarburgers.nomoreparties.site/'

    @allure.title('Проверка успешной работы кнопки Лента')
    def test_order_feed_button(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/')
        main_page = MainPage(self.driver)
        main_page.click_order_feed()
        assert main_page.get_current_url() == 'https://stellarburgers.nomoreparties.site/feed'

    @allure.title('Проверка успешной работы попапа')
    def test_flur_bulka_detailed(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/')
        main_page = MainPage(self.driver)
        main_page.click_flur_bulka()
        assert 'Детали ингредиента' in main_page.get_page_source()

    @allure.title('Проверка успешного закрытия попапа')
    def test_close_bulka_detailed(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/')
        main_page = MainPage(self.driver)
        main_page.click_flur_bulka()
        main_page.close_flur_bulka_popup()
        assert OPENED_POPUP_CLASSNAME not in main_page.get_page_source()

    @allure.title('Проверка калькуляции ингредииентов')
    def test_ingredient_count(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/')
        main_page = MainPage(self.driver)
        main_page.drag_and_drop_space_sauce()
        assert main_page.get_space_sauce_count() == '1'

    @allure.title('Проверка создания заказа')
    def test_logged_in_order(self, login_data):
        login_page = LoginPage(self.driver)
        login_page.set_local(login_data)
        self.driver.get('https://stellarburgers.nomoreparties.site/')
        main_page = MainPage(self.driver)
        main_page.drag_and_drop_space_sauce()
        main_page.click_order_button()
        assert 'Ваш заказ начали готовить' in main_page.get_page_source()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
