import random

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from utils import make_order


class OrderFeedPage(BasePage):
    history_feed = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]')
    all_time_orders = (By.XPATH, '//div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text '
                                 'text_type_digits-large"]')
    today_orders = (By.XPATH, '//div/p[@class="OrderFeed_number__2MbrQ text '
                              'text_type_digits-large"]')
    in_work_orders = (By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]')

    @allure.step('Нажать на случайный заказ из истории')
    def click_random_history_feed(self):
        return self.click_element(self.get_random_history_feed())

    @allure.step('Получить случайный заказ из истории')
    def get_random_history_feed(self):
        return random.choice(self.find_elements(self.history_feed))

    @allure.step('Получить заказы за все время')
    def get_all_time_orders(self):
        return self.get_text(self.all_time_orders)

    @allure.step('Получить заказы за сегодня')
    def get_today_orders(self):
        return self.get_text(self.today_orders)

    @allure.step('Получить заказы в работе')
    def get_in_work_orders(self):
        return self.get_text(self.in_work_orders)

    @allure.step('Получить заказы в готовке')
    def wait_order_to_appear(self, order_num):
        self.wait_until_text_change(self.in_work_orders, order_num)

    @staticmethod
    def make_order():
        return make_order()
