from playwright.sync_api import Page
from page_objects.controls import Button
from page_objects.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_button = Button("Checkout", self.page.get_by_text("Checkout"), self.page)

    def checkout_button_click(self):
        self.checkout_button.click()

