import logging
from playwright.sync_api import Page
from utils import capture_screenshot


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def check_error(self):
        if self.page.locator("[data-test='error']").is_visible():
            error_text = self.page.locator("[data-test='error']").text_content()
            screenshot_name = capture_screenshot(self.page)
            logging.error(f"Login error: {error_text}. Screenshot: {screenshot_name}")