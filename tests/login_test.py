from selenium import webdriver
import time
import pytest
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from utils import utils as util
import allure


@pytest.mark.usefixtures("test_setup")
class Testlogin():


    def test_login(self):
        driver=self.driver
        driver.get(util.URL)
        time.sleep(10)

        loginpage=LoginPage(driver)
        loginpage.enter_username(util.Username)
        loginpage.enter_password(util.Password)
        loginpage.login_button()

        # driver.find_element_by_id("username").send_keys("Anurag.Sharma")
        # driver.find_element_by_id("password").send_keys("P@ssword123")
        # driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)


    def test_logout(self):

        try:
            driver = self.driver
            home=HomePage(driver)
            home.click_profile()
            time.sleep(8)
            home.click_logout()
            #driver.find_element_by_id("profilePopover").click()
            #driver.find_element_by_xpath("//ul[@class='dropdown-menu profile-tab']/li[4]/strong/a[text()='Logoff']").click()
            time.sleep(5)
            x=driver.title
            assert x=="LHH NGen"

        except AssertionError as error1:
            print("unwanted error")
            print (error1)
            allure.attach(self.driver.get_screenshot_as_png(),name="screen_1", attachment_type=allure.attachment_type.JPG)
            raise



# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/meher.verma/PycharmProjects/Automation_Framework1/reports"),verbosity=2)


