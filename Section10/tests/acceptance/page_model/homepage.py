from tests.acceptance.locators.homepage import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return super(HomePage, self).url() +'/'

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)


