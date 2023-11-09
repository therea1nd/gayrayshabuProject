from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import time
import sqlite3
import cv2
import numpy as np
from io import BytesIO
import qrcode
from datetime import datetime
import requests
import re
import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

conn = sqlite3.connect("GAYSHABU2.db")
cursor = conn.cursor()


totalpriceWindow = None
stockWindow = None
entry_username = None
totalselect = []

# total_price = None
def first_page():
    global firstpageWindow
    
    firstpageWindow = tk.Tk()
    firstpageWindow.title("หน้าแรก")
    firstpageWindow.geometry("1600x900+100+10")
    img = Image.open("PAGE1.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(image=photo)
    lbl.place(x=0,y=0)
    table1_img = Image.open("fristBT.png")
    table1_photo = ImageTk.PhotoImage(table1_img)
    table1 = tk.Button(firstpageWindow, image=table1_photo, bd=0,command=main_page, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    table1.place(x=560,y=470)
    table1.image = table1_photo
    
    def update_clock():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        clock.config(text=current_time)
        firstpageWindow.after(1000, update_clock) # เรียกใช้ฟังก์ชันเองทุก 1 วินาที
        
    clock = Label(firstpageWindow, font=('calibri', 40, 'bold'), bg='#fa5601', fg='white')
    clock.place(x=50, y=50)
    update_clock()
    
    def show_date():
        now = datetime.now()
        current_year = now.strftime("%m-%Y")
        date_label.config(text=current_year)
        firstpageWindow.after(1000, show_date)  # เรียกใช้ฟังก์ชันเองทุก 1 วินาที

    date_label = Label(firstpageWindow, font=('calibri', 40, 'bold'), bg='#fa5601', fg='white')
    date_label.place(x=370, y=50)
    show_date()
    
    def show_date():
        now = datetime.now()
        current_day = now.strftime("%d-")
        date_label2.config(text=current_day)
        firstpageWindow.after(1000, show_date)  # เรียกใช้ฟังก์ชันเองทุก 1 วินาที

    date_label2 = Label(firstpageWindow, font=('calibri', 40, 'bold'), bg='#fa5601', fg='white')
    date_label2.place(x=300, y=50)
    show_date()

    firstpageWindow.mainloop()
    
def main_page():
    global mainpageWindow
    firstpageWindow.withdraw()
    mainpageWindow = tk.Toplevel()
    mainpageWindow.title("หน้าหลัก")
    mainpageWindow.geometry("1600x900+100+10")
    img = Image.open("PAGE2.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(mainpageWindow, image=photo)
    lbl.image = photo  # Prevent the image from being garbage collected
    lbl.place(x=0, y=0)
    
    def update_clock():
        try:
            current_time = time.strftime('%H:%M:%S')
            clock.config(text=current_time)
        except Exception as e:
            print(f"An error occurred: {e}")
        
    clock = Label(mainpageWindow, font=('calibri', 40, 'bold'), bg='#fa5601', fg='white')
    clock.place(x=50, y=50)
    update_clock()

    
    table1_img = Image.open("LOOKCARBT.png")
    table1_photo = ImageTk.PhotoImage(table1_img)
    table1 = tk.Button(mainpageWindow, image=table1_photo,command=user_login, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    table1.place(x=369,y=405)
    table1.image = table1_photo
    table2_img = Image.open("ADMINBT.png")
    table2_photo = ImageTk.PhotoImage(table2_img)
    table2 = tk.Button(mainpageWindow, image=table2_photo,command=login_admin, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    table2.place(x=950,y=405)
    table2.image = table2_photo
    
    left_img = Image.open("LEFTBT.png")
    left_photo = ImageTk.PhotoImage(left_img)
    left = tk.Button(mainpageWindow, image=left_photo,command=first_page, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    left.place(x=26,y=774)
    left.image = left_photo
    
    mainpageWindow.mainloop()
    
def login_admin():
    global loginadminWindow
    if mainpageWindow and mainpageWindow.winfo_exists():
        mainpageWindow.destroy()
    elif AdminMenuWindow and AdminMenuWindow.winfo_exists():
        AdminMenuWindow.destroy()
    loginadminWindow = tk.Toplevel()
    loginadminWindow.title("หน้าล็อกอินแอดมิน")
    loginadminWindow.geometry("1600x900+100+10")
    img = Image.open("PAGEADMINLOGIN.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(loginadminWindow, image=photo)
    lbl.image = photo  # Prevent the image from being garbage collected
    lbl.place(x=0, y=0)
    
    def validate_input():
        username = entry_username.get()
        password = entry_password.get()
        if username == "admin" and password == "admin":
            messagebox.showinfo("Success", "Login Successful!")
            Admin_Menu()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")
    
    entry_username = tk.Entry(loginadminWindow)
    entry_username.place(x=626, y=339, width=700, height=150)
    entry_username.configure(font=("DBHelvethaicaX-LiExt", 76), fg="#CE6857", bg="#ffffff", bd=0, relief="flat")

    entry_password = tk.Entry(loginadminWindow)
    entry_password.place(x=626, y=596, width=700, height=150)
    entry_password.configure(font=("DBHelvethaicaX-LiExt", 76), fg="#CE6857", bg="#ffffff", bd=0, relief="flat",show="*")
    
    left_img = Image.open("LEFTBT.png")
    left_photo = ImageTk.PhotoImage(left_img)
    left = tk.Button(loginadminWindow, image=left_photo,command=main_page, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    left.place(x=26,y=774)
    left.image = left_photo
    
    right_img = Image.open("RIGHTBT.png")
    right_photo = ImageTk.PhotoImage(right_img)
    right = tk.Button(loginadminWindow, image=right_photo,command=validate_input, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    right.place(x=1456,y=769)
    right.image = right_photo
    
    loginadminWindow.mainloop()

def Admin_Menu():
    global AdminMenuWindow
    if loginadminWindow and loginadminWindow.winfo_exists():
        loginadminWindow.destroy()
    elif totalpriceWindow and totalpriceWindow.winfo_exists():
        totalpriceWindow.destroy()
    elif stockWindow and stockWindow.winfo_exists():
        stockWindow.destroy()
    elif infocostomerWindow and infocostomerWindow.winfo_exists():
        infocostomerWindow.destroy()
    AdminMenuWindow = tk.Toplevel()
    AdminMenuWindow.title("หน้าหลักแอดมิน")
    AdminMenuWindow.geometry("1600x900+100+10")
    img = Image.open("ADMINMAINMENU.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(AdminMenuWindow, image=photo)
    lbl.image = photo  # Prevent the image from being garbage collected
    lbl.place(x=0, y=0)
    
    table1_img = Image.open("RaidaiBT.png")
    table1_photo = ImageTk.PhotoImage(table1_img)
    table1 = tk.Button(AdminMenuWindow, image=table1_photo,command=total_price, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    table1.place(x=209,y=405)
    table1.image = table1_photo

    table2_img = Image.open("SatokBT.png")
    table2_photo = ImageTk.PhotoImage(table2_img)
    table2 = tk.Button(AdminMenuWindow, image=table2_photo,command=stock, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    table2.place(x=593,y=381)
    table2.image = table2_photo

    table3_img = Image.open("InfoBT.png")
    table3_photo = ImageTk.PhotoImage(table3_img)
    table3 = tk.Button(AdminMenuWindow, image=table3_photo,command=info_costomer, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    table3.place(x=1109,y=405)
    table3.image = table3_photo
    
    left_img = Image.open("LEFTBT.png")
    left_photo = ImageTk.PhotoImage(left_img)
    left = tk.Button(AdminMenuWindow, image=left_photo,command=login_admin, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    left.place(x=26,y=774)
    left.image = left_photo
    
    AdminMenuWindow.mainloop()
    
def total_price():
    global totalpriceWindow
    if AdminMenuWindow and AdminMenuWindow.winfo_exists():
        AdminMenuWindow.destroy()
    totalpriceWindow = tk.Toplevel()
    totalpriceWindow.title("หน้ารายได้")
    totalpriceWindow.geometry("1600x900+100+10")
    img = Image.open("RAIDAIPAGE.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(totalpriceWindow, image=photo)
    lbl.image = photo  # Prevent the image from being garbage collected
    lbl.place(x=0, y=0)
    
    table1_img = Image.open("PajumwanBT.png")
    table1_photo = ImageTk.PhotoImage(table1_img)
    table1 = tk.Button(totalpriceWindow, image=table1_photo,command=total_price_day, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    table1.place(x=535,y=315)
    table1.image = table1_photo
    table2_img = Image.open("AllraidaiBT.png")
    table2_photo = ImageTk.PhotoImage(table2_img)
    table2 = tk.Button(totalpriceWindow, image=table2_photo,command=total_price_all, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    table2.place(x=555,y=516)
    table2.image = table2_photo
    
    left_img = Image.open("LEFTBT.png")
    left_photo = ImageTk.PhotoImage(left_img)
    left = tk.Button(totalpriceWindow, image=left_photo,command=Admin_Menu, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    left.place(x=26,y=774)
    left.image = left_photo
    
    totalpriceWindow.mainloop()
    
def total_price_day():
    global totalpricedayWindow
    if totalpriceWindow and totalpriceWindow.winfo_exists():
        totalpriceWindow.destroy()
    totalpricedayWindow = tk.Toplevel()
    totalpricedayWindow.title("หน้าหลัก")
    totalpricedayWindow.geometry("1600x900+100+10")
    img = Image.open("PAGEPajumwan.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(totalpricedayWindow, image=photo)
    lbl.image = photo  # Prevent the image from being garbage collected
    lbl.place(x=0, y=0)
    
    entry_day = tk.Entry(totalpricedayWindow)
    entry_day.place(x=426, y=339, width=700, height=150)
    entry_day.configure(font=("DBHelvethaicaX-LiExt", 76), fg="#CE6857", bg="#ffffff", bd=0, relief="flat")
    

    def day_price_select():
        day = entry_day.get()
        cursor.execute("SELECT SUM(Price) FROM allusecelect WHERE day = ?", (day,))
        daydata = cursor.fetchall()
        print(daydata)
        
        label = tk.Label(totalpricedayWindow,text=f"ราคารวมทั้งสิ้น {daydata[0][0]} บาท" , font=("DBHelvethaicaX-LiExt", 50), bg="white", fg="black")
        label.place(x=700, y=720)
        
    tk.Button(totalpricedayWindow, text="Update",font=("DBHelvethaicaX-LiExt", 30), command=day_price_select).place(x=1200, y=350)    

    
    
    left_img = Image.open("LEFTBT.png")
    left_photo = ImageTk.PhotoImage(left_img)
    left = tk.Button(totalpricedayWindow, image=left_photo,command=total_price, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    left.place(x=26,y=774)
    left.image = left_photo
    
        
    
    totalpricedayWindow.mainloop()
    
def total_price_all():
    global totalpriceallWindow
    if totalpriceWindow and totalpriceWindow.winfo_exists():
        totalpriceWindow.destroy()
    totalpriceallWindow = tk.Toplevel()
    totalpriceallWindow.title("หน้าหลัก")
    totalpriceallWindow.geometry("1600x900+100+10")
    img = Image.open("PAGEAllraidai.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(totalpriceallWindow, image=photo)
    lbl.image = photo  # Prevent the image from being garbage collected
    lbl.place(x=0, y=0)
    
    entry_day = tk.Entry(totalpriceallWindow)
    entry_day.place(x=426, y=339, width=700, height=150)
    entry_day.configure(font=("DBHelvethaicaX-LiExt", 76), fg="#CE6857", bg="#ffffff", bd=0, relief="flat")
    
    def day_price_select():
        day = entry_day.get()
        cursor.execute("SELECT SUM(Price) FROM allusecelect WHERE year = ?", (day,))
        daydata = cursor.fetchall()
        print(daydata)
        
        label = tk.Label(totalpriceallWindow,text=f"ราคารวมทั้งสิ้น {daydata[0][0]} บาท" , font=("DBHelvethaicaX-LiExt", 50), bg="white", fg="black")
        label.place(x=700, y=720)
        
    tk.Button(totalpriceallWindow, text="Update",font=("DBHelvethaicaX-LiExt", 30), command=day_price_select).place(x=1200, y=350)    
    
    left_img = Image.open("LEFTBT.png")
    left_photo = ImageTk.PhotoImage(left_img)
    left = tk.Button(totalpriceallWindow, image=left_photo,command=total_price, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    left.place(x=26,y=774)
    left.image = left_photo
    totalpriceallWindow.mainloop()
    
def stock():
    global stockWindow
    if AdminMenuWindow and AdminMenuWindow.winfo_exists():
        AdminMenuWindow.destroy()
    stockWindow = tk.Toplevel()
    stockWindow.title("หน้าหลัก")
    stockWindow.geometry("1600x900+100+10")
    img = Image.open("PAGEstock.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(stockWindow, image=photo)
    lbl.image = photo  # Prevent the image from being garbage collected
    lbl.place(x=0, y=0)
    
    left_img = Image.open("LEFTBT.png")
    left_photo = ImageTk.PhotoImage(left_img)
    left = tk.Button(stockWindow, image=left_photo,command=Admin_Menu, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    left.place(x=26,y=774)
    left.image = left_photo
    
    listbox = tk.Listbox(stockWindow, width=80, font=("DBHelvethaicaX-LiExt", 15), fg="#CE6857", bg="#ffffff", bd=0, relief="flat")
    listbox.place(x=100, y=350)
   
    def on_select(event):
        selected_item = listbox.get(listbox.curselection())
        item_id = selected_item.split('id = ')[1].split()[0]  # Extract the id from the selected_item
        print(f"Selected Item: {selected_item}")
        edit_item(item_id)  # Pass the id to the edit_item function

    listbox.bind('<<ListboxSelect>>', on_select)

# Rest of your code remains the same

    def edit_item(item_id):
        global new_entry
        new_entry = tk.Entry(stockWindow, font=("DBHelvethaicaX-LiExt", 25))
        new_entry.place(x=1200, y=400, width=300, height=150)
        new = new_entry.get()
        print(f"Editing {item_id}")

        def update_item(item_id):
            new = new_entry.get()
            print(new)
            listbox.delete(0, tk.END)
            cursor.execute("UPDATE Menu SET total = ? WHERE id = ?", (new, item_id))
            
            cursor.execute("SELECT * FROM Menu")
            rows = cursor.fetchall()

            for row in rows:
                
                listbox.insert(tk.END, f"id = {row[0]}    Menu = {row[1]}    Price = {row[2]}    จำนวน = {row[3]}")


            conn.commit()
      
        tk.Button(stockWindow, text="Update", command=lambda: update_item(item_id)).place(x=1400, y=450)



    # Fetch data from the "Menu" table
    cursor.execute("SELECT * FROM Menu")
    rows = cursor.fetchall()

    for row in rows:
        listbox.insert(tk.END, f"id = {row[0]}    Menu = {row[1]}    Price = {row[2]}    จำนวน = {row[3]}")


   
    stockWindow.mainloop()    
    
curreny_time = None
    
def info_costomer():
    global infocostomerWindow
    if AdminMenuWindow and AdminMenuWindow.winfo_exists():
        AdminMenuWindow.destroy()
    infocostomerWindow = tk.Toplevel()
    infocostomerWindow.title("หน้าหลัก")
    infocostomerWindow.geometry("1600x900+100+10")
    img = Image.open("PAGElookcar.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(infocostomerWindow, image=photo)
    lbl.image = photo  # Prevent the image from being garbage collected
    lbl.place(x=0, y=0)
    
    left_img = Image.open("LEFTBT.png")
    left_photo = ImageTk.PhotoImage(left_img)
    left = tk.Button(infocostomerWindow, image=left_photo,command=Admin_Menu, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    left.place(x=26,y=774)
    left.image = left_photo

    listbox = tk.Listbox(infocostomerWindow, width=80, font=("DBHelvethaicaX-LiExt", 15), fg="#CE6857", bg="#ffffff", bd=0, relief="flat")
    listbox.place(x=250, y=350)

    def on_select(event):
        selected_item = listbox.get(listbox.curselection())
        item_id = selected_item.split('id = ')[1].split()[0]  # Extract the id from the selected_item
        print(f"Selected Item: {selected_item}")

        listbox.bind('<<ListboxSelect>>', on_select)

    cursor.execute("SELECT * FROM Costomer")
    rows = cursor.fetchall()

    for row in rows:
        listbox.insert(tk.END, f"id = {row[0]}    Name = {row[1]}    Telephone = {row[2]}")

    infocostomerWindow.mainloop()
    
phone_table = []
def user_login():
    userloginWindow = tk.Toplevel()
    userloginWindow.title("หน้าหลัก")
    userloginWindow.geometry("1600x900+100+10")
    img = Image.open("USERloginpage.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(userloginWindow, image=photo)
    lbl.image = photo  # Prevent the image from being garbage collected
    lbl.place(x=0, y=0)

    entry_telephone = tk.Entry(userloginWindow)
    entry_telephone.place(x=658, y=420,width=680, height=150)
    entry_telephone.configure(font=("DBHelvethaicaX-LiExt", 80), fg="#CE6857", bg="#ffffff", bd=0, relief="flat")
    lbl = Label(userloginWindow, image=photo)
    
    def user_register():
        global telephone
        userregisterWindow = tk.Toplevel()
        userregisterWindow.title("หน้าหลัก")
        userregisterWindow.geometry("1600x900+100+10")
        img = Image.open("USERregisterpage.png")
        photo = ImageTk.PhotoImage(img)
        lbl = Label(userregisterWindow, image=photo)
        lbl.image = photo  # Prevent the image from being garbage collected
        lbl.place(x=0, y=0)
        
        
        entry_name = tk.Entry(userregisterWindow)
        entry_name.place(x=634, y=346, width=630, height=100)
        entry_name.configure(font=("DBHelvethaicaX-LiExt", 76), fg="#CE6857", bg="#ffffff", bd=0, relief="flat")
        
        entry_telephone = tk.Entry(userregisterWindow)
        entry_telephone.place(x=634, y=603, width=630, height=100)
        entry_telephone.configure(font=("DBHelvethaicaX-LiExt", 76), fg="#CE6857", bg="#ffffff", bd=0, relief="flat")
        
    
        def validate_name_input():
            name = entry_name.get()
            if not name.isalpha():
                messagebox.showerror("Error", "โปรดป้อนชื่อเป็นตัวอักษรเท่านั้น")

        def validate_telephone_input():
            telephone = entry_telephone.get()
            if len(telephone) != 10 or not telephone.isdigit():
                messagebox.showerror("Error", "โปรดป้อนหมายเลขโทรศัพท์ที่มีความยาว 10 ตัวเลข")

        def check_existing_data(name, telephone):
            cursor.execute("SELECT * FROM Costomer WHERE NAME = ? OR Telephone = ?", (name, telephone))
            existing_data = cursor.fetchone()
            return existing_data
        

        def save_to_database():
            name = entry_name.get()
            telephone = entry_telephone.get()
            print(name, telephone)
            # Check if both name and telephone are not empty and the telephone number has 10 digits
            if name.strip() and telephone.strip() and len(telephone) == 10 and telephone.isdigit():
                existing_data = check_existing_data(name, telephone)
                if existing_data:
                    messagebox.showerror("Error", "ข้อมูลนี้มีอยู่ในฐานข้อมูลแล้ว")
                else:
                    # Insert the values into the database
                    cursor.execute("INSERT INTO Costomer (NAME, Telephone) VALUES (?, ?)", (name, telephone))
                    conn.commit()
                    messagebox.showinfo("Success", "ลงทะเบียนสำเร็จ , กรุณาเข้าสู่ระบบ")
                    user_login() 
            else:
                messagebox.showerror("Error", "โปรดกรอกชื่อและหมายเลขโทรศัพท์ที่ถูกต้อง")
        resgister_photo = ImageTk.PhotoImage(resgister_img)
        resgister = tk.Button(userregisterWindow, image=resgister_photo,command=save_to_database, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
        resgister.place(x=750,y=787)
        resgister.image = resgister_photo
        
        
        userregisterWindow.mainloop()
    
    def user_select_table():
        selecttableWindow = tk.Toplevel()
        selecttableWindow.title("หน้าหลัก")
        selecttableWindow.geometry("1600x900+100+10")
        img = Image.open("USERtable.png")
        photo = ImageTk.PhotoImage(img)
        lbl = Label(selecttableWindow, image=photo)
        lbl.image = photo  # Prevent the image from being garbage collected
        lbl.place(x=0, y=0)
        
        def table1():
            phone =  entry_telephone.get()
            print(phone)
            try:
                if phone:
                    cursor.execute("SELECT NAME FROM Costomer WHERE Telephone=?", (phone,))
                    fetched_data = cursor.fetchone()  # ดึงข้อมูลที่ได้จากการ select

                    if fetched_data:  # ตรวจสอบว่ามีข้อมูลที่ได้หรือไม่
                        name = fetched_data[0]  # สมมติให้ข้อมูลที่เราต้องการเป็นตัวแรก

                        # ตรวจสอบว่ามีข้อมูลใน table1 หรือไม่
                        cursor.execute("SELECT * FROM table1")
                        data_in_table1 = cursor.fetchall()
                        if data_in_table1:
                            messagebox.showerror("Error", "มีข้อมูลใน table1 อยู่แล้ว")
                        else:
                            # เพิ่มข้อมูลลงใน table1
                            cursor.execute("INSERT INTO table1 (name) VALUES (?)", (name,))
                            conn.commit()
                            messagebox.showinfo("Success", "ข้อมูลถูกเพิ่มลงใน table1 เรียบร้อยแล้ว")
                            open_soupselection()
                    else:
                        messagebox.showerror("Error", "ไม่พบข้อมูลที่ต้องการ")
            except sqlite3.Error as e:
                messagebox.showerror("ERROR", "ลงทะเบียนไม่สำเร็จ")
        
        table1btn_img = Image.open("USERTable1.png")
        table1btn_photo = ImageTk.PhotoImage(table1btn_img)

        # Create the button
        table1bt = tk.Button(selecttableWindow, command=table1, image=table1btn_photo, bg="#e73a00", bd="0")
        table1bt.image = table1btn_photo  # Keep a reference to the image to prevent it from being garbage collected
        table1bt.place(x=229, y=349)
        
        def table2():
            phone =  entry_telephone.get()
            print(phone)
            try:
                if phone:
                    cursor.execute("SELECT NAME FROM Costomer WHERE Telephone=?", (phone,))
                    fetched_data = cursor.fetchone()  # ดึงข้อมูลที่ได้จากการ select

                    if fetched_data:  # ตรวจสอบว่ามีข้อมูลที่ได้หรือไม่
                        name = fetched_data[0]  # สมมติให้ข้อมูลที่เราต้องการเป็นตัวแรก

                        # ตรวจสอบว่ามีข้อมูลใน table1 หรือไม่
                        cursor.execute("SELECT * FROM table2")
                        data_in_table1 = cursor.fetchall()
                        if data_in_table1:
                            messagebox.showerror("Error", "มีข้อมูลใน table2 อยู่แล้ว")
                        else:
                            # เพิ่มข้อมูลลงใน table1
                            cursor.execute("INSERT INTO table2 (name) VALUES (?)", (name,))
                            conn.commit()
                            messagebox.showinfo("Success", "ข้อมูลถูกเพิ่มลงใน table2 เรียบร้อยแล้ว")
                            open_soupselection()
                    else:
                        messagebox.showerror("Error", "ไม่พบข้อมูลที่ต้องการ")
            except sqlite3.Error as e:
                messagebox.showerror("ERROR", "ลงทะเบียนไม่สำเร็จ")
                
        table2btn_img = Image.open("USERTable2.png")
        table2btn_photo = ImageTk.PhotoImage(table2btn_img)

        # Create the button
        table2bt = tk.Button(selecttableWindow, command=table2, image=table2btn_photo, bg="#e73a00", bd="0")
        table2bt.image = table2btn_photo  # Keep a reference to the image to prevent it from being garbage collected
        table2bt.place(x=520, y=349)
        
        def table3():
            phone =  entry_telephone.get()
            print(phone)
            try:
                if phone:
                    cursor.execute("SELECT NAME FROM Costomer WHERE Telephone=?", (phone,))
                    fetched_data = cursor.fetchone()  # ดึงข้อมูลที่ได้จากการ select

                    if fetched_data:  # ตรวจสอบว่ามีข้อมูลที่ได้หรือไม่
                        name = fetched_data[0]  # สมมติให้ข้อมูลที่เราต้องการเป็นตัวแรก

                        # ตรวจสอบว่ามีข้อมูลใน table1 หรือไม่
                        cursor.execute("SELECT * FROM table3")
                        data_in_table1 = cursor.fetchall()
                        if data_in_table1:
                            messagebox.showerror("Error", "มีข้อมูลใน table3 อยู่แล้ว")
                        else:
                            # เพิ่มข้อมูลลงใน table1
                            cursor.execute("INSERT INTO table3 (name) VALUES (?)", (name,))
                            conn.commit()
                            messagebox.showinfo("Success", "ข้อมูลถูกเพิ่มลงใน table3 เรียบร้อยแล้ว")
                            open_soupselection()
                    else:
                        messagebox.showerror("Error", "ไม่พบข้อมูลที่ต้องการ")
            except sqlite3.Error as e:
                messagebox.showerror("ERROR", "ลงทะเบียนไม่สำเร็จ")
                
        table3btn_img = Image.open("USERTable3.png")
        table3btn_photo = ImageTk.PhotoImage(table3btn_img)

        # Create the button
        table3bt = tk.Button(selecttableWindow, command=table3, image=table3btn_photo, bg="#e73a00", bd="0")
        table3bt.image = table3btn_photo  # Keep a reference to the image to prevent it from being garbage collected
        table3bt.place(x=812, y=350)
        
        def table4():
            phone =  entry_telephone.get()
            print(phone)
            try:
                if phone:
                    cursor.execute("SELECT NAME FROM Costomer WHERE Telephone=?", (phone,))
                    fetched_data = cursor.fetchone()  # ดึงข้อมูลที่ได้จากการ select

                    if fetched_data:  # ตรวจสอบว่ามีข้อมูลที่ได้หรือไม่
                        name = fetched_data[0]  # สมมติให้ข้อมูลที่เราต้องการเป็นตัวแรก

                        # ตรวจสอบว่ามีข้อมูลใน table1 หรือไม่
                        cursor.execute("SELECT * FROM table4")
                        data_in_table1 = cursor.fetchall()
                        if data_in_table1:
                            messagebox.showerror("Error", "มีข้อมูลใน table4 อยู่แล้ว")
                        else:
                            # เพิ่มข้อมูลลงใน table1
                            cursor.execute("INSERT INTO table4 (name) VALUES (?)", (name,))
                            conn.commit()
                            messagebox.showinfo("Success", "ข้อมูลถูกเพิ่มลงใน table4 เรียบร้อยแล้ว")
                            open_soupselection()
                    else:
                        messagebox.showerror("Error", "ไม่พบข้อมูลที่ต้องการ")
            except sqlite3.Error as e:
                messagebox.showerror("ERROR", "ลงทะเบียนไม่สำเร็จ")

        
        table4bt_img = Image.open("USERTable4.png")
        table4bt_photo = ImageTk.PhotoImage(table4bt_img)
        table4bt = tk.Button(selecttableWindow, command=table4, image=table4bt_photo, bg="#e73a00", bd="0")
        table4bt.image = table4bt_photo
        table4bt.place(x=1102, y=350)
        
        left_img = Image.open("LEFTBT.png")
        left_photo = ImageTk.PhotoImage(left_img)
        left = tk.Button(selecttableWindow, image=left_photo,command=main_page, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
        left.place(x=26,y=774)
        left.image = left_photo
     

    def open_login_phone():
        try:
            telephoneNum = entry_telephone.get()
            if telephoneNum:
                cursor.execute("SELECT * FROM Costomer WHERE Telephone=?", (telephoneNum,))
                existing_data = cursor.fetchone()
                cursor.execute("INSERT INTO allusecelect (Phone,Time,day,year) VALUES (?,?,?,?)", (telephoneNum,current_time,current_day,current_year))
                conn.commit()
                if not existing_data:
                    messagebox.showerror("Error", "ไม่พบข้อมูล , กรุณาสมัครสมาชิก")
                else:
                    messagebox.showinfo("title","ยินดีต้องรับ,ร้านชาบู เก(ย์)เร")
                    user_select_table()
                    # กระทำต่อไปที่นี่เมื่อหมายเลขโทรศัพท์ไม่ซ้ำ
                    pass
            else:
                messagebox.showerror("Error", "โปรดกรอกหมายเลขโทรศัพท์")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {str(e)}")

    def show_date():
        global current_year
        now = datetime.now()
        current_year = now.strftime("%m-%Y")
        date_label.config(text=current_year)
        firstpageWindow.after(1000, show_date)  # เรียกใช้ฟังก์ชันเองทุก 1 วินาที

    date_label = Label(firstpageWindow, font=('calibri', 40, 'bold'), bg='#fa5601', fg='white')
    date_label.place(x=370, y=50)
    show_date()
    
    def show_date():
        global current_day
        now = datetime.now()
        current_day = now.strftime("%d-%m-%Y")
        date_label2.config(text=current_day)
        firstpageWindow.after(1000, show_date)  # เรียกใช้ฟังก์ชันเองทุก 1 วินาที

    date_label2 = Label(firstpageWindow, font=('calibri', 40, 'bold'), bg='#fa5601', fg='white')
    date_label2.place(x=300, y=50)
    show_date()
    
    def update_clock():
            global current_time
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            clock.config(text=current_time)
            firstpageWindow.after(1000, update_clock) # เรียกใช้ฟังก์ชันเองทุก 1 วินาที
            
    clock = Label(firstpageWindow, font=('calibri', 40, 'bold'), bg='#fa5601', fg='white')
    clock.place(x=50, y=50)
    update_clock()
    
    resgister_img = Image.open("registerBT.png")
    resgister_photo = ImageTk.PhotoImage(resgister_img)
    resgister = tk.Button(userloginWindow, image=resgister_photo,command=user_register, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    resgister.place(x=789,y=735)
    resgister.image = resgister_photo

    left_img = Image.open("LEFTBT.png")
    left_photo = ImageTk.PhotoImage(left_img)
    left = tk.Button(userloginWindow, image=left_photo,command=main_page, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    left.place(x=26,y=774)
    left.image = left_photo

    right_img = Image.open("RIGHTBT.png")
    right_photo = ImageTk.PhotoImage(right_img)
    right = tk.Button(userloginWindow, image=right_photo,command=open_login_phone, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    right.place(x=1456,y=769)
    right.image = right_photo
    userloginWindow.mainloop()
    
        
   
    
def open_soupselection():
    soupselectionWindows = tk.Toplevel()
    soupselectionWindows.title("หน้าเลือกซุป")
    soupselectionWindows.geometry("1600x900+100+10")
    img = Image.open("USERsoup.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(soupselectionWindows, image=photo)
    lbl.image = photo  # Prevent the image from being garbage collected
    lbl.place(x=0, y=0)
    def handle_button_click(i):
        button = buttons[i]  # ใช้ตัวแปร buttons เพื่อเข้าถึงอ็อบเจ็กต์ปุ่ม
        cursor.execute(f"SELECT Namsoup FROM Nam WHERE rowid={i + 1}")
        selected_button = cursor.fetchone()
        
        if selected_button is not None:
            selected_buttons.append(selected_button[0])  # เก็บอ็อบเจ็กต์ปุ่ม
            selected_label.config(text=str(selected_buttons))  # อัปเดต Label
            button.config(state=tk.DISABLED)
        else:
            selected_buttons.remove(button)
            selected_label.config(text=str(selected_buttons))  # อัปเดต Label
            button.config(state=tk.NORMAL)
            
        if len(selected_buttons) == 2:
            for b in buttons:
                if b not in selected_buttons:
                    b.config(state=tk.DISABLED)
            messagebox.showwarning("Warning", "You have selected 2 buttons. Others are disabled.")

    def reset_button_states():
        for button in buttons:
            button.config(state=tk.NORMAL)
        selected_buttons.clear()
        selected_label.config(text=str(selected_buttons))  # รีเซ็ต Label

    selected_buttons = []

    buttons = []
    button_coords = [(330, 670), (625, 680), (910, 680), (1210, 680)]  # ตำแหน่งของปุ่ม

    for i in range(4):
        button = tk.Button(soupselectionWindows, text=f"น้ำซุปที่ {i+1}", command=lambda i=i: handle_button_click(i))
        button.place(x=button_coords[i][0], y=button_coords[i][1])
        button.config(width=5, height=2,font=("DBHelvethaicaX-LiExt", 10))
        buttons.append(button)

    reset_button = tk.Button(soupselectionWindows, text="Reset", command=reset_button_states)
    reset_button.config(width=5, height=2,font=("DBHelvethaicaX-LiExt", 10))
    reset_button.place(x=372,y=815)

    selected_label = tk.Label(soupselectionWindows, text="",font=("DBHelvethaicaX-LiExt", 20), padx=10, pady=10)
    selected_label.place(x=690,y=794)
    
    # def back_destroy_table():
    #     user_select_table()
        
        
    
    left_img = Image.open("LEFTBT.png")
    left_photo = ImageTk.PhotoImage(left_img)
    left = tk.Button(soupselectionWindows, image=left_photo,command=main_page, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    left.place(x=26,y=774)
    left.image = left_photo
    
    right_img = Image.open("RIGHTBT.png")
    right_photo = ImageTk.PhotoImage(right_img)
    right = tk.Button(soupselectionWindows, image=right_photo,command=open_menuseclection, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    right.place(x=1456,y=769)
    right.image = right_photo

    soupselectionWindows.mainloop()

def open_menuseclection():
    menuseclectionWindows = tk.Toplevel()
    menuseclectionWindows.title("หน้าเลือกเมนู")
    menuseclectionWindows.geometry("1600x900+100+10")
    img = Image.open("USERfood.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(menuseclectionWindows, image=photo)
    lbl.image = photo  # Prevent the image from being garbage collected
    lbl.place(x=0, y=0)
    
    selected_buttons = [] # Initialize the list for selected buttons
    
    def handle_button_click(i):
        button = buttons[i]  # Assuming 'buttons' is a list of your buttons
        cursor.execute(f"SELECT Menu FROM Menu WHERE rowid={i + 1}")
        selected_button = cursor.fetchone()
     
        
        if selected_button is not None:
            selected_buttons.append(selected_button[0])
            cursor.execute("UPDATE UserSeclect SET Menu = ? WHERE rowid = ?", (1, i + 1))
            conn.commit()  # Commit the changes to the database
            selected_label.config(text=str(selected_buttons))
            button.config(state=tk.DISABLED)
       
        if len(selected_buttons) == 1:
            for b in buttons:
                if b not in selected_buttons:
                    b.config(state=tk.DISABLED)
                
            messagebox.showwarning("Warning", "You have selected 1 button. Others are disabled.")
        print("click",i)
    def reset_button_states():
        i=0
        for button in buttons:
            if i < 3 :
                print("loop",i)
                button.config(state=tk.NORMAL)
                cursor.execute("UPDATE UserSeclect SET Menu = ? WHERE rowid = ?", (0, i + 1))
                conn.commit()
                selected_buttons.clear()
                selected_label.config(text=str(selected_buttons))  # รีเซ็ต Label
            i = i+1


    selected_buttons = []

    buttons = []
    button_coords = [(345, 626), (742, 626), (1203, 626)]  # ตำแหน่งของปุ่ม

    for i in range(3):
        button = tk.Button(menuseclectionWindows, text=f"เมนูที่ {i+1}", command=lambda i=i: handle_button_click(i))
        button.place(x=button_coords[i][0], y=button_coords[i][1])
        button.config(width=5, height=2,font=("DBHelvethaicaX-LiExt", 10))
        buttons.append(button)

    reset_button = tk.Button(menuseclectionWindows, text="Reset", command=reset_button_states)
    reset_button.config(width=5, height=2,font=("DBHelvethaicaX-LiExt", 10))
    reset_button.place(x=372,y=815)

    selected_label = tk.Label(menuseclectionWindows, text="",font=("DBHelvethaicaX-LiExt", 20), padx=10, pady=10)
    selected_label.place(x=690,y=794)

    right_img = Image.open("RIGHTBT.png")
    right_photo = ImageTk.PhotoImage(right_img)
    right = tk.Button(menuseclectionWindows, image=right_photo,command=open_drinkmenu, bd=0, bg="#de2f00",activebackground="#de2f00") #command=lambda:table1_click()
    right.place(x=1456,y=769)
    right.image = right_photo
    
    menuseclectionWindows.mainloop()


def open_drinkmenu():
    class ButtonCounterApp:
        def __init__(self, drinkmenuseclectionWindows):
            self.root = drinkmenuseclectionWindows
            self.root.title("Button Counter App")

            # สร้างฐานข้อมูล SQLite
            conn = sqlite3.connect('GAYSHABU2.db')
            cursor = conn.cursor()

            # ดึงข้อมูลจากฐานข้อมูล โดยกำหนด LIMIT เพื่อดึงแถวที่ 4 ขึ้นไป
            cursor.execute("SELECT Menu FROM Menu LIMIT -1 OFFSET 3")
            data = cursor.fetchall()
            print(data)
            self.button_counts = {row[0]: 0 for row in data}
            self.button_coords = [
                (274, 410),
                (537, 410),
                (769, 410),
                (983, 410),
                (1227, 410),
                (274, 646),
                (537, 646),
                (769, 646),
                (983, 646),
            ]
        
            self.labels = self.create_labels()
            self.create_buttons()
            self.create_reset_button()

        def create_buttons(self):
            for i, button_name in enumerate(self.button_counts.keys()):
                if i < len(self.button_coords):
                    x, y = self.button_coords[i]
                    print(i)
                else:
                    x, y = (0, 0)

                button = tk.Button(self.root, text=button_name, command=lambda name=button_name: self.update_count(name))
                button.config(width=5, height=2,font=("DBHelvethaicaX-LiExt", 10))
                button.place(x=x, y=y)
            cursor.execute("SELECT Menu FROM Menu LIMIT -1 OFFSET 3")
            data = cursor.fetchall()
            self.button_counts = {row[0]: 0 for row in data}
            # ...
        def create_labels(self):
            label_coords = [
                    ("น้ำแข็ง", (500, 780)),
                    ("น้ำเปล่า", (560, 780)),
                    ("น้ำอัดลม", (620, 780)),
                    ("เนื้อสไลด์", (680, 780)),
                    ("หมูสไลด์", (740, 780)),
                    ("ชุดรวมผัก", (800, 780)),
                    ("หมึกสด", (870, 780)),
                    ("กุ้งสด", (940, 780)),
                    ("หอยแมลงภู่", (1000, 780)),
                    # Add more items and coordinates as needed
                ]
            labels = {}
            for text, (x, y) in label_coords:
                label = tk.Label(self.root, text=f"{text} x 0")
                label.config(font=("DBHelvethaicaX-LiExt", 10))
                label.place(x=x, y=y)
                labels[text] = label
            return labels

        def create_reset_button(self):
            reset_button = tk.Button(self.root, text="Reset Counts", command=self.reset_counts)
            reset_button.place(x=740,y=820)
        
        def update_count(self, button_name):
            cursor.execute("SELECT total  FROM Menu WHERE Menu = ?", (button_name,))
            select = cursor.fetchall()
            print(select)
            self.button_counts[button_name] += 1
            if self.button_counts[button_name] <= select[0][0]:
                
                
                self.labels[button_name].config(text=f"{button_name} x {self.button_counts[button_name]}")
                cursor.execute("UPDATE UserSeclect SET Menu = ? WHERE name = ?", (self.button_counts[button_name], button_name))
                conn.commit()
            else :
                messagebox.showerror("Error", "สินค้าหมด")
            
            
            return self.button_counts[button_name]
        
        def reset_counts(self):
            print(self.button_counts)
            for button_name in self.button_counts.keys():
                self.button_counts[button_name] = 0
                self.labels[button_name].config(text=f"{button_name} {self.button_counts[button_name]}x")
            i=4
            for button in self.button_counts:
                if  i > 3 :
                    #print("loop",i)
                    #button.config(state=tk.NORMAL)
                    cursor.execute("UPDATE UserSeclect SET Menu = ? WHERE rowid = ?", (0, i))
                    conn.commit()
                    #selected_label.config(text=str())  # รีเซ็ต Label
                i = i+1
                
            
    if __name__ == "__main__":
        drinkmenuseclectionWindows = tk.Toplevel()
        drinkmenuseclectionWindows.title("หน้าเลือกเมนู")
        drinkmenuseclectionWindows.geometry("1600x900+100+10")
        img = Image.open("USERdrink.png")
        photo = ImageTk.PhotoImage(img)
        lbl = Label(drinkmenuseclectionWindows, image=photo)
        lbl.image = photo  # Prevent the image from being garbage collected
        lbl.place(x=0, y=0)

        ButtonCounterApp(drinkmenuseclectionWindows)
        
        selected_label = tk.Label(drinkmenuseclectionWindows, text="", padx=10, pady=10)
        selected_label.place(x=690,y=794)
        
        def next_page(self, button_name):
            
     
            total_menu()
        
        def back_clear():
                i=1
                x=0
                for x in range(3):
                    cursor.execute("UPDATE UserSeclect SET Menu = ? WHERE rowid = ?", (0, i))
                    conn.commit()
                    i=i+1
                    x=x+1
                open_menuseclection()
                
    
        left_img = Image.open("LEFTBT.png")
        left_photo = ImageTk.PhotoImage(left_img)
        left = tk.Button(drinkmenuseclectionWindows, image=left_photo,command=back_clear, bd=0, bg="#de2f00",activebackground="#de2f00")
        left.place(x=26,y=774)
        left.image = left_photo
        
        right_img = Image.open("RIGHTBT.png")
        right_photo = ImageTk.PhotoImage(right_img)
        right = tk.Button(drinkmenuseclectionWindows, image=right_photo,command=total_menu, bd=0, bg="#de2f00",activebackground="#de2f00") #command=lambda:table1_click()
        right.place(x=1456,y=769)
        right.image = right_photo
        
        
        
    drinkmenuseclectionWindows.mainloop()

def total_menu():
    totalWindow = tk.Toplevel()
    totalWindow.title("หน้าหลัก")
    totalWindow.geometry("1600x900+100+10")
    img = Image.open("USERtotle.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(totalWindow, image=photo)
    lbl.image = photo  # Prevent the image from being garbage collected
    lbl.place(x=0, y=0)
    
    def back_clear():
        i=4
        x=0
        for x in range(9):
            
    
            cursor.execute("UPDATE UserSeclect SET Menu = ? WHERE rowid = ?", (0, i))
            conn.commit()
            i=i+1
            x=x+1
        open_drinkmenu()
    
    left_img = Image.open("LEFTBT.png")
    left_photo = ImageTk.PhotoImage(left_img)
    left = tk.Button(totalWindow, image=left_photo,command=back_clear, bd=0, bg="#c50e00",activebackground="#de2f00")
    left.place(x=26,y=774)
    left.image = left_photo

    
    sum = 0 
    cursor.execute("SELECT *  FROM UserSeclect ")
    priceall = cursor.fetchall()
    for x in priceall:
        sum = sum +(x[1]*x[2])
    print(sum)
    
    #labelnamemenu = tk.Label(totalWindow, text=f"{billbillnamemanu}",bg="black", fg="white")
    billbillnamemanu=[]
    billbillquantity=[]
    count=[]
    run=True
    for loop in priceall:
        print(loop)
        if loop[1]>0 :
            
            billbillnamemanu.append(loop[3])
            billbillquantity.append(loop[1]*loop[2])
            count.append(loop[0])
    print(billbillquantity)
    print(billbillnamemanu)
    def show():
        products_listbox5.delete(0, tk.END)
        i=0
        for x in count:
            o=billbillnamemanu
            p=billbillquantity
            products_listbox5.insert(i," ▶   {}     = {}  THB  ".format(o[i],p[i]))
            i+=1  
    
    def clear_totalmenu():
        cursor.execute("SELECT Menu,name  FROM UserSeclect ")
        select = cursor.fetchall()
        print(select)
        for menu,name in select:
            print(name,menu)
            cursor.execute("UPDATE Menu SET total = total- ? WHERE Menu = ?", (menu, name))
            conn.commit()
            
    
    products_listbox5 = tk.Listbox(totalWindow, bg="#ffffff", borderwidth="0px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
    products_listbox5.place(x=570, y=270, width=430, height=550)
    label = tk.Label(totalWindow,text=f"ราคารวมทั้งสิ้น {sum} บาท" , font=("DBHelvethaicaX-LiExt", 17), bg="white", fg="black")
    label.place(x=700, y=720)    
    
    def qrmake():
        qrWindow = tk.Toplevel()
        qrWindow.title("จ่ายเงิน")
        qrWindow.geometry("1600x900+100+10")
        img = Image.open("USERbill.png")
        photo = ImageTk.PhotoImage(img)
        lbl = Label(qrWindow, image=photo)
        lbl.image = photo  # Prevent the image from being garbage collected
        lbl.place(x=0, y=0)
        # cursor.execute("SELECT Time  FROM allusecelect WHERE Time=?  ")(current_time)
        # existing_data = cursor.fetchone()
        cursor.execute("SELECT Time FROM allusecelect ORDER BY ID DESC LIMIT 1")
        latest_data = cursor.fetchone()
        # return latest_data
        print(latest_data)
        cursor.execute("UPDATE allusecelect SET Price = ? WHERE Time = ?", (sum, latest_data[0]))
        conn.commit()

        # URL of the QR code image
        text = "https://promptpay.io/0973582102/" + str(sum) + ".png"
        image_url = text
        print(sum)


        # Check if the request was successful (HTTP status code 200)
        response = requests.get(image_url)
        if response.status_code == 200:
            # Open the image using PIL
            image = Image.open(BytesIO(response.content))
            
            # Convert the image to grayscale if it's not already
            if image.mode != 'L':
                image = image.convert('L')
            
            # Convert the PIL image to a NumPy array
            img_np = np.array(image)

            # Initialize the QRCode detector
            qr_decoder = cv2.QRCodeDetector()

            # Detect and decode the QR code
            val = qr_decoder.detectAndDecode(img_np)

            # Print the decoded value from the QR code
            print("Decoded value from the QR code:", val)

            # Display the image in a Tkinter window
            # image = image.resize((int(image.width * 2), int(image.height * 2)))
            img_tk = ImageTk.PhotoImage(image)
            label = Label(qrWindow, image=img_tk)
            label.image = img_tk
            new_width = 300  # Adjust the desired width
            new_height = 300  # Adjust the desired height
            qr_image_resized = image.resize((new_width, new_height))
            img_tk_resized = ImageTk.PhotoImage(qr_image_resized)
            label_resized = Label(qrWindow, image=img_tk_resized)
            label_resized.image = img_tk_resized  # Keep a reference to avoid garbage collection
            label_resized.place(x=348, y=366)
        else:
            print("Failed to download the image. HTTP status code:", response.status_code)


            
        
        leftbt_img = Image.open("LEFTBT.png")
        leftbt_photo = ImageTk.PhotoImage(leftbt_img)
        leftbt = tk.Button(qrWindow, image=leftbt_photo,command=back_clear, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
        leftbt.place(x=26,y=774)
        leftbt.image = leftbt_photo  
        def destroyfirstpage():
                clear_totalmenu()
                i=1
                x=0
                for x in range(12):
                    cursor.execute("UPDATE UserSeclect SET Menu = ? WHERE rowid = ?", (0, i))
                    i=i+1
                    x=x+1
                cursor.execute(f"DELETE FROM table1 WHERE id = 1")
                cursor.execute(f"DELETE FROM table2 WHERE id = 1")
                cursor.execute(f"DELETE FROM table3 WHERE id = 1")
                cursor.execute(f"DELETE FROM table4 WHERE id = 1")
                conn.commit()
                firstpageWindow.destroy()
        
        pdf_img = Image.open("pdfBT.png")
        pdf_photo = ImageTk.PhotoImage(pdf_img)
        pdf = tk.Button(qrWindow, image=pdf_photo,command=make_pdf, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
        pdf.place(x=711,y=780)
        pdf.image = pdf_photo
            
        right_img = Image.open("RIGHTBT.png")
        right_photo = ImageTk.PhotoImage(right_img)
        right = tk.Button(qrWindow, image=right_photo,command=destroyfirstpage, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
        right.place(x=1456,y=769)
        right.image = right_photo
        
        qrWindow.mainloop()

    rightimg = Image.open("RIGHTBT.png")
    rightphoto = ImageTk.PhotoImage(rightimg)
    right = tk.Button(totalWindow, image=rightphoto,command=qrmake, bd=0, bg="#c50e00",activebackground="#de2f00") #command=lambda:table1_click()
    right.place(x=1456,y=769)
    right.image = rightphoto
   

    
    show()
    totalWindow.mainloop()

def make_pdf():
    conn = sqlite3.connect("GAYSHABU2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(id) FROM UserSeclect;")
    count_all = cursor.fetchone()[0]

    sum = 0 
    cursor.execute("SELECT *  FROM UserSeclect ")
    priceall = cursor.fetchall()
    for x in priceall:
        sum = sum +(x[1]*x[2])
        
        billbillnamemanu=[]
    billbillquantity=[]
    count=[]
    run=True
    for loop in priceall:
        print(loop)
        if loop[1]>0 :
            
            billbillnamemanu.append(loop[3])
            billbillquantity.append(loop[1]*loop[2])
            count.append(loop[0])
    print(billbillquantity)
    print(billbillnamemanu)
    result_list = []
    i=0
    for x in count:
        o=billbillnamemanu
        p=billbillquantity
        result_list.append((" {}     = {}".format(o[i], p[i])))
        i+=1
    
    pdfmetrics.registerFont(TTFont('THSarabun', r"THSarabun.ttf"))

    doc = SimpleDocTemplate("invoiceID%s.pdf"%f"{count_all}", pagesize=letter)

    elements = []


    styles = getSampleStyleSheet()
    normal_style_head = styles['Normal']
    normal_style_head.fontName = 'THSarabun'  
    normal_style_head.fontSize = 20


    styles = getSampleStyleSheet()
    normal_style1 = styles['Normal']
    normal_style1.fontName = 'THSarabun'  
    normal_style1.fontSize = 30

    styles = getSampleStyleSheet()
    normal_style2 = styles['Normal']
    normal_style2.fontName = 'THSarabun'  
    normal_style2.fontSize = 25


    #สร้างคำในใบเสร็จ
    
    cursor.execute("SELECT * FROM UserSeclect ")
    all = cursor.fetchall()
    for x in all:
        op = str(all)
    

        
    
    
    head = Paragraph("ใบเสร็จรับเงิน", normal_style1)
    head1 = Paragraph("ร้านชาบูเก(ย์)เร สาขา10", normal_style_head)
    head2 = Paragraph("69/9 หมู่ที่ 69 ต.หนองคิโมจิ อ.ทุ่ม จ.กาฬสินธุ์ 696969", normal_style_head)
    head3 = Paragraph("รายการทั้งหมด : %s"%result_list, normal_style_head)
    head4 = Paragraph("ราคา : %s บาท"%sum, normal_style_head)



    spacer = Spacer(1, 10)  
    spacer1 = Spacer(1, 50)
    spacer2 = Spacer(1, 20)


    elements.append(head)
    elements.append(spacer1)
    elements.append(head1)
    elements.append(spacer)
    elements.append(head2)
    elements.append(spacer1)
    elements.append(head3)
    elements.append(spacer2)
    elements.append(head4)




    doc.build(elements)

    #เปิดสลิปpdf
    subprocess.Popen(["start", "invoiceID%s.pdf"%f"{count_all}"], shell=True)
    

        

    

 
        
first_page()