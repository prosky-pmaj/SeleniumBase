from seleniumbase.fixtures.pages import Pages, By
from selenium.webdriver.remote.errorhandler import ElementNotVisibleException


class BlogPage(Pages):

    def __init__(self):
        super(BlogPage, self).__init__('ghost.ini', 'ui-map-ghost.ini', 'Blog')
        self.url = self._config.get('ghost', 'url')

    def go_to(self):
        self.open(self.url)
        self.wait_for_element('blog.homePage')

    def go_to_post(self, title):
        self.scroll_to("//a[text()='" + title + "']", By.XPATH)
        self.click("//a[text()='" + title + "']", By.XPATH)
        self.wait_for_element("//h1[text()='" + title + "']", By.XPATH)

    def is_post_present(self, title):
        # jse.executeScript("scroll(0, 250)");
        try:
            self.find_element("//a[text()='" + title + "']", By.XPATH)
            return True
        except ElementNotVisibleException:
            return False

    def get_post_title(self):
        return self.get_text('blog.postPage.title')

    def get_post_content(self):
        return self.get_text('blog.postPage.content')

    def is_post_data_correct(self, expected_post_title, expected_post_content):
        assert self.get_title() == expected_post_title
        # Assert.assertEquals(
        #         getPostContent()
        #                 .replaceAll("\\s+", " "),
        #         expectedPostContent
        #                 .replaceAll("\\!\\[[^(]*\\([^)]*\\)", "")
        #                 .replaceAll("<[^/>]*\\/>", "")
        #                 .replaceAll("(---)", "")
        #                 .replaceAll("[1-9]\\.", "")
        #                 .replaceAll("\\[([^\\[]*)\\]\\([^\\)]*\\)", "$1")
        #                 .replaceAll("\\!\\[([^\\[]*)\\]", "")
        #                 .replaceAll("\\n>", "")
        #                 .replaceAll("[`#*]", "")
        #                 .replaceAll("\\s+", " "));
        # return true;
        pass
