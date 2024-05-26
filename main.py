import tkinter
from disappearingtest import DisappearingTest

# Create window for application.
window = tkinter.Tk()
window.title("Speed-typing program")
window.minsize(width=750, height=500)
window.grid()

#Create DisappearingTest object.
test = DisappearingTest(window)

# Assign all tkinter objects of test object to grid.
test.frame.grid(row=0, column=0, padx=20, pady=20)
test.button_label.grid(row=0, column=2)
test.time_label.grid(row=1, column=1, padx=20)
test.input_box.grid(row=2, column=1, padx=20, rowspan=2, columnspan=2)
test.button.grid(row=1, column=2)

# Check for test update every 0.5 seconds.
window.after(500, test.update)

window.mainloop()
