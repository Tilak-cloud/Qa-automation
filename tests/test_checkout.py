import pytest
from playwright.sync_api import Page, expect

@pytest.mark.smoke
def test_checkout_missing_first_name(logged_in_page: Page,checkout_pages):
    """TC_SD_05: Verify checkout error when first name is missing."""

    invent, cart, checkout = checkout_pages

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


def test_successful_checkout(logged_in_page:Page, checkout_pages):
    invent, cart, checkout = checkout_pages
    invent.add_to_cart()

    cart.open_cart()
    cart.start_checkout()
    checkout.fill_details("Nanny","test","12345")
    checkout.finish()

    expect(logged_in_page.locator('[data-test="complete-header"]')).to_have_text("Thank you for your order!")