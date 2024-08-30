# Grocery Store Receipt Generator

## Introduction

This Python script generates a PDF receipt for a grocery store. The user can dynamically select items from a predefined list, enter the desired quantities, and the script will calculate the total price, apply discounts, and generate a formatted receipt.

## Features

- **Dynamic Item Selection**: Users can select items from a list by entering the corresponding item number.
- **Quantity Input**: Users can specify the quantity for each selected item.
- **Discount Calculation**: The script applies predefined discounts to items and calculates the final price.
- **PDF Generation**: The receipt is generated in PDF format, including the item details, discounts, subtotal, and total amount.

## Prerequisites

- **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **ReportLab**: This package is required to generate PDFs. You can install it using pip:

  ```bash
  pip install reportlab
  ```
