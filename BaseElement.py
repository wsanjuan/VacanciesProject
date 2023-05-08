from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, TimeoutException, ElementClickInterceptedException
from setupLogger import logger

class BaseElement(object):
    def __init__(self, driver, locator, elem_name):
        self.driver = driver
        self.locator = locator
        self.elem_name = elem_name
        self.web_element = None
        self.find()

    # This function checks if the web element (for which the locator has been passed) is visible or not. Returns the element if found
    def find(self):
        try:
            element = WebDriverWait(
            self.driver, 3).until(
            EC.visibility_of_element_located(self.locator))
            self.web_element = element
            logger.info("Element '{}' has been FOUND".format(self.elem_name))
            return None
        except ElementNotVisibleException:
            self.driver.close()
            logger.exception("'{}' not visible: ElementNotVisibleException".format(self.elem_name))
        except NoSuchElementException:
            self.driver.close()
            logger.exception("'{}' not found: NoSuchElementException occurred".format(self.elem_name))
        except TimeoutException:
            self.driver.close()
            logger.exception("'{}' not visible in time: TimeoutException occurred".format(self.elem_name))
        except Exception as e:
            self.driver.close()
            logger.exception("Error finding '{}': {}".format(self.elem_name, e))

    # this function performs click on the web element for which the locator has been passed
    def click(self):
        try:
            element = WebDriverWait(
                self.driver, 3).until(
                EC.element_to_be_clickable(self.locator))
            element.click()
            logger.info("Element '{}' has been SELECTED".format(self.elem_name))
            return None
        except TimeoutException:
            self.driver.close()
            logger.exception("'{}' not clickable in time: TimeoutException occurred".format(self.elem_name))
        except ElementClickInterceptedException:
            self.driver.close()
            logger.exception("'{}' not clickable in time: ElementClickInterceptedException occurred. The option may be disabled".format(self.elem_name))
        except Exception as e:
            self.driver.close()
            logger.exception("Error finding '{}': {}".format(self.elem_name, e))

