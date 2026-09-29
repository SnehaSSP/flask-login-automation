import pytest
from selenium.webdriver.common.by import By


@pytest.mark.regression
def test_logout_returns_to_login(driver, base_url):
    driver.get(f"{base_url}/login")
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.ID, "login-btn").click()
    driver.find_element(By.ID, "logout-link").click()
    assert "/login" in driver.current_url

@pytest.mark.regression
def test_whitespace_in_username_is_trimmed(driver, base_url):
    driver.get(f"{base_url}/login")
    driver.find_element(By.ID, "username").send_keys("  admin  ")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.ID, "login-btn").click()
    assert "Welcome" in driver.find_element(By.ID, "welcome-msg").text

@pytest.mark.regression
def test_case_sensitive_username_fails(driver, base_url):
    driver.get(f"{base_url}/login")
    driver.find_element(By.ID, "username").send_keys("Admin")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.ID, "login-btn").click()
    assert "Invalid" in driver.find_element(By.ID, "error").text

@pytest.mark.regression
def test_sql_injection_attempt_fails_safely(driver, base_url):
    driver.get(f"{base_url}/login")
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("' OR 1=1 --")
    driver.find_element(By.ID, "login-btn").click()
    assert "Invalid" in driver.find_element(By.ID, "error").text

@pytest.mark.regression
def test_empty_password_blocked_by_html5(driver, base_url):
    driver.get(f"{base_url}/login")
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "login-btn").click()
    assert "/login" in driver.current_url
