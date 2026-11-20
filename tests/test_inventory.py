from playwright.sync_api import Page
from pages.inventory import InventoryPage

def test_sort_products_a_to_z(logged_in_page: Page):
    invent= InventoryPage(logged_in_page)

    invent.sort("az")

    product_names= invent.get_item_names()

    assert product_names == sorted(product_names)

def test_sort_products_z_to_a(logged_in_page: Page):
    invent= InventoryPage(logged_in_page)

    invent.sort("za")

    product_names= invent.get_item_names()

    assert product_names == sorted(product_names, reverse=True)