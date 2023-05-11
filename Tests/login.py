import unittest
import os
from configparser import ConfigParser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.incomeStatementsReportPage import IncomeStatementsReportPage

config_object = ConfigParser()
fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, '../Configs/config.ini')
config_object.read(filename)

selenium_config = config_object["POWERBI_MICROSOFT_REPORT"]
report_uri = selenium_config["report_uri"]
delay = int(selenium_config["delay"])


class ReportTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.set_window_size(1024, 600)
        cls.driver.maximize_window()
        cls.driver.get(report_uri)

        income_report = IncomeStatementsReportPage(cls.driver, delay)
        income_report.open_power_bi_report()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('Tests are completed')

    def test_01_open_decomposition_tree_visualization(self):
        report_page = IncomeStatementsReportPage(self.driver, delay)
        report_page.switch_to_report_frame()
        report_title = report_page.get_revenue_report_title()
        assert report_title == 'REVENUE (in billions)'

    def test_02_your_test_name(self):
        pass

    def test_03_your_test_name(self):
        pass
