from time import sleep


from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import read_config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils


class Test_02_Admin_Login_Data_Driven:
    admin_page_url = read_config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path =".//test_data//admin_login_data.xlsx"
    status_list = []


    def test_admin_login_data_driven (self,setup):
        self.logger.info("=========================Test_admin_login_data_driven started=======================")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)

        self.rows = excel_utils.get_row_count(self.path,"Sheet1")
        print("num of rows: ",self.rows)



        for r in range(2, self.rows+1):
            self.username = excel_utils.read_data(self.path,"Sheet1",r,1)
            self.password = excel_utils.read_data(self.path, "Sheet1",r,2 )
            self.exp_login = excel_utils.read_data(self.path, "Sheet1",r,3 )
            if not self.username or not self.password:
                self.logger.info(f"Skipping row {r} due to blank username or password")
                continue

            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            sleep(10)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("========================Test data is passed=======================")
                    self.status_list.append("Pass")
                    self.admin_lp.Click_logout()
                elif self.exp_login == "No":
                    self.logger.info("========================Test data is failed=======================")
                    self.status_list.append("Fail")
                    self.admin_lp.Click_logout()

            elif act_title != exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("========================Test data is failed=======================")
                    self.status_list.append("Fail")
                elif self.exp_login == "No":
                    self.logger.info("========================Test data is passed=======================")
                    self.status_list.append("Pass")
        print("Status list is",self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("========================Test admin data driven test is Failed=======================")
            assert False
        else:
            self.logger.info("========================Test admin data driven test is Passed=======================")
            assert True
