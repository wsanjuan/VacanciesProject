from setupLogger import logger
class BasePage(object):
    url = None
    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
        logger.info("The page {} has been opened".format(self.url))

    def max_window(self):
        self.driver.maximize_window()