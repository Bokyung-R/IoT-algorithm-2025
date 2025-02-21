import tkinter as tk

def draw_sierpinski(canvas, x, y, size, depth):
    if depth == 0:
        canvas.create_polygon(
            x, y + size, 
            x + size / 2, y, 
            x + size, y + size, 
            outline='black', fill='', width=1
        )
        return
    
    new_size = size / 2
    draw_sierpinski(canvas, x, y + new_size, new_size, depth - 1)
    draw_sierpinski(canvas, x + new_size / 2, y, new_size, depth - 1)
    draw_sierpinski(canvas, x + new_size, y + new_size, new_size, depth - 1)

# 설정
root = tk.Tk()
root.title("Sierpinski Triangle Fractal")

canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack()

draw_sierpinski(canvas, 50, 50, 500, 7)

root.mainloop()
