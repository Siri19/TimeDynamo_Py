import XLUtils
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
sys.path.append("/home/siri/PycharmProjects/TimeDynamo_Py")
from pages.LoginPage import LoginPage
#from Login.XLUtils import XLUtils
class login(unittest.TestCase):
    globals()
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

    def test_login(self):
        self.driver.get("http://testing.timedynamo.com/login")
        self.driver.maximize_window()
        print("title is --->",self.driver.title)
        path = "/home/siri/Documents/TimeDynamo_Automation/TimeDyanmo_DataPython.xlsx"
        rows = XLUtils.getRowCount(path, 'Login_ValidData')
        print("no.of rows --->",rows)
        for r in range(2, rows + 1):
            username = str(XLUtils.readData(path, "Login_ValidData", r, 1))
            password = str(XLUtils.readData(path, "Login_ValidData", r, 2))
            status = str(XLUtils.readData(path,"Login_ValidData",r,3))
            print(username)
            print(password)
            lp = LoginPage(self.driver)
            lp.setusername(username,password)
            lp.loginclick(status,r)
           # lp.getfeedbackMsg()
    @classmethod
    def tearDownClass(cls):
        #pass
        cls.driver.close()


if __name__=="__main__":
    unittest.main()
