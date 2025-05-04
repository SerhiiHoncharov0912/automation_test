from playwright.sync_api import Locator


class ProductElement:
    def __init__(self, locator: Locator):
        self.name_control = locator.locator("[data-test='inventory-item-name']")
        self.price_control = locator.locator("[data-test='inventory-item-price']")
        self.add_to_card_button = locator.locator("[name*='add-to-cart']")
        self.name = self.name_control.text_content()
        self.price = self.price_control.text_content().replace("$", "")

    def click_add_to_card_button(self):
        self.add_to_card_button.click()