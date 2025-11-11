from tkinter import *
from tkinter import messagebox
from datetime import datetime
import os

root = Tk()
root.geometry("1200x600")
root.title("Restaurant Bill Management System")
root.resizable(False, False)
root.configure(bg="lightgray")

# Restaurant details
RESTAURANT_NAME = " KU CANTEEN"
RESTAURANT_ADDRESS = "KU College of Engineering And Technology, Hanamkonda"
RESTAURANT_PHONE = "Phone: +91-9347522528"

def Reset():
    entry_dosa.delete(0, END)
    entry_puri.delete(0, END)
    entry_idli.delete(0, END)
    entry_bonda.delete(0, END)
    entry_vada.delete(0, END)
    entry_tea.delete(0, END)
    entry_coffee.delete(0, END)
    
    # Clear the bill display
    bill_text.delete(1.0, END)
    Total_Bill.set("")

def calculate_total():
    try: a1 = int(dosa.get()) if dosa.get() else 0
    except: a1 = 0
    
    try: a2 = int(puri.get()) if puri.get() else 0
    except: a2 = 0
    
    try: a3 = int(idli.get()) if idli.get() else 0
    except: a3 = 0
    
    try: a4 = int(bonda.get()) if bonda.get() else 0
    except: a4 = 0
    
    try: a5 = int(vada.get()) if vada.get() else 0
    except: a5 = 0
    
    try: a6 = int(tea.get()) if tea.get() else 0
    except: a6 = 0
    
    try: a7 = int(coffee.get()) if coffee.get() else 0
    except: a7 = 0
    
    # Menu items with prices
    menu_items = [
        ("Dosa", 40, a1),
        ("Puri", 40, a2),
        ("Idli", 35, a3),
        ("Bonda", 40, a4),
        ("Vada", 40, a5),
        ("Tea", 10, a6),
        ("Coffee", 15, a7)
    ]
    
    return menu_items

def generate_bill():
    menu_items = calculate_total()
    
    # Check if any item is ordered
    if all(item[2] == 0 for item in menu_items):
        messagebox.showwarning("No Items", "Please select at least one item!")
        return
    
    # Clear previous bill
    bill_text.delete(1.0, END)
    
    # Get current date and time
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    
    # Generate bill content
    bill_content = f"""
{'='*50}
           {RESTAURANT_NAME}
{'='*50}
{RESTAURANT_ADDRESS}
{RESTAURANT_PHONE}
{'='*50}
Date & Time: {date_time}
{'='*50}
ITEM NAME        QTY    RATE    AMOUNT
{'='*50}
"""
    
    subtotal = 0
    for item_name, price, qty in menu_items:
        if qty > 0:
            amount = price * qty
            subtotal += amount
            bill_content += f"{item_name:<15} {qty:>3}  x {price:>3} = Rs.{amount:>6.2f}\n"
    
    # Calculate taxes and total
    tax_rate = 0.05  # 5% tax
    tax_amount = subtotal * tax_rate
    total_amount = subtotal + tax_amount
    
    bill_content += f"""
{'='*50}
SUBTOTAL:                    Rs.{subtotal:>8.2f}
TAX (5%):                    Rs.{tax_amount:>8.2f}
{'='*50}
TOTAL AMOUNT:                Rs.{total_amount:>8.2f}
{'='*50}

Thank you for dining with us!
Please visit again!
{'='*50}
"""
    
    # Display bill in text widget
    bill_text.insert(1.0, bill_content)
    
    # Update total display
    Total_Bill.set(f"Rs.{total_amount:.2f}")
    
    return bill_content

def open_print_window():
    """Open a new window with the bill formatted for printing"""
    menu_items = calculate_total()
    
    # Check if any item is ordered
    if all(item[2] == 0 for item in menu_items):
        messagebox.showwarning("No Items", "Please select at least one item!")
        return
    
    # Create new window for printing
    print_window = Toplevel(root)
    print_window.title("Bill - Ready for Print")
    print_window.geometry("600x800")
    print_window.configure(bg="white")
    
    # Make window modal
    print_window.transient(root)
    print_window.grab_set()
    
    # Create a frame for the bill content
    bill_frame = Frame(print_window, bg="white", padx=30, pady=30)
    bill_frame.pack(fill=BOTH, expand=True)
    
    # Get current date and time
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    
    # Restaurant header
    Label(bill_frame, text=RESTAURANT_NAME, font=("Arial", 18, "bold"), 
          bg="white", fg="black").pack(pady=(0, 5))
    
    Label(bill_frame, text="=" * 60, font=("Courier", 10), 
          bg="white", fg="black").pack()
    
    Label(bill_frame, text=RESTAURANT_ADDRESS, font=("Arial", 12), 
          bg="white", fg="black").pack(pady=2)
    
    Label(bill_frame, text=RESTAURANT_PHONE, font=("Arial", 12), 
          bg="white", fg="black").pack(pady=2)
    
    Label(bill_frame, text="=" * 60, font=("Courier", 10), 
          bg="white", fg="black").pack(pady=(5, 10))
    
    # Date and time
    Label(bill_frame, text=f"Date & Time: {date_time}", font=("Arial", 11, "bold"), 
          bg="white", fg="black").pack(pady=5)
    
    Label(bill_frame, text="=" * 60, font=("Courier", 10), 
          bg="white", fg="black").pack(pady=5)
    
    # Table header
    header_frame = Frame(bill_frame, bg="white")
    header_frame.pack(fill=X, pady=5)
    
    Label(header_frame, text="ITEM NAME", font=("Arial", 11, "bold"), 
          bg="white", fg="black", width=15, anchor="w").pack(side=LEFT)
    Label(header_frame, text="QTY", font=("Arial", 11, "bold"), 
          bg="white", fg="black", width=5).pack(side=LEFT)
    Label(header_frame, text="RATE", font=("Arial", 11, "bold"), 
          bg="white", fg="black", width=8).pack(side=LEFT)
    Label(header_frame, text="AMOUNT", font=("Arial", 11, "bold"), 
          bg="white", fg="black", width=10).pack(side=LEFT)
    
    Label(bill_frame, text="=" * 60, font=("Courier", 10), 
          bg="white", fg="black").pack()
    
    # Bill items
    subtotal = 0
    for item_name, price, qty in menu_items:
        if qty > 0:
            amount = price * qty
            subtotal += amount
            
            item_frame = Frame(bill_frame, bg="white")
            item_frame.pack(fill=X, pady=2)
            
            Label(item_frame, text=item_name, font=("Arial", 11), 
                  bg="white", fg="black", width=15, anchor="w").pack(side=LEFT)
            Label(item_frame, text=str(qty), font=("Arial", 11), 
                  bg="white", fg="black", width=5).pack(side=LEFT)
            Label(item_frame, text=f"Rs.{price}", font=("Arial", 11), 
                  bg="white", fg="black", width=8).pack(side=LEFT)
            Label(item_frame, text=f"Rs.{amount:.2f}", font=("Arial", 11), 
                  bg="white", fg="black", width=10).pack(side=LEFT)
    
    # Calculate taxes and total
    tax_rate = 0.05  # 5% tax
    tax_amount = subtotal * tax_rate
    total_amount = subtotal + tax_amount
    
    # Separator
    Label(bill_frame, text="=" * 60, font=("Courier", 10), 
          bg="white", fg="black").pack(pady=(10, 5))
    
    # Subtotal
    subtotal_frame = Frame(bill_frame, bg="white")
    subtotal_frame.pack(fill=X, pady=2)
    Label(subtotal_frame, text="SUBTOTAL:", font=("Arial", 12, "bold"), 
          bg="white", fg="black").pack(side=LEFT)
    Label(subtotal_frame, text=f"Rs.{subtotal:.2f}", font=("Arial", 12, "bold"), 
          bg="white", fg="black").pack(side=RIGHT)
    
    # Tax
    tax_frame = Frame(bill_frame, bg="white")
    tax_frame.pack(fill=X, pady=2)
    Label(tax_frame, text="TAX (5%):", font=("Arial", 12, "bold"), 
          bg="white", fg="black").pack(side=LEFT)
    Label(tax_frame, text=f"Rs.{tax_amount:.2f}", font=("Arial", 12, "bold"), 
          bg="white", fg="black").pack(side=RIGHT)
    
    # Final separator
    Label(bill_frame, text="=" * 60, font=("Courier", 10), 
          bg="white", fg="black").pack(pady=5)
    
    # Total
    total_frame = Frame(bill_frame, bg="white")
    total_frame.pack(fill=X, pady=5)
    Label(total_frame, text="TOTAL AMOUNT:", font=("Arial", 14, "bold"), 
          bg="white", fg="black").pack(side=LEFT)
    Label(total_frame, text=f"Rs.{total_amount:.2f}", font=("Arial", 14, "bold"), 
          bg="white", fg="black").pack(side=RIGHT)
    
    Label(bill_frame, text="=" * 60, font=("Courier", 10), 
          bg="white", fg="black").pack(pady=(5, 20))
    
    # Thank you message
    Label(bill_frame, text="Thank you for dining with us!", font=("Arial", 12, "bold"), 
          bg="white", fg="black").pack(pady=5)
    Label(bill_frame, text="Please visit again!", font=("Arial", 12, "bold"), 
          bg="white", fg="black").pack(pady=2)
    
    Label(bill_frame, text="=" * 60, font=("Courier", 10), 
          bg="white", fg="black").pack(pady=(10, 0))
    
    # Print and Close buttons
    button_frame = Frame(print_window, bg="white")
    button_frame.pack(pady=20)
    
    def print_bill_content():
        """Print the bill content"""
        try:
            # Create a temporary file for printing
            if not os.path.exists("bills"):
                os.makedirs("bills")
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"bills/bill_{timestamp}.txt"
            
            # Generate text content for file
            bill_content = generate_bill()
            
            with open(filename, 'w') as file:
                file.write(bill_content)
            
            # Try to print the file
            try:
                os.startfile(filename, "print")  # Windows
            except:
                try:
                    os.system(f"lpr {filename}")  # Linux/Unix
                except:
                    os.system(f"lp {filename}")  # Alternative Linux command
            
            messagebox.showinfo("Print", "Bill sent to printer!")
            
        except Exception as e:
            messagebox.showerror("Print Error", f"Could not print bill: {str(e)}")
    
    def save_and_close():
        """Save bill to file and close window"""
        try:
            if not os.path.exists("bills"):
                os.makedirs("bills")
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"bills/bill_{timestamp}.txt"
            
            bill_content = generate_bill()
            
            with open(filename, 'w') as file:
                file.write(bill_content)
            
            messagebox.showinfo("Saved", f"Bill saved as {filename}")
            print_window.destroy()
            
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save bill: {str(e)}")
    
    Button(button_frame, text="Print Bill", font=("Arial", 12, 'bold'), 
           bg="green", fg="white", width=12, command=print_bill_content).pack(side=LEFT, padx=10)
    
    Button(button_frame, text="Save & Close", font=("Arial", 12, 'bold'), 
           bg="blue", fg="white", width=12, command=save_and_close).pack(side=LEFT, padx=10)
    
    Button(button_frame, text="Close", font=("Arial", 12, 'bold'), 
           bg="red", fg="white", width=12, command=print_window.destroy).pack(side=LEFT, padx=10)
    
    # Also update the main bill display
    generate_bill()

def print_bill():
    """Generate and open print window"""
    open_print_window()

# Main header
Label(root, text="Restaurant Bill Management System", bg="darkblue", fg="white", 
      font=("Arial", 24, "bold"), width=50, height=2).pack(pady=10)

# Create main frames
main_frame = Frame(root, bg="lightgray")
main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

# MENU CARD Frame
menu_frame = Frame(main_frame, bg="yellow", highlightbackground="black", 
                   highlightthickness=2, width=400, height=400)
menu_frame.pack(side=LEFT, padx=10)
menu_frame.pack_propagate(False)

Label(menu_frame, text="MENU", font=("Arial", 24, "bold"), fg="darkred", 
      bg="yellow").pack(pady=10)

menu_items_display = [
    "Dosa ..................... Rs.40/-",
    "Puri ...................... Rs.40/-", 
    "Idli ....................... Rs.35/-",
    "Bonda .................. Rs.40/-",
    "Vada .................... Rs.40/-",
    "Tea ....................... Rs.10/-",
    "Coffee .................. Rs.15/-"
]

for item in menu_items_display:
    Label(menu_frame, font=("Courier", 12, 'bold'), text=item, 
          fg="black", bg="yellow").pack(pady=5)

# ORDER ENTRY Frame
entry_frame = Frame(main_frame, bd=5, relief=RAISED, bg="lightblue")
entry_frame.pack(side=LEFT, padx=10)

Label(entry_frame, text="Enter Quantities", font=("Arial", 16, "bold"), 
      bg="lightblue").grid(row=0, column=0, columnspan=2, pady=10)

# StringVar variables
dosa = StringVar()
puri = StringVar()
idli = StringVar()
bonda = StringVar()
vada = StringVar()
tea = StringVar()
coffee = StringVar()
Total_Bill = StringVar()

# Labels and Entry widgets
items = [
    ("Dosa", dosa),
    ("Puri", puri),
    ("Idli", idli),
    ("Bonda", bonda),
    ("Vada", vada),
    ("Tea", tea),
    ("Coffee", coffee)
]

entry_widgets = []
for i, (item_name, var) in enumerate(items, 1):
    Label(entry_frame, font=("Arial", 14, "bold"), text=item_name, 
          width=12, fg="darkblue", bg="lightblue").grid(row=i, column=0, padx=5, pady=5)
    
    entry = Entry(entry_frame, font=("Arial", 14, 'bold'), textvariable=var, 
                  bd=3, width=8, bg="white", justify=CENTER)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entry_widgets.append(entry)

# Store entry widgets for reset function
entry_dosa, entry_puri, entry_idli, entry_bonda, entry_vada, entry_tea, entry_coffee = entry_widgets

# Buttons
button_frame = Frame(entry_frame, bg="lightblue")
button_frame.grid(row=len(items)+1, column=0, columnspan=2, pady=20)

Button(button_frame, text="Generate Bill", font=("Arial", 12, 'bold'), 
       bg="green", fg="white", width=12, command=generate_bill).pack(side=LEFT, padx=5)

Button(button_frame, text="Print Bill", font=("Arial", 12, 'bold'), 
       bg="blue", fg="white", width=12, command=print_bill).pack(side=LEFT, padx=5)

Button(button_frame, text="Reset", font=("Arial", 12, 'bold'), 
       bg="red", fg="white", width=12, command=Reset).pack(side=LEFT, padx=5)

# Total display
total_frame = Frame(entry_frame, bg="lightblue")
total_frame.grid(row=len(items)+2, column=0, columnspan=2, pady=10)

Label(total_frame, text="Total Amount:", font=("Arial", 14, "bold"), 
      bg="lightblue").pack()
Entry(total_frame, font=("Arial", 16, 'bold'), textvariable=Total_Bill, 
      bd=3, width=15, bg="lightgreen", state="readonly", justify=CENTER).pack(pady=5)

# BILL DISPLAY Frame
bill_frame = Frame(main_frame, bg="white", highlightbackground="black", 
                   highlightthickness=2, width=400, height=400)
bill_frame.pack(side=RIGHT, padx=10)
bill_frame.pack_propagate(False)

Label(bill_frame, text="BILL RECEIPT", font=("Arial", 16, "bold"), 
      bg="white", fg="darkgreen").pack(pady=5)

# Text widget for bill display with scrollbar
text_frame = Frame(bill_frame)
text_frame.pack(fill=BOTH, expand=True, padx=10, pady=5)

bill_text = Text(text_frame, font=("Courier", 10), wrap=WORD, bg="white")
scrollbar = Scrollbar(text_frame, orient=VERTICAL, command=bill_text.yview)
bill_text.configure(yscrollcommand=scrollbar.set)

bill_text.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

root.mainloop()