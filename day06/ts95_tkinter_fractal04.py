import tkinter as tk
import random

def barnsley_fern(canvas, x, y, iterations):
    points = [(x, y)]
    for _ in range(iterations):
        x, y = points[-1]
        r = random.random()
        if r < 0.01:
            new_x = 0
            new_y = 0.16 * y
        elif r < 0.86:
            new_x = 0.85 * x + 0.04 * y
            new_y = -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            new_x = 0.2 * x - 0.26 * y
            new_y = 0.23 * x + 0.22 * y + 1.6
        else:
            new_x = -0.15 * x + 0.28 * y
            new_y = 0.26 * x + 0.24 * y + 0.44
        points.append((new_x, new_y))
    
    for px, py in points:
        canvas.create_oval(300 + px * 50, 550 - py * 50, 301 + px * 50, 551 - py * 50, fill='green', outline='green')

# 설정
root = tk.Tk()
root.title("Barnsley Fern Fractal")

canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack()

barnsley_fern(canvas, 0, 0, 40000)

root.mainloop()
