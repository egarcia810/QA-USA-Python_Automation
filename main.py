import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled
        from selenium.webdriver import DesiredCapabilities

        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        cls.driver = webdriver.Chrome()
        cls.page = UrbanRoutesPage(cls.driver)

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

    def test_select_plan(self):
        self.page.click_call_taxi()
        self.page.select_supportive_plan()

    def test_fill_phone_number(self):
        self.page.click_phone_button()
        self.page.set_phone_number(data.PHONE_NUMBER)
        self.page.click_next()

        code = helpers.retrieve_phone_code(self.driver)

        self.page.set_code(code)
        self.page.click_confirm()

    def test_fill_card(self):
        self.page.click_payment_method()
        self.page.click_add_card()
        self.page.set_card_number(data.CARD_NUMBER)
        self.page.set_card_code(data.CARD_CODE)
        self.page.click_link()

    def test_comment_for_driver(self):
        self.page.set_message_to_driver(
            data.MESSAGE_FOR_DRIVER
        )

    def test_order_blanket_and_handkerchiefs(self):
        self.page.select_blanket_and_handkerchiefs()

    def test_order_2_ice_creams(self):
        for i in range(2):
            self.page.add_ice_cream()

        assert self.page.get_ice_cream_count() == '2'

    def test_car_search_model_appears(self):
        self.page.click_order()

        car_search = self.page.wait_for_car_search()

        assert car_search.text == 'Car search'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()