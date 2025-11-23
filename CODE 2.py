import tkinter as tk
from tkinter import messagebox

# Your menu data
menu = {
    "Pizza": 150,
    "Burger": 100,
    "Salad": 250,
    "Cold Coffee": 125,
    "Momo": 120,
    "Dosa": 140
}

class BakeryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Taj")
        self.cart = []
        self.total_price = 0

        header = tk.Label(root, text="Welcome to Hotel Taj", font=("Helvetica", 18, "bold"), fg="#4b2e83")
        header.pack(pady=10)

        menu_label = tk.Label(root, text="Menu", font=("Helvetica", 16))
        menu_label.pack()

        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack(padx=10)

        # Create menu buttons
        for item, price in menu.items():
            frame = tk.Frame(self.menu_frame, borderwidth=1, relief="raised", padx=10, pady=5)
            frame.pack(pady=5, fill="x")

            name_label = tk.Label(frame, text=item, font=("Helvetica", 12), width=30, anchor="w")
            name_label.pack(side="left")

            price_label = tk.Label(frame, text=f"Rs. {price}", font=("Helvetica", 12, "bold"), fg="#cc5686")
            price_label.pack(side="left", padx=10)

            add_button = tk.Button(frame, text="Add to Order", command=lambda i=item: self.add_to_cart(i), bg="#cc5686", fg="white")
            add_button.pack(side="right")

        cart_label = tk.Label(root, text="Your Order", font=("Helvetica", 16))
        cart_label.pack(pady=(20, 5))

        self.cart_listbox = tk.Listbox(root, width=60, height=8)
        self.cart_listbox.pack()

        self.total_label = tk.Label(root, text="Total amount to pay is Rs. 0", font=("Helvetica", 14, "bold"), fg="#cc5686")
        self.total_label.pack(pady=10)

    def add_to_cart(self, item):
        self.cart.append(item)
        self.cart_listbox.insert(tk.END, f"{item} - Rs. {menu[item]}")
        self.total_price += menu[item]
        self.animate_total()
        self.total_label.config(text=f"Total amount to pay is Rs. {self.total_price}")

    def animate_total(self):
        def toggle_color():
            current = self.total_label.cget("fg")
            new_color = "#ff69b4" if current == "#cc5686" else "#cc5686"
            self.total_label.config(fg=new_color)

        for i in range(6):
            self.root.after(i * 300, toggle_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = BakeryApp(root)
    root.mainloop()

