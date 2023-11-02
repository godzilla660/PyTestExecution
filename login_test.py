import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
@pytest.mark.test

def test_login():
    print("login Success!")

@pytest.mark.xfail
def test_logoff():
    print("Logoff Success!")
def test_calculation():
    assert 2+2 ==  4

@pytest.mark.skip
def test_automation():
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("tysonleisiano@gmail.com")
    wait.until(EC.element_to_be_clickable((By.ID, "pass"))).send_keys("Leisiano08!")
    # wait.until(EC.element_to_be_clickable((By.ID, "login"))).click()

    # driver.find_element(By.ID, "email").send_keys("tysonleisiano@gmail.com")
    # driver.find_element(By.ID, "pass").send_keys("Leisiano08!")
    login_button_element = driver.find_element(By.NAME, "login")
    # driver.find_element(By.XPATH, "//span[contains(text(),'Memories')]")
    login_button_element.click()
    # wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w x1l7klhg x1iyjqo2 xs83m0k x2lwn1j'])[1]"))).click()
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/label/input").click()
