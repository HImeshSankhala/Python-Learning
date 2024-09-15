# Auto Login Bot using Selenium

## Introduction

This Python script automates the login process for any website using Selenium. It opens a web browser, navigates to the given URL, enters the user credentials, and submits the login form. The script can be configured to work with any website that requires login credentials.

## Features

- Automates the login process for any website.
- Uses Selenium WebDriver to interact with the browser.
- Allows the user to input their credentials and website URL.
- Keeps the browser open until the user manually closes it or presses Enter in the terminal.

## Prerequisites

### 1. Install Python

Ensure that Python is installed on your system. You can download and install Python from [python.org](https://www.python.org/downloads/).

### 2. Install Selenium

You will need the Selenium library for browser automation. Install it via pip:

```bash
pip install selenium
```

### 3. Install ChromeDriver

ChromeDriver is required to automate Chrome with Selenium. Download the version that matches your Chrome browser from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

Once downloaded, extract the `chromedriver.exe` and place it in a known location. Update the script's `path` variable to reflect the location of your `chromedriver.exe`.

## Setup

1. **Download ChromeDriver**: Download the appropriate version of ChromeDriver for your system from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

2. **Update the Script**: In the script, update the following variables:

   - `path = r"C:\path\to\your\chromedriver.exe"`: Replace with the actual path to your local `chromedriver.exe`.

   - `username = "your_username"`: Replace with your login username.

   - `password = "your_password"`: Replace with your login password.

   - `url = "https://example.com/login"`: Replace with the login page URL of the website you want to automate.

3. **Update Element Locators**: You need to inspect the login page to find the correct locators (ID, Name, Class, etc.) for the username, password, and login button fields. Update the following lines in the script:

   - `driver.find_element(By.NAME, "email")`: Change `"email"` to the appropriate locator for the username field.

   - `driver.find_element(By.NAME, "pass")`: Change `"pass"` to the appropriate locator for the password field.

   - `driver.find_element(By.NAME, "login")`: Change `"login"` to the appropriate locator for the login button.
