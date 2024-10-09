import pytest
from selenium import webdriver
from jproperties import Properties
import os

configs = Properties()
DIR_ABS_PATH = os.path.dirname(__file__)
README_PATH = os.path.join(DIR_ABS_PATH, './Utilities/config.properties')

with open(README_PATH, 'rb') as config_file:
    configs.load(config_file)

def pytest_configure():
    pytest.mobileModel = configs.get("MOBILE_MODEL").data


@pytest.fixture(scope="module")
# @pytest.yield_fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.maximize_window()
    yield driver
    driver.quit()
