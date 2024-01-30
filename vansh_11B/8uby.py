import tkinter as tk
def on_drag(event):
    """Updates button position based on mouse drag."""
    x = event.x - btn.winfo_width() // 2
    y = event.y - btn.winfo_height() // 2
    btn.place(x=x, y=y)

def on_click(event):
    """Binds mouse drag event to button click."""
    btn.bind("<B1-Motion>", on_drag)

def release_drag(event):
    """Unbinds mouse drag event on button release."""
    btn.unbind("<B1-Motion>")
root = tk.Tk()
root.geometry("300x250")

btn = tk.Button(root, text="Click and drag to move!")
btn.place(x=50, y=50)

btn.bind("<Button-1>", on_click)  # Bind click event
btn.bind("<ButtonRelease-1>", release_drag)  # Bind release event
root.mainloop()
