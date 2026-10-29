from playwright.sync_api import Page, expect


def test_valid_login(page: Page):
    # Open the login page
    page.goto("https://www.saucedemo.com/")

    # Enter valid credentials
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")

    # Click Login
    page.locator('[data-test="login-button"]').click()

    # Verify that login succeeded
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # Verify that the product list is visible
    expect(page.locator(".inventory_list")).to_be_visible()

def test_add_item_to_cart(page: Page):
    # Log in
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    # Add the first product to the cart
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    # Verify that the cart badge shows 1
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")
    page.screenshot(path="cart_screenshot.png")

def test_remove_item(page: Page):
    # Log in
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    # Add the first product
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    # Remove the product
    page.locator('[data-test="remove-sauce-labs-backpack"]').click()

    # Verify that the cart badge disappears
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)

def test_locked_out_user(page: Page):
    # Open the login page
    page.goto("https://www.saucedemo.com/")

    # Enter the locked-out user's credentials
    page.locator('[data-test="username"]').fill("locked_out_user")
    page.locator('[data-test="password"]').fill("secret_sauce")

    # Click Login
    page.locator('[data-test="login-button"]').click()

    # Verify the error message
    expect(page.locator('[data-test="error"]')).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )
