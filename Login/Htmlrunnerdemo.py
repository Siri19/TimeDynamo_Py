import unittest
import XLUtils
from selenium import webdriver
import HtmlTestRunner
import sys
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
sys.path.append("/home/siri/PycharmProjects/TimeDynamo_Py")
from pages.LoginPage import LoginPage



class login(unittest.TestCase):
    globals()
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

    def test_Launch(self):
        self.driver.get("http://tvishasystems.com/webdemo/timedynamo_testing/public/")
        self.driver.maximize_window()
        print("Title is -->", self.driver.title)
        assert "TimeDynamo-Best Biometric Attendance system" in self.driver.title

    def test_LoginbtnClk(self):
        self.driver.find_element_by_xpath("//a[@href='/webdemo/timedynamo_testing/public/login']").click()

    def test_Loginform(self):
        path = "/home/siri/Documents/TimeDynamo_Automation/TimeDyanmo_DataPython.xlsx"
        rows = XLUtils.getRowCount(path, 'Login')


        for r in range(2, rows + 1):
            username = str(XLUtils.readData(path, "Login", r, 1))
            password = str(XLUtils.readData(path, "Login", r, 2))
            print(username)
            print(password)
            lp=LoginPage(self.driver)
            lp.setusername(username)
            lp.setpassword(password)
            lp.loginclick(r)


    @classmethod
    def tearDownClass(cls):
        #pass
        cls.driver.close()

if __name__=="__main__":
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/siri/PycharmProjects/TimeDynamo_Py/Reports'))
    unittest.main()