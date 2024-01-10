import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

root = tk.Tk()
root.title('Matplotlib in Tkinter')

# Create a Matplotlib figure and subplot
fig, ax = plt.subplots()
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Matplotlib Plot')

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
ax.plot(x, y)

# Create a canvas widget to display Matplotlib plot
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

tk.mainloop()