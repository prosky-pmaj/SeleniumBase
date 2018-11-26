import ConfigParser
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class Pages(BaseCase):
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

    def __init__(self, *args, **kwargs):
        super(Pages, self).__init__(*args, **kwargs)

    def set_up(self, ui_map_file, ui_map_section):
        self.__ui_map = ConfigParser.SafeConfigParser()
        self.__ui_map.read(ui_map_file)
        self.__section = ui_map_section

    def _get_locator(self, locator_name):
        locator_property = self.__ui_map.get(self.__section, locator_name)
        locator_type = locator_property.split(':')[0]
        locator_value = locator_property.split(':')[1]
        return {"by": self.locators_map[locator_type], "selector": locator_value}

    def wait_for_element(self, selector, by=None, timeout=None):
        if by is None:
            return super(Pages, self).wait_for_element(
                self._get_locator(selector)['selector'],
                self._get_locator(selector)['by'])
        else:
            return super(Pages, self).wait_for_element(selector, by)

    def get_text(self, selector, by=None, timeout=None):
        if by is None:
            return super(Pages, self).get_text(
                self._get_locator(selector)['selector'],
                self._get_locator(selector)['by'])
        else:
            return super(Pages, self).get_text(selector, by)

    def find_element(self, selector, by=None, timeout=None):
        if by is None:
            return super(Pages, self).find_element(
                self._get_locator(selector)['selector'],
                self._get_locator(selector)['by'])
        else:
            return super(Pages, self).get_text(selector, by)

    def click(self, selector, by=None, timeout=None):
        if by is None:
            return super(Pages, self).click(
                self._get_locator(selector)['selector'],
                self._get_locator(selector)['by'])
        else:
            return super(Pages, self).click(selector, by)

    def update_text(self, selector, new_value, by=None, timeout=None, retry=False):
        if by is None:
            return super(Pages, self).update_text(
                self._get_locator(selector)['selector'],
                new_value,
                self._get_locator(selector)['by'])
        else:
            return super(Pages, self).update_text(selector, new_value, by)
