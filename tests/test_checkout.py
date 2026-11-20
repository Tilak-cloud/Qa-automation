from playwright.sync_api import Page, expect
from pages.checkout import CheckoutPage 
from pages.inventory import InventoryPage
from pages.cart_login import CartPage


def test_checkout_missing_first_name(logged_in_page: Page):
    """TC_SD_05: Verify checkout error when first name is missing."""

    checkout= CheckoutPage(logged_in_page)
    invent= InventoryPage(logged_in_page)
    cart= CartPage(logged_in_page)

    # Add a product to the cart
    invent.add_to_cart()
    
    # Open the cart
    cart.open_cart()
    
    # Start checkout
    cart.start_checkout()
    checkout.fill_details("","Test","12345")

    # Verify the error message
    expect(logged_in_page.locator('[data-test="error"]')).to_have_text(
        "Error: First Name is required"
    )