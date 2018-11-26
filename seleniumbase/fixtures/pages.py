import ConfigParser
from selenium.webdriver.common.by import By


class UiMapParser:
    locators_map = {
        "ById": By.ID,
        "ByName": By.NAME,
        "ByClassName": By.CLASS_NAME,
        "ByCssSelector": By.CSS_SELECTOR,
        "ByLinkText": By.LINK_TEXT,
        "ByPartialLinkText": By.PARTIAL_LINK_TEXT,
        "ByTagName": By.TAG_NAME,
        "ByXPath": By.XPATH,
    }

    def __init__(self, file_name, default_section):
        self.config = ConfigParser.SafeConfigParser()
        self.config.read(file_name)
        self.default_section = default_section

    def get_locator(self, locator_name, section=None):
        if not section:
            section = self.default_section
        locator_property = self.config.get(section, locator_name)
        locator_type = locator_property.split(':')[0]
        locator_value = locator_property.split(':')[1]

        return {"by": self.locators_map[locator_type], "selector": locator_value}


