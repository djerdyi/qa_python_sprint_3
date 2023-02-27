from .. import consts

from selenium.webdriver.common.by import By


class TestConstructor():

    def test_go_to_stuffings_tab(self):
        self.driver.get(consts.BASE_URL)
        tab = self.driver.find_element(By.XPATH, consts.LOC_CONSTRUCTOR_DIV_STUFFINGS)
        tab.click()
        last_element = self.driver.find_element(By.XPATH, consts.LOC_CONSTRUCTOR_LI_LAST)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_element)

        assert tab.get_attribute('class') == consts.CONSTRUCTOR_TAB_CLASS_SELECTED

    def test_go_to_sauses_tab(self):
        self.driver.get(consts.BASE_URL)
        tab = self.driver.find_element(By.XPATH, consts.LOC_CONSTRUCTOR_DIV_SAUSES)
        tab.click()

        assert tab.get_attribute('class') == consts.CONSTRUCTOR_TAB_CLASS_SELECTED

    def test_go_to_buns_tab(self):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_CONSTRUCTOR_DIV_SAUSES).click()
        tab = self.driver.find_element(By.XPATH, consts.LOC_CONSTRUCTOR_DIV_BUNS)
        tab.click()

        assert tab.get_attribute('class') == consts.CONSTRUCTOR_TAB_CLASS_SELECTED
