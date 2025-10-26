from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options
from Config.config import BASE_URL


@pytest.fixture()
def setup(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get(BASE_URL)
    request.cls.driver = driver
    yield
    driver.quit()
