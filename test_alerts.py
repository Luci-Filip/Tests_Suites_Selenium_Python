import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Alerts(unittest.TestCase):
    ALERT = (By.XPATH, "//button[text()='Click for JS Alert']")
    CONFIRM = (By.XPATH, "//button[text()='Click for JS Confirm']")
    PROMPT = (By.XPATH, "//button[text()='Click for JS Prompt']")

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.chrome.implicitly_wait(10)

    def tearDown(self):
        sleep(5)
        self.chrome.quit()

    def test_click_for_js_alert(self):
        self.chrome.find_element(*self.ALERT).click()
        obj = self.chrome.switch_to.alert
        sleep(2)
        print(obj.text)
        obj.accept()
        print("The test succeeded")
        sleep(2)

    def test_for_js_confirm_ok(self):
        self.chrome.find_element(*self.CONFIRM).click()
        obj = self.chrome.switch_to.alert
        sleep(2)
        print(f'Confirm shows following messages {obj.text}')
        obj.accept()
        sleep(2)
        print("Clicked on the ok Button in the Confirm Window")

    def test_for_js_confirm_cancel(self):
        self.chrome.find_element(*self.CONFIRM).click()
        obj = self.chrome.switch_to.alert
        sleep(2)
        obj.dismiss()
        sleep(2)
        print("Clicked on the Cancel Button in the Confirm Window")

    def test_for_js_prompt(self):
        self.chrome.find_element(*self.PROMPT).click()
        sleep(2)
        obj = self.chrome.switch_to.alert
        sleep(2)
        print(obj.text)
        obj.send_keys("I want to write 'anything'")
        sleep(2)
        obj.accept()
        sleep(2)
