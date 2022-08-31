import unittest
from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class CompleteWebForm(unittest.TestCase):
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    JOB_TITLE = (By.ID, "job-title")
    EDUCATION = (By.ID, "radio-button-2")
    GEN = (By.XPATH, "//input[@id='checkbox-1']")
    EXPERIENCE = (By.XPATH, "//option[2]")
    CLICK_DATE = (By.ID, 'datepicker')
    TODAY_DATE = (By.XPATH, "//tr/td[@class='today day']")
    SUBMIT_BUTTON = (By.XPATH, "//a[text()='Submit']")

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get('https://formy-project.herokuapp.com/form')
        self.driver.maximize_window()
        sleep(5)

    def tearDown(self):
        sleep(5)
        self.driver.quit()

    #@unittest.skip
    def test_correct_url(self):
        actual_url = self.driver.current_url
        assert actual_url == 'https://formy-project.herokuapp.com/form', 'URL incorrect!'

    #@unittest.skip
    def test_complete_form_page(self):
        self.driver.find_element(*self.FIRST_NAME).send_keys('Filip')
        self.driver.find_element(*self.LAST_NAME).send_keys('Lucian')
        self.driver.find_element(*self.JOB_TITLE).send_keys('Automation Tester')
        self.driver.find_element(*self.EDUCATION).click()
        self.driver.find_element(*self.GEN).click()
        self.driver.find_element(*self.EXPERIENCE).click()
        self.driver.find_element(*self.CLICK_DATE).click()
        self.driver.find_element(*self.TODAY_DATE).click()

    #@unittest.skip
    def test_displayed_submit_button(self):
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        assert button.is_displayed(), "The Submit Button is not displayed!"

    #@unittest.skip
    def test_new_url(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        actual_url = self.driver.current_url
        assert actual_url == 'https://formy-project.herokuapp.com/thanks', 'URL incorrect!'
