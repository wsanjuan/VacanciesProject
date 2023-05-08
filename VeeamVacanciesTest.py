from selenium import webdriver
from PageCareersVacancies import Veeam_Careers_Vacancies
from Options import expected_result, department, language
from setupLogger import logger
from lxml import etree

# Test Setup
browser = webdriver.Chrome()

# Veeam Page
Veeam_Vacancies = Veeam_Careers_Vacancies(driver=browser)
Veeam_Vacancies.go()
Veeam_Vacancies.max_window()

# Selecting the Department
Veeam_Vacancies.buttonALLDEPARMENTS.click()
Veeam_Vacancies.buttonDEPSELECTION.click()


#Selecting the Language
Veeam_Vacancies.buttonALLLANG().click()
Veeam_Vacancies.checkboxLANGSELECTION.click()
Veeam_Vacancies.buttonLANGSELECTED.click()

# Counting the results, asserting to the expected result and closing the browser
tree = etree.HTML(browser.page_source)
results = tree.findall(".//*[@id='root']/div/div[1]/div/div/div[2]/div/a")
try:
    assert (expected_result == len(results))
    logger.info('Test passed')
    browser.quit()
    logger.info('The browser has been closed')
except AssertionError as error:
    logger.exception(f"The amount of vacancies found ({len(results)}) for '{department}' & {language} does not match the expected value ({expected_result})")
    browser.quit()
    logger.info('The browser has been closed')
    raise error






