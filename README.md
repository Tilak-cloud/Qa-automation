# SauceDemo QA Automation Framework

A Python-based test automation project for the [SauceDemo](https://www.saucedemo.com/) web application. The project combines UI automation using Playwright, API testing using Requests, pytest test execution, Page Object Model (POM), and continuous integration with GitHub Actions.

## Project Overview

This framework covers selected end-to-end user workflows on SauceDemo and API scenarios against JSONPlaceholder.

### Technology Stack

| Tool / Technology | Purpose |
|---|---|
| Python 3.13 | Programming language |
| pytest | Test runner, fixtures, parametrization, and markers |
| Playwright (Sync API) | Browser UI automation |
| pytest-playwright | Playwright integration with pytest |
| Requests | HTTP API testing |
| Git and GitHub | Version control and repository hosting |
| GitHub Actions | Continuous integration |

## Project Structure

```text
Qa-automation/
│
├── .github/
│   └── workflows/
│       └── pytest.yml
│
├── api_tests/
│   └── test_api_demo.py
│
├── pages/
│   ├── cart_login.py
│   ├── checkout.py
│   ├── inventory.py
│   └── login_page.py
│
├── tests/
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_inventory.py
│   ├── test_login.py
│   └── test_logout.py
│
├── .gitignore
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## UI Automation Coverage

UI tests are located in `tests/`. Page interaction methods are organized into page classes in `pages/`.

| Area | Scenarios covered |
|---|---|
| Login | Valid standard user, locked-out user, problem user, and performance-glitch user |
| Cart | Add item, remove item, and cart persistence after page reload |
| Checkout | Missing first-name validation and successful checkout |
| Inventory | Sort products A–Z and Z–A |
| Logout | Log out and verify navigation back to the login page |

The login test uses pytest parametrization to run the same test with different user accounts.

## API Automation Coverage

API tests are located in `api_tests/test_api_demo.py` and use the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) test API.

| Scenario | What is checked |
|---|---|
| GET a post | Status code and returned post data |
| Create a post | POST status code and response fields |
| Invalid post | 404 response for a nonexistent post |
| Response validation | Required keys, data types, and post ID |
| Query parameter | Filter posts by `userId` |
| Parametrized GET | Retrieve posts with IDs 1, 2, and 3 |
| Request headers | Send an `Accept: application/json` header and inspect response content type |
| Authorization header | Send a demonstration Bearer Authorization header |
| Timeout setting | Send a request with a configured timeout |

**Note:** JSONPlaceholder is a demo API. Its POST endpoint simulates resource creation; it does not permanently save the new post. The Authorization-header test demonstrates sending a header only; JSONPlaceholder does not enforce authentication for this request.

## Framework Design and Test Features

- **Page Object Model:** Page locators and actions are grouped into page classes to keep UI tests more readable and maintainable.
- **Fixtures:** Shared setup is defined in `conftest.py`, including user data, a logged-in page, and page objects used by checkout tests.
- **Parametrization:** Login scenarios and API post IDs are tested with multiple input values.
- **Markers:** Smoke and regression tests can be selected independently.
- **Failure screenshots:** A pytest report hook captures a screenshot when a test call fails. Screenshots are written to `screenshots/`.
- **Playwright traces:** Trace recording is configured with `--tracing retain-on-failure` in `pytest.ini`.

## Prerequisites

- Windows, macOS, or Linux
- Python 3.13
- Git
- Internet access to reach SauceDemo and JSONPlaceholder

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Tilak-cloud/Qa-automation.git
cd Qa-automation
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, follow your organization's or system's PowerShell execution policy guidance.

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Install the Playwright Chromium browser

```bash
python -m playwright install chromium
```

On Linux CI environments, install browser system dependencies as well:

```bash
python -m playwright install --with-deps chromium
```

## Running Tests

Run the complete UI and API test suite:

```bash
pytest -v
```

Run tests with a visible browser:

```bash
pytest -v --headed
```

Run only UI tests:

```bash
pytest -v tests/
```

Run only API tests:

```bash
pytest -v api_tests/
```

Run smoke tests:

```bash
pytest -m smoke -v
```

Run regression tests:

```bash
pytest -m regression -v
```

Run tests that do not have either marker:

```bash
pytest -m "not smoke and not regression" -v
```

## Playwright Traces and Failure Screenshots

Trace recording is configured in `pytest.ini`:

```ini
[pytest]
addopts = --tracing retain-on-failure
```

When a test fails, the retained trace can be opened with:

```bash
playwright show-trace path/to/trace.zip
```

The pytest failure hook saves screenshots in the `screenshots/` directory. These generated artifacts are excluded from Git using `.gitignore`.

## Continuous Integration

The GitHub Actions workflow is located at `.github/workflows/pytest.yml`.

It runs on pushes and pull requests to the repository. The workflow:

1. Checks out the repository.
2. Sets up Python 3.13.
3. Installs dependencies from `requirements.txt`.
4. Installs Chromium and its Linux dependencies.
5. Runs the UI and API test suite using `pytest -v`.

## Repository

[GitHub – Qa-automation](https://github.com/Tilak-cloud/Qa-automation)

## Learning Objectives

This project was built to practise:

- Python-based test automation
- Writing and organizing pytest tests
- Browser automation with Playwright Sync API
- Page Object Model
- Fixtures, parametrization, and markers
- API testing with Requests
- HTTP methods, status codes, headers, query parameters, and JSON response validation
- Debugging with screenshots and Playwright traces
- Version control with Git and GitHub
- Running automated tests in GitHub Actions
