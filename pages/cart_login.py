from playwright.sync_api import Page

class CartPage:

    def __init__(self, page:Page):
        self.page= page

        self.remove=page.locator('[data-test="remove-sauce-labs-backpack"]')
        self.icon=page.locator('[data-test="shopping-cart-link"]')
        self.badge=page.locator('[data-test="shopping-cart-badge"]')
        self.checkout_btn=page.locator('[data-test="checkout"]')

    def open_cart(self):
        self.icon.click()

    def start_checkout(self):
        self.checkout_btn.click()

    def remove_item(self):
        self.remove.click()

    def get_count(self):
        if self.badge.count() > 0:
            return int(self.badge.inner_text())
        else:
            return 0
            