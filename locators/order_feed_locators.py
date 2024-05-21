from selenium.webdriver.common.by import By

class OrderFeedLocators:
    history_feed = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]')
    all_time_orders = (By.XPATH, '//div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text '
                                 'text_type_digits-large"]')
    today_orders = (By.XPATH, '//div/p[@class="OrderFeed_number__2MbrQ text '
                              'text_type_digits-large"]')
    in_work_orders = (By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]')
