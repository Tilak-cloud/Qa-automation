from playwright.sync_api import Page
from pages.inventory import InventoryPage

def test_sort_products(logged_in_page: Page):
    invent= InventoryPage(logged_in_page)

    invent.sort("az")

    product_names= invent.get_item_names()

    assert product_names == sorted(product_names)