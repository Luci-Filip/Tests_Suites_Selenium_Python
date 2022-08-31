import unittest
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):     # Tema 9 Verificatori
    CLICK_FORM_AUTHENTICATION = (By.XPATH, "//a[@href='/login']")
    CHECK_TEXT = (By.XPATH, "//h2")
    BUTTON_FOR_LOGIN = (By.XPATH, "//button[@class='radius']")
    CHECK_ATTRIBUTE_HREF = (By.XPATH, "//a[@href = 'http://elementalselenium.com/']")
    ERROR_DISPLAYED = (By.XPATH, "//div[@id='flash']")
    USER = (By.XPATH, "//input[@id='username']")
    PASS = (By.XPATH, "//input[@id='password']")
    CLICK_X_ON_TEXT_ERROR = (By.XPATH, "//a[@class='close']")
    FLASH_MESSAGES = (By.XPATH, "//div[@id='flash-messages']")
    ELEMENT_CLASS_FLASH_SUCCESS = (By.XPATH, "//div[@class='flash success']")
    LOGOUT = (By.XPATH, "//a[@class='button secondary radius']")
    INPUT_USERNAME = (By.XPATH, "//label[text()='Username']")
    INPUT_PASSWORD = (By.XPATH, "//label[text()='Password']")
    ELEMENT_H4 = (By.XPATH, "//h4/em[2]")


    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.CLICK_FORM_AUTHENTICATION).click()

    def tearDown(self):
        sleep(2)
        self.chrome.quit()

    #@unittest.skip     # test 1
    def test_check_url(self):
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.chrome.current_url
        self.assertEqual(expected_url,actual_url, "URL is incorrect!")

    #@unittest.skip     # test 2
    def test_page_title(self):
        expected_title = "The Internet"
        actual_title = self.chrome.title
        self.assertEqual(expected_title, actual_title, "The title is incorrect!")

    #@unittest.skip     # test 3
    def test_check_text(self):
        actual_text = self.chrome.find_element(*self.CHECK_TEXT).text
        expected_text = "Login Page"
        self.assertEqual(expected_text, actual_text, f'The text is not correct!')

    #@unittest.skip     # test 4
    def test_button_displayed(self):
        element = self.chrome.find_element(*self.BUTTON_FOR_LOGIN)
        self.assertTrue(element.is_displayed(), "The Login button is not visible!")

    #@unittest.skip     # test 5
    def test_check_attribute_href(self):
        the_link = self.chrome.find_element(*self.CHECK_ATTRIBUTE_HREF).get_attribute('href')
        assert the_link == "http://elementalselenium.com/", "The link is not correct"

    #@unittest.skip     # test 6
    def test_clik_login(self):
        self.chrome.find_element(*self.BUTTON_FOR_LOGIN).click()
        error = self.chrome.find_element(*self.ERROR_DISPLAYED)
        self.assertTrue(error.is_displayed(), "The error is not displayed!")

    #@unittest.skip     # test 7
    def test_user_and_pass_invalid(self):
        self.chrome.find_element(*self.USER).send_keys("2022")
        self.chrome.find_element(*self.PASS).send_keys("test")
        self.chrome.find_element(*self.BUTTON_FOR_LOGIN).click()
        expected = self.chrome.find_element(*self.ERROR_DISPLAYED)
        self.assertTrue(expected.is_displayed(), 'Error, the text is not displayed!')

    #@unittest.skip     # test 8
    def test_click_x(self):
        self.chrome.find_element(*self.BUTTON_FOR_LOGIN).click()
        self.chrome.find_element(*self.CLICK_X_ON_TEXT_ERROR).click()
        actual_error_messages = self.chrome.find_element(*self.ERROR_DISPLAYED).text
        assert actual_error_messages != "Your username is invalid!"

    #@unittest.skip     # test 9
    def test_list_of_label(self):
        user = self.chrome.find_element(*self.INPUT_USERNAME).text
        assert user == 'Username', f'User error'
        password = self.chrome.find_element(*self.INPUT_PASSWORD).text
        assert password == 'Password', f'Pass error'

    #@unittest.skip     # test 10
    def test_completes_user_pass_valide(self):
        self.chrome.find_element(*self.USER).send_keys("tomsmith")
        self.chrome.find_element(*self.PASS).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.BUTTON_FOR_LOGIN).click()

        try:
            WebDriverWait(self.chrome, 5).until(EC.url_contains('/secure'))
            print("The url contains the keyword '/secure' ")
        except TimeoutException:
            self.assertTrue(False, 'The url is incorrect!')

        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(self.ELEMENT_CLASS_FLASH_SUCCESS))
        element = self.chrome.find_element(*self.ELEMENT_CLASS_FLASH_SUCCESS)
        assert element.is_displayed(), f'The element is not displayed!'

        element = self.chrome.find_element(*self.ELEMENT_CLASS_FLASH_SUCCESS).text
        text = "secure area!"
        assert text in element, f'The text {element} does not contains: {text}'

    #@unittest.skip     # test 11
    def test_click_logout(self):
        self.chrome.find_element(*self.USER).send_keys("tomsmith")
        self.chrome.find_element(*self.PASS).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.BUTTON_FOR_LOGIN).click()
        self.chrome.find_element(*self.LOGOUT).click()
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        self.assertEqual(actual_url,expected_url), f'The url {actual_url} is not equal with the url {expected_url}'

    # OPTIONAL EXERCISE:

    def test_brute_force_password_hacking(self):
        first_url, last_url, the_brute_force_password = '   '
        possible_passwords = ['Enter', 'tomsmith', 'for', 'the', 'username', 'and', 'SuperSecretPassword!', 'for', 'the', 'password.']
        for i in possible_passwords:
            self.chrome.find_element(*self.USER).send_keys("tomsmith")
            first_url = self.chrome.current_url
            self.chrome.find_element(*self.PASS).send_keys(i)
            self.chrome.find_element(*self.BUTTON_FOR_LOGIN).click()
            last_url = self.chrome.current_url
            if last_url != first_url:
                the_brute_force_password = i
                break
        assert first_url != last_url, 'I do not succeed the password!'
        print(f'I succeed to find the password, it is: "{the_brute_force_password}"')
