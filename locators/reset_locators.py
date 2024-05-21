from selenium.webdriver.common.by import By

class ResetLocators:
    mail_input = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"]')
    reset_submit_button = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx '
                                     'button_button_size_medium__3zxIa"]')
