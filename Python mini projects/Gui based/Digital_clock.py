import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("350x150")
root.resizable(False, False)
root.configure(bg="black")

# Define the label to display the time
clock_label = tk.Label(root, font=("Arial", 48), bg="black", fg="cyan")
clock_label.pack(pady=20)

# Update time function
def update_time():
    current_time = strftime("%H:%M:%S")  
    clock_label.config(text=current_time)
    root.after(1000, update_time)  

# Start the clock
update_time()

# Run the GUI loop
root.mainloop()
