import logging
from playwright.sync_api import Locator, Page
from page_objects.controls.control import Control
from utils import capture_screenshot


class TextBox(Control):
    def __init__(self, name: str, locator: Locator, page: Page):
        super().__init__(name, locator, page)

    def fill(self, text: str):
        try:
            self.locator.fill(text)
        except Exception as e:
            logging.error(f"Attempt to fill '{self.name}' text box failed with error: {e} Screenshot: '{capture_screenshot(self.page)}'")
        else:
            logging.info(f"'{self.name}' text box filled with text '{text}'")