import pytest
from playwright.sync_api import Page


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

    yield page

    page.locator("#react-burger-menu-btn").click()
    page.locator('[data-test="logout-sidebar-link"]').wait_for(state="visible")
    page.locator('[data-test="logout-sidebar-link"]').click()