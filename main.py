from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Saad Mazhar - Python Currency Converter')
root.geometry('500x500')

# Create Tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# Create two frames
curr_frame = Frame(my_notebook, width=480, height=480)
conv_frame = Frame(my_notebook, width=480, height=480)

curr_frame.pack(fill='both', expand=1)
conv_frame.pack(fill='both', expand=1)

# Add our tabs
my_notebook.add(curr_frame, text='Currencies')
my_notebook.add(conv_frame, text='Convert')

# Disable 2nd Tab
my_notebook.tab(1, state='disabled')

################################
# Currency Stuff
################################

def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning('WARNING!', "You have left some fields empty.")
    else:
        # disable entry boxes
        home_entry.config(state='disabled')
        conversion_entry.config(state='disabled')
        rate_entry.config(state='disabled')
        # enable tab
        my_notebook.tab(1, state='normal')
        # Change Tab fields
        amount_label.config(text=f'Amount of {home_entry.get()} To Convert To {conversion_entry.get()}')
        converted_label.config(text=f'Equals this many {conversion_entry.get()}')
        convert_button.config(text=f"Convert From {home_entry.get()}")

def unlock():
    # enable entry boxes
    home_entry.config(state='normal')
    conversion_entry.config(state='normal')
    rate_entry.config(state='normal')
    # Disable tab
    my_notebook.tab(1, state='disabled')


home = LabelFrame(curr_frame, text='Home Currency')
home.pack(pady=20)

# Home entry box
home_entry = Entry(home, font=('Helvetica', 24))
home_entry.pack(pady=10, padx=10)

# Conversion currency frame
conversion = LabelFrame(curr_frame, text='Conversion Currency')
conversion.pack(pady=20)

# convert to label
conversion_label = Label(conversion, text='Currency To Convert To:')
conversion_label.pack(pady=10)

# convert to entry
conversion_entry = Entry(conversion, font=('Helvetica', 24))
conversion_entry.pack(padx=10, pady=10)

# rate label
rate_label = Label(conversion, text='Current Conversion Rate:')
rate_label.pack(pady=10)

# rate entry
rate_entry = Entry(conversion, font=('Helvetica', 24))
rate_entry.pack(padx=10, pady=10)

# Button Frame
button_frame = Frame(curr_frame)
button_frame.pack(pady=20)

# Create Buttons
lock_button = Button(button_frame, text='Lock', command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text='Unlock', command=unlock)
unlock_button.grid(row=0, column=1, padx=10)

################################
# Conversion Stuff
################################

def convert():
    # Clear converted_entry
    converted_entry.delete(0, END)

    # Convert
    conversion = float(rate_entry.get()) * float(amount_entry.get())

    # Convert to two decimals
    conversion = round(conversion, 2)
    # add commas
    conversion = '{:,}'.format(conversion)

    # Update entry box
    converted_entry.insert(0, conversion)


def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)

amount_label = LabelFrame(conv_frame, text='Amount to Convert:')
amount_label.pack(pady=20)

# Entry box for amount
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

# Convert Button
convert_button = Button(amount_label, text='Convert', command=convert)
convert_button.pack(pady=20)

# Equals Frame
converted_label = LabelFrame(conv_frame, text = 'Converted Currency')
converted_label.pack(pady=20)

# Converted entry
converted_entry = Entry(converted_label, font=('Helvetica', 24), bd=0, bg='systembuttonface')
converted_entry.pack(pady=10, padx=10)

# Clear Button
clear_button = Button(conv_frame, text='Clear', command=clear)
clear_button.pack(pady=20)

# Fake Label for spacing
spacer = Label(conv_frame, text='', width = 68)
spacer.pack()


root.mainloop()