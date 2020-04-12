import pytest
from selenium import webdriver
from utils import utils as util

@pytest.fixture(scope="class")
def test_setup(request):
    driver=webdriver.Chrome(executable_path=util.chromepath)

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()