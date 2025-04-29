import tkinter as tk
from tkinter import messagebox
import math

def draw_polygon():
    try:
        sides = int(entry.get())
        if sides < 3 or sides > 20:
            raise ValueError("Number of sides must be between 3 and 20.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")
        return

    canvas.delete("all")
    width, height = 400, 400
    center_x, center_y = width // 2, height // 2
    radius = 150
    angle = 2 * math.pi / sides

    points = [
        (
            center_x + radius * math.cos(i * angle),
            center_y + radius * math.sin(i * angle)
        )
        for i in range(sides)
    ]

    canvas.create_polygon(points, outline="black", fill="lightblue", width=2)

# Create the main window
root = tk.Tk()
root.title("Geometric Figure Drawer")

# Input field and button
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Enter number of sides (3-20):").pack(side=tk.LEFT)
entry = tk.Entry(frame, width=5)
entry.pack(side=tk.LEFT)
tk.Button(frame, text="Draw", command=draw_polygon).pack(side=tk.LEFT)

# Canvas for drawing
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Run the application
root.mainloop()