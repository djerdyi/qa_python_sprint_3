from .. import consts

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class TestNavigation():

    def test_go_to_personal_cabinet(self):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET).click()
        elements = self.driver.find_elements(By.XPATH, consts.LOC_LOGIN_BUTTON_LOGIN)

        assert len(elements) == 1

    def test_go_to_constructor_by_button(self):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET).click()
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_CONSTRUCTOR).click()
        elements = self.driver.find_elements(By.XPATH, consts.LOC_MAIN_BUTTON_LOGIN)

        assert len(elements) == 1

    def test_go_to_constructor_by_logo(self):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET).click()
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_LOGO).click()
        elements = self.driver.find_elements(By.XPATH, consts.LOC_MAIN_BUTTON_LOGIN)

        assert len(elements) == 1

    def test_go_to_orders_list_by_button(self):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET).click()
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_ORDERS).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, consts.LOC_FEED_HEADER_ORDERS_LIST)))
        elements = self.driver.find_elements(By.XPATH, consts.LOC_FEED_HEADER_ORDERS_LIST)

        assert len(elements) == 1
