from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from Config.config import BASE_URL


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(BASE_URL)
    request.cls.driver = driver
    yield
    driver.quit()
