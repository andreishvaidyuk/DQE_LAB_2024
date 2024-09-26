from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


def test_get_locators_one():
    options = ChromeOptions()
    options.headless = False
    service = ChromeService()

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://phptravels.com/demo/")

    submit_button_by_class = driver.find_element(By.CLASS_NAME, "btn_submit")
    submit_button_by_id = driver.find_element(By.ID, "demo")
    country_field_by_name = driver.find_element(By.NAME, "country_id")
    country_field_by_css_selector = driver.find_element(By.CSS_SELECTOR, "#country_id.form-select.w-100.rounded-2.px-4")
    country_field_by_xpath = driver.find_element(By.XPATH,
            './/*[@id="country_id"]'
            '[contains(concat(" ",normalize-space(@class)," ")," form-select ")]'
            '[contains(concat(" ",normalize-space(@class)," ")," w-100 ")]'
            '[contains(concat(" ",normalize-space(@class)," ")," rounded-2 ")]'
            '[contains(concat(" ",normalize-space(@class)," ")," px-4 ")]')

    print(f"Submit_button_by_class: {submit_button_by_class}")
    print(f"Submit_button_by_id: {submit_button_by_id}")
    print(f"Country_field_by_name: {country_field_by_name}")
    print(f"country_field_by_css_selector: {country_field_by_css_selector}")
    print(f"country_field_by_xpath: {country_field_by_xpath}")
    driver.quit()


def test_get_locators_two():
    options = ChromeOptions()
    options.headless = False
    service = ChromeService()

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://app.phptravels.com/signup")

    whatsapp_by_class = driver.find_element(By.CLASS_NAME, "whatsapp")
    last_name_by_id = driver.find_element(By.ID, "last_name")
    email_by_name = driver.find_element(By.NAME, "email")
    signup_button_by_css_selector = driver.find_element(By.CSS_SELECTOR, "body > div.container > div > div > div > div > form > div > div.p-2")
    signup_button_by_xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/form/div/div[7]')

    print(f"Whatsapp_by_class: {whatsapp_by_class}")
    print(f"Last_name_by_id: {last_name_by_id}")
    print(f"Email_by_name: {email_by_name}")
    print(f"Signup_button_by_css_selector: {signup_button_by_css_selector}")
    print(f"Signup_button_by_xpath: {signup_button_by_xpath}")
    driver.quit()


def test_get_locators_three():
    options = ChromeOptions()
    options.headless = False
    service = ChromeService()

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://phptravels.com/blog/")

    post_title_by_class = driver.find_element(By.CLASS_NAME, "post-title")
    article_by_id = driver.find_element(By.ID, "post-2690")
    popular_post_by_css_selector = driver.find_element(By.CSS_SELECTOR, "#popular-posts > "
              "article.post-featured-link.column.flex.post-18.post.type-post.status-publish.format-standard."
              "has-post-thumbnail.hentry.category-travel.category-business > div > h3 > a")
    post_by_xpath = driver.find_element(By.XPATH, '//*[@id="post-2951"]/div/div[1]/div/div/a')

    print(f"Post_title_by_class: {post_title_by_class}")
    print(f"Article_by_id: {article_by_id}")
    print(f"Popular_post_by_css_selector: {popular_post_by_css_selector}")
    print(f"Post_by_xpath: {post_by_xpath}")
    driver.quit()