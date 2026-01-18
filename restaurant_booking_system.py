import csv
from tkinter import *
from tkinter import messagebox
from datetime import datetime

def readcsv(file):
    info=[]
    with open(file,newline="") as csvfile:
        csvreader=csv.DictReader(csvfile)
        
        for row in csvreader:
            info.append(row)
    return info

def writecsv(files,data):
    with open(files,'w',newline='') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerows(data)

names=readcsv("/Users/dakshasg/Desktop/game/restaurants.csv")

class restaurant:
    def __init__(self,restaurant_id,name,cuisine,rating,location,total_tables,total_configuration,opening_hours,closing_hours):
        self.restaurant_id=restaurant_id
        self.name=name
        self.cuisine=cuisine
        self.rating=rating
        self.location=location
        self.total_tables=total_tables
        self.total_configuration=total_configuration
        self.opening_hours=opening_hours
        self.closing_hours=closing_hours
    
    def get_available_tables(self,date,time,party_size):
        booking=readcsv("/Users/dakshasg/Desktop/game/bookings.csv")
        
        booked=set()
        for i in booking:
            if i['date']==date and i['time']==time:
                booked.add(i['table_id'])
        s=set(range(1,self.total_tables+1))
        available=s.difference(booked)
        return available
    
    def display(self):
        x=(f"{self.name} ({self.cuisine})- ratings:{self.rating},Location:{self.location},Duration:{self.opening_hours} to {self.closing_hours}")
        return x     
    
    def check_validity_booking_time(self,time):
        opens=datetime.strptime(self.opening_hours,'%I:%M:%p')
        close=datetime.strptime(self.closing_hours,'%I:%M:%p')
        booking_time=datetime.strptime(time,'%I:%M:%p')
        return opens<=booking_time<=close

people=readcsv("/Users/dakshasg/Desktop/game/bookings.csv")

class user:
    def __init__(self,name,email,phone_number):
        self.name=name
        self.email=email
        self.phone_number=phone_number
        self.current_bookings=[]
    
    def make_reservation(self,restaurant_id,date,time,table_id,party_size):
        book=readcsv("/Users/dakshasg/Desktop/game/bookings.csv")
        booking_id=len(book)+1
        new_booking={'booking_id':booking_id, 'restaurant_id':restaurant_id,'date':date,'time':time,'party_size':party_size,'table_id':table_id}
        book.append(new_booking)
        writecsv("/Users/dakshasg/Desktop/game/bookings.csv",[list(new_booking.keys())] + [list(b.values()) for b in book])
        self.current_bookings.append(new_booking)
        return f"your booking confirmed and your booking id is {booking_id}"
    
    def cancel(self,booking_id):
        book=readcsv("/Users/dakshasg/Desktop/game/bookings.csv")
        cancel=[d for d in book if int(d['booking_id'])!=booking_id]
        writecsv("/Users/dakshasg/Desktop/game/bookings.csv",cancel)
        self.current_bookings=[d for d in self.current_bookings if int(d['booking_id'])!=booking_id]
        return f"your booking i.e {booking_id} is canceled"
    
    def view_booking_history(self):
        return self.current_bookings

# GUI Setup
wn=Tk()
wn.title("Restaurant Booking System")
wn.geometry("1000x700")

l1=Label(wn,text="Restaurants :").place(x=400,y=60)
menu = StringVar()
menu.set("Restaurants")

show=[i['name'] for i in names]

def detail(show):
    for i in names:
        if menu.get() == i['name']:
            details = "\n".join([f"{key}: {value}" for key, value in i.items()])
            messagebox.showinfo(f"You selected {i['name']}", details)

drop=OptionMenu(wn,menu,*show)
drop.place(x=500,y=60)
b=Button(wn,text="OK",command=lambda :detail(show))
b.place(x=450,y=100)

l2=Label(wn,text="search for restaurants :")
l2.place(x=340,y=140)
e1=Entry(wn)
e1.place(x=520,y=140)

def search(show):
    for i in names:
        if str(e1.get()).lower() == i['name'].lower():
            details = "\n".join([f"{key}: {value}" for key, value in i.items()])
            messagebox.showinfo(f"You selected {i['name']}", details)

b1=Button(wn,text="search",command=lambda :search(show))
b1.place(x=480,y=170)

# Filter by cuisine
menu1 = StringVar()
menu1.set("Cuisine")
cuisine=[i['cuisine_type'] for i in names]

def detail1(cuisine):
    fc=[j['name'] for j in names if menu1.get() == j['cuisine_type']]
    details1 = "\n".join(fc)
    l3=Label(wn,text=details1)
    l3.place(x=400,y=260)

drop1=OptionMenu(wn,menu1,*cuisine)
drop1.place(x=370,y=230)
b3=Button(wn,text="OK",command=lambda :detail1(cuisine))
b3.place(x=500,y=220)

# Time input
l4=Label(wn,text="time (HH:mm)")
l4.place(x=340,y=260)
e2=Entry(wn)
e2.place(x=420,y=260)

# Date input
l5=Label(wn,text="Date (YYYY-MM-DD) :")
l5.place(x=340,y=340)
e3=Entry(wn)
e3.place(x=420,y=340)

# Party size input
l6=Label(wn,text="Party size :")
l6.place(x=340,y=390)
e4=Entry(wn)
e4.place(x=420,y=390)

# Table id input
l7=Label(wn,text="Table id :")
l7.place(x=340,y=440)
e5=Entry(wn)
e5.place(x=420,y=440)

def check_table():
    try:
        table_id = e5.get()
        date = e3.get()
        time = e2.get()
        
        for j in people:
            if j['date']==date and j['time']==time and j['table_id']==table_id:
                messagebox.showinfo("Table Status", f"Table {table_id} is already reserved at this time")
                return
        messagebox.showinfo("Table Status", "Table is available. Continue with your reservation process")
    except Exception as e:
        messagebox.showerror("Error", f"Error checking table: {str(e)}")

b4=Button(wn,text="Check",command=check_table)
b4.place(x=450,y=480)

# Customer info labels and inputs
l8=Label(wn,text="Customer Name :")
l8.place(x=340,y=520)
e6=Entry(wn)
e6.place(x=420,y=520)

l9=Label(wn,text="Email:")
l9.place(x=340,y=560)
e7=Entry(wn)
e7.place(x=420,y=560)

l11=Label(wn,text="Phone Number :")
l11.place(x=340,y=600)
e8=Entry(wn)
e8.place(x=420,y=600)

def book_reservation():
    try:
        use = user(e6.get(), e7.get(), e8.get())
        result = use.make_reservation(menu.get(), e3.get(), e2.get(), int(e5.get()), int(e4.get()))
        messagebox.showinfo("Booking Confirmed", result)
    except Exception as e:
        messagebox.showerror("Error", f"Booking failed: {str(e)}")

b5=Button(wn,text="Book",command=book_reservation)
b5.place(x=450,y=640)

wn.mainloop()
