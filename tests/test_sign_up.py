from .. import consts
from ..src import utils

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class TestSignUp():

    def test_successfull_sign_up(self, get_correct_credentials):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_LOGIN_LINK_REGISTER)))
        self.driver.find_element(By.XPATH, consts.LOC_LOGIN_LINK_REGISTER).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_REGISTER_BUTTON_REGISTER)))
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_INPUT_NAME).send_keys(get_correct_credentials['name'])
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_INPUT_EMAIL).send_keys(get_correct_credentials['email'])
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_INPUT_PASSWORD).send_keys(get_correct_credentials['password'])
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_BUTTON_REGISTER).click()
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET).click()
        utils.login(self.driver, get_correct_credentials['email'], get_correct_credentials['password'])
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_MAIN_BUTTON_MAKE_ORDER)))

        assert self.driver.find_element(By.XPATH, consts.LOC_MAIN_BUTTON_MAKE_ORDER).text == 'Оформить заказ'
        utils.logout(self.driver)

    def test_sign_up_wrong_password(self, get_incorrect_credentials):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_LOGIN_LINK_REGISTER)))
        self.driver.find_element(By.XPATH, consts.LOC_LOGIN_LINK_REGISTER).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_REGISTER_BUTTON_REGISTER)))
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_INPUT_NAME).send_keys(get_incorrect_credentials['name'])
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_INPUT_EMAIL).send_keys(get_incorrect_credentials['email'])
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_INPUT_PASSWORD).send_keys(get_incorrect_credentials['password'])
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_BUTTON_REGISTER).click()
        elements = self.driver.find_elements(By.XPATH, consts.LOC_REGISTER_PARAGRAPH_INCORRECT_PASSWORD)

        assert len(elements) == 1

    def test_sign_up_user_exists(self, get_correct_credentials):
        self.driver.get(consts.BASE_URL)
        self.driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_LOGIN_LINK_REGISTER)))
        self.driver.find_element(By.XPATH, consts.LOC_LOGIN_LINK_REGISTER).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_REGISTER_BUTTON_REGISTER)))
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_INPUT_NAME).send_keys(get_correct_credentials['name'])
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_INPUT_EMAIL).send_keys(get_correct_credentials['email'])
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_INPUT_PASSWORD).send_keys(get_correct_credentials['password'])
        self.driver.find_element(By.XPATH, consts.LOC_REGISTER_BUTTON_REGISTER).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, consts.LOC_REGISTER_PARAGRAPH_USER_EXIST)))
        elements = self.driver.find_elements(By.XPATH, consts.LOC_REGISTER_PARAGRAPH_USER_EXIST)

        assert len(elements) == 1
