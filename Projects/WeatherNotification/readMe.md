# Live Weather and Air Quality Notification Script

## Introduction

This Python script fetches the current temperature and air quality index from weather.com and displays it as a desktop notification using `win10toast`. It uses the `requests` library to get the webpage content and `BeautifulSoup` to parse the HTML and extract the required data.

## How It Works

1. **Fetch Data**: The script sends an HTTP request to the weather.com website for the specified location and retrieves the webpage's HTML content.
2. **Parse Data**: Using `BeautifulSoup`, the script parses the HTML and extracts the current temperature and air quality index using specific HTML element attributes.
3. **Display Notification**: The extracted data is formatted into a string and displayed as a desktop notification using the `win10toast` library.

## Requirements

The script requires the following Python libraries:

- `requests`
- `beautifulsoup4`
- `win10toast`

You can install these libraries using `pip`:

```bash
pip install requests
pip install beautifulsoup4
pip install win10toast
```
