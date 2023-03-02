import time

from .. import consts

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def login(driver, login, password):
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_LOGIN_BUTTON_LOGIN)))
    driver.find_element(By.XPATH, consts.LOC_LOGIN_INTPUT_EMAIL).send_keys(login)
    driver.find_element(By.XPATH, consts.LOC_LOGIN_INTPUT_PASSWORD).send_keys(password)
    driver.find_element(By.XPATH, consts.LOC_LOGIN_BUTTON_LOGIN).click()

def logout(driver):
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET)))
    driver.find_element(By.XPATH, consts.LOC_HEADER_BUTTON_PERSONAL_CABINET).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOC_ACCOUNT_BUTTON_LOGOUT)))
    driver.find_element(By.XPATH, consts.LOC_ACCOUNT_BUTTON_LOGOUT).click()

    # Без следующего шага выход не успевает отработать, подскажите, чего мне нужно дождаться, чтобы не писать подобное.
    # Пробовал с разными элементами, WebDriverWait отрабатывает, но кажется, что следующие тесты не видят нужные элементы.
    time.sleep(1)
