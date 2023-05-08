from selenium.webdriver.common.by import By
from BaseElement import BaseElement
from Options import department, language
from BasePage import BasePage
from Locator import Locator



class Veeam_Careers_Vacancies(BasePage):

    url = 'https://cz.careers.veeam.com/vacancies'

    @property
    def buttonALLDEPARMENTS(self):
        locator = Locator(by=By.XPATH, value="//button[contains(text(),'All dep')]")
        return BaseElement(
            driver=self.driver,
            locator=locator,
            elem_name= 'All Departments Dropdown'
        )

    @property
    def buttonDEPSELECTION(self):
        selection = "//a[contains(text(),'" + department + "')]"
        locator = (By.XPATH, selection)
        return BaseElement(
            driver=self.driver,
            locator=locator,
            elem_name='Department ' + department
        )

    def buttonALLLANG(self):
        locator = (By.XPATH, "//button[contains(text(),'All lang')]")
        return BaseElement(
            driver=self.driver,
            locator=locator,
            elem_name='All languages Dropdown'
        )

    @property
    def checkboxLANGSELECTION(self):
        selection = "//label[contains(text(),'" + language + "')]"
        locator = (By.XPATH, selection)
        return BaseElement(
            driver=self.driver,
            locator=locator,
            elem_name= 'Checkbox for language: ' + language
        )

    @property
    def buttonLANGSELECTED(self):
        selection = "//button[contains(text(),'" + language + "')]"
        locator = (By.XPATH, selection)
        return BaseElement(
            driver=self.driver,
            locator=locator,
            elem_name="Close the language dropdown"
        )

