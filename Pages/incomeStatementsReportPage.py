from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import *


class IncomeStatementsReportPage:
    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay

        self.total_revenue_link = "//*[@id='dataTable']/div/table/tbody/tr[4]/th[2]/a"
        self.total_revenue_header = "PerformanceHeader"
        self.total_revenue_text = "#dataTable > p:nth-child(3)"

    def open_total_revenue(self):
        revenue_link = WDW(self.driver, self.delay).until(EC.element_to_be_clickable((By.XPATH,
                                                                                      self.total_revenue_link)))
        revenue_link.click()

    def get_total_revenue_title(self):
        report_header = WDW(self.driver, self.delay).until(EC.presence_of_element_located((By.ID,
                                                           self.total_revenue_header)))
        return report_header.text

    def get_total_revenue_text(self):
        revenue_text = WDW(self.driver, self.delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          self.total_revenue_text)))
        return revenue_text.text