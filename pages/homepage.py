class HomePage():

    def __init__(self, driver):
        self.driver=driver
        self.driver.profile_id="profilePopover"
        self.driver.logout_xpath="//ul[@class='dropdown-menu profile-tab']/li[4]/strong/a[text()='Logoff']"

    def click_profile(self):
        self.driver.find_element_by_id(self.driver.profile_id).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.driver.logout_xpath).click()

