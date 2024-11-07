#TEST THANH TOÁN
from driver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#test chức năng checkout thành công
def test_checkout(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, f"//i[@class='fa fa-search search-btn']").click()
    driver.find_element(By.CLASS_NAME, "form-control").send_keys("Laptop")
    driver.find_element(By.XPATH, f"//button[@type='submit']").click()
    driver.find_element(By.XPATH, f"/html/body/div[4]/div/div/div[2]/div[3]/div[1]/div/a").click()
    driver.find_element(By.XPATH, f"//i[@class='fa fa-shopping-cart']").click()
    driver.find_element(By.XPATH, f"//button[@type = 'button']").click()
    driver.find_element(By.XPATH, f"//a[contains(text(),'Step 1: Choose your city')]").click()
    time.sleep(2)
    city = Select(driver.find_element(By.ID, "mySelect"))
    city.select_by_visible_text("Hà Nội")
    time.sleep(2)
    driver.find_element(By.XPATH, f"//a[contains(text(),'Step 2: Payment Method')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='radio' and @name='paymentmethod']").click()
    time.sleep(2)
    driver.find_element(By.ID, "button-payment-method").click()
    time.sleep(2)
    driver.find_element(By.XPATH, f"//button[@class='btn btn-primary pull-right']").click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    alert2 = driver.switch_to.alert
    alert2.accept()
    time.sleep(2)
    result = driver.find_element(By.ID, "cartCounter").text
    assert "0" in result

#test chức năng hủy checkout
def test_cancel_checkout(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, f"//i[@class='fa fa-search search-btn']").click()
    driver.find_element(By.CLASS_NAME, "form-control").send_keys("Laptop")
    driver.find_element(By.XPATH, f"//button[@type='submit']").click()
    driver.find_element(By.XPATH, f"/html/body/div[4]/div/div/div[2]/div[3]/div[1]/div/a").click()
    driver.find_element(By.XPATH, f"//i[@class='fa fa-shopping-cart']").click()
    driver.find_element(By.XPATH, f"//button[@type = 'button']").click()
    driver.find_element(By.XPATH, f"//a[contains(text(),'Step 1: Choose your city')]").click()
    time.sleep(2)
    city = Select(driver.find_element(By.ID, "mySelect"))
    city.select_by_visible_text("Hà Nội")
    time.sleep(2)
    driver.find_element(By.XPATH, f"//a[contains(text(),'Step 2: Payment Method')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='radio' and @name='paymentmethod']").click()
    time.sleep(2)
    driver.find_element(By.ID, "button-payment-method").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]").click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:5000/cart", f"Expected URL to be 'http://127.0.0.1:5000/cart', but got {current_url}"
    result = driver.find_element(By.ID, "cartCounter").text
    assert result == "1", f"Expected cart quantity to be '1', but got '{result}'"

