from playwright.sync_api import Page

class InventoryPage:

    def __init__(self, page:Page):
        self.page= page

        self.add=page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.sort_item=page.locator('[data-test="product-sort-container"]')
        self.products=page.locator('[data-test="inventory-item-name"]')

    def add_to_cart(self):
        self.add.click()

    def sort(self, option):
        self.sort_item.select_option(option)

    def get_item_names(self):
        return self.products.all_text_contents()