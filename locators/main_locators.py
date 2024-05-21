from selenium.webdriver.common.by import By

class MainLocators:
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
