import logging
import os
from dataclasses import asdict
from typing import List
import pandas as pd
from playwright.async_api import Page
from dtos.product_info_dto import ProductInfo

screenshot_counter = 1

def save_products_to_csv(products: List[ProductInfo], filename="products.csv"):
    df = pd.DataFrame([asdict(p) for p in products])
    df.to_csv(filename, index=False)

def capture_screenshot(page: Page) -> str:
    global screenshot_counter
    folder = 'automation_screenshots'
    os.makedirs(folder, exist_ok=True)
    screenshot_name = f"screenshot{screenshot_counter}.png"
    screenshot_counter += 1
    path = os.path.join(folder, screenshot_name)
    page.screenshot(path=path)
    return path

def setup_logger():
    logging.basicConfig(
        filename='automation.log',
        filemode='w',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )