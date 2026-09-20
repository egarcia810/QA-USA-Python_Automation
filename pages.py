from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')

    CALL_TAXI_BUTTON_LOCATOR = (
        By.XPATH,
        '//button[text()="Call a taxi"]'
    )

    SUPPORTIVE_PLAN_LOCATOR = (
        By.XPATH,
        '//div[@class="tcard-title" and text()="Supportive"]/parent::div'
    )

    PHONE_BUTTON_LOCATOR = (
        By.XPATH,
        '//div[@class="np-text" and text()="Phone number"]/parent::div'
    )

    PHONE_NUMBER_LOCATOR = (By.ID, 'phone')

    NEXT_BUTTON_LOCATOR = (
        By.XPATH,
        '//button[text()="Next"]'
    )

    CODE_LOCATOR = (By.ID, 'code')

    CONFIRM_BUTTON_LOCATOR = (
        By.XPATH,
        '//button[text()="Confirm"]'
    )

    PAYMENT_METHOD_LOCATOR = (
        By.XPATH,
        '//div[@class="pp-text" and text()="Payment method"]/parent::div'
    )

    ADD_CARD_LOCATOR = (
        By.CLASS_NAME,
        'pp-plus-container'
    )

    CARD_NUMBER_LOCATOR = (By.ID, 'number')

    CARD_CODE_LOCATOR = (
        By.XPATH,
        '//div[@class="card-code-input"]/input[@id="code"]'
    )

    LINK_BUTTON_LOCATOR = (
        By.XPATH,
        '//button[text()="Link"]'
    )

    MESSAGE_TO_DRIVER_LOCATOR = (By.ID, 'comment')

    BLANKET_AND_HANDKERCHIEFS_LOCATOR = (
        By.XPATH,
        '//div[text()="Blanket and handkerchiefs"]/following::span[@class="slider round"][1]'
    )

    ICE_CREAM_PLUS_LOCATOR = (
        By.XPATH,
        '//div[@class="r-counter-label" and text()="Ice cream"]'
        '/following-sibling::div//div[@class="counter-plus"]'
    )

    ICE_CREAM_COUNT_LOCATOR = (
        By.XPATH,
        '//div[@class="r-counter-label" and text()="Ice cream"]'
        '/following-sibling::div//div[@class="counter-value"]'
    )

    ORDER_BUTTON_LOCATOR = (
        By.CLASS_NAME,
        'smart-button'
    )

    CAR_SEARCH_LOCATOR = (
        By.CLASS_NAME,
        'order-header-title'
    )

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.FROM_LOCATOR
            )
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(
            *self.TO_LOCATOR
        ).send_keys(to_address)

    def click_call_taxi(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.CALL_TAXI_BUTTON_LOCATOR
            )
        ).click()

    def select_supportive_plan(self):
        self.driver.find_element(
            *self.SUPPORTIVE_PLAN_LOCATOR
        ).click()

    def click_phone_button(self):
        self.driver.find_element(
            *self.PHONE_BUTTON_LOCATOR
        ).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(
            *self.PHONE_NUMBER_LOCATOR
        ).send_keys(phone_number)

    def click_next(self):
        self.driver.find_element(
            *self.NEXT_BUTTON_LOCATOR
        ).click()

    def set_code(self, code):
        self.driver.find_element(
            *self.CODE_LOCATOR
        ).send_keys(code)

    def click_confirm(self):
        self.driver.find_element(
            *self.CONFIRM_BUTTON_LOCATOR
        ).click()

    def click_payment_method(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.PAYMENT_METHOD_LOCATOR
            )
        ).click()

    def click_add_card(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.ADD_CARD_LOCATOR
            )
        ).click()

    def set_card_number(self, card_number):
        self.driver.find_element(
            *self.CARD_NUMBER_LOCATOR
        ).send_keys(card_number)

    def set_card_code(self, card_code):
        self.driver.find_element(
            *self.CARD_CODE_LOCATOR
        ).send_keys(card_code)

    def click_link(self):
        self.driver.find_element(
            *self.LINK_BUTTON_LOCATOR
        ).click()

    def set_message_to_driver(self, message):
        self.driver.find_element(
            *self.MESSAGE_TO_DRIVER_LOCATOR
        ).send_keys(message)

    def select_blanket_and_handkerchiefs(self):
        element = self.driver.find_element(
            *self.BLANKET_AND_HANDKERCHIEFS_LOCATOR
        )
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def add_ice_cream(self):
        element = self.driver.find_element(
            *self.ICE_CREAM_PLUS_LOCATOR
        )
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def get_ice_cream_count(self):
        return self.driver.find_element(
            *self.ICE_CREAM_COUNT_LOCATOR
        ).text

    def click_order(self):
        element = self.driver.find_element(
            *self.ORDER_BUTTON_LOCATOR
        )
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def wait_for_car_search(self):
        return WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.CAR_SEARCH_LOCATOR
            )
        )