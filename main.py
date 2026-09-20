import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    def setup_method(self):
        # do not modify - we need additional logging enabled
        from selenium.webdriver import DesiredCapabilities

        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        self.driver = webdriver.Chrome()
        self.page = UrbanRoutesPage(self.driver)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print('Connected to the Urban Routes server')
        else:
            print(
                'Cannot connect to Urban Routes. '
                'Check the server is on and still running'
            )

    def prepare_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page.set_from(data.ADDRESS_FROM)
        self.page.set_to(data.ADDRESS_TO)

    def prepare_plan(self):
        self.prepare_route()
        self.page.click_call_taxi()
        self.page.select_supportive_plan()

    def prepare_phone(self):
        self.prepare_plan()
        self.page.click_phone_button()
        self.page.set_phone_number(data.PHONE_NUMBER)
        self.page.click_next()

        code = helpers.retrieve_phone_code(self.driver)

        self.page.set_code(code)
        self.page.click_confirm()

    def prepare_card(self):
        self.prepare_phone()
        self.page.click_payment_method()
        self.page.click_add_card()
        self.page.set_card_number(data.CARD_NUMBER)
        self.page.set_card_code(data.CARD_CODE)
        self.page.click_link()

    def prepare_comment(self):
        self.prepare_card()
        self.page.set_message_to_driver(
            data.MESSAGE_FOR_DRIVER
        )

    def prepare_blanket(self):
        self.prepare_comment()
        self.page.select_blanket_and_handkerchiefs()

    def prepare_ice_cream(self):
        self.prepare_blanket()

        for i in range(2):
            self.page.add_ice_cream()

    def test_set_route(self):
        self.prepare_route()

        assert self.driver.find_element(
            *self.page.FROM_LOCATOR
        ).get_attribute('value') == data.ADDRESS_FROM

        assert self.driver.find_element(
            *self.page.TO_LOCATOR
        ).get_attribute('value') == data.ADDRESS_TO

    def test_select_plan(self):
        self.prepare_plan()

        assert self.driver.find_element(
            *self.page.SUPPORTIVE_PLAN_LOCATOR
        ).is_displayed()

    def test_fill_phone_number(self):
        self.prepare_phone()

        assert data.PHONE_NUMBER is not None

    def test_fill_card(self):
        self.prepare_card()

        assert self.driver.find_element(
            *self.page.MESSAGE_TO_DRIVER_LOCATOR
        ).is_displayed()

    def test_comment_for_driver(self):
        self.prepare_comment()

        assert self.driver.find_element(
            *self.page.MESSAGE_TO_DRIVER_LOCATOR
        ).get_attribute('value') == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.prepare_blanket()

        assert self.driver.find_element(
            *self.page.BLANKET_AND_HANDKERCHIEFS_LOCATOR
        ).is_displayed()

    def test_order_2_ice_creams(self):
        self.prepare_ice_cream()

        assert self.page.get_ice_cream_count() == '2'

    def test_car_search_model_appears(self):
        self.prepare_ice_cream()

        self.page.click_order()

        car_search = self.page.wait_for_car_search()

        assert car_search.text == 'Car search'

    def teardown_method(self):
        self.driver.quit()