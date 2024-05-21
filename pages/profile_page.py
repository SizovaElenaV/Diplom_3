import allure

from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    locators = ProfileLocators

    @allure.step('Нажать кнопку истории')
    def click_history_button(self):
        self.click(self.locators.history_button)

    @allure.step('Нажать кнопку выхода')
    def click_quit_button(self):
        self.click(self.locators.quit_button)
