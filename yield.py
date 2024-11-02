import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Main window
root = tk.Tk()
root.title("Yield Calculator")
root.geometry("300x200")

# Functions
def calculate_yield():
    try:
        # Practical Yield
        riw = float(RIWE.get())
        pw = float(PWe.get())

        # Theoretical Yield
        rmw = float(RMWE.get())
        pmw = float(PMWE.get())
        a = ((pmw / rmw) * riw)

        # Percentage yield calculation
        d = ((pw / a) * 100)

        # Display the result
        messagebox.showinfo("Result", f"The percentage yield is: {d:.2f}%")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# UI elements
tk.Label(root, text="Initial Weight:").grid(row=0, column=0, padx=10, pady=5)
RIWE = tk.Entry(root)
RIWE.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Product Weight:").grid(row=1, column=0, padx=10, pady=5)
PWe = tk.Entry(root)
PWe.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Initial Product Mw:").grid(row=2, column=0, padx=10, pady=5)
RMWE = tk.Entry(root)
RMWE.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Final Product Mw:").grid(row=3, column=0, padx=10, pady=5)
PMWE = tk.Entry(root)
PMWE.grid(row=3, column=1, padx=10, pady=5)

# Calculate button
calc_button = ttk.Button(root, text="Calculate Yield", command=calculate_yield)
calc_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
