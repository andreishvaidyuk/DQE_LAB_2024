import os
import sys
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Pages.incomeStatementsReportPage import IncomeStatementsReportPage


def get_selenium_config(config_name):
    module_dir = os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))
    parent_dir = os.path.dirname(module_dir)
    with open(os.path.join(parent_dir, 'Configs', config_name), 'r') as stream:
        config = yaml.safe_load(stream)
    return config['global']


@pytest.fixture(scope="function")
def open_income_statements_report_webpage():
    report_uri = get_selenium_config('config_selenium.yaml')['report_uri']
    delay = get_selenium_config('config_selenium.yaml')['delay']
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    driver.get(report_uri)

    income_report = IncomeStatementsReportPage(driver, delay)
    income_report.open_total_revenue()
    yield income_report
    driver.close()


def test_01_open_total_revenue_report(open_income_statements_report_webpage):
    report_page = open_income_statements_report_webpage
    report_title = report_page.get_total_revenue_title()
    assert report_title == 'Performance'


def test_02_has_correct_revenue_text(open_income_statements_report_webpage):
    report_page = open_income_statements_report_webpage
    report_title = report_page.get_total_revenue_text()
    assert report_title == 'Cost of revenue increased $513 million or 3% driven by growth in Microsoft Cloud, ' \
                           'offset in part by a reduction in depreciation expense due to the change in accounting ' \
                           'estimate for the useful lives of our server and network equipment.'
