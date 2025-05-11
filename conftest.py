import pytest
from selenium import webdriver


@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://feddev.seido.me/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    pass
