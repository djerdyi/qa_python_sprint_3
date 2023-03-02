from .. import consts
from ..src import utils
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class TestSignIn():

    def test_sign_in_from_main_page(self):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_MAIN_BUTTON_LOGIN).click()
        utils.login(self.driver, consts.LOGIN, consts.PASSWORD)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, consts.LOC_MAIN_BUTTON_MAKE_ORDER)))

        assert self.driver.find_element(By.XPATH, consts.LOC_MAIN_BUTTON_MAKE_ORDER).text == 'Оформить заказ'

    def test_log_out_from_personal_cabinet(self):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_MAIN_BUTTON_LOGIN).click()
        utils.login(self.driver, consts.LOGIN, consts.PASSWORD)
        utils.logout(self.driver)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, consts.LOC_LOGIN_INTPUT_EMAIL)))

        assert self.driver.find_element(By.XPATH, consts.LOC_LOGIN_BUTTON_LOGIN).text == 'Войти'

    def test_sign_in_from_personal_cabinet(self):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET).click()
        utils.login(self.driver, consts.LOGIN, consts.PASSWORD)
        utils.logout(self.driver)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, consts.LOC_LOGIN_INTPUT_EMAIL)))

        assert self.driver.find_element(By.XPATH, consts.LOC_LOGIN_BUTTON_LOGIN).text == 'Войти'

    def test_sign_in_from_registration_form(self):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_LOGIN_LINK_REGISTER)))
        self.driver.find_element(By.XPATH, consts.LOC_LOGIN_LINK_REGISTER).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_REGISTER_LINK_LOGIN)))
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_LINK_LOGIN).click()
        utils.login(self.driver, consts.LOGIN, consts.PASSWORD)
        utils.logout(self.driver)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, consts.LOC_LOGIN_INTPUT_EMAIL)))

        assert self.driver.find_element(By.XPATH, consts.LOC_LOGIN_BUTTON_LOGIN).text == 'Войти'

    def test_sign_in_from_password_recovery_form(self):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_LOGIN_LINK_FORGOT_PASSWORD)))
        self.driver.find_element(By.XPATH, consts.LOC_LOGIN_LINK_FORGOT_PASSWORD).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_FORGOTPASSWORD_LINK_LOGIN)))
        self.driver.find_element(By.XPATH, consts.LOC_FORGOTPASSWORD_LINK_LOGIN).click()
        utils.login(self.driver, consts.LOGIN, consts.PASSWORD)
        utils.logout(self.driver)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_LOGIN_INTPUT_EMAIL)))

        assert self.driver.find_element(By.XPATH, consts.LOC_LOGIN_BUTTON_LOGIN).text == 'Войти'
