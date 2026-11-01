from playwright.sync_api import Page, expect


def test_add_item_to_cart(logged_in_page: Page):
    """TC_SD_03: Verify that a product can be added to a cart."""
    page = logged_in_page

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")

    page.screenshot(path="cart_screenshot.png")


def test_remove_item(logged_in_page: Page):
    """TC_SD_04: Verify that a product can be added to a cart."""
    page = logged_in_page

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="remove-sauce-labs-backpack"]').click()

    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)
