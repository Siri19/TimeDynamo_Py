from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class TestTD():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homeTitle(self,setup):
        self.driver.get("http://tvishasystems.com/webdemo/timedynamo_testing/public/login")
        print(self.driver.title)
        assert "TimeDynamo-Login" in self.driver.title

    def test_Login(self,setup):
        self.driver.get("http://tvishasystems.com/webdemo/timedynamo_testing/public/login")
        self.driver.find_element_by_id("bG9naW5Vc2VybmFtZUVsZW1lbnQ").send_keys("username")
        self.driver.find_element(By.ID, "bG9naW5QYXNzd29yZEVsZW1lbnQ").send_keys("password")
        self.driver.find_element_by_css_selector("input[value=LOGIN]").click()
