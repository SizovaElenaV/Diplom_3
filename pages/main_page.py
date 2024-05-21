import allure

from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainLocators

    @allure.step('Нажатие на кнопку Личный Кабинет')
    def click_personal_account_button(self):
        self.click(self.locators.personal_account_button)

    @allure.step('Нажатие на кнопку Конструктор')
    def click_konstrukt_button(self):
        self.click(self.locators.konstrukt_button)

    @allure.step('Нажатие на кнопку Лента')
    def click_order_feed(self):
        self.click(self.locators.order_feed)

    @allure.step('Нажатие на Булку')
    def click_flur_bulka(self):
        self.click(self.locators.flur_bulka)

    @allure.step('Закрытие попапа с Булкой')
    def close_flur_bulka_popup(self):
        self.click(self.locators.flur_bulka_button_popup)

    @allure.step('Перетащить И Уронить Космический Соус')
    def drag_and_drop_space_sauce(self):
        self.drag_and_drop_elem(self.locators.space_sauce, self.locators.bulka_drop_area)

    @allure.step('Посчитать кол-во космических соусов')
    def get_space_sauce_count(self):
        return self.get_text(self.locators.space_sauce_counter)

    @allure.step('Нажать кнопку заказа')
    def click_order_button(self):
        return self.click(self.locators.order_button)
