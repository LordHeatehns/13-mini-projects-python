
import time
from tkinter import *
from tkinter import messagebox
from turtle import title
from PIL import Image ,ImageTk
from plyer import notification

#notification.notify(title= "Title",app_icon=None,message = "msg",app_name = "notifier",timeout = 10)
fonts = "popins",10
tk = Tk()

tk.title("Notify")
tk.geometry("500x300")

img = Image.open("Sachi-iro.jpg")
tkImage =   ImageTk.PhotoImage(img)

def get_details():
    get_title = title1.get()
    get_msg = msg.get()
    get_time = time1.get()


    if get_details == "" and get_msg =="" and get_time =="" :
        messagebox.showerror("Alert", "All fields are required  ?")
    
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set","set notification ?")

        time.sleep(min_to_sec)

        notification.notify(title= get_title,app_icon=None,message = get_msg,app_name = "notifier",timeout = 10)
imgLabel = Label(tk,image=tkImage).grid()


label = Label(tk,text="Title Notify",font=(fonts))
label.place(x =12 ,y =50)

title1= Entry(tk,width="25" , font=(fonts))
title1.place(x=100 , y=50)



messageLabel = Label(tk,text="enter  messages !",font=(fonts))
messageLabel.place(x=12,y=120)

msg = Entry(tk,width=40 ,font=(fonts))
msg.place(x=130 ,y = 110 , height=30)

timeLabel = Label(tk,text="settime!",font=(fonts))
timeLabel.place(x=12,y=175)

time1 = Entry(tk ,text="",font=(fonts))
time1.place(x=70,y= 175)


timeMinLabel = Label(tk,text="min",font=(fonts))
timeMinLabel.place(x=220,y= 175)


button = Button(tk, text="set Notification" ,font=(fonts) ,fg="#ffffff" ,bg="#528DFF" ,width=20 ,relief="raised", command=get_details)
button.place(x=170 , y= 230)

tk.resizable(0, 0)
tk.mainloop()







