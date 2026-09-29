import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.smoke
def test_valid_login_reaches_welcome(driver, base_url):
    driver.get(f"{base_url}/login")
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.ID, "login-btn").click()

    welcome = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "welcome-msg"))
    )
    assert "Welcome" in welcome.text


@pytest.mark.smoke
def test_invalid_login_shows_error(driver, base_url):
    driver.get(f"{base_url}/login")
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.ID, "login-btn").click()

    error = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "error"))
    )
    assert "Invalid" in error.text
