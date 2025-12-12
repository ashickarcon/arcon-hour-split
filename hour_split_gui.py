import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        hours = int(entry_hours.get())
        days = int(entry_days.get())
        h1 = int(entry_option1.get())
        h2_input = entry_option2.get()
    except:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        return

    output.delete("1.0", tk.END)

    if h2_input.strip() == "":
        found = False
        for h2 in range(2, 9):  # Try for 2 to 8 hours
            for x in range(days + 1):
                y = days - x
                total = x * h1 + y * h2
                if total == hours:
                    found = True
                    output.insert(tk.END, f"• {x} days of {h1} hours\n")
                    output.insert(tk.END, f"• {y} days of {h2} hours\n\n")
                    output.insert(tk.END, "Breakdown:\n")
                    output.insert(tk.END, f"• {x} × {h1} = {x*h1} hours\n")
                    output.insert(tk.END, f"• {y} × {h2} = {y*h2} hours\n")
                    output.insert(tk.END, f"\n• Total = {x*h1} + {y*h2} = {total} hours ✅\n")
                    output.insert(tk.END, "-"*35 + "\n")
        if not found:
            output.insert(tk.END, "❌ No valid combinations found (2-8 hours tried for Option 2).\n")
    else:
        try:
            h2 = int(h2_input)
        except:
            messagebox.showerror("Input Error", "Hour Option 2 must be a number or left blank.")
            return

        results_found = False
        for x in range(days + 1):
            y = days - x
            total = x * h1 + y * h2
            if total == hours:
                results_found = True
                output.insert(tk.END, f"• {x} days of {h1} hours\n")
                output.insert(tk.END, f"• {y} days of {h2} hours\n\n")
                output.insert(tk.END, "Breakdown:\n")
                output.insert(tk.END, f"• {x} × {h1} = {x*h1} hours\n")
                output.insert(tk.END, f"• {y} × {h2} = {y*h2} hours\n")
                output.insert(tk.END, f"\n• Total = {x*h1} + {y*h2} = {total} hours ✅\n")
                output.insert(tk.END, "-"*35 + "\n")
        if not results_found:
            output.insert(tk.END, "❌ No valid combinations found.\n")

def clear_all():
    """Clear all inputs and output."""
    entry_hours.delete(0, tk.END)
    entry_days.delete(0, tk.END)
    entry_option1.delete(0, tk.END)
    entry_option2.delete(0, tk.END)
    output.delete("1.0", tk.END)

# GUI Setup
app = tk.Tk()
app.title("Arcon Hour Split")
app.iconbitmap("icon.ico")

# Input fields
tk.Label(app, text="Total Hours:").grid(row=0, column=0)
tk.Label(app, text="Total Days:").grid(row=1, column=0)
tk.Label(app, text="Hour Option 1:").grid(row=2, column=0)
tk.Label(app, text="Hour Option 2 (optional):").grid(row=3, column=0)

entry_hours = tk.Entry(app)
entry_days = tk.Entry(app)
entry_option1 = tk.Entry(app)
entry_option2 = tk.Entry(app)

entry_hours.grid(row=0, column=1)
entry_days.grid(row=1, column=1)
entry_option1.grid(row=2, column=1)
entry_option2.grid(row=3, column=1)

# Buttons
tk.Button(app, text="Calculate", command=calculate).grid(row=4, column=0, pady=10)
tk.Button(app, text="Clear", command=clear_all).grid(row=4, column=1, pady=10)

# Output display
output = tk.Text(app, height=15, width=50, font=("Segoe UI", 10))
output.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
