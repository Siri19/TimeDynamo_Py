import XLUtils
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

path = "/home/siri/Documents/TimeDynamo_Automation/TimeDyanmo_DataPython.xlsx"
class LoginPage:
    text_id="bG9naW5Vc2VybmFtZUVsZW1lbnQ"
    text_id1="bG9naW5QYXNzd29yZEVsZW1lbnQ"
    link_cssSelector="input[value=LOGIN]"


    def __init__(self,driver):
        self.driver=driver
    def loginlink(self):
        self.driver.find_element_by_xpath("//a[@href='/webdemo/timedynamo_testing/public/login']").click()

    def setusername(self,username,password):
        self.driver.find_element_by_id(self.text_id).send_keys(username)
        self.driver.find_element_by_id(self.text_id1).send_keys(password)

    def loginclick(self,status,r):

        if status =='false':

            self.driver.find_element_by_xpath("//input[@id='bG9naW5CdG4'][@value='LOGIN']").click()
            time.sleep(1.0)
            s = self.driver.find_element_by_xpath("//div[@id='feedbackSection']").text
            print("--->" + s)
            time.sleep(5)
            self.driver.find_element_by_id("bG9naW5Vc2VybmFtZUVsZW1lbnQ").clear()
            self.driver.find_element(By.ID , "bG9naW5QYXNzd29yZEVsZW1lbnQ").clear()
        else:
            self.driver.find_element_by_xpath("//input[@id='bG9naW5CdG4'][@value='LOGIN']").click()
            time.sleep(3.0)
            ele = self.driver.find_element_by_xpath("//a[@href='/dashboard']")
            b = ele.is_displayed()
            print("Dash board display :--" , b)
            if b == 'True':
                XLUtils.writeData(path , "Login_ValidData" , r , 4 , "Pass")

            else:
                XLUtils.writeData(path , "Login_ValidData" , r , 4 , "Fail")



    def getMessage(self):
        self.driver.find_element_by_xpath("//input[@id='bG9naW5CdG4'][@value='LOGIN']").click()
        try:
                msg = self.driver.find_element(By.XPATH, "//div[@class='tooltip-inner']").text
                print("--------->", msg)
                time.sleep(5)
                self.driver.find_element_by_id("bG9naW5Vc2VybmFtZUVsZW1lbnQ").clear()
                self.driver.find_element(By.ID, "bG9naW5QYXNzd29yZEVsZW1lbnQ").clear()

        except:

                ele = self.driver.find_element_by_xpath("//a[@href='/dashboard']")
                b = ele.is_displayed()
                print("Dash board display :--" , b)
                '''if b=="true":
                    XLUtils.writeData(path, "Login", r, 3, "Pass")

                else:
                    XLUtils.writeData(path, "Login", r, 3, "Fail")'''

        try:
            self.driver.find_element_by_id("bG9naW5Vc2VybmFtZUVsZW1lbnQ").clear()
            self.driver.find_element(By.ID, "bG9naW5QYXNzd29yZEVsZW1lbnQ").clear()
        except NoSuchElementException:
            print("NameError" )

    def getfeedbackMsg(self):
        self.driver.find_element_by_xpath("//input[@id='bG9naW5CdG4'][@value='LOGIN']").click()
        try:
            time.sleep(1.0)
            s = self.driver.find_element_by_xpath("//div[@id='feedbackSection']").text
            print("--->" + s)
        except (exception1) as pc:
            time.sleep(2.0)
            ele = self.driver.find_element_by_xpath("//a[@href='/dashboard']")
            b = ele.is_displayed()
            print("Dash board display :--" , b)
        else:

            time.sleep(5)
            try:
                self.driver.find_element_by_id("bG9naW5Vc2VybmFtZUVsZW1lbnQ").clear()
                self.driver.find_element(By.ID, "bG9naW5QYXNzd29yZEVsZW1lbnQ").clear()
            except:
                print("sdfs")

    def display(b):
        val="false"
        if b =="true":
            val="true"

'''if b=="true":
                XLUtils.writeData(path, "Login", r, 3, "Pass")

            else:
                XLUtils.writeData(path, "Login", r, 3, "Fail")'''



