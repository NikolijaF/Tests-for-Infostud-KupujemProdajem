#Autorka: Nikolija Filipovic
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# START GOOGLE CHROME AND OPEN INFOSTUD SITE
def launch_chrome_and_go_to_site(url):
    driver = webdriver.Chrome(service=Service("C:\Windows\chromedriver-win64\chromedriver.exe"))
    driver.maximize_window()
    driver.get(url)
    time.sleep(1)
    return driver


# MAKE NEW ACCOUNT WITH EXISTING ACCOUNT INFO:
def test_TC1():
    driver= launch_chrome_and_go_to_site("https://poslovi.infostud.com/")
    time.sleep(1)
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.CLASS_NAME, \
                                          "uk-button.uk-button-primary.uk-button-small.nav-button-primary.chevron-button")).perform()
    time.sleep(1)
    assert 'Prijavite se' in driver.find_element(By.CLASS_NAME, \
                                                 "uk-button.uk-button-primary.uk-button-small.nav-button-primary.chevron-button").text
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Kao kandidat')]").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "link.gtm_reg_link").click()
    time.sleep(1)
    driver.find_element(By.ID, "registration_form_username").send_keys("ljiljanafilipovic9@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "registration_form_password").send_keys("automatskotestiranje2023")
    time.sleep(1)
    driver.find_element(By.ID, "registration_form_passwordRepeat").send_keys("automatskotestiranje2023")
    time.sleep(1)
    driver.find_element(By.ID, "save").click()
    time.sleep(1)
    driver.save_screenshot("screenshotsInfostud/test_case1.png")
    time.sleep(1)
    quit_testing(driver)
#novi mejl: dusan.filipovic1963@gmail.com, lozinka: requiemforadream2023


# LOGIN WITH INVALID MAIL ADDRESS
def test_TC2():
    driver = launch_chrome_and_go_to_site("https://poslovi.infostud.com/")
    time.sleep(1)
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.CLASS_NAME, \
                                          "uk-button.uk-button-primary.uk-button-small.nav-button-primary.chevron-button")).perform()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Kao kandidat')]").click()
    time.sleep(1)
    driver.find_element(By.ID, "username").send_keys("nikolijaf@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("autoQA2023")
    time.sleep(1)
    driver.find_element(By.ID, "save").click()
    time.sleep(1)
    driver.save_screenshot("screenshotsInfostud/test_case2.png")
    time.sleep(1)
    assert "Pogrešna email adresa ili lozinka." in driver.find_element(By.CLASS_NAME,
                                                                       "error__general").text, "Wrong or unexisting error message."
    time.sleep(1)
    quit_testing(driver)
#novi mejl: dusan.filipovic1963@gmail.com, lozinka: requiemforadream2023


# LOGIN WITH INVALID PASSWORD
def test_TC3():
    driver= launch_chrome_and_go_to_site("https://poslovi.infostud.com/")
    time.sleep(1)
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.CLASS_NAME, \
                                          "uk-button.uk-button-primary.uk-button-small.nav-button-primary.chevron-button")).perform()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Kao kandidat')]").click()
    time.sleep(1)
    driver.find_element(By.ID, "username").send_keys("nikolijaf4@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("QA2023")
    time.sleep(1)
    driver.find_element(By.ID, "save").click()
    time.sleep(1)
    driver.save_screenshot("screenshotsInfostud/test_case3.png")
    time.sleep(1)
    assert "Pogrešna email adresa ili lozinka." in driver.find_element(By.CLASS_NAME,
                                                                       "error__general").text, "Wrong or unexisting error message."
    time.sleep(1)
    quit_testing(driver)


# CHECK FILTER OPTION
def test_TC4():
    driver = launch_chrome_and_go_to_site("https://poslovi.infostud.com/")
    time.sleep(1)
    driver.find_element(By.ID, "q").send_keys("QA")
    time.sleep(2)
    driver.find_element(By.ID, "__search_button").click()
    time.sleep(1)
    driver.find_element(By.ID, "__expand_filters").click()
    time.sleep(1)
    driver.find_element(By.ID, "__disabled-checkbox").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "uk-float-right.popper-close.uk-icon.uk-close").click()
    time.sleep(1)
    assert driver.title=="Posao Srbija: Beograd, Novi Sad, Niš... - Poslovi Infostud", "Title is wrong"
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "las.la-times").click()
    time.sleep(5)
    driver.save_screenshot("screenshotsInfostud/test_case4.png")
    time.sleep(1)
    quit_testing(driver)


# CHECK PRIVACY NOTICE
def test_TC5():
    driver = launch_chrome_and_go_to_site("https://poslovi.infostud.com/")
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='/profili-poslodavaca']").click()
    time.sleep(7)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.END)
    time.sleep(1)
    driver.find_element(By.XPATH,
                        "//button[@type='button']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Obaveštenje o privatnosti')]").click()
    time.sleep(1)
    assert driver.title=='Privatnost / Uslovi', "Title is wrong"
    time.sleep(1)
    driver.save_screenshot("screenshotsInfostud/test_case5.png")
    time.sleep(1)
    quit_testing(driver)


# SEARCH FOR TEXT BY PARTIAL TITLE TEXT, CHECK DOES SEARCH FOR TEXT WORKS CORRECTLY, NEWS PAGE
def test_TC6():
    driver = launch_chrome_and_go_to_site("https://poslovi.infostud.com/")
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'U redu')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='/vesti?esource=homepage']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[@uk-icon='search']").click()
    time.sleep(1)
    driver.find_element(By.ID, "q").send_keys("kako se pripremiti")
    time.sleep(1)
    driver.find_element(By.ID, "q").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.save_screenshot("screenshots/test_case6.png")
    time.sleep(1)
    assert driver.title=="Vesti o zapošljavanju | Poslovi Infostud", "Title is wrong"
    time.sleep(1)
    quit_testing(driver)


# CHECK IF WE CAN SHARE ON FACEBOOK DESCRIPTION OF SOFTWARE ENGEENIER JOB
def test_TC7():
    driver = launch_chrome_and_go_to_site("https://poslovi.infostud.com/")
    time.sleep(1)
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.XPATH, "//a[contains(.,'Dok tražite posao')]")).perform()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='/opisi-zanimanja']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'U redu')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Informacione tehnologije')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Softver inženjer')]").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "a[title='Podeli na Facebook']").click()
    time.sleep(1)
    assert driver.title=="Facebook", "Wrong title"
    time.sleep(1)
    driver.save_screenshot("screenshotsInfostud/test_case7.png")
    time.sleep(1)
    quit_testing(driver)


# CHECK SETTINGS OF THE ACCOUNT, FILL FIRST PAGE OF INFO
def test_TC8():
    driver = launch_chrome_and_go_to_site("https://poslovi.infostud.com/")
    time.sleep(1)
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.XPATH, "//a[contains(.,'Prijavite se')]")).perform()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='/prijava?redirect=%2F']").click()
    time.sleep(1)
    driver.find_element(By.ID, "username").send_keys("nikolijaf4@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("autoQA2023")
    time.sleep(1)
    driver.find_element(By.ID, "save").send_keys(Keys.ENTER)
    time.sleep(1)
    a.move_to_element(driver.find_element(By.CLASS_NAME, "uk-border-circle.mr-15")).perform()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "a[href='/moj-profil/podesavanja?ref=podesavanja']").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[name='ime']").send_keys("Nikolija")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[name='prezime']").send_keys("Filipovic")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("0668688099")
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[contains(.,'Sačuvajte')]").click()
    time.sleep(1)
    driver.save_screenshot("screenshotsInfostud/test_case8.png")
    time.sleep(1)
    assert driver.title=="​Primajte ponude Poslovi na e-mail | Poslovi.infostud.com", "Wrong title"
    time.sleep(1)
    quit_testing(driver)


# CHECK SAVE SEARCH FOR HELLO WORLD COMPANY
def test_TC9():
    driver = launch_chrome_and_go_to_site("https://poslovi.infostud.com/")
    time.sleep(1)
    driver.find_element(By.ID, "q").send_keys("Hello World")
    time.sleep(1)
    driver.find_element(By.ID, "__search_button").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(.,'Sačuvajte pretragu')]").click()
    time.sleep(1)
    driver.find_element(By.ID, "username").send_keys("nikolijaf4@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("autoQA2023")
    time.sleep(1)
    driver.find_element(By.ID, "save").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Bez obaveštenja')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(.,'Najnovije')]").click()
    time.sleep(1)
    driver.save_screenshot("screenshotsInfostud/test_case9.png")
    time.sleep(1)
    assert "Najnovije" in driver.find_element(By.CLASS_NAME,
                                              "uk-button.uk-button-secondary.uk-button-small.__search_sort.uk-active").text, "Wrong button text"
    time.sleep(1)
    quit_testing(driver)


# DELETE SAVED SEARCH FROM PROFILE
def test_TC10():
    driver = launch_chrome_and_go_to_site("https://poslovi.infostud.com/")
    time.sleep(1)
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.CLASS_NAME, \
                                          "uk-button.uk-button-primary.uk-button-small.nav-button-primary.chevron-button")).perform()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Kao kandidat')]").click()
    time.sleep(1)
    driver.find_element(By.ID, "username").send_keys("nikolijaf4@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("autoQA2023")
    time.sleep(1)
    driver.find_element(By.ID, "save").click()
    time.sleep(1)
    a = ActionChains(driver)
    time.sleep(1)
    a = ActionChains(driver)
    time.sleep(1)
    a.move_to_element(driver.find_element(By.ID, "menu-imeiprezime")).perform()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Sačuvane pretrage')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Obrišite')]").click()
    time.sleep(1)
    driver.find_element(By.ID, "__ssearch-delete-submit").click()
    time.sleep(1)
    driver.save_screenshot("screenshotsInfostud/test_case10.png")
    time.sleep(1)
    assert driver.title=="Posao Srbija: Beograd, Novi Sad, Niš... - Poslovi Infostud", "Wrong title"
    time.sleep(1)
    quit_testing(driver)


# CLOSE GOOGLE CHROME AND QIUT TESTING
def quit_testing(driver):
    driver.minimize_window()
    driver.quit()