# QA Automation – Python & Playwright

A beginner QA automation project using Python, Pytest, and Playwright. This project automates testing of the [SauceDemo](https://www.saucedemo.com/) website.

## Test Cases

| Test ID | Test Case | Description |
|---|---|---|
| TC_SD_01 | Valid Login | Verify login with valid credentials |
| TC_SD_02 | Locked-out User | Verify error for a locked-out user |
| TC_SD_03 | Add Item to Cart | Verify that a product can be added |
| TC_SD_04 | Remove Item from Cart | Verify that a product can be removed |
| TC_SD_05 | Checkout Validation | Verify error when first name is missing |

## Project Structure

```text
qa-automation/
├── tests/
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_login.py
├── conftest.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3
- Git
- VS Code
- Pytest
- Playwright

## Setup

Clone the repository:

```bash
git clone https://github.com/Tilak-cloud/Qa-automation.git
cd Qa-automation
```

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies and the Chromium browser:

```bash
pip install pytest-playwright
playwright install chromium
```

## Run Tests

Run all tests:

```bash
pytest -v
```

Run tests with a visible browser:

```bash
pytest -v --headed --slowmo 1000
```

## Tools Used

- Python
- Pytest
- Playwright
- Git and GitHub

## Learning Objective

Practise browser automation, locators, actions, assertions, auto-waiting, fixtures, and test organization using a real website.
