import pytest
from playwright.sync_api import Page, expect
from pathlib import Path
from pages.cart_login import CartPage
from pages.inventory import InventoryPage
from pages.checkout import CheckoutPage

@pytest.fixture
def standard_user():
    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }

@pytest.fixture
def locked_out_user():
    return {
        "username": "locked_out_user",
        "password": "secret_sauce"
    }


@pytest.fixture
def logged_in_page(page: Page, standard_user):
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill(standard_user["username"])
    page.locator('[data-test="password"]').fill(standard_user["password"])
    page.locator('[data-test="login-button"]').click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    yield page

    if page.locator("#react-burger-menu-btn").count()>0:
        page.locator("#react-burger-menu-btn").click()
        page.locator('[data-test="logout-sidebar-link"]').wait_for(state="visible")
        page.locator('[data-test="logout-sidebar-link"]').click()

@pytest.fixture
def checkout_pages(logged_in_page):
    invent = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)
    return invent, cart, checkout


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page") or item.funcargs.get("logged_in_page")

        if page:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            page.screenshot(
                path=str(screenshot_dir / f"{item.name}.png")
            )