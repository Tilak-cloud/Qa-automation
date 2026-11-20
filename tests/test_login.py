import pytest 
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

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
# def test_valid_login(page: Page, standard_user):
#     """TC_SD_01: Verify successful login with valid credentials"""
    
#     login_page= LoginPage(page)
#     # Open the login page
#     page.goto("https://www.saucedemo.com/")

#     login_page.login(
#         standard_user["username"],
#         standard_user["password"]
#     )

#     expect(page).to_have_url(
#         "https://www.saucedemo.com/inventory.html"
#     )


#     # # Verify that the product list is visible
#     # expect(page.locator(".inventory_list")).to_be_visible()


# def test_locked_out_user(page: Page, locked_out_user):
#     """TC_SD_02: Verify login error fro a locked-out user."""
#     # Open the login page
#     login_page = LoginPage(page)

#     page.goto("https://www.saucedemo.com/")

#     login_page.login(
#         locked_out_user["username"],
#         locked_out_user["password"]
#     )

#     expect(page.locator('[data-test="error"]')).to_be_visible()