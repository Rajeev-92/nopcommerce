import pytest
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import read_config
from utilities.custom_logger import Log_Maker


class Test_01_admin_login:
    admin_page_url = read_config.get_admin_page_url()
    username = read_config.get_username()
    password = read_config.get_password()
    invalid_username = read_config.get_invalid_username()
    invalid_password = read_config.get_invalid_password()
    blank_username = read_config.get_blank_username()
    blank_password = read_config.get_blank_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.sanity
    def test_title_verification(self,setup):
        self.logger.info("=========================Test_01_admin_login================================")
        self.logger.info("========================Verification of admin login page title================================")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            self.logger.info("========================Test_title_verification matched=======================")
            assert True
            self.driver.close()
        else:
            self.logger.info("========================Test_title_verification not matched========================")
            self.driver.save_screenshot(".\\screenshot\\test_title_verification.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_invalid_email_admin_login(self,setup):
        self.logger.info("=========================Test_invalid_email_admin_login=======================")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(self.driver)
        admin_lp.enter_username(self.invalid_username)
        admin_lp.enter_password(self.password)
        admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH, "//li").text
        if error_message == "No customer account found":
            self.logger.info("========================Test_invalid_email_admin_login error message match========================")
            assert True
            self.driver.close()
        else:
            self.logger.info("========================Test_invalid_email_admin_login error message not matched========================")
            self.driver.save_screenshot(".\\screenshot\\test_invalid_email_admin_login.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalid_password_admin_login(self,setup):
        self.logger.info("=========================Test_invalid_password_admin_login=====================")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(self.driver)
        admin_lp.enter_username(self.username)
        admin_lp.enter_password(self.invalid_password)
        admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH, "//li").text
        if error_message == "The credentials provided are incorrect":
            self.logger.info("========================Test_invalid_password_admin_login error message match====================")
            assert True
            self.driver.close()
        else:
            self.logger.info("========================Test_invalid_password_admin_login error message not matched=====================")
            self.driver.save_screenshot(".\\screenshot\\test_invalid_password_admin_login.png")
            self.driver.close()
            assert False


    def test_blank_email_admin_login(self,setup):
        self.logger.info("=========================Test_blank_email_admin_login=====================")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(self.driver)
        admin_lp.enter_username(self.blank_username)
        admin_lp.enter_password(self.password)
        admin_lp.click_login()
        error_message = self.driver.find_element(By.ID,"Email-error").text
        if error_message == "Please enter your email":
            self.logger.info("========================Test_blank_email_admin_login error message match====================")
            assert True
            self.driver.close()
        else:
            self.logger.infor("=================Test_blank_email_admin_login error message not matched================")
            self.driver.save_screenshot(".\\screenshot\\test_blank_email_admin_login.png")
            self.driver.close()
            assert False


    def test_blank_password_admin_login(self,setup):
        self.logger.info("========================Test_blank_password_admin_login=====================")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(self.driver)
        admin_lp.enter_username(self.username)
        admin_lp.enter_password(self.blank_password)
        admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH, "//li").text
        if error_message == "The credentials provided are incorrect":
            self.logger.info("========================Test_blank_password_admin_login error message match==============")
            assert True
            self.driver.close()
        else:
            self.logger.info("======================Test_blank_password_admin_login error message not matched=================")
            self.driver.save_screenshot(".\\screenshot\\test_blank_password_admin_login.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_valid_admin_login(self,setup):
        self.logger.info("========================Test_valid_admin_login=======================")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(self.driver)
        admin_lp.enter_username(self.username)
        admin_lp.enter_password(self.password)
        admin_lp.click_login()
        dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text
        if dashboard_text == 'Dashboard':
            self.logger.info("========================Test_valid_admin_login message matched=================")
            assert True
            self.driver.close()
        else:
            self.logger.info("========================Test_valid_admin_login message not matched===============")
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False
