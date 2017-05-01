import tkinter as TK
from tkinter import Button, Label, Entry, messagebox
from datetime import datetime
from dateutil import relativedelta

# procedure for centering window
def center_window(width=600, height=400):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


# open root window
root = TK.Tk()
center_window(400, 350)
root.geometry("400x350")
root.resizable(0, 0)
title = Label(root, text = "Date Calculator", font="30").place(x = 130, y = 10)

def instructions():
	messagebox.showinfo("Help","Enter values for the future year, month, and date")
	
def calculate():
	
	# get current year, month, day
	current_time = datetime.now()
	current_year = str(current_time.year)
	current_month = str(current_time.month)
	current_day = str(current_time.day)
	
	try:
		# test a valid input that is not null and positive
		date_input = year_entry.get() + "-" + month_entry.get() + "-" + day_entry.get()
		current_date = current_year + "-" + current_month + "-" + current_day
		date1 = datetime.strptime(str(current_date), '%Y-%m-%d')
		date2 = datetime.strptime(str(date_input), '%Y-%m-%d')
		r = relativedelta.relativedelta(date2, date1)
	except:
		messagebox.showinfo("Error","Please enter a valid date")
	else:
		# convert dates for strptime format
		date_input = year_entry.get() + "-" + month_entry.get() + "-" + day_entry.get()
		current_date = current_year + "-" + current_month + "-" + current_day
		
		# compute difference
		date1 = datetime.strptime(str(current_date), '%Y-%m-%d')
		date2 = datetime.strptime(str(date_input), '%Y-%m-%d')
		r = relativedelta.relativedelta(date2, date1)
	
		# update labels if the date is in the future
		if date1 < date2:
			years_until.set("Years Until: " + str(r.years))  
			months_until.set("Months Until: " + str(r.months))  
			days_until.set("Days Until: " + str(r.days))  
		else:
			messagebox.showinfo("Error", "Please enter a valid date")

# labels for entries
year_label = Label(root, text="Enter Year:").place(x=20, y=75)
month_label = Label(root, text="Enter Month:").place(x=20, y=125)
day_label = Label(root, text="Enter Day:").place(x=20, y=175)

# output
months_until = TK.StringVar()
months_until.set("Months Until: ")
months_until_label = Label(root, textvariable = months_until).place(x = 250, y = 75)

years_until = TK.StringVar()
years_until.set("Years Until: ")
years_until_label = Label(root, textvariable = years_until).place(x = 250, y = 125)

days_until = TK.StringVar()
days_until.set("Days Until: ")
days_until_label = Label(root, textvariable = days_until).place(x = 250, y = 175)

# entry boxes
year_entry = Entry(root, width="10")
year_entry.place(x=95, y=75)
month_entry = Entry(root, width="10")
month_entry.place(x=95, y=125)
day_entry = Entry(root, width="10")
day_entry.place(x=95, y=175)

# submit, close, help buttons
submit = Button(root, text="Submit", command = calculate, padx=20, pady=10).place(x=160, y=305)
close = Button(root, text="Close", command=quit, padx=20, pady=10).place(x=321, y=305)
instructions = Button(root, text="Help", command=instructions, padx=20, pady=10).place(x=1, y=305)

root.mainloop()
