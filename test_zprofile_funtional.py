#TEST HỒ SƠ
from driver import *
from selenium.webdriver.common.by import By
import time

#Test xem hồ sơ
def test_view_profile(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Bui Truong Thinh')]").click()
    time.sleep(2)
    result = driver.find_element(By.XPATH, f"//h1[contains(text(), 'My Profile')]").text
    assert "MY PROFILE" in result

#Test cập nhật hồ sơ
def test_update_profile(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Bui Truong Thinh')]").click()
    driver.find_element(By.ID, "fullname").clear()
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "telephone").clear()
    driver.find_element(By.ID, "fullname").send_keys("Bui Truong Thinh") 
    driver.find_element(By.ID, "email").send_keys("thinh12345@gmail.com") 
    driver.find_element(By.ID, "telephone").send_keys("0987114120") 
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Continue')]").click()
    time.sleep(2)
    result = driver.find_element(By.XPATH, f"//div[@class ='alert alert-danger']").text
    assert "Updated Successfully" in result

#Test đổi mật khẩu với mật khẩu cũ không đúng
def test_wrong_old_pwd(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Bui Truong Thinh')]").click()
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Change password')]").click()
    driver.find_element(By.ID, "old-password").send_keys("Thinh@123456789")
    driver.find_element(By.ID, "new-password").send_keys("Thinh@1234")
    driver.find_element(By.ID, "confirm-password").send_keys("Thinh@1234")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Change')]").click()
    alert_mess = driver.find_element(By.XPATH, f"//div[@class='alert alert-danger']").text
    assert "Check your information again" in alert_mess

#Test đổi mật khẩu
def test_change_pwd(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Bui Truong Thinh')]").click()
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Change password')]").click()
    driver.find_element(By.ID, "old-password").send_keys("Thinh@12345")
    driver.find_element(By.ID, "new-password").send_keys("Thinh@1234")
    driver.find_element(By.ID, "confirm-password").send_keys("Thinh@1234")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Change')]").click()
    time.sleep(5)
    assert "http://127.0.0.1:5000/user-login" in driver.current_url
    time.sleep(5)

