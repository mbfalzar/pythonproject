import tkinter as tk
from tkinter import ttk
from datetime import datetime
import requests
from tkcalendar import Calendar


def submit():
    barcode = barcode_entry.get()
    expiration_date = expiration_entry.get_date()
    price = price_entry.get()

    # Calculate days until expiration
    expiration_date_obj = datetime.strptime(expiration_date, "%m/%d/%y")
    current_date_obj = datetime.now()
    bestBeforeInDays = (expiration_date_obj - current_date_obj).days

    # Preparing data
    data = {
        "barcode": str(barcode),
        "bestBeforeInDays": str(bestBeforeInDays),
        "price": str(price)
    }
    headers = {
        "accept": "application/json",
        # requests won't add a boundary if this header is set when you pass files=

        #'Content-Type': 'multipart/form-data',
    }

    # Convert data to JSON and send via POST request
    response = requests.post("https://barcode.tombs.rip/api/action/scan?apikey=kJSvfMoXiuhZ5GgbIDzB6ty4jrEWc9", headers=headers, data=data)

    if response.ok:
        result_label.config(text=f"Data sent successfully: {response.text}")
    else:
        result_label.config(text=f"Error sending data: {response.status_code}")

# GUI setup

root = tk.Tk()


root.title("Barcode Submission Form")

ttk.Label(root, text="Barcode:").grid(column=0, row=0, padx=10, pady=10)
barcode_entry = ttk.Entry(root)
barcode_entry.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="Expiration Date").grid(column=0, row=1, padx=10, pady=10)
expiration_entry = Calendar(root, selectmode='day')
expiration_entry.grid(column=1, row=1, padx=10, pady=10)

ttk.Label(root, text="Price:").grid(column=0, row=2, padx=10, pady=10)
price_entry = ttk.Entry(root)
price_entry.grid(column=1, row=2, padx=10, pady=10)

ttk.Button(root, text="Submit", command=submit).grid(column=0, row=3, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=4, columnspan=2)

root.mainloop()
