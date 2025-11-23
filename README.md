Hotel Taj Restaurant Management System 
Overview
This is a simple graphical user interface (GUI) restaurant management system developed using Python and Tkinter. It allows users to view a menu, add items to their order, and see the total price dynamically updated with engaging visual feedback.

Features
GUI application with a clean interface and attractive styling

Displays restaurant menu with item names and prices

Users can add items to their order via buttons

Dynamically updates the order list and total amount to pay

Animates the total price label for better user experience

Supports multiple item selections and updates accordingly

Menu
Item	       Price (Rs.)
Pizza	       150
Burger	     100
Salad	       250
Cold Coffee	 125
Momo	       120
Dosa	       140
How to Run
Ensure Python is installed on your system (Python 3.x recommended).

Tkinter is typically included with Python installations.

Save the Python script to a file, e.g., hotel_taj.py.

Run the script using a terminal or command prompt:

text
python hotel_taj.py
The app window will open displaying the menu and options to add items.

Click "Add to Order" to add items. The order list and total price update automatically.

User Interaction
The main window shows a welcome message, the menu with prices, and buttons for ordering.

Clicking "Add to Order" next to an item adds it to the order list below.

The total price label updates with a smooth color animation for visual feedback.

The order list shows all selected items with their price details.

Code Structure Highlights
The app uses a class BakeryApp to encapsulate the UI and order logic.

Menu items are stored in a dictionary with item names as keys and prices as values.

Dynamic Listbox displays the current order items.

add_to_cart method handles item addition and updates the total.

animate_total method creates a color toggle animation on the total price label.

This project is a great starting point to build more robust restaurant management systems by adding features such as item quantity, order removal, payment processing, and database integration.
