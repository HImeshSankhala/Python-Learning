from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Predefined grocery items with their prices
GROCERY_ITEMS = {
    "Apples": 100.00,
    "Bananas": 40.00,
    "Milk": 50.00,
    "Bread": 30.00,
    "Eggs": 60.00,
    "Rice": 200.00,
    "Chicken": 250.00,
}

# Discounts associated with items (in percentage)
DISCOUNTS = {
    "Apples": 10,  # 10% discount
    "Bananas": 0,  # No discount
    "Milk": 5,     # 5% discount
    "Bread": 0,    # No discount
    "Eggs": 25,    # 25% discount
    "Rice": 15,    # 15% discount
    "Chicken": 20, # 20% discount
}

def display_items():
    """Display available grocery items."""
    print("Available Items:")
    for idx, item in enumerate(GROCERY_ITEMS, start=1):
        print(f"{idx}. {item} - Rs. {GROCERY_ITEMS[item]:.2f}/-")
    print("\nEnter the number of the item you want to purchase, or type 'done' when finished.")

def select_items():
    """Allow the user to select items and enter their quantities."""
    selected_items = {}
    item_list = list(GROCERY_ITEMS.keys())
    
    while True:
        item_choice = input("Select an item (by number) or type 'done': ").strip()
        if item_choice.lower() == 'done':
            break
        
        try:
            item_index = int(item_choice) - 1
            if 0 <= item_index < len(item_list):
                item = item_list[item_index]
                quantity = float(input(f"Enter quantity for {item} (in kg or units): "))
                if quantity > 0:
                    selected_items[item] = quantity
                else:
                    print("Please enter a positive quantity.")
            else:
                print("Invalid item selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    return selected_items

# Calculate prices after discount
def calculate_price(item, quantity):
    original_price = GROCERY_ITEMS[item] * quantity
    discount = DISCOUNTS[item]
    discount_amount = original_price * (discount / 100)
    final_price = original_price - discount_amount
    return original_price, discount_amount, final_price

# Display available items
display_items()

# Collect user input for item selection and quantities
selected_items = select_items()

# Generate data for the table
DATA = [
    ["Item", "Quantity", "Original Price (Rs.)", "Discount (Rs.)", "Final Price (Rs.)"],
]

subtotal = 0
total_discount = 0
total = 0

for item, quantity in selected_items.items():
    original_price, discount_amount, final_price = calculate_price(item, quantity)
    subtotal += original_price
    total_discount += discount_amount
    total += final_price
    DATA.append([item, str(quantity), f"{original_price:.2f}/-", f"-{discount_amount:.2f}/-", f"{final_price:.2f}/-"])

DATA.append(["Sub Total", "", "", "", f"{subtotal:.2f}/-"])
DATA.append(["Total Discount", "", "", "", f"-{total_discount:.2f}/-"])
DATA.append(["Total", "", "", "", f"{total:.2f}/-"])

# Create the PDF
pdf = SimpleDocTemplate("grocery_receipt.pdf", pagesize=A4)

# Standard stylesheet defined within reportlab
styles = getSampleStyleSheet()

# Fetch the style of Top level heading (Heading1)
title_style = styles["Heading1"]

# 0: left, 1: center, 2: right
title_style.alignment = 1

# Creating the paragraph with the heading text and passing the styles to it
title = Paragraph("Grocery Store Receipt", title_style)

# Create a Table Style object and define the styles row-wise
style = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ]
)

# Create a table object and pass the style to it
table = Table(DATA, style=style)

# Build the PDF
pdf.build([title, table])
