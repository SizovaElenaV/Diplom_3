from selenium.webdriver.common.by import By

class SubmitMailLocators:
    highlight_password_icon = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    password_field = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"]/div/div/input')
