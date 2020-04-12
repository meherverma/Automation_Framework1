class LoginPage():

    def __init__(self, driver):
        self.driver=driver
        self.driver.username_id="username"
        self.driver.password_id="password"
        self.driver.login_xpath="//button[@type='submit']"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.driver.username_id).clear()
        self.driver.find_element_by_id(self.driver.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.driver.password_id).clear()
        self.driver.find_element_by_id(self.driver.password_id).send_keys(password)

    def login_button(self):
        self.driver.find_element_by_xpath(self.driver.login_xpath).click()