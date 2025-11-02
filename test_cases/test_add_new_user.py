import string
import random
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from test_cases.conftest import setup
from utilities.read_properties import read_config
from utilities.custom_logger import Log_Maker
from base_pages.Add_Customer_Page import Add_Customer_Page

class Test_03_Add_New_Customer:
    admin_page_url = read_config.get_admin_page_url()
    username = read_config.get_username()
    password = read_config.get_password()
    logger = Log_Maker.log_gen()


    def test_add_new_user(self,setup):
        self.logger.info("==========Test_03_Add_New_Customer started==========")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("==========Login Completed==========")
        self.logger.info("==========Starting Add New Customer==========")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.add_customer.click_addnew()
        self.logger.info("==========Providing Add New Customer info==========")
        email = generate_random_email()
        self.add_customer.enter_email(email)
        self.add_customer.enter_password('Test@123')
        self.add_customer.enter_firstname("Johnny")
        self.add_customer.enter_lastname("Singh")
        self.add_customer.select_gender("Male")
        #self.add_customer.enter_dob("09/05/1992")
        self.add_customer.enter_companyname("My Company")
        self.add_customer.select_chbx_tax_exempt()
        self.add_customer.select_newsletter("nopCommerce admin demo store")
        self.logger.info("=================nopCommerce admin demo store selected==========")
        self.add_customer.select_customer_role("Guests")
        self.add_customer.select_manager_of_vendor("Vendor 1")
        self.add_customer.enter_admin_comments("Test Admin Comments")
        self.add_customer.click_save()
        time.sleep(5)
        #Test case validation as success message in body text
        customer_add_success_text = "The new customer has been added successfully"
        success_text = self.driver.find_element(By.XPATH,"//div[@class='content-wrapper']/div[1]").text

        if customer_add_success_text in success_text:
            assert True
            self.logger.info("==========Test_03_Add_New_Customer is Passed==========")
            self.driver.close()
        else:
            self.logger.info("==========Test_03_Add_New_Customer is Failed==========")
            self.driver.save_screenshot(".\\screenshots\\test_add_new_Customer.png")
            self.driver.close()
            assert False


def generate_random_email():
    username = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    #random_number = random.randint(1000, 99999)
    #username = "".join(text_fname_id + random.choices(firstname + string.digits, k=8))
    domain = random.choices(['gmail.com', 'yahoo.com', 'outlook.com', 'example.com', 'yopmail.com'])
    #domain = 'yopmail.com'
    return f'{username}@{domain}'



