import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProfilePage(BasePage):
    history_button = (By.XPATH, '//a[@href="/account/order-history"]')
    quit_button = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')

    @allure.step('Нажать кнопку истории')
    def click_history_button(self):
        self.click(self.history_button)

    @allure.step('Нажать кнопку выхода')
    def click_quit_button(self):
        self.click(self.quit_button)
