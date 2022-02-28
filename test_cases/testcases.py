from selenium.webdriver.common.keys import Keys
from multiprocessing.sharedctypes import Value
from operator import contains
from re import T
import unittest
import time
import test_cases.constants as const
from pickle import NONE 
from selenium import webdriver
import os

class tcscenarios(webdriver.Chrome,unittest.TestCase):
    def __init__(self, driver_path=r"C:\SeleniumDrivers",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        
        super(tcscenarios, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
    def __exit__(self, exc_type ,exc_val, exc_tb):
        if self.teardown:
            self.quit()


    def land_first_page(self):
        try:
            self.get(const.BASE_URL)
        except Exception as ex:
            print(ex)

        

    def invalid_login(self):
        usname = self.find_element_by_css_selector('input[autocomplete="username"]')
        pwd = self.find_element_by_css_selector('input[autocomplete="current-password"]')
        usname.clear()
        pwd.clear()
        usname.send_keys(const.wrong_username)
        pwd.send_keys(const.wrong_pass)
        logn = self.find_element_by_css_selector('button[class="chakra-button css-yen36m"]')
        logn.click()
        time.sleep(5)
        curr_url = self.current_url
        expect_url = 'https://testing-assessment-foh15kew9-edvora.vercel.app/'
        if curr_url == expect_url:
            print(
                "PASS: user not able to login with wrong credentials"
                )
            
        else:
            print(
                "FAILED: USER LOGGED IN"
                )
        
    def create_acc_name(self):
        tex = self.find_element_by_tag_name(
            'body'
            )
        content = tex.text
        flag = False
        for i in const.signuptxt:
            x = content.find(i)
            if x > -1:
                flag = True
                break
        
        if flag==True:
            print(
                "PASS: Page contains button with correct name for creating account !"
                )
        else:
            print(
                "FAILED: Page does not have the correct name for create account or signup button !"
                )
    def pwd_masked(self):
        mark = self.find_element_by_css_selector('input[autocomplete="current-password"]')
        if mark.get_attribute("type") == 'password':
            print("PASS: Password field is masked !")
        else:
            print("FAILED: Password field is not masked !")

    def goto_signup(self):

        signupbutton = self.find_element_by_css_selector("button[class='chakra-button css-33x21s']")
        signupbutton.click()

        time.sleep(3)
        curr_url = self.current_url
        expectedurl = 'https://testing-assessment-foh15kew9-edvora.vercel.app/r'

        if curr_url==expectedurl:
            print("PASS: Signup button redirects user to signup page !")
        else:
            print("FAILED: User is not redirected to signup page !")



    def confrmpwd(self):
        name = self.find_element_by_class_name('css-llqj01')
        contnts = name.text
        if contnts.find("Confirm Password")>-1:
            print("PASS: there is confirm password field present !")
        else:
            print("FAILED: There is no confirm password field present")


    def test_pwd_allcombo(self):
        usname = self.find_element_by_css_selector('input[autocomplete="username"]')
        pwd = self.find_element_by_css_selector('input[autocomplete="current-password"]')
        usname.send_keys(const.username)
        pwd.send_keys(const.password)
        submit = self.find_element_by_css_selector('button[class="chakra-button css-yen36m"]')
        submit.click()
        msg = self.switch_to.alert
        if msg.text == "something went wrong":
            print("FAILED: user cannot make account password using any combination")
        elif msg.text == "Account sucessfully created.":
            print("user account created !")
        self.switch_to.alert.accept()

        

    
    def account_creation(self):
        usname = self.find_element_by_css_selector('input[value="trial"]')
        pwd = self.find_element_by_css_selector('input[autocomplete="current-password"]')
       
        usname.send_keys(Keys.CONTROL,'a')
        usname.send_keys(Keys.BACK_SPACE)
        usname.send_keys(const.username1)
        pwd.send_keys(Keys.CONTROL,'a')
        pwd.send_keys(Keys.BACK_SPACE)
        pwd.send_keys(const.pass1)
        submit = self.find_element_by_css_selector('button[class="chakra-button css-yen36m"]')
        submit.click()
        time.sleep(6)
        msg1 = self.switch_to.alert
        if msg1.text == "something went wrong":
            print("FAILED: Account creation failed ")
        elif msg1.text == "Account sucessfully created.":
            print("PASS: user account created !")
        
        self.switch_to.alert.accept()
        time.sleep(5)
        expectedUrl = "https://testing-assessment-foh15kew9-edvora.vercel.app/s"
        if expectedUrl== self.current_url:
            print("PASS: User is redirected to dashbaord after account creation.")
        else:
            print("FAILED: User is not redirected to dashbaord.")

        

           

        

