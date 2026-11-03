class BasePage:
    """Common actions. Every page class inherits from this."""

    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def select_option(self, locator, value):
        self.page.locator(locator).select_option(value)

    def get_url(self):
        return self.page.url
