import allure

from data import UrlPageData

from pages.login_page import LoginPage
from pages.reset_page import ResetPage
from pages.submit_mail_page import SubmitMailPage


class TestPasswordReset:

    @allure.title('Проверка удачного ресета пароля')
    def test_success_reset_button_redirect(self, driver):
        driver.get(UrlPageData.LOGIN_URL)
        login_page = LoginPage(driver)

        login_page.reset_password_button_click()
        assert login_page.get_current_url() == UrlPageData.FORGOT_PASSWORD_URL

    @allure.title('Проверка удачного ресета формы')
    def test_success_reset_form(self, driver):
        driver.get(UrlPageData.FORGOT_PASSWORD_URL)
        reset_page = ResetPage(driver)

        reset_page.fill_reset_form('adssa@mail.ru')

        assert reset_page.get_current_url() == UrlPageData.RESET_PASSWORD_URL

    @allure.title('Проверка подсветки пароля')
    def test_is_password_highlighted(self, driver):
        reset_page = ResetPage(driver)
        reset_page.click_reset_button()
        submit_mail_page = SubmitMailPage(driver)
        submit_mail_page.click_highlight_password_button()
        assert submit_mail_page.is_password_highlighted()
