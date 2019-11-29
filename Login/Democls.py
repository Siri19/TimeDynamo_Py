import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select
class democlas(unittest.TestCase):
    globals()
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")


    def test_form(self):
        self.driver.get("https://www.toolsqa.com/automation-practice-form/")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//input[@name='firstname']").send_keys("43242")
        self.driver.find_element_by_id("lastname").send_keys("dsfs")
        self.driver.execute_script("window.scrollTo(0,500)")

        gender=self.driver.find_elements_by_xpath("//div[@class='control-group']/input[@name='sex']")
        for opt in gender:
            txt= opt.get_attribute("value")
            print(opt.get_attribute("value"))
            if txt == 'Female':
                opt.click()
        exp=self.driver.find_elements_by_xpath("//input[@name='exp']")
        for opr in exp:
            text=opr.get_attribute("value")
            print(text)
            if text=='3':
                opr.click()
                break

        self.driver.find_element_by_id("datepicker").send_keys("2019/10/23")
        prof=self.driver.find_elements_by_xpath("//input[@name='profession']")
        for prf in prof:
            prf.click()
        self.driver.find_element_by_xpath("//input[@id='photo'][@type='file']").send_keys("/home/siri/Pictures/am.jpg")
        self.driver.execute_script("window.scrollTo(0,900)")
        tools=self.driver.find_elements_by_xpath("//input[@name='tool']")
        for tool in tools:
            tool.click()


      #  self.driver.find_element_by_id("continents").click()
        selectopt= Select(self.driver.find_element_by_id("continents"))
        #print(o.text for o in selectopt.options)
        selectopt.select_by_visible_text("Africa")
        selectContint=Select(self.driver.find_element_by_id("continentsmultiple"))
        selectContint.select_by_visible_text("Australia")

        selectcmd=Select(self.driver.find_element_by_id("selenium_commands"))
        selectcmd.select_by_visible_text("Switch Commands")
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/siri/PycharmProjects/TimeDynamo_Py/Reports'))
