import pytest
import random
import string
from copy import copy

from . import consts

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True, scope="function")
def get_driver(request):
    '''Get Chrome webdriver'''
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="session")
def get_correct_credentials():
    '''Get correct credentials'''
    domains = ['@gmail.com', '@ya.ru', '@mail.ru']
    credentials = {
        'name': '',
        'email': '',
        'password': ''
    }
    letters = string.ascii_letters
    name = ''.join(random.choice(letters) for i in range(6))
    email = name + domains[random.randint(0, len(domains) - 1)]
    letters += string.digits
    password = ''.join(random.choice(letters) for i in range(consts.VALID_PASSWORD_LENGTH))
    
    credentials['name'] = name
    credentials['email'] = email
    credentials['password'] = password

    return credentials

@pytest.fixture(scope="session")
def get_incorrect_credentials(get_correct_credentials):
    '''Replace correct password to incorrect'''
    incorrect_credentials = copy(get_correct_credentials)
    letters = string.ascii_letters + string.digits
    password = ''.join(random.choice(letters) for i in range(consts.INVALID_PASSWORD_LENGTH))
    incorrect_credentials['password'] = password

    return incorrect_credentials
