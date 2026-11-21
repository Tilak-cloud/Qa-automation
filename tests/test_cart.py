import pytest
from playwright.sync_api import Page, expect

@pytest.mark.regression

def test_add_item_to_cart(logged_in_page: Page,checkout_pages):
    """TC_SD_03: Verify that a product can be added to a cart."""
    invent, cart, _ = checkout_pages

    invent.add_to_cart()
    cart.open_cart()

    assert cart.get_count() == 1

    logged_in_page.screenshot(path="cart_screenshot.png")

def test_cart_persistence(logged_in_page: Page, checkout_pages):
    invent, cart, _ = checkout_pages

    invent.add_to_cart()
    cart.open_cart()

    logged_in_page.reload()

    expect(logged_in_page.get_by_text("Sauce Labs Backpack", exact=True)).to_be_visible()
    assert cart.get_count()==1

def test_remove_item(logged_in_page: Page, checkout_pages):
    """TC_SD_04: Verify that a product can be removed from the cart."""
    invent, cart, _ = checkout_pages
    
    invent.add_to_cart()
    cart.open_cart()
    cart.remove_item()

    assert cart.get_count() == 0
