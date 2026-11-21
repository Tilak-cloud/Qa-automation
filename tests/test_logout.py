import pytest
from playwright.sync_api import Page, expect

@pytest.mark.regression
def test_logout(logged_in_page: Page):

    logged_in_page.locator("#react-burger-menu-btn").click()
    logged_in_page.locator('[data-test="logout-sidebar-link"]').click()

    expect(logged_in_page).to_have_url("https://www.saucedemo.com/")