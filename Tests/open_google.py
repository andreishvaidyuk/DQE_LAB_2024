from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


def test_open_automatic():
    options = ChromeOptions()
    options.headless = False
    service = ChromeService()

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.google.com")

    print(f"Chrome (Automatic): {driver.title}")
    driver.quit()


def test_open_manual():
    options = ChromeOptions()
    options.headless = False

    service = ChromeService()

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.google.com")

    print(f"Chrome (Manual): {driver.title}")
    driver.quit()


if __name__ == "__main__":
    # Using automatic driver
    test_open_automatic()

    # Using manual driver
    test_open_manual()
