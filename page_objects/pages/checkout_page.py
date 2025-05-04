import logging
from playwright.sync_api import Page
from page_objects.controls import TextBox, Button
from page_objects.pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_field = TextBox("First Name", page.locator("#first-name"), page)
        self.last_name_field = TextBox("Last Name", page.locator("#last-name"), page)
        self.postal_code_field = TextBox("Zip/Postal Code", page.locator("#postal-code"), page)
        self.continue_button = Button("Continue", page.locator("#continue"), page)

    def checkout(self, first_name: str = '', last_name: str = '', postal_code: str = ''):
        logging.info(f"Checkout with first_name '{first_name}', last_name '{last_name}', postal_code '{postal_code}'")
        self.first_name_field.fill(first_name) if first_name != '' else None
        self.last_name_field.fill(last_name) if last_name != '' else None
        self.postal_code_field.fill(postal_code) if postal_code != '' else None
        self.continue_button.click()
        self.check_error()