import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe - Python GUI")
current_player = "X"

# Create 3x3 board buttons
buttons = [[None for _ in range(3)] for _ in range(3)]

# Check for a win
def check_winner():
    for i in range(3):
        # Check rows and columns
        if (buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "") or \
           (buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != ""):
            return True
    # Check diagonals
    if (buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "") or \
       (buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != ""):
        return True
    return False

# Check for draw
def is_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

# Handle button click
def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        buttons[row][col]["state"] = "disabled"

        if check_winner():
            messagebox.showinfo("Game Over", f"🎉 Player {current_player} wins!")
            root.quit()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
        else:
            current_player = "O" if current_player == "X" else "X"

# Create buttons in grid
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                        command=lambda row=i, col=j: on_click(row, col))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

# Start GUI loop
root.mainloop()
