import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    personal_account_button = (By.XPATH, '//a[@href="/account"]')
    konstrukt_button = (By.XPATH, '//a[@href="/"]')
    order_feed = (By.XPATH, '//a[@href="/feed"]')
    flur_bulka = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    flur_bulka_button_popup = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']/div["
                                         "@class='Modal_modal__container__Wo2l_']/button")
    space_sauce = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]')
    space_sauce_counter = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa73']/div["
                                     "@class='counter_counter__ZNLkj counter_default__28sqi']/p["
                                     "@class='counter_counter__num__3nue1']")
    bulka_drop_area = (By.XPATH, "//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']")
    order_button = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    @allure.step('Нажатие на кнопку Личный Кабинет')
    def click_personal_account_button(self):
        self.click(self.personal_account_button)

    @allure.step('Нажатие на кнопку Конструктор')
    def click_konstrukt_button(self):
        self.click(self.konstrukt_button)

    @allure.step('Нажатие на кнопку Лента')
    def click_order_feed(self):
        self.click(self.order_feed)

    @allure.step('Нажатие на Булку')
    def click_flur_bulka(self):
        self.click(self.flur_bulka)

    @allure.step('Закрытие попапа с Булкой')
    def close_flur_bulka_popup(self):
        self.click(self.flur_bulka_button_popup)

    @allure.step('Перетащить И Уронить Космический Соус')
    def drag_and_drop_space_sauce(self):
        self.drag_and_drop_elem(self.space_sauce, self.bulka_drop_area)

    @allure.step('Посчитать кол-во космических соусов')
    def get_space_sauce_count(self):
        return self.get_text(self.space_sauce_counter)

    @allure.step('Нажать кнопку заказа')
    def click_order_button(self):
        return self.click(self.order_button)
