import logging
from playwright.sync_api import Locator, Page
from page_objects.controls.control import Control
from utils import capture_screenshot


class Button(Control):
    def __init__(self, name: str, locator: Locator, page: Page):
        super().__init__(name, locator, page)

    def click(self):
        try:
            self.locator.click()
        except Exception as e:
            logging.error(f"Attempt to click '{self.name}' button failed with error: {e} Screenshot: '{capture_screenshot(self.page)}'")
        else:
            logging.info(f"'{self.name}' button clicked")