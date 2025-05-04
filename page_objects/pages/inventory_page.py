from typing import List
from playwright.sync_api import Page
from page_objects.controls import Button
from page_objects.elements.product_element import ProductElement
from page_objects.pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.shopping_cart_button = Button("Shopping Cart", page.locator("[data-test='shopping-cart-link']"), page)
        self.product = self.page.locator("[data-test='inventory-item']")

    def get_products(self) -> List[ProductElement]:
        products: List[ProductElement] = []

        for product in self.product.all():
            products.append(ProductElement(product))

        return products

    def shopping_cart_button_click(self):
        self.shopping_cart_button.click()
