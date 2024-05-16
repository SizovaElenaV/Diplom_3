import allure
from selenium import webdriver

from pages.order_feed_page import OrderFeedPage

from data import OPENED_POPUP_CLASSNAME


class TestOrderFeed:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title('Проверка попапа')
    def test_detailed_order_popup(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/feed')
        order_feed_page = OrderFeedPage(self.driver)
        order_feed_page.click_random_history_feed()
        assert OPENED_POPUP_CLASSNAME in order_feed_page.get_page_source()

    @allure.title('Проверка истории и ленты')
    def test_history_in_feed(self, order_number):
        self.driver.get('https://stellarburgers.nomoreparties.site/feed')
        order_feed_page = OrderFeedPage(self.driver)
        assert str(order_number) in order_feed_page.get_page_source()

    @allure.title('Проверка подсчета всех заказов')
    def test_all_time_orders_counter(self):
        order_feed_page = OrderFeedPage(self.driver)
        before_count = int(order_feed_page.get_all_time_orders())
        order_feed_page.make_order()
        after_count = int(order_feed_page.get_all_time_orders())
        assert before_count < after_count

    @allure.title('Проверка подсчета сегодняшних')
    def test_today_orders_counter(self):
        order_feed_page = OrderFeedPage(self.driver)
        before_count = int(order_feed_page.get_today_orders())
        order_feed_page.make_order()
        after_count = int(order_feed_page.get_today_orders())
        assert before_count < after_count

    @allure.title('Проверка заказов в работе')
    def test_order_in_work(self):
        order_feed_page = OrderFeedPage(self.driver)
        num = order_feed_page.make_order()
        order_feed_page.wait_order_to_appear(str(num))
        assert str(num) in order_feed_page.get_in_work_orders()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()