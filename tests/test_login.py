import pytest 
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.parametrize(
    "username, expected_outcome",
    [
        ("standard_user", "success"),
        ("locked_out_user", "locked_out"),
        ("problem_user", "success"),
        ("performance_glitch_user", "success"),
    ],
    ids=[
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
    ]
)

def test_login(page:Page, username, expected_outcome):
    page.goto("https://www.saucedemo.com/")

    login=LoginPage(page)
    login.login(username, "secret_sauce")

    if expected_outcome == "success":
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        expect(page.locator('[data-test="error"]')).to_contain_text("locked out")
