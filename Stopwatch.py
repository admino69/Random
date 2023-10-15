from tkinter import *
import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0

    def start(self):
        self.start_time = time.time()
        self.update_label()

    def stop(self):
        if self.start_time is not None:
            self.end_time = time.time()
            self.elapsed_time += self.end_time - self.start_time
            self.start_time = None

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0

    def update_label(self):
        if self.start_time is not None:
            elapsed_time = self.elapsed_time + (time.time() - self.start_time)
            rounded_time = round(elapsed_time,2)
            time_str = f"Time: {rounded_time} seconds"
            time_var.set(time_str)
            window.after(50, self.update_label)

stopwatch = Stopwatch()

window = Tk()
window.title("Stopwatch")

window.geometry("200x430")
window.resizable(False, False)

time_var = StringVar()
time_var.set("Time: 0.00 seconds")

label = Label(textvariable=time_var)
label.config(font=(50))
label.pack()

start_button = Button(window,text="Start", command=stopwatch.start)
start_button.config(font=("Cooper Black",50))
start_button.config(bg="#26ff00")
start_button.pack()

end_button = Button(window,text="Stop", command=stopwatch.stop)
end_button.config(font=("Cooper Black",50))
end_button.config(bg="#ff0000")
end_button.pack()

reset_button = Button(window,text="Reset", command=stopwatch.reset)
reset_button.config(font=("Cooper Black",50))
reset_button.config(bg="#ffff00")
reset_button.pack()

window.mainloop()