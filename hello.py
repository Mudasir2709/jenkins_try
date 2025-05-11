import time

import pytest
from selenium import webdriver


class TestJenkins:
    @pytest.mark.usefixtures("setup")
    def test_screenshot(self):
        time.sleep(5)

