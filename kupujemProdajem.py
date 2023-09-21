from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def chrome(url):
    driver = webdriver.Chrome(service=Service("C:\Windows\chromedriver-win64\chromedriver.exe"))
    driver.maximize_window()
    driver.get(url)
    time.sleep(1)
    return driver



# DOES CURRENCY CONVERTER WORKS CORRECTLY
def test_TC1():
    driver = chrome("https://novi.kupujemprodajem.com/")
    time.sleep(1)
    driver.find_element(By.ID, "amount").click()
    time.sleep(1)
    driver.find_element(By.ID, "amount").send_keys(Keys.CONTROL, "a")
    driver.find_element(By.ID, "amount").send_keys(Keys.DELETE)
    time.sleep(1)
    driver.find_element(By.ID, "amount").send_keys("153")
    time.sleep(1)
    assert "Najnoviji oglasi" in driver.find_element(By.CLASS_NAME, "CategoryHeadlineItem_item__hkmI9").text

# CHECK SEARCH ENGINE FOR WORD "MIKSER"
def test_TC2():
    driver = chrome("https://novi.kupujemprodajem.com/")
    time.sleep(1)
    driver.find_element(By.ID, "keywords").click()
    time.sleep(1)
    driver.find_element(By.ID, "keywords").send_keys("mikser")
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, " css-1ue7hhz").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, " css-1ue7hhz").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, " css-1ue7hhz").send_keys("Beograd")
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, " css-1ue7hhz").click()
    assert "Još filtera" in driver.find_element(By.CLASS_NAME, "Button_children__3mYJw").text
    # NE RADIIII
