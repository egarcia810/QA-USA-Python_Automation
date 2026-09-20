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

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.page.set_from(data.ADDRESS_FROM)
        self.page.set_to(data.ADDRESS_TO)

        assert self.page.get_from() == data.ADDRESS_FROM
        assert self.page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.page.set_from(data.ADDRESS_FROM)
        self.page.set_to(data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()

        assert 'Supportive' in self.page.get_selected_plan()

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.page.set_from(data.ADDRESS_FROM)
        self.page.set_to(data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()

        self.page.click_phone_button()
        self.page.set_phone_number(data.PHONE_NUMBER)

        assert self.page.get_phone_number() == data.PHONE_NUMBER

        self.page.click_next()

        code = helpers.retrieve_phone_code(self.driver)

        self.page.set_code(code)
        self.page.click_confirm()

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.page.set_from(data.ADDRESS_FROM)
        self.page.set_to(data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()

        self.page.click_phone_button()
        self.page.set_phone_number(data.PHONE_NUMBER)
        self.page.click_next()

        code = helpers.retrieve_phone_code(self.driver)

        self.page.set_code(code)
        self.page.click_confirm()

        self.page.click_payment_method()
        self.page.click_add_card()
        self.page.set_card_number(data.CARD_NUMBER)
        self.page.set_card_code(data.CARD_CODE)
        self.page.click_link()
        self.page.close_payment_method()

        assert self.page.get_payment_method() == 'Card'

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.page.set_from(data.ADDRESS_FROM)
        self.page.set_to(data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()

        self.page.set_message_to_driver(
            data.MESSAGE_FOR_DRIVER
        )

        assert (
            self.page.get_message_to_driver()
            == data.MESSAGE_FOR_DRIVER
        )

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.page.set_from(data.ADDRESS_FROM)
        self.page.set_to(data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()

        self.page.select_blanket_and_handkerchiefs()

        assert self.page.is_blanket_and_handkerchiefs_selected()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.page.set_from(data.ADDRESS_FROM)
        self.page.set_to(data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()

        for i in range(2):
            self.page.add_ice_cream()

        assert self.page.get_ice_cream_count() == '2'

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.page.set_from(data.ADDRESS_FROM)
        self.page.set_to(data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()

        self.page.click_phone_button()
        self.page.set_phone_number(data.PHONE_NUMBER)
        self.page.click_next()

        code = helpers.retrieve_phone_code(self.driver)

        self.page.set_code(code)
        self.page.click_confirm()

        self.page.click_payment_method()
        self.page.click_add_card()
        self.page.set_card_number(data.CARD_NUMBER)
        self.page.set_card_code(data.CARD_CODE)
        self.page.click_link()
        self.page.close_payment_method()

        self.page.set_message_to_driver(
            data.MESSAGE_FOR_DRIVER
        )

        self.page.select_blanket_and_handkerchiefs()

        for i in range(2):
            self.page.add_ice_cream()

        self.page.click_order()

        assert self.page.is_car_search_displayed()

    def teardown_method(self):
        self.driver.quit()