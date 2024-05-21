from selenium.webdriver.common.by import By

class LoginLocators:
    restore_password_button = (By.XPATH, "//a[@href='/forgot-password']")
    email_field = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default']/input")
    password_field = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"]/div/div/input[@type="password"]')
    submit_button = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx '
                               'button_button_size_medium__3zxIa"]')
