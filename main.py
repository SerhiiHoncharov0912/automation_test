import logging
import config
from playwright.sync_api import sync_playwright
from dtos.product_info_dto import ProductInfo
from page_objects.pages import LoginPage, InventoryPage, CartPage, CheckoutPage
from utils import setup_logger, save_products_to_csv


def main():
    setup_logger()
    logging.info("Starting automation script")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
        cart_page = CartPage(page)
        checkout_page = CheckoutPage(page)

        logging.info("========== Valid login ==========")
        login_page.goto_page()
        login_page.login(config.STANDARD_USER, config.VALID_PASSWORD)

        logging.info("========== Invalid logins ==========")
        login_page.goto_page()
        login_page.login(config.PROBLEM_USER, config.NOT_VALID_PASSWORD, False)

        login_page.goto_page()
        login_page.login(config.LOCKED_OUT_USER, config.VALID_PASSWORD, False)

        login_page.goto_page()
        login_page.login('', config.VALID_PASSWORD, False)

        login_page.goto_page()
        login_page.login(config.STANDARD_USER, '', False)

        logging.info("========== Extract product names and prices ==========")
        login_page.goto_page()
        login_page.login(config.STANDARD_USER, config.VALID_PASSWORD)
        products = inventory_page.get_products()
        product_details = [ProductInfo(name=p.name, price=p.price) for p in products]
        save_products_to_csv(product_details)

        logging.info("========== Go to cart and simulate empty checkout ==========")
        products[0].click_add_to_card_button()
        inventory_page.shopping_cart_button_click()
        cart_page.checkout_button_click()
        checkout_page.checkout()

        browser.close()
        logging.info("Script completed")

if __name__ == "__main__":
    main()