from playwright.sync_api import Locator, Page


class Control:
    def __init__(self, name: str, locator: Locator, page: Page):
        self.locator = locator
        self.name = name
        self.page = page

    def is_visible(self):
        return self.locator.is_visible()