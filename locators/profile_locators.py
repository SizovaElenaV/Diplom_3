from selenium.webdriver.common.by import By


class ProfileLocators:
    history_button = (By.XPATH, '//a[@href="/account/order-history"]')
    quit_button = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')
