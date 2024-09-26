from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_get_selenium_from_google():
    # create driver
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    # wait 10 seconds
    driver.implicitly_wait(10)

    # search bo[ on Google site has name "q"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium")
    search_box.send_keys(Keys.RETURN)

    # wait 10 seconds,
    wait = WebDriverWait(driver, 10)
    first_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'h3'))
    )
    # click on first link
    first_link.click()

    # wait 10 seconds
    driver.implicitly_wait(10)
    driver.quit()