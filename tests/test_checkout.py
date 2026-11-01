from playwright.sync_api import Page, expect


def test_checkout_missing_first_name(logged_in_page: Page):
    """TC_SD_05: Verify checkout error when first name is missing."""

    page = logged_in_page

    # Add a product to the cart
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    # Open the cart
    page.locator('[data-test="shopping-cart-link"]').click()

    # Start checkout
    page.locator('[data-test="checkout"]').click()

    # Leave first name empty; enter the other details
    page.locator('[data-test="lastName"]').fill("Tester")
    page.locator('[data-test="postalCode"]').fill("560001")

    # Continue checkout
    page.locator('[data-test="continue"]').click()

    # Verify the error message
    expect(page.locator('[data-test="error"]')).to_have_text(
        "Error: First Name is required"
    )