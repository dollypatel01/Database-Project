#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dolly

refernences used: 
https://www.youtube.com/watch?v=gdDI_GhIRGo 
https://www.youtube.com/watch?v=5pFbjXdGXGg&list=PL2aJidc6QnyOGOhMM51cHsXWXmrTij6PW 
https://www.geeksforgeeks.org/python-sqlite-insert-data/ 
"""

import tkinter as tk
import sqlite3

# Create the main window
root = tk.Tk()
root.title("Hair Salon Database")

# Create the database connection
conn = sqlite3.connect("salondb1.db")

# Create a cursor to interact with the database
cursor = conn.cursor()

# CREATING TABLES
create_customer_query = '''CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY, 
    name TEXT, 
    phone TEXT, 
    email TEXT)'''
cursor.execute(create_customer_query)


create_stylist_query = '''CREATE TABLE IF NOT EXISTS stylists (
    id INTEGER PRIMARY KEY, 
    stylistname TEXT, 
    stylistsphone TEXT, 
    stylistemail TEXT)'''
cursor.execute(create_stylist_query)


create_service_query = '''CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY, 
    name TEXT, 
    price REAL)'''
cursor.execute(create_service_query)

create_appointment_query = '''CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY, 
    customer_id INTEGER, 
    stylist_id INTEGER, 
    service_id INTEGER, 
    date TEXT, 
    time TEXT, 
    FOREIGN KEY(customer_id) REFERENCES customers(id), 
    FOREIGN KEY(stylist_id) REFERENCES stylists(id), 
    FOREIGN KEY(service_id) REFERENCES services(id))'''
cursor.execute(create_appointment_query)
conn.commit()

# INSERTING DATA
def insert_customer():
    name = customer_name_entry.get()
    phone = customer_phone_entry.get()
    email = customer_email_entry.get()

    # Insert the data into the customers table
    insert_customer= '''
            INSERT INTO customers (name, phone, email) 
            VALUES (?, ?, ?)'''
    cursor.execute(insert_customer, (name, phone, email))
    #conn.commit()

    # Clear after inserting
    customer_name_entry.delete(0, tk.END)
    customer_phone_entry.delete(0, tk.END)
    customer_email_entry.delete(0, tk.END)

def insert_stylist():
    stylistname = stylist_name_entry.get()
    stylistphone = stylist_phone_entry.get()
    stylistemail = stylist_email_entry.get()

    # Insert the data into the stylists table
    insert_stylist= '''
                INSERT INTO stylists (stylistname, stylistsphone, stylistemail) 
                VALUES (?, ?, ?)'''
    cursor.execute(insert_stylist, (stylistname, stylistphone, stylistemail))
    #conn.commit()

    # Clear after inserting
    stylist_name_entry.delete(0, tk.END)
    stylist_phone_entry.delete(0, tk.END)
    stylist_email_entry.delete(0, tk.END)

def insert_service():
    name = service_name_entry.get()
    price = service_price_entry.get()

    # Insert the data into the services table
    insert_service= '''
                INSERT INTO services (name, price) 
                VALUES (?, ?)'''
    cursor.execute(insert_service, (name, price))
   # conn.commit()
    
    # Clear after inserting
    service_name_entry.delete(0, tk.END)
    service_price_entry.delete(0, tk.END)

def insert_appointment():
    customer_id = appointment_customer_entry.get()
    stylist_id = appointment_stylist_entry.get()
    service_id = appointment_service_entry.get()
    date = appointment_date_entry.get()
    time = appointment_time_entry.get()

    # Insert the data into the appointments table
    insert_appt= '''
                INSERT INTO appointments (customer_id, stylist_id, service_id, date, time) 
                VALUES (?, ?, ?, ?, ?)'''
    cursor.execute(insert_appt, (customer_id, stylist_id, service_id, date, time))
    conn.commit()

    # Clear after inserting
    appointment_customer_entry.delete(0, tk.END)
    appointment_stylist_entry.delete(0, tk.END)
    appointment_service_entry.delete(0, tk.END)
    appointment_date_entry.delete(0, tk.END)
    appointment_time_entry.delete(0, tk.END)

# Create the labels and entries for the customer
customer_name_label = tk.Label(root, text="Name:")
customer_name_label.grid(row=0, column=0)
customer_name_entry = tk.Entry(root)
customer_name_entry.grid(row=0, column=1)

customer_phone_label = tk.Label(root, text="Phone:")
customer_phone_label.grid(row=1, column=0)
customer_phone_entry = tk.Entry(root)
customer_phone_entry.grid(row=1, column=1)

customer_email_label = tk.Label(root, text="Email:")
customer_email_label.grid(row=2, column=0)
customer_email_entry = tk.Entry(root)
customer_email_entry.grid(row=2, column=1)

# Create the insert button for the customer 
customer_insert_button = tk.Button(root, text="Insert Customer", command=insert_customer)
customer_insert_button.grid(row=3, column=0, columnspan=2)

# Create the labels and entries for the stylist entity
stylist_name_label = tk.Label(root, text="Name:")
stylist_name_label.grid(row=4, column=0)
stylist_name_entry = tk.Entry(root)
stylist_name_entry.grid(row=4, column=1)

stylist_phone_label = tk.Label(root, text="Phone:")
stylist_phone_label.grid(row=5, column=0)
stylist_phone_entry = tk.Entry(root)
stylist_phone_entry.grid(row=5, column=1)

stylist_email_label = tk.Label(root, text="Email:")
stylist_email_label.grid(row=6, column=0)
stylist_email_entry = tk.Entry(root)
stylist_email_entry.grid(row=6, column=1)


# Create the insert button for the stylist 
stylist_insert_button = tk.Button(root, text="Insert Stylist", command=insert_stylist)
stylist_insert_button.grid(row=7, column=0, columnspan=2)

# Create the labels and entries for the service entity
service_name_label = tk.Label(root, text="Name:")
service_name_label.grid(row=8, column=0)
service_name_entry = tk.Entry(root)
service_name_entry.grid(row=8, column=1)

service_price_label = tk.Label(root, text="Price:")
service_price_label.grid(row=9, column=0)
service_price_entry = tk.Entry(root)
service_price_entry.grid(row=9, column=1)

# Create the insert button for the service 
service_insert_button = tk.Button(root, text="Insert Service", command=insert_service)
service_insert_button.grid(row=10, column=0, columnspan=2)

# Create the labels and entries for the appointment 
appointment_customer_label = tk.Label(root, text="Customer ID:")
appointment_customer_label.grid(row=11, column=0)
appointment_customer_entry = tk.Entry(root)
appointment_customer_entry.grid(row=11, column=1)

appointment_stylist_label = tk.Label(root, text="Stylist ID:")
appointment_stylist_label.grid(row=12, column=0)
appointment_stylist_entry = tk.Entry(root)
appointment_stylist_entry.grid(row=12, column=1)

appointment_service_label = tk.Label(root, text="Service ID:")
appointment_service_label.grid(row=13, column=0)
appointment_service_entry = tk.Entry(root)
appointment_service_entry.grid(row=13, column=1)

appointment_date_label = tk.Label(root, text="Date:")
appointment_date_label.grid(row=14, column=0)
appointment_date_entry = tk.Entry(root)
appointment_date_entry.grid(row=14, column=1)

appointment_time_label = tk.Label(root, text="Time:")
appointment_time_label.grid(row=15, column=0)
appointment_time_entry = tk.Entry(root)
appointment_time_entry.grid(row=15, column=1)

# Create the insert button for the appointment 
appointment_insert_button = tk.Button(root, text="Insert Appointment", command=insert_appointment)
appointment_insert_button.grid(row=16, column=0, columnspan=2)

# Run the main loop to display the GUI
root.mainloop()

# Close the database connection when the program is closed
conn.close()
