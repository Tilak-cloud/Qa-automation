from playwright.sync_api import Page

class CheckoutPage:

    def __init__(self,page:Page):
        self.page= page
        self.fname=page.locator('[data-test="firstName"]')
        self.lname=page.locator('[data-test="lastName"]')
        self.code=page.locator('[data-test="postalCode"]')
        self.continuebtn=page.locator('[data-test="continue"]')
        self.finishbtn=page.locator('[data-test="finish"]')

    def fill_details(self,firstName,lastName,postalCode):
        self.fname.fill(firstName)
        self.lname.fill(lastName)
        self.code.fill(postalCode)
        self.continuebtn.click()

    def finish(self):
        self.finishbtn.click()


        