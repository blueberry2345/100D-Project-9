import math
import time
import tkinter
from tkinter import font


class DisappearingTest:
    def __init__(self, window):
        self.frame = tkinter.Frame()
        self.window = window
        self.time_label = tkinter.Label(window, text="",
                                        font=font.Font(family="Arial", size=12, weight="bold"), padx=20)
        self.button = tkinter.Button(window, command=self.start, width=15, height=2)
        self.input_box = tkinter.Text(window, width=100, height=10)
        self.time_of_last_change = time.time()
        self.button_label = tkinter.Label(text="Click button to start test.")
        self.text = ""
        self.test_on = False
        self.time_difference = 10
        self.background_colour = "#FFFFFF"
        self.background_colours = ["#FFFFFF", "#FFE5E5", "#FFCCCC", "#FFB2B2", "#FF9999", "#FF7F7F", "#FF6666",
                                   "#FF4C4C", "#FF3232", "#FF0000"]

    # Function updates timer and changes background colour depending on how much time remains. Empties input box if no interaction for 10 seconds.
    def update(self):
        current_time = time.time()
        if self.test_on:
            if self.input_box.get('1.0', 'end-1c') != self.text:
                self.time_of_last_change = current_time
            self.text = self.input_box.get('1.0', 'end-1c')
            self.time_difference = math.floor(current_time - self.time_of_last_change)
            self.window.configure(bg=self.background_colour)
            self.time_label.config(text=f"{10 - self.time_difference}s")
            if self.time_difference <= 10:
                self.background_colour = self.background_colours[self.time_difference]
                self.window.configure(bg=self.background_colour)
            else:

                self.test_on = False
                self.input_box.delete('1.0', 'end')
                self.background_colour = self.background_colours[0]
                self.window.configure(bg=self.background_colour)
        else:
            self.button_label.config(text="Click button to start test.")



        self.window.after(500, self.update)

    # Function starts new test or if a test is ongoing then it stops it.
    def start(self):
        self.test_on = self.test_on == False
        self.input_box.delete('1.0', 'end')
        self.time_of_last_change = time.time()
        self.button_label.config(text="Click button to finish test.")
