import logging
import config
from playwright.sync_api import Page
from page_objects.controls import TextBox, Button
from page_objects.pages import InventoryPage
from page_objects.pages.base_page import BasePage
from utils import capture_screenshot


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.user_name = TextBox("", page.locator("#user-name"), page)
        self.username_input = TextBox("Username", page.locator("#user-name"), page)
        self.password_input = TextBox("Password", page.locator("#password"), page)
        self.login_button = Button("Login", page.locator("#login-button"), page)

    def goto_page(self):
        self.page.goto(config.BASE_URL)

    def login(self, user_name: str, password: str, expect_success: bool = True):
        logging.info(f"Login with user_name '{user_name}', password '{password}'")
        self.username_input.fill(user_name)
        self.password_input.fill(password)
        self.login_button.click()
        self.check_error()

        if expect_success and not InventoryPage(self.page).shopping_cart_button.is_visible():
            logging.error(f"Inventory page is npt opened. Screenshot '{capture_screenshot(self.page)}'")