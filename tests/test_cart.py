from playwright.sync_api import Page, expect
from pages.cart_login import CartPage
from pages.inventory import InventoryPage


def test_add_item_to_cart(logged_in_page: Page):
    """TC_SD_03: Verify that a product can be added to a cart."""
    cart= CartPage(logged_in_page)
    invent= InventoryPage(logged_in_page)

    invent.add_to_cart()
    cart.open_cart()

    assert cart.get_count() == 1

    logged_in_page.screenshot(path="cart_screenshot.png")


def test_remove_item(logged_in_page: Page):
    """TC_SD_04: Verify that a product can be removed from the cart."""
    cart= CartPage(logged_in_page)
    invent= InventoryPage(logged_in_page)
    
    invent.add_to_cart()
    cart.open_cart()
    cart.remove_item()

    assert cart.get_count() == 0
