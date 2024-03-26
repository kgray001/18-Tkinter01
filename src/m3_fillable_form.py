import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
form = tk.Tk()
form.title("Form")

name = tk.Label(
    form,
    text = "Name:",
    bg =  "#37799a",
    fg = "black" 
)
name.pack()
name_2 = tk.Entry(
    form
)
name_2.pack()

A1 = tk.Label(
    form,
    text = "Adress Line 1:",
    bg =  "#37799a",
    fg = "black" 
)
A1.pack()
A1_2 = tk.Entry(
    form
)
A1_2.pack()

A2 = tk.Label(
    form,
    text = "Address Line 2:",
    bg =  "#37799a",
    fg = "black" 
)
A2.pack()
A2_2 = tk.Entry(
    form
)
A2_2.pack()

city = tk.Label(
    form,
    text = "City:",
    bg =  "#37799a",
    fg = "black" 
)
city.pack()
city_2 = tk.Entry(
    form
)
city_2.pack()

state = tk.Label(
    form,
    text = "State:",
    bg =  "#37799a",
    fg = "black" 
)
state.pack()
state_2 = tk.Entry(
    form
)
state_2.pack()

zip = tk.Label(
    form,
    text = "Zip Code:",
    bg =  "#37799a",
    fg = "black" 
)
zip.pack()
zip_2 = tk.Entry(
    form
)
zip_2.pack()

number = tk.Label(
    form,
    text = "Phone Number:",
    bg =  "#37799a",
    fg = "black" 
)
number.pack()
number_2 = tk.Entry(
    form
)
number_2.pack()

email = tk.Label(
    form,
    text = "Email Address:",
    bg =  "#37799a",
    fg = "black" 
)
email.pack()
email_2 = tk.Entry(
    form
)
email_2.pack()

submit = tk.Button(
    form,
    text = "Submit",
    bg = "black",
    fg = "white"
)
submit.pack()

form.mainloop()