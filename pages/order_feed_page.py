import random

import allure

from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage

from utils import make_order


class OrderFeedPage(BasePage):
    locators = OrderFeedLocators

    @allure.step('Нажать на случайный заказ из истории')
    def click_random_history_feed(self):
        return self.click_element(self.get_random_history_feed())

    @allure.step('Получить случайный заказ из истории')
    def get_random_history_feed(self):
        return random.choice(self.find_elements(self.locators.history_feed))

    @allure.step('Получить заказы за все время')
    def get_all_time_orders(self):
        return self.get_text(self.locators.all_time_orders)

    @allure.step('Получить заказы за сегодня')
    def get_today_orders(self):
        return self.get_text(self.locators.today_orders)

    @allure.step('Получить заказы в работе')
    def get_in_work_orders(self):
        return self.get_text(self.locators.in_work_orders)

    @allure.step('Получить заказы в готовке')
    def wait_order_to_appear(self, order_num):
        self.wait_until_text_change(self.locators.in_work_orders, order_num)

    @staticmethod
    def make_order():
        return make_order()
