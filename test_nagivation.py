#TEST SẮP XẾP
from driver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#test chức năng điều hướng trên trang web
def test_navigate_to_product_list(driver):
    valid_account(driver)
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, "//a[contains(text(), 'Products')]").click()
    expected_url = "http://127.0.0.1:5000/product-list"
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL to be {expected_url}, but got {current_url}"

    driver.find_element(By.XPATH, "//a[contains(text(), 'Contact')]").click()
    expected_contact_url = "http://127.0.0.1:5000/careers"
    current_contact_url = driver.current_url
    assert current_contact_url == expected_contact_url, f"Expected URL to be {expected_contact_url}, but got {expected_contact_url}"

    driver.find_element(By.XPATH, f"//i[@class='fa fa-shopping-cart']").click()
    expected_cart_url = "http://127.0.0.1:5000/cart"
    current_cart_url = driver.current_url
    assert current_cart_url == expected_cart_url, f"Expected URL to be {expected_cart_url}, but got {expected_cart_url}"

#test các title ở web admin
def test_admin_navigation(driver):
    driver.get("http://127.0.0.1:5000/admin/")
    time.sleep(10)
    assert "Laptop UTE's ADMIN" in driver.title