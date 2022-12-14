import matplotlib.pyplot as plt
from calendar import c
from cgitb import enable, reset, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from textwrap import wrap
from tkinter import font
from tkinter.font import BOLD
from urllib.parse import parse_qs
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Tk, Canvas

import customtkinter
import PIL.Image
from PIL import ImageGrab
from PIL import ImageTk, Image, ImageFile
import PIL.Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

finsysdb = mysql.connector.connect(
    host="localhost", user="root", password="", database="finsysinfox21", port="3306"
)
fbcursor = finsysdb.cursor(buffered=True)

root=Tk()
root.geometry("1366x768+0+0")

root.title("Fin sYs")

p1 = PhotoImage(file = 'images/favicon.png')
root.iconphoto(False, p1)

#-------------------------------------------------------------------------------------------------------------------------Images
# banking = PhotoImage(file="images/banking.PNG")
# sales = PhotoImage(file="images/sheet.PNG")
# expenses = PhotoImage(file="images/expense.PNG")
# payroll = PhotoImage(file="images/payroll.PNG")
# report = PhotoImage(file="images/reports.PNG")
# taxes = PhotoImage(file="images/taxes.PNG")
# accounts = PhotoImage(file="images/accounting.PNG")



imgr1 =PIL.Image.open("images\logs.png")
exprefreshIcon=ImageTk.PhotoImage(imgr1)

notic =PIL.Image.open("images/bell.png")
noti=ImageTk.PhotoImage(notic)

mnu =PIL.Image.open("images\menu bar.PNG")
mnus=ImageTk.PhotoImage(mnu)


srh =PIL.Image.open("images\search.PNG")
srh_img=ImageTk.PhotoImage(srh)

stn =PIL.Image.open("images/brightness-solid-24.png")
stn_img=ImageTk.PhotoImage(stn)

logo =PIL.Image.open("images\logo-icon.png")
resized_image= logo.resize((50,50))
mai_logo= ImageTk.PhotoImage(resized_image)

sig_up =PIL.Image.open("images/register.png")
resized_sign_up= sig_up.resize((500,400))
sign_up=ImageTk.PhotoImage(resized_sign_up)

lowstock = PhotoImage(file="images/lowstock.png")
outofstock = PhotoImage(file="images/outofstock.png")

#------------------------------------------------------------------------------------------------------------Login Button Function

def main_sign_in():
    try:
        main_frame_signup.pack_forget()
    except:
        pass
    try:
        main_frame_signin.pack_forget()
    except:
        pass
    Sys_top_frame=Frame(root, height=70,bg="#213b52")
    Sys_top_frame.pack(fill=X,)

    #---------------------------------------------------------------------------------------Top Menu
    tp_lb_nm=LabelFrame(Sys_top_frame,bg="#213b52")#-----------------------------Logo Name Frame
    tp_lb_nm.grid(row=1,column=1,sticky='nsew')
    tp_lb_nm.grid_rowconfigure(0,weight=1)
    tp_lb_nm.grid_columnconfigure(0,weight=1)

    label = Label(tp_lb_nm, image = mai_logo,height=70,bg="#213b52",border=0)
    label.grid(row=2,column=1,sticky='nsew')
    label = Label(tp_lb_nm, text="Fin sYs",bg="#213b52", fg="white",font=('Calibri 30 bold'),border=0)
    label.grid(row=2,column=2,sticky='nsew')
  
    mnu_btn = Button(tp_lb_nm, image=mnus, bg="white", fg="black",border=0)
    mnu_btn.grid(row=2,column=4,padx=50)

    

    tp_lb_srh=LabelFrame(Sys_top_frame,bg="#213b52")#-------------------------Serch area Frame
    tp_lb_srh.grid(row=1,column=2,sticky='nsew')
    tp_lb_srh.grid_rowconfigure(0,weight=1)
    tp_lb_srh.grid_columnconfigure(0,weight=1)

    def srh_fn(event):
        if srh_top.get()=="Search":
            srh_top.delete(0,END)
        else:
            pass

    srh_top = Entry(tp_lb_srh, width=50, font=('Calibri 16'))
    srh_top.insert(0,"Search")
    srh_top.bind("<Button-1>",srh_fn)
    srh_top.grid(row=2,column=1,padx=(30,0), pady=20,sticky='nsew')

    srh_btn = Button(tp_lb_srh, image=srh_img, bg="#213b52", fg="black",border=0)
    srh_btn.grid(row=2,column=4,padx=(0,30))

    #------------------------------------------------------settings 
    def close_lst_2():
            lst_prf2.place_forget()
            set_btn4 = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
            set_btn4.grid(row=2,column=5,padx=(0,30))
            
    def settings():
        

        # create a list box
        stng = ("Accounts And Settings","Customize From Style","Chart Of Accounts")

        stngs = StringVar(value=stng)
        global lst_prf2
        lst_prf2 = Listbox(root,listvariable=stngs,height=3 ,selectmode='extended',bg="black",fg="white")

        lst_prf2.place(relx=0.70, rely=0.10)
        lst_prf2.bind('<<ListboxSelect>>', )
        set_btn.grid_forget()
        set_btn2 = Button(tp_lb_srh, image=stn_img,command=close_lst_2, bg="#213b52", fg="black",border=0)
        set_btn2.grid(row=2,column=5,padx=(0,30))

    set_btn = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
    set_btn.grid(row=2,column=5,padx=(0,30))

    tp_lb_nm=LabelFrame(Sys_top_frame,bg="#213b52")#-----------------------------Notification
    tp_lb_nm.grid(row=1,column=3,sticky='nsew')
    tp_lb_nm.grid_rowconfigure(0,weight=1)
    tp_lb_nm.grid_columnconfigure(0,weight=1)
    srh_btn = Button(tp_lb_nm, image=noti, bg="#213b52", fg="black",border=0)
    srh_btn.grid(row=0,column=0,padx=35)
    
    tp_lb_npr=LabelFrame(Sys_top_frame,bg="#213b52")#---------------------------profile area name
    tp_lb_npr.grid(row=1,column=4,sticky='nsew')
    tp_lb_npr.grid_rowconfigure(0,weight=1)
    tp_lb_npr.grid_columnconfigure(0,weight=1)

    label = Label(tp_lb_npr, text="Errors",bg="#213b52", fg="white", anchor="center",width=10,font=('Calibri 16 bold'),border=0)
    label.grid(row=1,column=1,sticky='nsew')
    label = Label(tp_lb_npr, text="Online",bg="#213b52", fg="white",width=15,font=('Calibri 12 bold'),border=0)
    label.grid(row=2,column=1,sticky='nsew')

    pro =PIL.Image.open("images/user.png")
    resized_pro= pro.resize((20,20))
    pro_pic= ImageTk.PhotoImage(resized_pro)
    
    def lst_frt():
        lst_prf.place_forget()
        srh_btn3 = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=profile)
        srh_btn3.grid(row=2,column=2,padx=15)
    def lst_prf_slt(event):
        def edit_profile():
            def responsive_widgets_edit(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                


                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/13
                y2 = dheight/.53

                dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )                              

                
                # dcanvas.coords("bg_polygen_pr",dwidth/16,dheight/.6,dwidth/1.07,dheight/9)
                dcanvas.coords("my_pro",dwidth/2.3,dheight/12.5)

                dcanvas.coords("pr_hr_l",dwidth/16,dheight/7,dwidth/1.07,dheight/7)
                dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                dcanvas.coords("pr_crpass_lb",dwidth/17.075,dheight/1.33)
                dcanvas.coords("pr_crpass_ent",dwidth/17.075,dheight/1.26)
                dcanvas.coords("pr_re_pass_lb",dwidth/17.075,dheight/1.16)
                dcanvas.coords("pr_re_pass_ent",dwidth/17.075,dheight/1.1)
                dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)
                dcanvas.coords("pr_new_pass_lb",dwidth/1.92,dheight/1.33)
                dcanvas.coords("pr_new_pass_ent",dwidth/1.92,dheight/1.26)

                
                #-------------------------------------------------------------------------company section
                dcanvas.coords("cmp_hd",dwidth/20,dheight/1)
                dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/0.93)
                dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/0.89)
                dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/0.84)
                dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/0.81)
                dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/0.77)
                dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.745)
                dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.712)
                dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.69)
                dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.66)
                dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.64)
                dcanvas.coords("cmp_file_lb",dwidth/17.075,dheight/.615)
                dcanvas.coords("cmp_file_ent",dwidth/17.075,dheight/.6)
                

                #--------------------------------------------------------------------------company right

                dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/0.93)
                dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/0.89)
                dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/0.84)
                dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/0.81)
                dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/0.77)
                dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.745)
                dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.712)
                dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.69)
                dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.66)
                dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.64)
                dcanvas.coords("btn_edit",dwidth/2.4,dheight/.57)
            
            Sys_mains_frame_pr.place_forget()
            global Sys_mains_frame_pr_ed
            Sys_mains_frame_pr_ed=Frame(tab1, height=750)
            Sys_mains_frame_pr_ed.grid(row=0,column=0,sticky='nsew')
            Sys_mains_frame_pr_ed.grid_rowconfigure(0,weight=1)
            Sys_mains_frame_pr_ed.grid_columnconfigure(0,weight=1)

            pr_canvas_ed=Canvas(Sys_mains_frame_pr_ed,height=766,width=1340,scrollregion=(0,0,766,1650),bg="#2f516f",border=0)
            pr_canvas_ed.bind('<Configure>', responsive_widgets_edit)
            
            pr_myscrollbar_ed=Scrollbar(Sys_mains_frame_pr_ed,orient="vertical",command=pr_canvas_ed.yview)
            pr_canvas_ed.configure(yscrollcommand=pr_myscrollbar_ed.set)

            pr_myscrollbar_ed.pack(side="right",fill="y")
            pr_canvas_ed.pack(fill=X)

            rth2 = pr_canvas_ed.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_pr"),smooth=True,)

            grd1c=Label(pr_canvas_ed, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
            win_inv1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

            pr_canvas_ed.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
            #----------------------------------------------------------------------------------------Personal info
            pr_hd=Label(pr_canvas_ed, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
            win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

            fir_name=Label(pr_canvas_ed, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

            fr_name_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

            pr_em_lb=Label(pr_canvas_ed, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

            pr_crpass_lb=Label(pr_canvas_ed, text="Enter your Current Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_lb,tag=("pr_crpass_lb"))

            pr_crpass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_ent,tag=("pr_crpass_ent"))

            pr_re_pass_lb=Label(pr_canvas_ed, text="Re-type new Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_lb,tag=("pr_re_pass_lb"))

            pr_re_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_ent,tag=("pr_re_pass_ent"))


            em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

            last_nm_lb=Label(pr_canvas_ed, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

            lst_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

            usr_nm_lb=Label(pr_canvas_ed, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

            usr_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

            pr_new_pass_lb=Label(pr_canvas_ed, text="Enter New Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_lb,tag=("pr_new_pass_lb"))

            pr_new_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_ent,tag=("pr_new_pass_ent"))


            # #------------------------------------------------------------------------------------------------COMPANY SECTION
            cmp_hd=Label(pr_canvas_ed, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
            win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

            cmp_nm_lb=Label(pr_canvas_ed, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

            cmp_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

            cmp_cty_lb=Label(pr_canvas_ed, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

            cmp_cty_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

            cmp_pin_lb=Label(pr_canvas_ed, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

            cmp_pin_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

            cmp_ph_lb=Label(pr_canvas_ed, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

            cmp_ph_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

            cmp_indest_lb=Label(pr_canvas_ed, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

            cmp_indest_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

            # #----------------------------------------------------------------------------------------------------RIGHT SIDE
            cmp_addr_lb=Label(pr_canvas_ed, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

            cmp_addr_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

            cmp_st_lb=Label(pr_canvas_ed, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

            cmp_st_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

            cmp_em_lb=Label(pr_canvas_ed, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

            cmp_em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

            cmp_lg_nm=Label(pr_canvas_ed, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

            cmp_lg_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

            cmp_typ_lb=Label(pr_canvas_ed, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

            cmp_typ_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))

            cmp_file_lb=Label(pr_canvas_ed, text="File",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_lb,tag=("cmp_file_lb"))

            cmp_file_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_ent,tag=("cmp_file_ent"))


            btn_edit = Button(pr_canvas_ed, text='Update Profile', command=edit_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))

        
        selected_indices = lst_prf.curselection()
        selected_langs = ",".join([lst_prf.get(i) for i in selected_indices])
        lst_prf.place_forget()

        def pr_responsive_widgets(event):
                
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
             
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/13
                y2 = dheight/.6

                dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )                   
 
                dcanvas.coords("my_pro",dwidth/2.3,dheight/12.5)

                dcanvas.coords("pr_hr_l",dwidth/16,dheight/7,dwidth/1.07,dheight/7)
                dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                
                dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)

                #-------------------------------------------------------------------------company section
                dcanvas.coords("cmp_hd",dwidth/20,dheight/1.32)
                dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/1.22)
                dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/1.16)
                dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/1.07)
                dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/1.02)
                dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/.95)
                dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.91)
                dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.86)
                dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.83)
                dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.78)
                dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.755)

                #--------------------------------------------------------------------------company right

                dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/1.22)
                dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/1.16)
                dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/1.07)
                dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/1.02)
                dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/.95)
                dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.91)
                dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.86)
                dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.83)
                dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.78)
                dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.755)
                dcanvas.coords("btn_edit",dwidth/2.4,dheight/.71)

        if selected_langs=="Profile":
            # canvas.pack_forget()
            # myscrollbar.pack_forget()
            # Sys_mains_frame.pack_forget()
            
            Sys_mains_frame_pr=Frame(tab1, height=750,bg="#2f516f",)
            Sys_mains_frame_pr.grid(row=0,column=0,sticky='nsew')
            Sys_mains_frame_pr.grid_rowconfigure(0,weight=1)
            Sys_mains_frame_pr.grid_columnconfigure(0,weight=1)

            pr_canvas=Canvas(Sys_mains_frame_pr,height=700,width=1340,scrollregion=(0,0,700,1300),bg="#2f516f",border=0)
            pr_canvas.bind("<Configure>", pr_responsive_widgets)
            
            pr_myscrollbar=Scrollbar(Sys_mains_frame_pr,orient="vertical",command=pr_canvas.yview)
            pr_canvas.configure(yscrollcommand=pr_myscrollbar.set)

            pr_myscrollbar.pack(side="right",fill="y")
            pr_canvas.pack(fill=X)

            rth2 = pr_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",smooth=True,tags=("bg_polygen_pr"))

            grd1c=Label(pr_canvas, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
            win_inv1 = pr_canvas.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

            pr_canvas.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
            #----------------------------------------------------------------------------------------Personal info
            pr_hd=Label(pr_canvas, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
            win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

            fir_name=Label(pr_canvas, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

            fr_name_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

            pr_em_lb=Label(pr_canvas, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

            em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

            last_nm_lb=Label(pr_canvas, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

            lst_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

            usr_nm_lb=Label(pr_canvas, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

            usr_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

            #------------------------------------------------------------------------------------------------COMPANY SECTION
            cmp_hd=Label(pr_canvas, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
            win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

            cmp_nm_lb=Label(pr_canvas, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

            cmp_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

            cmp_cty_lb=Label(pr_canvas, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

            cmp_cty_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

            cmp_pin_lb=Label(pr_canvas, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

            cmp_pin_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

            cmp_ph_lb=Label(pr_canvas, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

            cmp_ph_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

            cmp_indest_lb=Label(pr_canvas, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

            cmp_indest_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

            #----------------------------------------------------------------------------------------------------RIGHT SIDE
            cmp_addr_lb=Label(pr_canvas, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

            cmp_addr_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

            cmp_st_lb=Label(pr_canvas, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

            cmp_st_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

            cmp_em_lb=Label(pr_canvas, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

            cmp_em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

            cmp_lg_nm=Label(pr_canvas, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

            cmp_lg_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

            cmp_typ_lb=Label(pr_canvas, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

            cmp_typ_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))


            btn_edit = Button(pr_canvas, text='Edit Profile', command=edit_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))
        
        elif selected_langs=="Log Out":
            
            Sys_top_frame2.pack_forget()
            Sys_top_frame.pack_forget()
            main_frame_signin.pack(fill=X,)
        elif selected_langs== "Dashboard":
            try:
                Sys_mains_frame_pr_ed.place_forget()
            except:
                pass
            try:
                
                Sys_mains_frame_pr.place_forget()
            except:
                pass

        else:
            pass

    def profile():
        # create a list box
        langs = ("Dashboard","Profile","Log Out")

        langs_var = StringVar(value=langs)
        global lst_prf
        lst_prf = Listbox(root,listvariable=langs_var,height=3 ,selectmode='extended',bg="black",fg="white")

        lst_prf.place(relx=0.90, rely=0.10)
        lst_prf.bind('<<ListboxSelect>>', lst_prf_slt)
        srh_btn.grid_forget()
        srh_btn2 = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=lst_frt)
        srh_btn2.grid(row=2,column=2,padx=15)
   
    srh_btn = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=profile)
    srh_btn.grid(row=2,column=2,padx=15)

    Sys_top_frame2=Frame(root, height=10,bg="#213b52")
    Sys_top_frame2.pack(fill=X,)
    
    s = ttk.Style()
    s.theme_use('default')
    s.configure('TNotebook.Tab', background="#213b52",foreground="white", width=150,anchor="center", padding=5)
    s.map('TNotebook.Tab',background=[("selected","#2f516f")])
    def right_nav():
        
        tabControl.pack_forget()
        btn_nav.place_forget()
        tabControl2.pack(expand = 1, fill ="both")
        btn_nav2.place(relx=0, rely=0)
        try:
            btn_nav3.place_forget()
        except:
            pass
    def left_nav():
        
        tabControl2.pack_forget()
        btn_nav2.place_forget()
        tabControl.pack(expand = 1, fill ="both")
        global btn_nav3
        btn_nav3=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
        btn_nav3.place(relx=0.97, rely=0)

    tabControl = ttk.Notebook(Sys_top_frame2)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3=  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6=  ttk.Frame(tabControl)
    tab7 = ttk.Frame(tabControl)
    tab8 = ttk.Frame(tabControl)
    
    
    btn_nav=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
    btn_nav.place(relx=0.97, rely=0)
    tabControl.add(tab1,compound = LEFT, text ='Dashboard',)
    tabControl.add(tab2,compound = LEFT, text ='Banking')
    tabControl.add(tab3,compound = LEFT, text ='Sales')
    tabControl.add(tab4,compound = LEFT, text ='Expenses')
    tabControl.add(tab5,compound = LEFT, text ='Payroll') 
    tabControl.add(tab6,compound = LEFT, text ='Report')
    tabControl.add(tab7,compound = LEFT, text ='Taxes')
    tabControl.add(tab8,compound = LEFT, text ='Accounting')
    
    tabControl.pack(expand = 1, fill ="both")


    
    tabControl2 = ttk.Notebook(Sys_top_frame2)
    tab9 =  ttk.Frame(tabControl2)
    tab10=  ttk.Frame(tabControl2)
    tab11 = ttk.Frame(tabControl2)
    tab12=  ttk.Frame(tabControl2)
    tab13 = ttk.Frame(tabControl2)
    tab14 = ttk.Frame(tabControl2)
    tab15 =  ttk.Frame(tabControl2)

    btn_nav2=Button(Sys_top_frame2,text="<<", command=left_nav, width=3, bg="#213b52",fg="white")
    
        
    tabControl2.add(tab9,compound = LEFT, text ='My Account')
    tabControl2.add(tab10,compound = LEFT, text ='Cash Management')
    tabControl2.add(tab11,compound = LEFT, text ='Production')
    tabControl2.add(tab12,compound = LEFT, text ='Quality Management')
    tabControl2.add(tab13,compound = LEFT, text ='Project Management')
    tabControl2.add(tab14,compound = LEFT, text ='Usage Decisions')
    tabControl2.add(tab15,compound = LEFT, text ='Account & Payable')

   
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Dash Board}
    tab1.grid_columnconfigure(0,weight=1)
    tab1.grid_rowconfigure(0,weight=1)
    
    Sys_mains_frame=Frame(tab1,bg="#2f516f",)
    Sys_mains_frame.grid(row=0,column=0,sticky='nsew')

    
    
    def responsive_wid(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
      
        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/1.021
        y1 = dheight/13
        y2 = dheight/6

        dcanvas.coords("bg_polygen_dash",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )                    

        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/3.1
        y1 = dheight/5
        y2 = dheight/1.1

        dcanvas.coords("bg_polygen_dash1",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        r1 = 25
        x1 = dwidth/2.95
        x2 = dwidth/1.529
        y1 = dheight/5
        y2 = dheight/1.1

        dcanvas.coords("bg_polygen_dash2",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        r1 = 25
        x1 = dwidth/1.49
        x2 = dwidth/1.021
        y1 = dheight/5
        y2 = dheight/1.1

        dcanvas.coords("bg_polygen_dash3",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/3.1
        y1 = dheight/1.06
        y2 = dheight/.59
        
        #-----------------------------------------second row
        dcanvas.coords("bg_polygen_dash4",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        r1 = 25
        x1 = dwidth/2.95
        x2 = dwidth/1.529
        y1 = dheight/1.06
        y2 = dheight/.59

        dcanvas.coords("bg_polygen_dash5",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        r1 = 25
        x1 = dwidth/1.49
        x2 = dwidth/1.021
        y1 = dheight/1.06
        y2 = dheight/.59

        dcanvas.coords("bg_polygen_dash6",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        dcanvas.coords("head_lb",dwidth/2,dheight/8.4)
        dcanvas.coords("prf_lb",dwidth/53,dheight/4.7)
        
        dcanvas.coords("prf_hr",dwidth/53,dheight/3.7,dwidth/3.15,dheight/3.7)
        dcanvas.coords("net_prf",dwidth/53,dheight/3.2)
        dcanvas.coords("graph",dwidth/53,dheight/2.2)
        #--------------------------------------------------------------second
        dcanvas.coords("exp_hd_lb",dwidth/2.9,dheight/4.7)
        dcanvas.coords("exp_hr",dwidth/2.9,dheight/3.7,dwidth/1.54,dheight/3.7)
        dcanvas.coords("graph_2",dwidth/2.9,dheight/2.2)
        
        #-----------------------------------------------------------third
        dcanvas.coords("bnk_lb",dwidth/1.48,dheight/4.7)
        dcanvas.coords("bank_hr",dwidth/1.48,dheight/3.7,dwidth/1.03,dheight/3.7)
        #--------------------------------------------------------------forth
        dcanvas.coords("incom_lb",dwidth/53,dheight/1.04)
        
        dcanvas.coords("incom_hr",dwidth/53,dheight/0.99,dwidth/3.15,dheight/0.99)

     
        dcanvas.coords("graph_4",dwidth/53,dheight/0.85)
   
        #-------------------------------------------------------------fifth
        dcanvas.coords("inv_lb",dwidth/2.9,dheight/1.04)
        dcanvas.coords("invs_hr",dwidth/2.9,dheight/0.99,dwidth/1.54,dheight/0.99)
        dcanvas.coords("inv_lb2",dwidth/2.9,dheight/0.95)
        dcanvas.coords("inv_lb3",dwidth/2.9,dheight/0.90)
        dcanvas.coords("graph_5",dwidth/2.9,dheight/0.85)
        #-------------------------------------------------------------sixth
        dcanvas.coords("sales_lb",dwidth/1.48,dheight/1.04)
        dcanvas.coords("sales_hr",dwidth/1.48,dheight/0.99,dwidth/1.03,dheight/0.99)
        
        


        dcanvas.coords("grapg_6",dwidth/1.48,dheight/0.85)
        

        
    Sys_mains_frame.grid_rowconfigure(0,weight=1)
    Sys_mains_frame.grid_columnconfigure(0,weight=1)

    canvas = Canvas(Sys_mains_frame,height=700,bg='#2f516f',scrollregion=(0,0,700,1200))
    sr_Scroll = Scrollbar(Sys_mains_frame,orient=VERTICAL)
    sr_Scroll.grid(row=0,column=1,sticky='ns')
    sr_Scroll.config(command=canvas.yview)
    canvas.bind("<Configure>", responsive_wid)
    canvas.config(yscrollcommand=sr_Scroll.set)
    canvas.grid(row=0,column=0,sticky='nsew')
    

    cmp_name=Label(canvas, text="Clown",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
  
    win_inv1 = canvas.create_window(0, 0, anchor="center", window=cmp_name,tag=("head_lb"))
    
    rth2 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash"),smooth=True,)
    # #----------------------------------------------------------------------------------------------------------------grid 1
    rth1 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash1"),smooth=True,)

    prf_lb=Label(canvas, text="PROFIT AND LOSS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=prf_lb, tag=("prf_lb"))

    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("prf_hr") )

    net_prf=Label(canvas, text="NET INCOME: ??? 0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=net_prf,tag=("net_prf"))

    figlast = plt.figure(figsize=(8, 4), dpi=50)

    x="Income"
    y=10 
    plt.barh(x,y, label="Undefined", color="blue") 
    plt.legend()
  
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()

    x="Expense"
    y=100
    plt.barh(x,y, color="red") 
    plt.legend()
 
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()
              

    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph"))
    # #----------------------------------------------------------------------------------------------------------------grid 2
    rth2 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash2"),smooth=True,)

    exp_hd_lb=Label(canvas, text="EXPENSES: ??? 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=exp_hd_lb, tag=("exp_hd_lb"))
    canvas.create_line(0, 0, 0, 0,fill="gray" ,tag=("exp_hr"))
    fig, ax = plt.subplots(figsize=(8, 4), dpi=50)

    size = 0.3
    vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

    cmap = plt.colormaps["tab20c"]
    outer_colors = cmap(np.arange(3)*4)
    # inner_colors = cmap([1, 2, 5, 6, 9, 10])

    ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
        wedgeprops=dict(width=size, edgecolor='w'))

    # ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
    #        wedgeprops=dict(width=size, edgecolor='w'))

    ax.set(aspect="equal", title='Pie plot with `ax.pie`')

    canvasbar = FigureCanvasTkAgg(fig, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_2"))

    # #----------------------------------------------------------------------------------------------------------------grid 3
    rth3 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash3"),smooth=True,)

    bnk_lb=Label(canvas, text="BANK ACCOUNTS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=bnk_lb,tag=("bnk_lb"))
    canvas.create_line(910, 195, 1290, 195,fill="gray",tag=("bank_hr"))
    # #----------------------------------------------------------------------------------------------------------------grid 4
    rth4 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash4"),smooth=True,)

    incom_lb=Label(canvas, text="INCOME: ??? 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=incom_lb,tag=("incom_lb"))
    canvas.create_line(0, 0, 0, 0,fill="gray",tag=("incom_hr") )

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots(figsize=(8, 4), dpi=50)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    canvasbar = FigureCanvasTkAgg(fig1, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_4"))

    # #----------------------------------------------------------------------------------------------------------------grid 5
    rth5 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash5"),smooth=True,)
    inv_lb=Label(canvas, text="INVOICE",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb, tag=("inv_lb"))

    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("invs_hr") )
    inv_lb2=Label(canvas, text="UNPAID:??? 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb2, tag=("inv_lb2"))
    inv_lb3=Label(canvas, text="PAID:??? 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0,0 , anchor="nw", window=inv_lb3, tag=("inv_lb3"))

    figlast = plt.figure(figsize=(8, 4), dpi=50)

    x="Unpaid"
    y=10 
    plt.barh(x,y, label="Undefined", color="blue") 
    plt.legend()
  
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()

    x="Paid"
    y=100
    plt.barh(x,y, color="red") 
    plt.legend()
 
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()
              

    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(480, 780, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_5"))
    # #----------------------------------------------------------------------------------------------------------------grid 5
    

    # win_inv1 = canvas.create_window(920, 640, anchor="nw", window=grd1)
    
    # canvas.create_line(910, 675, 1290, 675,fill="gray" )
    # figlast = plt.figure(figsize=(8, 4), dpi=50)

    # x="Income"
    # y=10 
    # plt.barh(x,y, label="Undefined", color="blue") 
    # plt.legend()
  
    # plt.ylabel("")
    # axes=plt.gca()
    # axes.xaxis.grid()

    # canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
    # canvasbar
    # canvasbar.draw()
    # canvasbar.get_tk_widget()
    # win_inv1 = canvas.create_window(900, 780, anchor="nw", window=canvasbar.get_tk_widget())
    # #----------------------------------------------------------------------------------------------------------------grid 6
    rth6 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash6"),smooth=True,)
    sales_lb=Label(canvas, text="SALES $0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=sales_lb, tag=("sales_lb"))

    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("sales_hr") )
    
    
    fig, ax = plt.subplots(figsize=(8, 4), dpi=50)
    ax.plot(range(10))
    ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
   

    canvasbar = FigureCanvasTkAgg(fig, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("grapg_6"))
    
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333Banking Section(Tab2)

    tab_bank = ttk.Notebook(tab2)
    tab2_1 =  ttk.Frame(tab_bank)
    tab2_2=  ttk.Frame(tab_bank)
    tab2_3 = ttk.Frame(tab_bank)

    tab_bank.add(tab2_1,compound = LEFT, text ='Online Banking')
    tab_bank.add(tab2_2,compound = LEFT, text ='Offline banking')
    tab_bank.add(tab2_3,compound = LEFT, text ='Bank Reconvilation')

    
    tab_bank.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Sales Tab}
    tab_sales = ttk.Notebook(tab3)
    tab3_1 =  ttk.Frame(tab_sales)
    tab3_2=  ttk.Frame(tab_sales)
    tab3_3 = ttk.Frame(tab_sales)
    tab3_4=  ttk.Frame(tab_sales)

    
        
    tab_sales.add(tab3_1,compound = LEFT, text ='Sales Records')
    tab_sales.add(tab3_2,compound = LEFT, text ='Invoices')
    tab_sales.add(tab3_3,compound = LEFT, text ='Customers')
    tab_sales.add(tab3_4,compound = LEFT, text ='Product & Services')
 
    tab_sales.pack(expand = 1, fill ="both")

    #--------------------------------Invoices-----------------------------#
    tab3_2.grid_columnconfigure(0,weight=1)
    tab3_2.grid_rowconfigure(0,weight=1)

    inv_frame = Frame(tab3_2)
    inv_frame.grid(row=0,column=0,sticky='nsew')

    def inv_responsive_widgets(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget

        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/1.021
        y1 = dheight/14 
        y2 = dheight/3.505

        dcanvas.coords("ipoly1",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        dcanvas.coords("ihline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
        dcanvas.coords("ilabel1",dwidth/2.5,dheight/8.00)

        r2 = 25
        x11 = dwidth/63
        x21 = dwidth/1.021
        y11 = dheight/2.8
        y21 = dheight/1.168


        dcanvas.coords("ipoly2",x11 + r2,y11,
        x11 + r2,y11,
        x21 - r2,y11,
        x21 - r2,y11,     
        x21,y11,     
        #--------------------
        x21,y11 + r2,     
        x21,y11 + r2,     
        x21,y21 - r2,     
        x21,y21 - r2,     
        x21,y21,
        #--------------------
        x21 - r2,y21,     
        x21 - r2,y21,     
        x11 + r2,y21,
        x11 + r2,y21,
        x11,y21,
        #--------------------
        x11,y21 - r2,
        x11,y21 - r2,
        x11,y11 + r2,
        x11,y11 + r2,
        x11,y11,
        )

        dcanvas.coords("iline1", dwidth/22.00, dheight/1.8, dwidth/1.060, dheight/1.8)
        dcanvas.coords("iline2", dwidth/22.00, dheight/1.8, dwidth/22.00, dheight/1.35)
        dcanvas.coords("iline3", dwidth/22.00, dheight/1.35, dwidth/1.060, dheight/1.35)
        dcanvas.coords("iline4", dwidth/1.060, dheight/1.8, dwidth/1.060, dheight/1.35)
        dcanvas.coords("iline5", dwidth/22.00, dheight/1.575, dwidth/1.060, dheight/1.575)
        dcanvas.coords("iline6", dwidth/6.20, dheight/1.8, dwidth/6.20, dheight/1.35)
        dcanvas.coords("iline7", dwidth/4.00, dheight/1.8, dwidth/4.00, dheight/1.35)
        dcanvas.coords("iline8", dwidth/2.7, dheight/1.8, dwidth/2.7, dheight/1.35)
        dcanvas.coords("iline9", dwidth/1.95, dheight/1.8, dwidth/1.95, dheight/1.35)
        dcanvas.coords("iline10", dwidth/1.65, dheight/1.8, dwidth/1.65, dheight/1.35)
        dcanvas.coords("iline11", dwidth/1.38, dheight/1.8, dwidth/1.38, dheight/1.35)
        dcanvas.coords("iline12", dwidth/1.20, dheight/1.8, dwidth/1.20, dheight/1.35)


        dcanvas.coords("ilabel2",dwidth/13.5,dheight/1.74)
        dcanvas.coords("ilabel3",dwidth/5.78,dheight/1.74)
        dcanvas.coords("ilabel4",dwidth/3.6,dheight/1.74)
        dcanvas.coords("ilabel5",dwidth/2.45,dheight/1.74)
        dcanvas.coords("ilabel6",dwidth/1.9,dheight/1.74)
        dcanvas.coords("ilabel7",dwidth/1.59,dheight/1.74)
        dcanvas.coords("ilabel8",dwidth/1.345,dheight/1.74)
        dcanvas.coords("ilabel9",dwidth/1.17,dheight/1.74)

        dcanvas.coords("ibutton1",dwidth/1.28,dheight/2.4)
        dcanvas.coords("icombo1",dwidth/1.179,dheight/1.52)



    inv_canvas=Canvas(inv_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

    inv_frame.grid_rowconfigure(0,weight=1)
    inv_frame.grid_columnconfigure(0,weight=1)

    vertibar=Scrollbar(inv_frame, orient=VERTICAL)
    vertibar.grid(row=0,column=1,sticky='ns')
    vertibar.config(command=inv_canvas.yview)
    
    inv_canvas.bind("<Configure>", inv_responsive_widgets)
    inv_canvas.config(yscrollcommand=vertibar.set)
    inv_canvas.grid(row=0,column=0,sticky='nsew')

    
    inv_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ipoly1"))

    label_1 = Label(inv_canvas,width=10,height=1,text="INVOICES", font=('arial 25'),background="#1b3857",fg="white") 
    window_label_1 = inv_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("ilabel1"))

    inv_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("ihline"))

    inv_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ipoly2"))


    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline1"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline2"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline3"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline4"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline5"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline6"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline7"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline8"))
    inv_canvas.create_line(0, 0, 0, 0, 
    fill='gray',width=1,tags=("iline9"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline10"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline11"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline12"))
    
    

    label_2 = Label(inv_canvas,width=10,height=1,text="INVOICE NO", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = inv_canvas.create_window(0, 0, anchor="nw", window=label_2,tags=('ilabel2'))

    label_3 = Label(inv_canvas,width=11,height=1,text="INVOICE DATE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_3 = inv_canvas.create_window(0, 0, anchor="nw", window=label_3,tags=('ilabel3'))

    label_4 = Label(inv_canvas,width=11,height=1,text="CUSTOMER", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('ilabel4'))

    label_4 = Label(inv_canvas,width=11,height=1,text="EMAIL ID", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('ilabel5'))

    label_4 = Label(inv_canvas,width=11,height=1,text="DUE DATE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('ilabel6'))

    label_4 = Label(inv_canvas,width=11,height=1,text="GRAND TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('ilabel7'))

    label_4 = Label(inv_canvas,width=11,height=1,text="BALANCE DUE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('ilabel8'))

    label_4 = Label(inv_canvas,width=11,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('ilabel9'))




    def add_invoice():
        inv_frame.grid_forget()
        inv_frame_1 = Frame(tab3_2)
        inv_frame_1.grid(row=0,column=0,sticky='nsew')

        def inv_responsive_widgets2(event):
            try:
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("aipoly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("ailabel1",dwidth/2.45,dheight/8.24)
                dcanvas.coords("aihline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.36


                dcanvas.coords("aipoly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("ailabel2",dwidth/2.45,dheight/2.34)
                dcanvas.coords("ailabel3",dwidth/22.80,dheight/1.90)
                dcanvas.coords("ailabel4",dwidth/20.00,dheight/1.65)
                dcanvas.coords("ailabel5",dwidth/20.00,dheight/1.37)
                dcanvas.coords("ailabel6",dwidth/3.34,dheight/1.37)
                dcanvas.coords("ailabel7",dwidth/21.66 ,dheight/1.12)
                dcanvas.coords("ailabel8",dwidth/3.34,dheight/1.12)
                dcanvas.coords("ailabel9",dwidth/19.10,dheight/0.947)
                dcanvas.coords("ailabel10",dwidth/19.40,dheight/0.717)
                dcanvas.coords("ailabel11",dwidth/16.50,dheight/0.638)
                dcanvas.coords("ailabel12",dwidth/8.40,dheight/0.638)
                dcanvas.coords("ailabel13",dwidth/3.34,dheight/0.638)
                dcanvas.coords("ailabel14",dwidth/2.28,dheight/0.638)
                dcanvas.coords("ailabel15",dwidth/1.73,dheight/0.638)
                dcanvas.coords("ailabel16",dwidth/1.52,dheight/0.638)
                dcanvas.coords("ailabel17",dwidth/1.325,dheight/0.638)
                dcanvas.coords("ailabel18",dwidth/1.165,dheight/0.638)
                dcanvas.coords("ailabel19",dwidth/16.50,dheight/0.604)
                dcanvas.coords("ailabel20",dwidth/16.50,dheight/0.562)
                dcanvas.coords("ailabel21",dwidth/16.50,dheight/0.526)
                dcanvas.coords("ailabel22",dwidth/16.50,dheight/0.496)
                dcanvas.coords("ailabel23",dwidth/1.53,dheight/0.45)
                dcanvas.coords("ailabel24",dwidth/1.54,dheight/0.435)
                dcanvas.coords("ailabel25",dwidth/1.54,dheight/0.42)
                dcanvas.coords("ailabel26",dwidth/1.54,dheight/0.406)
                dcanvas.coords("ailabel27",dwidth/1.54,dheight/0.392)
                dcanvas.coords("ailabel28",dwidth/1.72,dheight/1.12)

                dcanvas.coords("aientry1",dwidth/3.0,dheight/1.295)
                dcanvas.coords("aientry2",dwidth/18.00,dheight/0.91)
                dcanvas.coords("aientry3",dwidth/4.00,dheight/0.604)
                dcanvas.coords("aientry4",dwidth/2.51,dheight/0.604)
                dcanvas.coords("aientry5",dwidth/1.8,dheight/0.604)
                dcanvas.coords("aientry6",dwidth/1.565,dheight/0.604)
                dcanvas.coords("aientry7",dwidth/1.357,dheight/0.604)
                dcanvas.coords("aientry8",dwidth/4.00,dheight/0.562)
                dcanvas.coords("aientry9",dwidth/4.00,dheight/0.526)
                dcanvas.coords("aientry10",dwidth/4.00,dheight/0.496)
                dcanvas.coords("aientry11",dwidth/2.51,dheight/0.562)
                dcanvas.coords("aientry12",dwidth/2.51,dheight/0.526)
                dcanvas.coords("aientry13",dwidth/2.51,dheight/0.496)
                dcanvas.coords("aientry14",dwidth/1.8,dheight/0.562)
                dcanvas.coords("aientry15",dwidth/1.8,dheight/0.526)
                dcanvas.coords("aientry16",dwidth/1.8,dheight/0.496)
                dcanvas.coords("aientry17",dwidth/1.565,dheight/0.562)
                dcanvas.coords("aientry18",dwidth/1.565,dheight/0.526)
                dcanvas.coords("aientry19",dwidth/1.565,dheight/0.496)
                dcanvas.coords("aientry20",dwidth/1.357,dheight/0.562)
                dcanvas.coords("aientry21",dwidth/1.357,dheight/0.526)
                dcanvas.coords("aientry22",dwidth/1.357,dheight/0.496)
                dcanvas.coords("aientry23",dwidth/1.33,dheight/0.452)
                dcanvas.coords("aientry24",dwidth/1.33,dheight/0.4365)
                dcanvas.coords("aientry25",dwidth/1.33,dheight/0.4215)
                dcanvas.coords("aientry26",dwidth/1.33,dheight/0.407)
                dcanvas.coords("aientry27",dwidth/1.33,dheight/0.393)

                dcanvas.coords("aicombo1",dwidth/18.00,dheight/1.295)
                dcanvas.coords("aicombo2",dwidth/3.00,dheight/1.074)
                dcanvas.coords("aicombo3",dwidth/18.00,dheight/0.695)
                dcanvas.coords("aicombo4",dwidth/10.10,dheight/0.604)
                dcanvas.coords("aicombo5",dwidth/1.21,dheight/0.604)
                dcanvas.coords("aicombo6",dwidth/10.10,dheight/0.562)
                dcanvas.coords("aicombo7",dwidth/10.10,dheight/0.526)
                dcanvas.coords("aicombo8",dwidth/10.10,dheight/0.496)
                dcanvas.coords("aicombo9",dwidth/1.21,dheight/0.562)
                dcanvas.coords("aicombo10",dwidth/1.21,dheight/0.526)
                dcanvas.coords("aicombo11",dwidth/1.21,dheight/0.496)

                dcanvas.coords("aibutton1",dwidth/4.74,dheight/1.295)
                dcanvas.coords("aibutton2",dwidth/1.28,dheight/0.377)
                dcanvas.coords("aibutton3",dwidth/23,dheight/3.415)

                #-------------------------------H Lines-----------------------------------#
                dcanvas.coords("ailine1",dwidth/21,dheight/0.645,dwidth/1.055,dheight/0.645)
                dcanvas.coords("ailine2",dwidth/21,dheight/0.617,dwidth/1.055,dheight/0.617)
                dcanvas.coords("ailine3",dwidth/21,dheight/0.576,dwidth/1.055,dheight/0.576)
                dcanvas.coords("ailine4",dwidth/21,dheight/0.536,dwidth/1.055,dheight/0.536)
                dcanvas.coords("ailine5",dwidth/21,dheight/0.506,dwidth/1.055,dheight/0.506)
                dcanvas.coords("ailine6",dwidth/21,dheight/0.476,dwidth/1.055,dheight/0.476)
                #-------------------------------V Lines-----------------------------------#
                dcanvas.coords("ailine7",dwidth/21,dheight/0.645,dwidth/21,dheight/0.476)
                dcanvas.coords("ailine8",dwidth/1.055,dheight/0.645,dwidth/1.055,dheight/0.476)
                dcanvas.coords("ailine9",dwidth/11,dheight/0.645,dwidth/11,dheight/0.476)
                dcanvas.coords("ailine10",dwidth/4.15,dheight/0.645,dwidth/4.15,dheight/0.476)
                dcanvas.coords("ailine11",dwidth/2.55,dheight/0.645,dwidth/2.55,dheight/0.476)
                dcanvas.coords("ailine12",dwidth/1.83,dheight/0.645,dwidth/1.83,dheight/0.476)
                dcanvas.coords("ailine13",dwidth/1.58,dheight/0.645,dwidth/1.58,dheight/0.476)
                dcanvas.coords("ailine14",dwidth/1.37,dheight/0.645,dwidth/1.37,dheight/0.476)
                dcanvas.coords("ailine15",dwidth/1.22,dheight/0.645,dwidth/1.22,dheight/0.476)

                #-------------------------------V Lines-----------------------------------#
                dcanvas.coords("ailine16",dwidth/1.58,dheight/0.455,dwidth/1.58,dheight/0.383)
                dcanvas.coords("ailine17",dwidth/1.348,dheight/0.455,dwidth/1.348,dheight/0.383)
                dcanvas.coords("ailine18",dwidth/1.084,dheight/0.455,dwidth/1.084,dheight/0.383)
                #-------------------------------H Lines-----------------------------------#
                dcanvas.coords("ailine19",dwidth/1.58,dheight/0.455,dwidth/1.084,dheight/0.455)
                dcanvas.coords("ailine20",dwidth/1.58,dheight/0.383,dwidth/1.084,dheight/0.383)
                dcanvas.coords("ailine21",dwidth/1.58,dheight/0.439,dwidth/1.084,dheight/0.439)
                dcanvas.coords("ailine22",dwidth/1.58,dheight/0.424,dwidth/1.084,dheight/0.424)
                dcanvas.coords("ailine23",dwidth/1.58,dheight/0.41,dwidth/1.084,dheight/0.41)
                dcanvas.coords("ailine24",dwidth/1.58,dheight/0.396,dwidth/1.084,dheight/0.396)
            except:
                pass

            try:
                dcanvas.coords("aidate1",dwidth/17.8,dheight/1.074)
                dcanvas.coords("aidate2",dwidth/1.65,dheight/1.074)
            except:
                pass



        inv_canvas_1=Canvas(inv_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1800))

        inv_frame_1.grid_columnconfigure(0,weight=1)
        inv_frame_1.grid_rowconfigure(0,weight=1)
        
        vertibar=Scrollbar(inv_frame_1, orient=VERTICAL)
        vertibar.grid(row=0,column=1,sticky='ns')
        vertibar.config(command=inv_canvas_1.yview)

        inv_canvas_1.bind("<Configure>", inv_responsive_widgets2)
        inv_canvas_1.config(yscrollcommand=vertibar.set)
        inv_canvas_1.grid(row=0,column=0,sticky='nsew')

        inv_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly1"))

        
        label_1 = Label(inv_canvas_1,width=10,height=1,text="INVOICE", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel1"))

        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("aihline"))

        inv_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly2"))

        label_1 = Label(inv_canvas_1,width=10,height=1,text="Fin sYs", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel2"))

        label_2 = Label(inv_canvas_1,width=15,height=1,text="Company name", font=('arial 16'),background="#1b3857",fg="skyblue") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel3"))

        label_2 = Label(inv_canvas_1,width=15,height=1,text="Company email-id", font=('arial 16'),background="#1b3857",fg="skyblue") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel4"))

        label_2 = Label(inv_canvas_1,width=15,height=1,text="Select Customer", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel5"))

        aicomb_1 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        aicomb_1['values'] = ("Select Customer",)
        aicomb_1.current(0)
        window_aicomb_1 = inv_canvas_1.create_window(0, 0, anchor="nw", width=200, height=30,window=aicomb_1, tags=("aicombo1"))

        def add_inv_customer():
            #inv_frame.grid_forget()
            inv_frame_1.grid_forget()
            inv_frame_2 = Frame(tab3_2)
            inv_frame_2.grid(row=0,column=0,sticky='nsew')

            def inc_responsive_widgets2(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
            
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("acpoly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
                dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.45


                dcanvas.coords("acpoly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
                dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
                dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
                dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
                dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
                dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
                dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
                dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
                dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
                dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
                dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
                dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
                dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
                dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
                dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
                dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
                dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
                dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
                dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
                dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
                dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
                dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
                dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
                dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
                dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

                dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
                dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

                dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
                dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
                dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
                dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
                dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
                dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
                dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
                dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
                dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
                dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
                dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
                dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
                dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
                dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
                dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
                dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
                dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
                dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
                dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

                dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
                dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

                dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
                dcanvas.coords("acbutton2",dwidth/23,dheight/3.415)


            inv_canvas_2=Canvas(inv_frame_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

            inv_frame_2.grid_columnconfigure(0,weight=1)
            inv_frame_2.grid_rowconfigure(0,weight=1)

            
            vertibar=Scrollbar(inv_frame_2, orient=VERTICAL)
            vertibar.grid(row=0,column=1,sticky='ns')
            vertibar.config(command=inv_canvas_2.yview)

            inv_canvas_2.bind("<Configure>", inc_responsive_widgets2)
            inv_canvas_2.config(yscrollcommand=vertibar.set)
            inv_canvas_2.grid(row=0,column=0,sticky='nsew')
            

            inv_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

            label_1 = Label(inv_canvas_2,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

            inv_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

            inv_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

            label_1 = Label(inv_canvas_2,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

            inv_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

            ic_comb_cus_1 = ttk.Combobox(inv_canvas_2, font=('arial 10'),foreground="white")
            ic_comb_cus_1['values'] = ("Mr","Mrs","Miss","Ms",)
            ic_comb_cus_1.current(0)
            window_ic_comb_cus_1 = inv_canvas_2.create_window(0, 0, anchor="nw", width=245, height=30,window=ic_comb_cus_1, tags=("accombo1"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

            ic_entry_cus_1=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_1 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_1, tags=("acentry1"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

            ic_entry_cus_2=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_2 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_2, tags=("acentry2"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

            ic_entry_cus_3=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_3 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_3, tags=("acentry3"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

            ic_cus_4=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_cus_4 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_cus_4, tags=("acentry4"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

            ic_comb_cus_2 = ttk.Combobox(inv_canvas_2, font=('arial 10'),foreground="white")
            ic_comb_cus_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
            ic_comb_cus_2.current(0)
            window_ic_comb_cus_2 = inv_canvas_2.create_window(0, 0, anchor="nw", width=245, height=30,window=ic_comb_cus_2, tags=("accombo2"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))

            ic_cus_entry_str_1 = StringVar()
            ic_entry_cus_5=Entry(inv_canvas_2,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=ic_cus_entry_str_1)
            ic_cus_entry_str_1.set(' 29APPCK7465F1Z1')
            window_ic_entry_cus_5 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_5, tags=("acentry5"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

            ic_cus_entry_str_2 = StringVar()
            ic_entry_cus_6=Entry(inv_canvas_2,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=ic_cus_entry_str_2)
            ic_cus_entry_str_2.set(' APPCK7465F')
            window_ic_entry_cus_6 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_6, tags=("acentry6"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

            ic_entry_cus_7=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_7 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_7, tags=("acentry7"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

            ic_entry_cus_8=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_8 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_8, tags=("acentry8"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))

            ic_entry_cus_9=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_9 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_9, tags=("acentry9"))

            label_1 = Label(inv_canvas_2,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

            ic_entry_cus_10=Entry(inv_canvas_2,width=95,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_10 = inv_canvas_2.create_window(0, 0, anchor="nw", height=60,window=ic_entry_cus_10, tags=("acentry10"))

            label_1 = Label(inv_canvas_2,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

            ic_chk_str = StringVar()
            ic_chkbtn1 = Checkbutton(inv_canvas_2, text = "Same As Billing Address", variable = ic_chk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
            ic_chkbtn1.select()
            window_ic_chkbtn_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=ic_chkbtn1, tags=("accheck1"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

            ic_entry_cus_11=Entry(inv_canvas_2,width=95,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_11 = inv_canvas_2.create_window(0, 0, anchor="nw", height=60,window=ic_entry_cus_11, tags=("acentry11"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

            ic_entry_cus_12=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_12 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_12, tags=("acentry12"))
            
            label_2 = Label(inv_canvas_2,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

            ic_entry_cus_13=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_13 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_13, tags=("acentry13"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

            ic_entry_cus_14=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_14 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_14, tags=("acentry14"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

            ic_entry_cus_15=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_15 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_15, tags=("acentry15"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

            ic_entry_cus_12=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_12 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_12, tags=("acentry16"))
            
            label_2 = Label(inv_canvas_2,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

            ic_entry_cus_13=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_13 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_13, tags=("acentry17"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

            ic_entry_cus_14=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_14 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_14, tags=("acentry18"))

            label_2 = Label(inv_canvas_2,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

            ic_entry_cus_15=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_15 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_15, tags=("acentry19"))

            ic_chk_str_1 = StringVar()
            ic_chkbtn2 = Checkbutton(inv_canvas_2, text = "Agree to terms and conditions", variable = ic_chk_str_1, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
            ic_chkbtn2.select()
            window_ic_chkbtn_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=ic_chkbtn2,tags=("accheck2"))

            ic_cus_btn2=Button(inv_canvas_2,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_ic_cus_btn2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=ic_cus_btn2,tags=("acbutton1"))

            def inv_back_1_():
                inv_frame_2.grid_forget()
                inv_frame_1.grid(row=0,column=0,sticky='nsew')

            bck_btn1=Button(inv_canvas_2,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=inv_back_1_)
            window_bck_btn1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('acbutton2'))
            


        aibtn2=Button(inv_canvas_1,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=add_inv_customer)
        window_aibtn2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=aibtn2, tags=('aibutton1'))

        label_2 = Label(inv_canvas_1,width=15,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel6'))

        aientry_1=Entry(inv_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_aientry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30,window=aientry_1,tags=('aientry1'))


        label_2 = Label(inv_canvas_1,width=15,height=1,text="Terms", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel8'))

        comb_t_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        comb_t_2['values'] = ("Due on Receipt","NET 15","NET 30","NET 60","Add New Term",)
        comb_t_2.current(0)
        window_comb_t_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=251, height=30,window=comb_t_2,tags=('aicombo2'))


        label_2 = Label(inv_canvas_1,width=6,height=1,text="Bill To:", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel9'))

        # text_1=Text(inv_canvas_1,width=31)
        # window_text_1 = inv_canvas_1.create_window(81, 675, anchor="nw", height=150, window=text_1)
        ai_b_entry_1=Entry(inv_canvas_1,width=42,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_b_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=150, window=ai_b_entry_1,tags=('aientry2'))

        label_2 = Label(inv_canvas_1,width=12,height=1,text="Place of supply", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel10'))

        ai_p_comb_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_p_comb_2['values'] = ("Kerala","Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Other Territory",)
        ai_p_comb_2.current(0)
        window_ai_p_comb_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=251, height=30,window=ai_p_comb_2,tags=('aicombo3'))


        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine1'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine2'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine3'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine4'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine5'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine6'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine7'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine8'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine9'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine10'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine11'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine12'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine13'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine14'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine15'))


        label_2 = Label(inv_canvas_1,width=2,height=1,text="#", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel11'))

        label_3 = Label(inv_canvas_1,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_3 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_3,tags=('ailabel12'))

        label_4 = Label(inv_canvas_1,width=4,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel13'))

        label_4 = Label(inv_canvas_1,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel14'))

        label_4 = Label(inv_canvas_1,width=4,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel15'))

        label_4 = Label(inv_canvas_1,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel16'))

        label_4 = Label(inv_canvas_1,width=6,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel17'))

        label_4 = Label(inv_canvas_1,width=7,height=1,text="TAX (%)", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel18'))

        label_2 = Label(inv_canvas_1,width=2,height=1,text="1", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(90, 1020, anchor="nw", window=label_2,tags=('ailabel19'))

        ai_comb_p_1 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_p_1['values'] = ("Select Product",)
        ai_comb_p_1.current(0)
        window_ai_comb_p_1 = inv_canvas_1.create_window(0, 0, anchor="nw", width=180, height=30,window=ai_comb_p_1,tags=('aicombo4'))

        ai_entry_p_1=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1,tags=('aientry3'))

        ai_entry_p_1_2=Entry(inv_canvas_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_1_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_2,tags=('aientry4'))

        ai_entry_p_1_3=Entry(inv_canvas_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_1_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_3,tags=('aientry5'))

        ai_entry_p_1_4=Entry(inv_canvas_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_1_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_4,tags=('aientry6'))

        ai_entry_p_1_5=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_1_5 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_5,tags=('aientry7'))

        ai_comb_p_1_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_p_1_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
        ai_comb_p_1_2.current(0)
        window_ai_comb_p_1_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_p_1_2,tags=('aicombo5'))


        label_2 = Label(inv_canvas_1,width=2,height=1,text="2", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel20'))

        ai_comb_P_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_P_2['values'] = ("Select Product",)
        ai_comb_P_2.current(0)
        window_ai_comb_P_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=180, height=30,window=ai_comb_P_2,tags=('aicombo6'))

        ai_entry_p_2=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_2,tags=('aientry8'))

        ai_entry_p_2_1=Entry(inv_canvas_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_2_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_2_1,tags=('aientry11'))

        ai_entry_2_2=Entry(inv_canvas_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_2_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_2_2,tags=('aientry14'))

        ai_entry_2_3=Entry(inv_canvas_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_2_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_2_3,tags=('aientry17'))

        ai_entry_2_4=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_2_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_2_4,tags=('aientry20'))

        ai_comb_P_2_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_P_2_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
        ai_comb_P_2_2.current(0)
        window_ai_comb_P_2_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_P_2_2,tags=('aicombo9'))


        label_2 = Label(inv_canvas_1,width=2,height=1,text="3", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel21'))

        ai_comb_p_3 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_p_3['values'] = ("Select Product",)
        ai_comb_p_3.current(0)
        window_ai_comb_p_3 = inv_canvas_1.create_window(0, 0, anchor="nw", width=180, height=30,window=ai_comb_p_3,tags=('aicombo7'))

        ai_entry_3=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3,tags=('aientry9'))

        ai_entry_3_1=Entry(inv_canvas_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_3_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_1,tags=('aientry12'))

        ai_entry_3_2=Entry(inv_canvas_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_3_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_2,tags=('aientry15'))

        ai_entry_3_3=Entry(inv_canvas_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_3_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_3,tags=('aientry18'))

        ai_entry_3_4=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_3_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_4,tags=('aientry21'))

        ai_comb_P_3_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_P_3_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
        ai_comb_P_3_2.current(0)
        window_ai_comb_P_3_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_P_3_2,tags=('aicombo10'))

        label_2 = Label(inv_canvas_1,width=2,height=1,text="4", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel22'))

        ai_comb_p_4 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_p_4['values'] = ("Select Product",)
        ai_comb_p_4.current(0)
        window_ai_comb_p_4 = inv_canvas_1.create_window(0, 0, anchor="nw", width=180, height=30,window=ai_comb_p_4,tags=('aicombo8'))

        ai_entry_4=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4,tags=('aientry10'))

        ai_entry_4_1=Entry(inv_canvas_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_4_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_1,tags=('aientry13'))

        ai_entry_4_2=Entry(inv_canvas_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_4_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_2,tags=('aientry16'))

        ai_entry_4_3=Entry(inv_canvas_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_4_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_3,tags=('aientry19'))

        ai_entry_4_4=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_4_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_4,tags=('aientry22'))

        ai_comb_P_4_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_P_4_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
        ai_comb_P_4_2.current(0)
        window_ai_comb_P_4_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_P_4_2,tags=('aicombo11'))

        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine16'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine17'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine18'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine19'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine20'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine21'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine22'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine23'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine24'))
        

        label_5 = Label(inv_canvas_1,width=10,height=1,text="Sub Total", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel23'))

        label_5 = Label(inv_canvas_1,width=12,height=1,text="Tax Amount", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel24'))

        label_5 = Label(inv_canvas_1,width=12,height=1,text="Grand Total", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel25'))

        label_5 = Label(inv_canvas_1,width=12,height=1,text="Amount Received", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel26'))

        label_5 = Label(inv_canvas_1,width=12,height=1,text="Balance Due", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel27'))

        sub_entry_1=Entry(inv_canvas_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_sub_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=sub_entry_1,tags=('aientry23'))

        tax_entry_1=Entry(inv_canvas_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_tax_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=tax_entry_1,tags=('aientry24'))

        grand_entry_1=Entry(inv_canvas_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_grand_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=grand_entry_1,tags=('aientry25'))

        amount_entry_1=Entry(inv_canvas_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_amount_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=amount_entry_1,tags=('aientry26'))

        bal_entry_1=Entry(inv_canvas_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_bal_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=bal_entry_1,tags=('aientry27'))
        

        ai_save_btn1=Button(inv_canvas_1,text='Save', width=15,height=2,foreground="white",background="#1b3857",font='arial 12')
        window_ai_save_btn1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=ai_save_btn1,tags=('aibutton2'))

        def inv_back_1_():
            inv_frame_1.grid_forget()
            inv_frame.grid(row=0,column=0,sticky='nsew')

        bck_btn1=Button(inv_canvas_1,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=inv_back_1_)
        window_bck_btn1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('aibutton3'))

        label_2 = Label(inv_canvas_1,width=14,height=1,text="Invoice Date:", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel7'))

        label_2 = Label(inv_canvas_1,width=15,height=1,text="Due Date:", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel28'))

        aid_entry_1=DateEntry(inv_canvas_1,width=40,justify=LEFT,foreground='white')
        window_aid_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=aid_entry_1,tags=('aidate1'))

        aid_entry_2=DateEntry(inv_canvas_1,width=40,justify=LEFT,foreground='white')
        window_aid_entry_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=aid_entry_2,tags=('aidate2'))


    def edit_invoice(event):
        inv_frame.grid_forget()
        inv_frame_edit_1 = Frame(tab3_2)
        inv_frame_edit_1.grid(row=0,column=0,sticky='nsew')

        def inv_eresponsive_widgets2(event):
            try:
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("aipoly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("ailabel1",dwidth/2.45,dheight/8.24)
                dcanvas.coords("aihline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.36


                dcanvas.coords("aipoly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("ailabel2",dwidth/2.45,dheight/2.34)
                dcanvas.coords("ailabel3",dwidth/22.80,dheight/1.90)
                dcanvas.coords("ailabel4",dwidth/20.00,dheight/1.65)
                dcanvas.coords("ailabel5",dwidth/20.00,dheight/1.37)
                dcanvas.coords("ailabel6",dwidth/3.34,dheight/1.37)
                dcanvas.coords("ailabel7",dwidth/21.66 ,dheight/1.12)
                dcanvas.coords("ailabel8",dwidth/3.34,dheight/1.12)
                dcanvas.coords("ailabel9",dwidth/19.10,dheight/0.947)
                dcanvas.coords("ailabel10",dwidth/19.40,dheight/0.717)
                dcanvas.coords("ailabel11",dwidth/16.50,dheight/0.638)
                dcanvas.coords("ailabel12",dwidth/8.40,dheight/0.638)
                dcanvas.coords("ailabel13",dwidth/3.34,dheight/0.638)
                dcanvas.coords("ailabel14",dwidth/2.28,dheight/0.638)
                dcanvas.coords("ailabel15",dwidth/1.73,dheight/0.638)
                dcanvas.coords("ailabel16",dwidth/1.52,dheight/0.638)
                dcanvas.coords("ailabel17",dwidth/1.325,dheight/0.638)
                dcanvas.coords("ailabel18",dwidth/1.165,dheight/0.638)
                dcanvas.coords("ailabel19",dwidth/16.50,dheight/0.604)
                dcanvas.coords("ailabel20",dwidth/16.50,dheight/0.562)
                dcanvas.coords("ailabel21",dwidth/16.50,dheight/0.526)
                dcanvas.coords("ailabel22",dwidth/16.50,dheight/0.496)
                dcanvas.coords("ailabel23",dwidth/1.53,dheight/0.45)
                dcanvas.coords("ailabel24",dwidth/1.54,dheight/0.435)
                dcanvas.coords("ailabel25",dwidth/1.54,dheight/0.42)
                dcanvas.coords("ailabel26",dwidth/1.54,dheight/0.406)
                dcanvas.coords("ailabel27",dwidth/1.54,dheight/0.392)
                dcanvas.coords("ailabel28",dwidth/1.72,dheight/1.12)

                dcanvas.coords("aientry1",dwidth/3.0,dheight/1.295)
                dcanvas.coords("aientry2",dwidth/18.00,dheight/0.91)
                dcanvas.coords("aientry3",dwidth/4.00,dheight/0.604)
                dcanvas.coords("aientry4",dwidth/2.51,dheight/0.604)
                dcanvas.coords("aientry5",dwidth/1.8,dheight/0.604)
                dcanvas.coords("aientry6",dwidth/1.565,dheight/0.604)
                dcanvas.coords("aientry7",dwidth/1.357,dheight/0.604)
                dcanvas.coords("aientry8",dwidth/4.00,dheight/0.562)
                dcanvas.coords("aientry9",dwidth/4.00,dheight/0.526)
                dcanvas.coords("aientry10",dwidth/4.00,dheight/0.496)
                dcanvas.coords("aientry11",dwidth/2.51,dheight/0.562)
                dcanvas.coords("aientry12",dwidth/2.51,dheight/0.526)
                dcanvas.coords("aientry13",dwidth/2.51,dheight/0.496)
                dcanvas.coords("aientry14",dwidth/1.8,dheight/0.562)
                dcanvas.coords("aientry15",dwidth/1.8,dheight/0.526)
                dcanvas.coords("aientry16",dwidth/1.8,dheight/0.496)
                dcanvas.coords("aientry17",dwidth/1.565,dheight/0.562)
                dcanvas.coords("aientry18",dwidth/1.565,dheight/0.526)
                dcanvas.coords("aientry19",dwidth/1.565,dheight/0.496)
                dcanvas.coords("aientry20",dwidth/1.357,dheight/0.562)
                dcanvas.coords("aientry21",dwidth/1.357,dheight/0.526)
                dcanvas.coords("aientry22",dwidth/1.357,dheight/0.496)
                dcanvas.coords("aientry23",dwidth/1.33,dheight/0.452)
                dcanvas.coords("aientry24",dwidth/1.33,dheight/0.4365)
                dcanvas.coords("aientry25",dwidth/1.33,dheight/0.4215)
                dcanvas.coords("aientry26",dwidth/1.33,dheight/0.407)
                dcanvas.coords("aientry27",dwidth/1.33,dheight/0.393)
                dcanvas.coords("aientry28",dwidth/18.00,dheight/1.295)

                dcanvas.coords("aicombo2",dwidth/3.00,dheight/1.074)
                dcanvas.coords("aicombo3",dwidth/18.00,dheight/0.695)
                dcanvas.coords("aicombo4",dwidth/10.10,dheight/0.604)
                dcanvas.coords("aicombo5",dwidth/1.21,dheight/0.604)
                dcanvas.coords("aicombo6",dwidth/10.10,dheight/0.562)
                dcanvas.coords("aicombo7",dwidth/10.10,dheight/0.526)
                dcanvas.coords("aicombo8",dwidth/10.10,dheight/0.496)
                dcanvas.coords("aicombo9",dwidth/1.21,dheight/0.562)
                dcanvas.coords("aicombo10",dwidth/1.21,dheight/0.526)
                dcanvas.coords("aicombo11",dwidth/1.21,dheight/0.496)

                dcanvas.coords("aibutton1",dwidth/4.74,dheight/1.295)
                dcanvas.coords("aibutton2",dwidth/1.28,dheight/0.377)
                dcanvas.coords("aibutton3",dwidth/23,dheight/3.415)

                #-------------------------------H Lines-----------------------------------#
                dcanvas.coords("ailine1",dwidth/21,dheight/0.645,dwidth/1.055,dheight/0.645)
                dcanvas.coords("ailine2",dwidth/21,dheight/0.617,dwidth/1.055,dheight/0.617)
                dcanvas.coords("ailine3",dwidth/21,dheight/0.576,dwidth/1.055,dheight/0.576)
                dcanvas.coords("ailine4",dwidth/21,dheight/0.536,dwidth/1.055,dheight/0.536)
                dcanvas.coords("ailine5",dwidth/21,dheight/0.506,dwidth/1.055,dheight/0.506)
                dcanvas.coords("ailine6",dwidth/21,dheight/0.476,dwidth/1.055,dheight/0.476)
                #-------------------------------V Lines-----------------------------------#
                dcanvas.coords("ailine7",dwidth/21,dheight/0.645,dwidth/21,dheight/0.476)
                dcanvas.coords("ailine8",dwidth/1.055,dheight/0.645,dwidth/1.055,dheight/0.476)
                dcanvas.coords("ailine9",dwidth/11,dheight/0.645,dwidth/11,dheight/0.476)
                dcanvas.coords("ailine10",dwidth/4.15,dheight/0.645,dwidth/4.15,dheight/0.476)
                dcanvas.coords("ailine11",dwidth/2.55,dheight/0.645,dwidth/2.55,dheight/0.476)
                dcanvas.coords("ailine12",dwidth/1.83,dheight/0.645,dwidth/1.83,dheight/0.476)
                dcanvas.coords("ailine13",dwidth/1.58,dheight/0.645,dwidth/1.58,dheight/0.476)
                dcanvas.coords("ailine14",dwidth/1.37,dheight/0.645,dwidth/1.37,dheight/0.476)
                dcanvas.coords("ailine15",dwidth/1.22,dheight/0.645,dwidth/1.22,dheight/0.476)

                #-------------------------------V Lines-----------------------------------#
                dcanvas.coords("ailine16",dwidth/1.58,dheight/0.455,dwidth/1.58,dheight/0.383)
                dcanvas.coords("ailine17",dwidth/1.348,dheight/0.455,dwidth/1.348,dheight/0.383)
                dcanvas.coords("ailine18",dwidth/1.084,dheight/0.455,dwidth/1.084,dheight/0.383)
                #-------------------------------H Lines-----------------------------------#
                dcanvas.coords("ailine19",dwidth/1.58,dheight/0.455,dwidth/1.084,dheight/0.455)
                dcanvas.coords("ailine20",dwidth/1.58,dheight/0.383,dwidth/1.084,dheight/0.383)
                dcanvas.coords("ailine21",dwidth/1.58,dheight/0.439,dwidth/1.084,dheight/0.439)
                dcanvas.coords("ailine22",dwidth/1.58,dheight/0.424,dwidth/1.084,dheight/0.424)
                dcanvas.coords("ailine23",dwidth/1.58,dheight/0.41,dwidth/1.084,dheight/0.41)
                dcanvas.coords("ailine24",dwidth/1.58,dheight/0.396,dwidth/1.084,dheight/0.396)

                #-------------------------------View Section-----------------------------------#
                dcanvas.coords("aivbutton1",dwidth/1.45,dheight/8.24)
                dcanvas.coords("aivbutton2",dwidth/1.20,dheight/8.24)
                
                r2 = 5
                x11 = dwidth/12
                x21 = dwidth/1.1
                y11 = dheight/2.5
                y21 = dheight/0.38


                dcanvas.coords("aivpoly1",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("aivlabel1",dwidth/9.40,dheight/1.85)
                dcanvas.coords("aivlabel2",dwidth/9,dheight/1.70)
                dcanvas.coords("aivlabel3",dwidth/9,dheight/1.55)
                dcanvas.coords("aivlabel4",dwidth/9.45,dheight/1.42)
                dcanvas.coords("aivlabel5",dwidth/9.50,dheight/1.32)
                dcanvas.coords("aivlabel6",dwidth/9.35,dheight/1.22)
                dcanvas.coords("aivlabel7",dwidth/9.70,dheight/1.14)
                dcanvas.coords("aivlabel8",dwidth/9.50,dheight/1.0)
                dcanvas.coords("aivlabel9",dwidth/1.45,dheight/1.0)
                dcanvas.coords("aivlabel10",dwidth/1.44,dheight/0.95)
                dcanvas.coords("aivlabel11",dwidth/1.46,dheight/0.90)
                dcanvas.coords("aivlabel12",dwidth/1.48,dheight/0.85)

                dcanvas.coords("aivtree1",dwidth/7.5,dheight/0.75)

                dcanvas.coords("aivline16",dwidth/1.56,dheight/0.6,dwidth/1.56,dheight/0.52)
                dcanvas.coords("aivline17",dwidth/1.346,dheight/0.6,dwidth/1.346,dheight/0.52)
                dcanvas.coords("aivline18",dwidth/1.182,dheight/0.6,dwidth/1.182,dheight/0.52)
                dcanvas.coords("aivline19",dwidth/1.56,dheight/0.6,dwidth/1.182,dheight/0.6)
                dcanvas.coords("aivline20",dwidth/1.56,dheight/0.52,dwidth/1.182,dheight/0.52)
                dcanvas.coords("aivline21",dwidth/1.56,dheight/0.572,dwidth/1.182,dheight/0.572)
                dcanvas.coords("aivline22",dwidth/1.56,dheight/0.545,dwidth/1.182,dheight/0.545)

                dcanvas.coords("aivlabel13",dwidth/1.54,dheight/0.59)
                dcanvas.coords("aivlabel14",dwidth/1.54,dheight/0.565)
                dcanvas.coords("aivlabel15",dwidth/1.5,dheight/0.54)

                dcanvas.coords("aivline23",dwidth/10,dheight/0.4,dwidth/1.12,dheight/0.4)

                dcanvas.coords("aivlabel16",dwidth/4,dheight/0.395)

            except:
                pass

            try:
                dcanvas.coords("aidate1",dwidth/17.8,dheight/1.074)
                dcanvas.coords("aidate2",dwidth/1.65,dheight/1.074)
            except:
                pass


        inv_canvas_edit_1=Canvas(inv_frame_edit_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1800))

        inv_frame_edit_1.grid_columnconfigure(0,weight=1)
        inv_frame_edit_1.grid_rowconfigure(0,weight=1)
        
        vertibar=Scrollbar(inv_frame_edit_1, orient=VERTICAL)
        vertibar.grid(row=0,column=1,sticky='ns')
        vertibar.config(command=inv_canvas_edit_1.yview)

        inv_canvas_edit_1.bind("<Configure>", inv_eresponsive_widgets2)
        inv_canvas_edit_1.config(yscrollcommand=vertibar.set)
        inv_canvas_edit_1.grid(row=0,column=0,sticky='nsew')

        if inv_comb_1.get() == 'Edit':

            inv_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly1"))

            
            label_1 = Label(inv_canvas_edit_1,width=10,height=1,text="INVOICE", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel1"))

            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("aihline"))

            inv_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly2"))

            label_1 = Label(inv_canvas_edit_1,width=10,height=1,text="Fin sYs", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel2"))

            label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Company name", font=('arial 16'),background="#1b3857",fg="skyblue") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel3"))

            label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Company email-id", font=('arial 16'),background="#1b3857",fg="skyblue") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel4"))

            label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Select Customer", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel5"))


            eientry_1=Entry(inv_canvas_edit_1,width=42,justify=LEFT,background='#2f516f',foreground="white")
            window_eientry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=eientry_1,tags=('aientry28'))


            label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel6'))

            eaientry_1=Entry(inv_canvas_edit_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_eaientry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=eaientry_1,tags=('aientry1'))


            label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Terms", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel8'))

            ecomb_t_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            ecomb_t_2['values'] = ("Due on Receipt","NET 15","NET 30","NET 60","Add New Term",)
            ecomb_t_2.current(0)
            window_ecomb_t_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=251, height=30,window=ecomb_t_2,tags=('aicombo2'))


            label_2 = Label(inv_canvas_edit_1,width=6,height=1,text="Bill To:", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel9'))

            
            eai_b_entry_1=Entry(inv_canvas_edit_1,width=42,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_b_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=150, window=eai_b_entry_1,tags=('aientry2'))

            label_2 = Label(inv_canvas_edit_1,width=12,height=1,text="Place of supply", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel10'))

            eai_p_comb_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_p_comb_2['values'] = ("Kerala","Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Other Territory",)
            eai_p_comb_2.current(0)
            window_eai_p_comb_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=251, height=30,window=eai_p_comb_2,tags=('aicombo3'))


            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine1'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine2'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine3'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine4'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine5'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine6'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine7'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine8'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine9'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine10'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine11'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine12'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine13'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine14'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine15'))


            label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="#", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel11'))

            label_3 = Label(inv_canvas_edit_1,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_3,tags=('ailabel12'))

            label_4 = Label(inv_canvas_edit_1,width=4,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel13'))

            label_4 = Label(inv_canvas_edit_1,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel14'))

            label_4 = Label(inv_canvas_edit_1,width=4,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel15'))

            label_4 = Label(inv_canvas_edit_1,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel16'))

            label_4 = Label(inv_canvas_edit_1,width=6,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel17'))

            label_4 = Label(inv_canvas_edit_1,width=7,height=1,text="TAX (%)", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel18'))

            label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="1", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(90, 1020, anchor="nw", window=label_2,tags=('ailabel19'))

            eai_comb_p_1 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_p_1['values'] = ("Select Product",)
            eai_comb_p_1.current(0)
            window_eai_comb_p_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=180, height=30,window=eai_comb_p_1,tags=('aicombo4'))

            eai_entry_p_1=Entry(inv_canvas_edit_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1,tags=('aientry3'))

            eai_entry_p_1_2=Entry(inv_canvas_edit_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_1_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1_2,tags=('aientry4'))

            eai_entry_p_1_3=Entry(inv_canvas_edit_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_1_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1_3,tags=('aientry5'))

            eai_entry_p_1_4=Entry(inv_canvas_edit_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_1_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1_4,tags=('aientry6'))

            eai_entry_p_1_5=Entry(inv_canvas_edit_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_1_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1_5,tags=('aientry7'))

            eai_comb_p_1_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_p_1_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
            eai_comb_p_1_2.current(0)
            window_eai_comb_p_1_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=150, height=30,window=eai_comb_p_1_2,tags=('aicombo5'))


            label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="2", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel20'))

            eai_comb_P_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_P_2['values'] = ("Select Product",)
            eai_comb_P_2.current(0)
            window_eai_comb_P_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=180, height=30,window=eai_comb_P_2,tags=('aicombo6'))

            eai_entry_p_2=Entry(inv_canvas_edit_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_2,tags=('aientry8'))

            eai_entry_p_2_1=Entry(inv_canvas_edit_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_2_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_2_1,tags=('aientry11'))

            eai_entry_2_2=Entry(inv_canvas_edit_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_2_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_2_2,tags=('aientry14'))

            eai_entry_2_3=Entry(inv_canvas_edit_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_2_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_2_3,tags=('aientry17'))

            eai_entry_2_4=Entry(inv_canvas_edit_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_2_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_2_4,tags=('aientry20'))

            eai_comb_P_2_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_P_2_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
            eai_comb_P_2_2.current(0)
            window_eai_comb_P_2_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=150, height=30,window=eai_comb_P_2_2,tags=('aicombo9'))


            label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="3", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel21'))

            eai_comb_p_3 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_p_3['values'] = ("Select Product",)
            eai_comb_p_3.current(0)
            window_eai_comb_p_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=180, height=30,window=eai_comb_p_3,tags=('aicombo7'))

            eai_entry_3=Entry(inv_canvas_edit_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3,tags=('aientry9'))

            eai_entry_3_1=Entry(inv_canvas_edit_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_3_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3_1,tags=('aientry12'))

            eai_entry_3_2=Entry(inv_canvas_edit_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_3_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3_2,tags=('aientry15'))

            eai_entry_3_3=Entry(inv_canvas_edit_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_3_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3_3,tags=('aientry18'))

            eai_entry_3_4=Entry(inv_canvas_edit_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_3_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3_4,tags=('aientry21'))

            eai_comb_P_3_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_P_3_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
            eai_comb_P_3_2.current(0)
            window_eai_comb_P_3_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=150, height=30,window=eai_comb_P_3_2,tags=('aicombo10'))

            label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="4", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel22'))

            eai_comb_p_4 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_p_4['values'] = ("Select Product",)
            eai_comb_p_4.current(0)
            window_eai_comb_p_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=180, height=30,window=eai_comb_p_4,tags=('aicombo8'))

            eai_entry_4=Entry(inv_canvas_edit_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4,tags=('aientry10'))

            eai_entry_4_1=Entry(inv_canvas_edit_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_4_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4_1,tags=('aientry13'))

            eai_entry_4_2=Entry(inv_canvas_edit_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_4_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4_2,tags=('aientry16'))

            eai_entry_4_3=Entry(inv_canvas_edit_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_4_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4_3,tags=('aientry19'))

            eai_entry_4_4=Entry(inv_canvas_edit_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_4_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4_4,tags=('aientry22'))

            eai_comb_P_4_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_P_4_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
            eai_comb_P_4_2.current(0)
            window_eai_comb_P_4_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=150, height=30,window=eai_comb_P_4_2,tags=('aicombo11'))

            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine16'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine17'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine18'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine19'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine20'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine21'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine22'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine23'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine24'))
            

            label_5 = Label(inv_canvas_edit_1,width=10,height=1,text="Sub Total", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel23'))

            label_5 = Label(inv_canvas_edit_1,width=12,height=1,text="Tax Amount", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel24'))

            label_5 = Label(inv_canvas_edit_1,width=12,height=1,text="Grand Total", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel25'))

            label_5 = Label(inv_canvas_edit_1,width=12,height=1,text="Amount Received", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel26'))

            label_5 = Label(inv_canvas_edit_1,width=12,height=1,text="Balance Due", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel27'))

            esub_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
            window_esub_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=esub_entry_1,tags=('aientry23'))

            etax_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
            window_etax_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=etax_entry_1,tags=('aientry24'))

            egrand_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
            window_egrand_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=egrand_entry_1,tags=('aientry25'))

            eamount_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
            window_eamount_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eamount_entry_1,tags=('aientry26'))

            ebal_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
            window_ebal_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=ebal_entry_1,tags=('aientry27'))
            

            eai_save_btn1=Button(inv_canvas_edit_1,text='Save', width=15,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_eai_save_btn1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=eai_save_btn1,tags=('aibutton2'))

            def einv_back_1_():
                inv_frame_edit_1.grid_forget()
                inv_frame.grid(row=0,column=0,sticky='nsew')

            eibck_btn1=Button(inv_canvas_edit_1,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=einv_back_1_)
            window_eibck_btn1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=eibck_btn1,tags=('aibutton3'))

            label_2 = Label(inv_canvas_edit_1,width=14,height=1,text="Invoice Date:", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel7'))

            label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Due Date:", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel28'))

            eaid_entry_1=DateEntry(inv_canvas_edit_1,width=40,justify=LEFT,foreground='white')
            window_eaid_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eaid_entry_1,tags=('aidate1'))

            eaid_entry_2=DateEntry(inv_canvas_edit_1,width=40,justify=LEFT,foreground='white')
            window_eaid_entry_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eaid_entry_2,tags=('aidate2'))

        elif inv_comb_1.get() == 'View':

            inv_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly1"))

            
            label_1 = Label(inv_canvas_edit_1,width=10,height=1,text="INVOICE", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel1"))

            eai_dwnl_btn1=Button(inv_canvas_edit_1,text='Download Pdf', width=15,height=2,foreground="skyblue",background="#1b3857",font='arial 12')
            window_eai_dwnl_btn1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=eai_dwnl_btn1,tags=('aivbutton1'))

            eai_prnt_btn1=Button(inv_canvas_edit_1,text='Print', width=15,height=2,foreground="skyblue",background="#1b3857",font='arial 12')
            window_eai_prnt_btn1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=eai_prnt_btn1,tags=('aivbutton2'))

            inv_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly2"))

            inv_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="white",tags=("aivpoly1"))

            label_1 = Label(inv_canvas_edit_1,width=11,height=1,text="Unknown", font=('arial 12 bold'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel1"))

            label_1 = Label(inv_canvas_edit_1,width=13,height=1,text="Addressline 1", font=('arial 12 '),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel2"))

            label_1 = Label(inv_canvas_edit_1,width=13,height=1,text="Addressline 2", font=('arial 12 '),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel3"))

            label_1 = Label(inv_canvas_edit_1,width=11,height=1,text="Pincode", font=('arial 12'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel4"))

            label_1 = Label(inv_canvas_edit_1,width=11,height=1,text="Email ID", font=('arial 12'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel5"))

            label_1 = Label(inv_canvas_edit_1,width=15,height=1,text="Phone Number", font=('arial 12'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel6"))

            label_1 = Label(inv_canvas_edit_1,width=13,height=1,text="TAX INVOICE", font=('arial 20 bold'),background="white",fg="skyblue") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel7"))

            label_1 = Label(inv_canvas_edit_1,width=11,height=1,text="Bill To", font=('arial 14 bold'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel8"))

            label_1 = Label(inv_canvas_edit_1,width=11,height=1,text="Invoice No", font=('arial 12 bold'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel9"))

            label_1 = Label(inv_canvas_edit_1,width=11,height=1,text="Invoice Date", font=('arial 12 bold'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel10"))

            label_1 = Label(inv_canvas_edit_1,width=11,height=1,text="Due Date", font=('arial 12 bold'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel11"))

            label_1 = Label(inv_canvas_edit_1,width=11,height=1,text="Terms", font=('arial 12 bold'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel12"))

            style=ttk.Style()
            style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('arial 12')) # Modify the font of the body
            style.configure("mystyle.Treeview.Heading", font=('arial 12'), background='white') # Modify the font of the headings
            style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

            # Add a Treeview widge                    
            cus_prv_tree=ttk.Treeview(inv_canvas_edit_1, column=("c1", "c2","c3", "c4", "c5", "c6"), show='headings', height=40, style='mystyle.Treeview')
            cus_prv_tree.column("# 1", anchor=E, stretch=NO, width=250)
            cus_prv_tree.heading("# 1", text="PRODUCT/SERVICES")
            cus_prv_tree.column("# 2", anchor=E, stretch=NO, width=150)
            cus_prv_tree.heading("# 2", text="HSN")
            cus_prv_tree.column("# 3", anchor=E, stretch=NO, width=100)
            cus_prv_tree.heading("# 3", text="QTY")
            cus_prv_tree.column("# 4", anchor=E, stretch=NO, width=150)
            cus_prv_tree.heading("# 4", text="PRICE")
            cus_prv_tree.column("# 5", anchor=E, stretch=NO, width=150)
            cus_prv_tree.heading("# 5", text="TOTAL")
            cus_prv_tree.column("# 6", anchor=E, stretch=NO, width=160)
            cus_prv_tree.heading("# 6", text="TAX(%)")

            window = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=25, window=cus_prv_tree,tags=('aivtree1'))

            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline16'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline17'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline18'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline19'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline20'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline21'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline22'))

            label_1 = Label(inv_canvas_edit_1,width=11,height=1,text="Subtotal", font=('arial 12 bold'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel13"))

            label_1 = Label(inv_canvas_edit_1,width=11,height=1,text="Tax Amount", font=('arial 12 bold'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel14"))

            label_1 = Label(inv_canvas_edit_1,width=5,height=1,text="Total", font=('arial 12 bold'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel15"))

            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='grey',width=1, tags=('aivline23'))

            label_1 = Label(inv_canvas_edit_1,width=75,height=0,text="Invoice was created on a computer and is valid without the signature and seal.", font=('arial 12'),background="white",fg="black") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel16"))

            def einv_back_1_():
                inv_frame_edit_1.grid_forget()
                inv_frame.grid(row=0,column=0,sticky='nsew')

            eibck_btn1=Button(inv_canvas_edit_1,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=einv_back_1_)
            window_eibck_btn1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=eibck_btn1,tags=('aibutton3'))


        else:
            pass
            
        
    # Define the style for combobox widget
    # styl= ttk.Style()
    # styl.theme_use('clam')
    # styl.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")

    inv_comb_1 = ttk.Combobox(inv_canvas,)
    inv_comb_1['values'] = ("Actions","Edit","View","Delete")
    inv_comb_1.current(0)
    inv_comb_1.bind('<<ComboboxSelected>>',edit_invoice)
    window_inv_comb_1 = inv_canvas.create_window(0, 0, anchor="nw", width=110,height=30,window=inv_comb_1,tags=('icombo1'))
        

    btn1=Button(inv_canvas,text='Add Invoices', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_invoice)
    window_btn1 = inv_canvas.create_window(0, 0, anchor="nw", window=btn1,tags=('ibutton1'))

    #-------------------------------Customers-----------------------------#
    tab3_3.grid_columnconfigure(0,weight=1)
    tab3_3.grid_rowconfigure(0,weight=1)

    cus_frame = Frame(tab3_3)
    cus_frame.grid(row=0,column=0,sticky='nsew')

    def cus_responsive_widgets(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
        dcanvas.coords("cline1", dwidth/22.00, dheight/1.8, dwidth/1.060, dheight/1.8)
        dcanvas.coords("cline2", dwidth/22.00, dheight/1.8, dwidth/22.00, dheight/1.35)
        dcanvas.coords("cline3", dwidth/22.00, dheight/1.35, dwidth/1.060, dheight/1.35)
        dcanvas.coords("cline4", dwidth/1.060, dheight/1.8, dwidth/1.060, dheight/1.35)
        dcanvas.coords("cline5", dwidth/22.00, dheight/1.575, dwidth/1.060, dheight/1.575)
        dcanvas.coords("cline6", dwidth/5.00, dheight/1.8, dwidth/5.00, dheight/1.35)
        dcanvas.coords("cline7", dwidth/2.9, dheight/1.8, dwidth/2.9, dheight/1.35)
        dcanvas.coords("cline8", dwidth/2.2, dheight/1.8, dwidth/2.2, dheight/1.35)
        dcanvas.coords("cline9", dwidth/1.75, dheight/1.8, dwidth/1.75, dheight/1.35)
        dcanvas.coords("cline10", dwidth/1.37, dheight/1.8, dwidth/1.37, dheight/1.35)
        dcanvas.coords("cline11", dwidth/1.20, dheight/1.8, dwidth/1.20, dheight/1.35)
        

        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/1.021
        y1 = dheight/14 
        y2 = dheight/3.505

        dcanvas.coords("cpoly1",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        dcanvas.coords("chline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
        dcanvas.coords("clabel1",dwidth/2.5,dheight/8.00)

        r2 = 25
        x11 = dwidth/63
        x21 = dwidth/1.021
        y11 = dheight/2.8
        y21 = dheight/1.168


        dcanvas.coords("cpoly2",x11 + r2,y11,
        x11 + r2,y11,
        x21 - r2,y11,
        x21 - r2,y11,     
        x21,y11,     
        #--------------------
        x21,y11 + r2,     
        x21,y11 + r2,     
        x21,y21 - r2,     
        x21,y21 - r2,     
        x21,y21,
        #--------------------
        x21 - r2,y21,     
        x21 - r2,y21,     
        x11 + r2,y21,
        x11 + r2,y21,
        x11,y21,
        #--------------------
        x11,y21 - r2,
        x11,y21 - r2,
        x11,y11 + r2,
        x11,y11 + r2,
        x11,y11,
        )

        dcanvas.coords("clabel2",dwidth/11.5,dheight/1.74)
        dcanvas.coords("clabel3",dwidth/4.2,dheight/1.74)
        dcanvas.coords("clabel4",dwidth/2.75,dheight/1.74)
        dcanvas.coords("clabel5",dwidth/2.05,dheight/1.74)
        dcanvas.coords("clabel6",dwidth/1.60,dheight/1.74)
        dcanvas.coords("clabel7",dwidth/1.34,dheight/1.74)
        dcanvas.coords("clabel8",dwidth/1.17,dheight/1.74)
        dcanvas.coords("cbutton1",dwidth/1.28,dheight/2.4)
        dcanvas.coords("ccombo1",dwidth/1.179,dheight/1.52)

        dcanvas.coords("cclabel1",dwidth/12.5,dheight/1.52)
        dcanvas.coords("cclabel2",dwidth/4.8,dheight/1.52)
        dcanvas.coords("cclabel3",dwidth/2.85,dheight/1.52)
        dcanvas.coords("cclabel4",dwidth/2.1,dheight/1.52)
        dcanvas.coords("cclabel5",dwidth/1.64,dheight/1.52)
        dcanvas.coords("cclabel6",dwidth/1.34,dheight/1.52)

    cus_canvas=Canvas(cus_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

    cus_frame.grid_rowconfigure(0,weight=1)
    cus_frame.grid_columnconfigure(0,weight=1)

    vertibar=Scrollbar(cus_frame, orient=VERTICAL)
    vertibar.grid(row=0,column=1,sticky='ns')
    vertibar.config(command=cus_canvas.yview)
    cus_canvas.bind("<Configure>", cus_responsive_widgets)
    cus_canvas.config(yscrollcommand=vertibar.set)
    cus_canvas.grid(row=0,column=0,sticky='nsew')

    cus_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("cpoly1"))

    label_1 = Label(cus_canvas,width=12,height=1,text="CUSTOMERS", font=('arial 25'),background="#1b3857",fg="white") 
    window_label_1 = cus_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("clabel1"))

    cus_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("chline"))

    
    cus_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("cpoly2"))


    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline1"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline2"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline3"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline4"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline5"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline6"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline7"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline8"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline9"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline10"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline11"))
    
    

    label_2 = Label(cus_canvas,width=10,height=1,text="CUSTOMER", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = cus_canvas.create_window(0, 0, anchor="nw", window=label_2, tags=("clabel2"))

    label_3 = Label(cus_canvas,width=11,height=1,text="GST TYPE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_3 = cus_canvas.create_window(0, 0, anchor="nw", window=label_3, tags=("clabel3"))

    label_4 = Label(cus_canvas,width=11,height=1,text="GSTIN", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = cus_canvas.create_window(0, 0, anchor="nw", window=label_4, tags=("clabel4"))

    label_4 = Label(cus_canvas,width=8,height=1,text="PAN NO", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = cus_canvas.create_window(0, 0, anchor="nw", window=label_4, tags=("clabel5"))

    label_4 = Label(cus_canvas,width=8,height=1,text="EMAIL ID", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = cus_canvas.create_window(0, 0, anchor="nw", window=label_4, tags=("clabel6"))

    label_4 = Label(cus_canvas,width=11,height=1,text="MOBILE NO", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = cus_canvas.create_window(0, 0, anchor="nw", window=label_4, tags=("clabel7"))

    label_4 = Label(cus_canvas,width=11,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = cus_canvas.create_window(0, 0, anchor="nw", window=label_4, tags=("clabel8"))


    def add_customer():
        cus_frame.grid_forget()
        cus_frame_1 = Frame(tab3_3)
        cus_frame_1.grid(row=0,column=0,sticky='nsew')

        def cus_responsive_widgets2(event):
            dwidth = event.width
            dheight = event.height
            dcanvas = event.widget
            
            r1 = 25
            x1 = dwidth/63
            x2 = dwidth/1.021
            y1 = dheight/14 
            y2 = dheight/3.505

            dcanvas.coords("acpoly1",x1 + r1,y1,
            x1 + r1,y1,
            x2 - r1,y1,
            x2 - r1,y1,     
            x2,y1,     
            #--------------------
            x2,y1 + r1,     
            x2,y1 + r1,     
            x2,y2 - r1,     
            x2,y2 - r1,     
            x2,y2,
            #--------------------
            x2 - r1,y2,     
            x2 - r1,y2,     
            x1 + r1,y2,
            x1 + r1,y2,
            x1,y2,
            #--------------------
            x1,y2 - r1,
            x1,y2 - r1,
            x1,y1 + r1,
            x1,y1 + r1,
            x1,y1,
            )

            dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
            dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

            r2 = 25
            x11 = dwidth/63
            x21 = dwidth/1.021
            y11 = dheight/2.8
            y21 = dheight/0.45


            dcanvas.coords("acpoly2",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
            dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
            dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
            dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
            dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
            dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
            dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
            dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
            dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
            dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
            dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
            dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
            dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
            dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
            dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
            dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
            dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
            dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
            dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
            dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
            dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
            dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
            dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
            dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
            dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

            dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
            dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

            dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
            dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
            dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
            dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
            dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
            dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
            dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
            dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
            dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
            dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
            dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
            dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
            dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
            dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
            dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
            dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
            dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
            dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
            dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

            dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
            dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

            dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
            dcanvas.coords("acbutton3",dwidth/23,dheight/3.415)


        cus_canvas_1=Canvas(cus_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

        cus_frame_1.grid_columnconfigure(0,weight=1)
        cus_frame_1.grid_rowconfigure(0,weight=1)

        
        vertibar=Scrollbar(cus_frame_1, orient=VERTICAL)
        vertibar.grid(row=0,column=1,sticky='ns')
        vertibar.config(command=cus_canvas_1.yview)

        cus_canvas_1.bind("<Configure>", cus_responsive_widgets2)
        cus_canvas_1.config(yscrollcommand=vertibar.set)
        cus_canvas_1.grid(row=0,column=0,sticky='nsew')
        
        def sales_add_new_cus():
            title = comb_cus_1.get()
            firstname = entry_cus_f1.get()
            lastname = entry_cus_l2.get()
            company = entry_cus_com3.get()
            location = cus_loc4.get()
            gsttype = comb_cus_g2.get()
            gstin = entry_cus_gin5.get()
            panno = entry_cus_pan6.get()
            email = entry_cus_em7.get()
            website = entry_cus_web8.get()
            mobile = entry_cus_mob9.get()
            street = entry_cus_10.get()
            city = entry_cus_12.get()
            state = entry_cus_13.get()
            pincode = entry_cus_p12.get()
            country = entry_cus_c13.get()
            shipstreet = entry_cus_11.get()
            shipcity = entry_cus_14.get()
            shipstate = entry_cus_15.get()
            shippincode = entry_cus_pin.get()
            shipcountry = entry_cus_c15.get()

            cus_sql = "INSERT INTO app1_customer (title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cus_val=(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,1)
            fbcursor.execute(cus_sql,cus_val)
            finsysdb.commit()

        cus_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

        label_1 = Label(cus_canvas_1,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

        cus_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

        cus_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

        label_1 = Label(cus_canvas_1,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

        cus_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

        comb_cus_1 = ttk.Combobox(cus_canvas_1, font=('arial 10'))
        comb_cus_1['values'] = ("Mr","Mrs","Miss","Ms",)
        comb_cus_1.current(0)
        window_comb_cus_1 = cus_canvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_cus_1, tags=("accombo1"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

        entry_cus_f1=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_f1 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_f1, tags=("acentry1"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

        entry_cus_l2=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_l2 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_l2, tags=("acentry2"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

        entry_cus_com3=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_com3 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_com3, tags=("acentry3"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

        cus_loc4=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_cus_loc4 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=cus_loc4, tags=("acentry4"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

        comb_cus_g2 = ttk.Combobox(cus_canvas_1, font=('arial 10'))
        comb_cus_g2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
        comb_cus_g2.current(0)
        window_comb_cus_g2 = cus_canvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_cus_g2, tags=("accombo2"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))

        cus_entry_str_1 = StringVar()
        entry_cus_gin5=Entry(cus_canvas_1,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=cus_entry_str_1)
        cus_entry_str_1.set(' 29APPCK7465F1Z1')
        window_entry_cus_gin5 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_gin5, tags=("acentry5"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

        cus_entry_str_2 = StringVar()
        entry_cus_pan6=Entry(cus_canvas_1,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=cus_entry_str_2)
        cus_entry_str_2.set(' APPCK7465F')
        window_entry_cus_pan6 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_pan6, tags=("acentry6"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

        entry_cus_em7=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_em7 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_em7, tags=("acentry7"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

        entry_cus_web8=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_web8 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_web8, tags=("acentry8"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))

        entry_cus_mob9=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_mob9 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_mob9, tags=("acentry9"))

        def copy_cus_details():
            entry_cus_11.delete(0, END)
            entry_cus_11.insert(0,entry_cus_10.get())
            entry_cus_14.delete(0, END)
            entry_cus_14.insert(0,entry_cus_12.get())
            entry_cus_15.delete(0, END)
            entry_cus_15.insert(0,entry_cus_13.get())
            entry_cus_pin.delete(0, END)
            entry_cus_pin.insert(0,entry_cus_p12.get())
            entry_cus_c15.delete(0, END)
            entry_cus_c15.insert(0,entry_cus_c13.get())

        label_1 = Label(cus_canvas_1,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
        window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

        entry_cus_10=Entry(cus_canvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_10 = cus_canvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_cus_10, tags=("acentry10"))

        label_1 = Label(cus_canvas_1,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
        window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

        entry_cus_11=Entry(cus_canvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_11 = cus_canvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_cus_11, tags=("acentry11"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

        entry_cus_12=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_12 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_12, tags=("acentry12"))
        
        label_2 = Label(cus_canvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

        entry_cus_13=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_13 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_13, tags=("acentry13"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

        entry_cus_14=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_14 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_14, tags=("acentry14"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

        entry_cus_15=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_15 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_15, tags=("acentry15"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

        entry_cus_p12=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_p12 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_p12, tags=("acentry16"))
        
        label_2 = Label(cus_canvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

        entry_cus_c13=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_c13 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_c13, tags=("acentry17"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

        entry_cus_pin=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_pin = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_pin, tags=("acentry18"))

        label_2 = Label(cus_canvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

        entry_cus_c15=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_c15 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_c15, tags=("acentry19"))

        chk_str = StringVar()
        chkbtn1 = Checkbutton(cus_canvas_1, text = "Same As Billing Address", variable = chk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f",command=copy_cus_details)
        chkbtn1.select()
        window_chkbtn_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=chkbtn1, tags=("accheck1"))

        chk_str_1 = StringVar()
        chkbtn2 = Checkbutton(cus_canvas_1, text = "Agree to terms and conditions", variable = chk_str_1, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
        chkbtn2.select()
        window_chkbtn_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=chkbtn2,tags=("accheck2"))

        def ac_back_1_():
            cus_frame_1.grid_forget()
            cus_frame.grid(row=0,column=0,sticky='nsew')

        ac_bck_btn1=Button(cus_canvas_1,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=ac_back_1_)
        window_ac_bck_btn1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=ac_bck_btn1,tags=('acbutton3'))

        cus_btn2=Button(cus_canvas_1,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12',command=sales_add_new_cus)
        window_cus_btn2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=cus_btn2,tags=("acbutton1"))

    btn1=Button(cus_canvas,text='Add Customer', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_customer)
    window_btn1 = cus_canvas.create_window(0, 0, anchor="nw", window=btn1, tags=("cbutton1"))

    def edit_customer(event):
        cus_frame.grid_forget()
        cus_eframe_1 = Frame(tab3_3)
        cus_eframe_1.grid(row=0,column=0,sticky='nsew')

        def ecus_responsive_widgets2(event):
            dwidth = event.width
            dheight = event.height
            dcanvas = event.widget
            
            r1 = 25
            x1 = dwidth/63
            x2 = dwidth/1.021
            y1 = dheight/14 
            y2 = dheight/3.505

            dcanvas.coords("acpoly1",x1 + r1,y1,
            x1 + r1,y1,
            x2 - r1,y1,
            x2 - r1,y1,     
            x2,y1,     
            #--------------------
            x2,y1 + r1,     
            x2,y1 + r1,     
            x2,y2 - r1,     
            x2,y2 - r1,     
            x2,y2,
            #--------------------
            x2 - r1,y2,     
            x2 - r1,y2,     
            x1 + r1,y2,
            x1 + r1,y2,
            x1,y2,
            #--------------------
            x1,y2 - r1,
            x1,y2 - r1,
            x1,y1 + r1,
            x1,y1 + r1,
            x1,y1,
            )

            dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
            dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

            r2 = 25
            x11 = dwidth/63
            x21 = dwidth/1.021
            y11 = dheight/2.8
            y21 = dheight/0.45


            dcanvas.coords("acpoly2",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
            dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
            dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
            dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
            dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
            dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
            dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
            dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
            dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
            dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
            dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
            dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
            dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
            dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
            dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
            dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
            dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
            dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
            dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
            dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
            dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
            dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
            dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
            dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
            dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

            dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
            dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

            dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
            dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
            dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
            dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
            dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
            dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
            dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
            dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
            dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
            dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
            dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
            dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
            dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
            dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
            dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
            dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
            dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
            dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
            dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

            dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
            dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

            dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
            dcanvas.coords("acbutton3",dwidth/23,dheight/3.415)


        cus_ecanvas_1=Canvas(cus_eframe_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

        cus_eframe_1.grid_columnconfigure(0,weight=1)
        cus_eframe_1.grid_rowconfigure(0,weight=1)

        
        vertibar=Scrollbar(cus_eframe_1, orient=VERTICAL)
        vertibar.grid(row=0,column=1,sticky='ns')
        vertibar.config(command=cus_ecanvas_1.yview)

        cus_ecanvas_1.bind("<Configure>", ecus_responsive_widgets2)
        cus_ecanvas_1.config(yscrollcommand=vertibar.set)
        cus_ecanvas_1.grid(row=0,column=0,sticky='nsew')

        
        if ecus_comb_1.get() == 'Edit':

            cus_sql_2 = "SELECT * FROM app1_customer"
            fbcursor.execute(cus_sql_2)
            ecus_records = fbcursor.fetchone()

            cus_ecanvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

            label_1 = Label(cus_ecanvas_1,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

            cus_ecanvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

            cus_ecanvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

            label_1 = Label(cus_ecanvas_1,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

            cus_ecanvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

            comb_ecus_1 = ttk.Combobox(cus_ecanvas_1, font=('arial 10'))
            comb_ecus_1['values'] = ("Mr","Mrs","Miss","Ms",)
            comb_ecus_1.current(0)
            window_comb_ecus_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_ecus_1, tags=("accombo1"))
            comb_ecus_1.delete(0,'end')
            comb_ecus_1.insert(0, ecus_records[1])

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

            entry_ecus_1=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_1, tags=("acentry1"))
            entry_ecus_1.delete(0,'end')
            entry_ecus_1.insert(0, ecus_records[2])

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

            entry_ecus_2=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_2, tags=("acentry2"))
            entry_ecus_2.delete(0,'end')
            entry_ecus_2.insert(0, ecus_records[3])

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

            entry_ecus_3=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_3 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_3, tags=("acentry3"))
            entry_ecus_3.delete(0,'end')
            entry_ecus_3.insert(0, ecus_records[4])


            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

            ecus_4=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ecus_4 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=ecus_4, tags=("acentry4"))
            ecus_4.delete(0,'end')
            ecus_4.insert(0, ecus_records[5])


            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

            comb_ecus_2 = ttk.Combobox(cus_ecanvas_1, font=('arial 10'))
            comb_ecus_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
            comb_ecus_2.current(0)
            window_comb_ecus_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_ecus_2, tags=("accombo2"))
            comb_ecus_2.delete(0,'end')
            comb_ecus_2.insert(0, ecus_records[6])

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))

            ecus_entry_str_1 = StringVar()
            entry_ecus_5=Entry(cus_ecanvas_1,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=ecus_entry_str_1)
            ecus_entry_str_1.set(' 29APPCK7465F1Z1')
            window_entry_ecus_5 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_5, tags=("acentry5"))
            entry_ecus_5.delete(0,'end')
            entry_ecus_5.insert(0, ecus_records[7])

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

            ecus_entry_str_2 = StringVar()
            entry_ecus_6=Entry(cus_ecanvas_1,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=ecus_entry_str_2)
            ecus_entry_str_2.set(' APPCK7465F')
            window_entry_ecus_6 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_6, tags=("acentry6"))
            entry_ecus_6.delete(0,'end')
            entry_ecus_6.insert(0, ecus_records[8])

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

            entry_ecus_7=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_7 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_7, tags=("acentry7"))
            entry_ecus_7.delete(0,'end')
            entry_ecus_7.insert(0, ecus_records[9])


            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

            entry_ecus_8=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_8 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_8, tags=("acentry8"))
            entry_ecus_8.delete(0,'end')
            entry_ecus_8.insert(0, ecus_records[10])

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))
            

            entry_ecus_9=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_9 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_9, tags=("acentry9"))
            entry_ecus_9.delete(0,'end')
            entry_ecus_9.insert(0, ecus_records[11])

            label_1 = Label(cus_ecanvas_1,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
            window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

            entry_ecus_10=Entry(cus_ecanvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_10 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_ecus_10, tags=("acentry10"))
            entry_ecus_10.delete(0,'end')
            entry_ecus_10.insert(0, ecus_records[12])


            label_1 = Label(cus_ecanvas_1,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
            window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

            echk_str = StringVar()
            echkbtn1 = Checkbutton(cus_ecanvas_1, text = "Same As Billing Address", variable = echk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
            echkbtn1.select()
            window_echkbtn_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=echkbtn1, tags=("accheck1"))

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

            entry_ecus_11=Entry(cus_ecanvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_11 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_ecus_11, tags=("acentry11"))
            entry_ecus_11.delete(0,'end')
            entry_ecus_11.insert(0, ecus_records[17])

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

            entry_ecus_12=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_12 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_12, tags=("acentry12"))
            entry_ecus_12.delete(0,'end')
            entry_ecus_12.insert(0, ecus_records[13])
            
            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

            entry_ecus_13=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_13 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_13, tags=("acentry13"))
            entry_ecus_13.delete(0,'end')
            entry_ecus_13.insert(0, ecus_records[14])

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

            entry_ecus_14=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_14 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_14, tags=("acentry14"))
            entry_ecus_14.delete(0,'end')
            entry_ecus_14.insert(0, ecus_records[18])

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

            entry_ecus_15=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_15 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_15, tags=("acentry15"))
            entry_ecus_15.delete(0,'end')
            entry_ecus_15.insert(0, ecus_records[19])

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

            entry_ecus_p12=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_p12 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_p12, tags=("acentry16"))
            entry_ecus_p12.delete(0,'end')
            entry_ecus_p12.insert(0, ecus_records[15])
            
            label_2 = Label(cus_ecanvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

            entry_ecus_c13=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_c13 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_c13, tags=("acentry17"))
            entry_ecus_c13.delete(0,'end')
            entry_ecus_c13.insert(0, ecus_records[16])

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

            entry_ecus_pin14=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_pin14 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_pin14, tags=("acentry18"))
            entry_ecus_pin14.delete(0,'end')
            entry_ecus_pin14.insert(0, ecus_records[20])

            label_2 = Label(cus_ecanvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

            entry_ecus_co15=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_co15 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_co15, tags=("acentry19"))
            entry_ecus_co15.delete(0,'end')
            entry_ecus_co15.insert(0, ecus_records[21])

            echk_str_1 = StringVar()
            echkbtn2 = Checkbutton(cus_ecanvas_1, text = "Agree to terms and conditions", variable = echk_str_1, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
            echkbtn2.select()
            window_echkbtn_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=echkbtn2,tags=("accheck2"))

            def ec_back_1_():
                cus_eframe_1.grid_forget()
                cus_frame.grid(row=0,column=0,sticky='nsew')

            ec_bck_btn1=Button(cus_ecanvas_1,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=ec_back_1_)
            window_ec_bck_btn1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=ec_bck_btn1,tags=('acbutton3'))

            ecus_btn2=Button(cus_ecanvas_1,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_ecus_btn2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=ecus_btn2,tags=("acbutton1"))
        else:
            pass
    
    cus_sql_1 = "SELECT * FROM app1_customer"
    fbcursor.execute(cus_sql_1)
    cus_records = fbcursor.fetchone()

    label_2 = Label(cus_canvas,width=16,height=1,text=""+cus_records[1]+" "+""+cus_records[2]+""+cus_records[3], font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = cus_canvas.create_window(0, 0, anchor="nw", window=label_2, tags=("cclabel1"))

    label_2 = Label(cus_canvas,width=18,height=1,text=cus_records[6], font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = cus_canvas.create_window(0, 0, anchor="nw", window=label_2, tags=("cclabel2"))

    label_2 = Label(cus_canvas,width=16,height=1,text=cus_records[7], font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = cus_canvas.create_window(0, 0, anchor="nw", window=label_2, tags=("cclabel3"))

    label_2 = Label(cus_canvas,width=11,height=1,text=cus_records[8], font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = cus_canvas.create_window(0, 0, anchor="nw", window=label_2, tags=("cclabel4"))

    label_2 = Label(cus_canvas,width=15,height=1,text=cus_records[9], font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = cus_canvas.create_window(0, 0, anchor="nw", window=label_2, tags=("cclabel5"))

    label_2 = Label(cus_canvas,width=11,height=1,text=cus_records[11], font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = cus_canvas.create_window(0, 0, anchor="nw", window=label_2, tags=("cclabel6"))


    # Define the style for combobox widget
    # style= ttk.Style()
    # style.theme_use('clam')
    # style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")

    ecus_comb_1 = ttk.Combobox(cus_canvas,)
    ecus_comb_1['values'] = ['Actions','Edit','Delete']
    ecus_comb_1.current(0)
    ecus_comb_1.bind('<<ComboboxSelected>>',edit_customer)
    window_ecus_comb_1 = cus_canvas.create_window(0, 0, anchor="nw", width=110,height=30,window=ecus_comb_1, tags=("ccombo1"))

    # btn1=Button(cus_canvas,text='Add Customer', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_customer)
    # window_btn1 = cus_canvas.create_window(0, 0, anchor="nw", window=btn1, tags=("cbutton1"))

    #---------------------------Product & Services------------------------#
    tab3_4.grid_columnconfigure(0,weight=1)
    tab3_4.grid_rowconfigure(0,weight=1)

    pro_frame = Frame(tab3_4)
    pro_frame.grid(row=0,column=0,sticky='nsew')

    def pro_responsive_widgets(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget

        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/1.021
        y1 = dheight/14 
        y2 = dheight/3.505

        dcanvas.coords("ppoly1",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        dcanvas.coords("phline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
        dcanvas.coords("plabel1",dwidth/2.75,dheight/8.00)

        r2 = 25
        x11 = dwidth/63
        x21 = dwidth/1.021
        y11 = dheight/2.8
        y21 = dheight/0.850


        dcanvas.coords("ppoly2",x11 + r2,y11,
        x11 + r2,y11,
        x21 - r2,y11,
        x21 - r2,y11,     
        x21,y11,     
        #--------------------
        x21,y11 + r2,     
        x21,y11 + r2,     
        x21,y21 - r2,     
        x21,y21 - r2,     
        x21,y21,
        #--------------------
        x21 - r2,y21,     
        x21 - r2,y21,     
        x11 + r2,y21,
        x11 + r2,y21,
        x11,y21,
        #--------------------
        x11,y21 - r2,
        x11,y21 - r2,
        x11,y11 + r2,
        x11,y11 + r2,
        x11,y11,
        )

        dcanvas.coords("pline1", dwidth/22.00, dheight/1.24, dwidth/1.060, dheight/1.24)
        dcanvas.coords("pline2", dwidth/22.00, dheight/1.13, dwidth/1.060, dheight/1.13)
        dcanvas.coords("pline3", dwidth/22.00, dheight/1.015, dwidth/1.060, dheight/1.015)
        dcanvas.coords("pline4", dwidth/22.00, dheight/1.24, dwidth/22.00, dheight/1.015)
        dcanvas.coords("pline5", dwidth/1.060, dheight/1.24, dwidth/1.060, dheight/1.015)
        dcanvas.coords("pline6", dwidth/5.00, dheight/1.24, dwidth/5.00, dheight/1.015)
        dcanvas.coords("pline7", dwidth/2.50, dheight/1.24, dwidth/2.50, dheight/1.015)
        dcanvas.coords("pline8", dwidth/1.80, dheight/1.24, dwidth/1.80, dheight/1.015)
        dcanvas.coords("pline9", dwidth/1.40, dheight/1.24, dwidth/1.40, dheight/1.015)
        dcanvas.coords("pline10", dwidth/1.20, dheight/1.24, dwidth/1.20, dheight/1.015)

        dcanvas.coords("pimage1",dwidth/5.29,dheight/2.15)
        dcanvas.coords("pimage2",dwidth/2.05,dheight/2.15)

        dcanvas.coords("plabel2",dwidth/5.60,dheight/1.60)
        dcanvas.coords("plabel3",dwidth/2.09,dheight/1.60)
        dcanvas.coords("plabel4",dwidth/10.55,dheight/1.21)
        dcanvas.coords("plabel5",dwidth/3.60,dheight/1.21)
        dcanvas.coords("plabel6",dwidth/2.15,dheight/1.21)
        dcanvas.coords("plabel7",dwidth/1.63,dheight/1.21)
        dcanvas.coords("plabel8",dwidth/1.35,dheight/1.21)
        dcanvas.coords("plabel9",dwidth/1.17,dheight/1.21)

        dcanvas.coords("pcombo1",dwidth/1.18,dheight/1.10)
        dcanvas.coords("pbutton1",dwidth/1.28,dheight/1.45)

    pro_canvas=Canvas(pro_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

    pro_frame.grid_rowconfigure(0,weight=1)
    pro_frame.grid_columnconfigure(0,weight=1)

    vertibar=Scrollbar(pro_frame, orient=VERTICAL)
    vertibar.grid(row=0,column=1,sticky='ns')
    vertibar.config(command=pro_canvas.yview)
    
    pro_canvas.bind("<Configure>", pro_responsive_widgets)
    pro_canvas.config(yscrollcommand=vertibar.set)
    pro_canvas.grid(row=0,column=0,sticky='nsew')

    
    pro_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ppoly1"))
    
    label_1 = Label(pro_canvas,width=23,height=1,text="PRODUCT AND SERVICES", font=('arial 25'),background="#1b3857",fg="white") 
    window_label_1 = pro_canvas.create_window(480, 85, anchor="nw", window=label_1, tags=("plabel1"))

    pro_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("phline"))

    pro_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ppoly2"))


    image_1 = Image.open("images/lowstock.png")
    resize_image = image_1.resize((90,90))
    image_1 = ImageTk.PhotoImage(resize_image)
    btlogo = Label(pro_canvas, width=90, height=90, background="#1b3857", image = image_1) 
    window_image = pro_canvas.create_window(0, 0, anchor="nw", window=btlogo,tags=('pimage1'))
    btlogo.photo = image_1

    label_2 = Label(pro_canvas,width=14,height=1,text="LOW STOCK : ", font=('arial 18'),background="#1b3857",fg="white") 
    window_label_2 = pro_canvas.create_window(0, 0, anchor="nw", window=label_2,tags=('plabel2'))

    image_2 = Image.open("images/outofstock.png")
    resize_image_1 = image_2.resize((90,90))
    image_2 = ImageTk.PhotoImage(resize_image_1)
    btlogo_1 = Label(pro_canvas, width=90, height=90, background="#1b3857", image = image_2) 
    window_image_1 = pro_canvas.create_window(0, 0, anchor="nw", window=btlogo_1,tags=('pimage2'))
    btlogo_1.photo = image_2

    label_2 = Label(pro_canvas,width=15,height=1,text="OUT OF STOCK : ", font=('arial 18'),background="#1b3857",fg="white") 
    window_label_2 = pro_canvas.create_window(0, 0, anchor="nw", window=label_2,tags=('plabel3'))


    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline1'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline2'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline3'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline4'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline5'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline6'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline7'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline8'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline9'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline10'))


    label_2 = Label(pro_canvas,width=9,height=1,text="TYPE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = pro_canvas.create_window(0, 0, anchor="nw", window=label_2,tags=('plabel4'))

    label_3 = Label(pro_canvas,width=5,height=1,text="NAME", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_3 = pro_canvas.create_window(0, 0, anchor="nw", window=label_3,tags=('plabel5'))

    label_4 = Label(pro_canvas,width=5,height=1,text="SKU", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = pro_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('plabel6'))

    label_4 = Label(pro_canvas,width=8,height=1,text="HSN/SAC", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = pro_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('plabel7'))

    label_4 = Label(pro_canvas,width=11,height=1,text="QUANTITY", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = pro_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('plabel8'))

    label_4 = Label(pro_canvas,width=11,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = pro_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('plabel9'))

   
    # Define the style for combobox widget
    # style= ttk.Style(canvas)
    # style.theme_use('clam')
    # style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")

    cus_comb_1 = ttk.Combobox(pro_canvas,font=('arial 10'),foreground="white")
    cus_comb_1['values'] = ("Actions","Edit","Delete")
    cus_comb_1.current(0)
    window_cus_comb_1 = pro_canvas.create_window(1135, 560, anchor="nw", width=110,height=30,window=cus_comb_1,tags=('pcombo1'))


    def add_product():
        pro_frame.grid_forget()
        pro_frame_1 = Frame(tab3_4)
        pro_frame_1.grid(row=0,column=0,sticky='nsew')

        def pro_responsive_widgets_1(event):
            dwidth = event.width
            dheight = event.height
            dcanvas = event.widget
            
            r1 = 25
            x1 = dwidth/63
            x2 = dwidth/1.021
            y1 = dheight/14 
            y2 = dheight/3.505

            dcanvas.coords("appoly1",x1 + r1,y1,
            x1 + r1,y1,
            x2 - r1,y1,
            x2 - r1,y1,     
            x2,y1,     
            #--------------------
            x2,y1 + r1,     
            x2,y1 + r1,     
            x2,y2 - r1,     
            x2,y2 - r1,     
            x2,y2,
            #--------------------
            x2 - r1,y2,     
            x2 - r1,y2,     
            x1 + r1,y2,
            x1 + r1,y2,
            x1,y2,
            #--------------------
            x1,y2 - r1,
            x1,y2 - r1,
            x1,y1 + r1,
            x1,y1 + r1,
            x1,y1,
            )

            dcanvas.coords("aplabel1",dwidth/3,dheight/8.24)
            dcanvas.coords("aphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

            r2 = 25
            x11 = dwidth/63
            x21 = dwidth/1.021
            y11 = dheight/2.8
            y21 = dheight/0.60


            dcanvas.coords("appoly2",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            r2 = 25
            x11 = dwidth/7
            x21 = dwidth/2.07
            y11 = dheight/2.0
            y21 = dheight/1.1


            dcanvas.coords("appoly3",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            dcanvas.coords("aplabel2",dwidth/3.9,dheight/1.75)
            dcanvas.coords("aplabel3",dwidth/6.30,dheight/1.54)
            dcanvas.coords("apbutton1",dwidth/4.1,dheight/1.30)

            r2 = 25
            x11 = dwidth/1.93
            x21 = dwidth/1.15
            y11 = dheight/2.0
            y21 = dheight/1.1


            dcanvas.coords("appoly4",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            dcanvas.coords("aplabel4",dwidth/1.58,dheight/1.75)
            dcanvas.coords("aplabel5",dwidth/1.85,dheight/1.54)
            dcanvas.coords("apbutton2",dwidth/1.6,dheight/1.30)

            r2 = 25
            x11 = dwidth/7
            x21 = dwidth/2.07
            y11 = dheight/1.0
            y21 = dheight/0.719


            dcanvas.coords("appoly5",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            dcanvas.coords("aplabel6",dwidth/3.9,dheight/0.95)
            dcanvas.coords("aplabel7",dwidth/6.30,dheight/0.88)
            dcanvas.coords("apbutton3",dwidth/4.1,dheight/0.80)

            r2 = 25
            x11 = dwidth/1.93
            x21 = dwidth/1.15
            y11 = dheight/1.0
            y21 = dheight/0.719


            dcanvas.coords("appoly6",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            dcanvas.coords("aplabel8",dwidth/1.58,dheight/0.95)
            dcanvas.coords("aplabel9",dwidth/1.85,dheight/0.88)
            dcanvas.coords("apbutton4",dwidth/1.6,dheight/0.80)
            dcanvas.coords("apbutton5",dwidth/23,dheight/3.415)


        p_canvas_1=Canvas(pro_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1000))

        pro_frame_1.grid_columnconfigure(0,weight=1)
        pro_frame_1.grid_rowconfigure(0,weight=1)
        
        vertibar=Scrollbar(pro_frame_1, orient=VERTICAL)
        vertibar.grid(row=0,column=1,sticky='ns')
        vertibar.config(command=p_canvas_1.yview)

        p_canvas_1.bind("<Configure>", pro_responsive_widgets_1)
        p_canvas_1.config(yscrollcommand=vertibar.set)
        p_canvas_1.grid(row=0,column=0,sticky='nsew')
        
        
        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("appoly1"))

        label_1 = Label(p_canvas_1,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aplabel1"))

        p_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("aphline"))

        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("appoly2"))

        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly3"))

        label_1 = Label(p_canvas_1,width=10,height=1,text="Inventory", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel2'))

        label_1 = Label(p_canvas_1,width=45,height=2,text="Inventory is the goods available for sale and raw materials \nused to produce goods available for sale.", font=('arial 12'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel3'))

        def inv_add_item():
            pro_frame_1.grid_forget()
            pro_frame_2 = Frame(tab3_4)
            pro_frame_2.grid(row=0,column=0,sticky='nsew')

            def pro_responsive_widgets_2(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
            
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("ippoly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("iplabel1",dwidth/3,dheight/8.24)
                dcanvas.coords("iphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.29


                dcanvas.coords("ippoly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                r2 = 25
                x11 = dwidth/24
                x21 = dwidth/1.050
                y11 = dheight/2.1
                y21 = dheight/1.35


                dcanvas.coords("ippoly3",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("iplabel2",dwidth/2.5,dheight/1.77)
                dcanvas.coords("ipbutton1",dwidth/1.8,dheight/1.77)

                dcanvas.coords("iplabel3",dwidth/23.2,dheight/1.23)
                dcanvas.coords("iplabel4",dwidth/23.3,dheight/1.02)
                dcanvas.coords("iplabel5",dwidth/1.9,dheight/1.02)
                dcanvas.coords("iplabel6",dwidth/1.9,dheight/0.92)
                dcanvas.coords("iplabel7",dwidth/27,dheight/0.865)
                dcanvas.coords("iplabel8",dwidth/1.915,dheight/0.865)
                dcanvas.coords("iplabel9",dwidth/50,dheight/0.76)
                dcanvas.coords("iplabel10",dwidth/2.95,dheight/0.76)
                dcanvas.coords("iplabel11",dwidth/1.54,dheight/0.76)
                dcanvas.coords("iplabel12",dwidth/38,dheight/0.675)
                dcanvas.coords("iplabel13",dwidth/26.8,dheight/0.606)
                dcanvas.coords("iplabel14",dwidth/28.3,dheight/0.538)
                dcanvas.coords("iplabel15",dwidth/1.9,dheight/0.538)
                dcanvas.coords("iplabel16",dwidth/28.4,dheight/0.485)
                dcanvas.coords("iplabel17",dwidth/29.3,dheight/0.438)
                dcanvas.coords("iplabel18",dwidth/28,dheight/0.401)
                dcanvas.coords("iplabel19",dwidth/1.91,dheight/0.401)
                dcanvas.coords("iplabel20",dwidth/28,dheight/0.37)
                dcanvas.coords("iplabel21",dwidth/26,dheight/0.35)
                dcanvas.coords("iplabel22",dwidth/1.9,dheight/0.35)

                dcanvas.coords("ipentry1",dwidth/23.2,dheight/1.165)
                dcanvas.coords("ipentry2",dwidth/23.2,dheight/0.975)
                dcanvas.coords("ipentry3",dwidth/1.9,dheight/0.975)
                dcanvas.coords("ipentry4",dwidth/1.9,dheight/0.83)
                dcanvas.coords("ipentry5",dwidth/23.2,dheight/0.73)
                dcanvas.coords("ipentry6",dwidth/1.52,dheight/0.73)
                dcanvas.coords("ipentry7",dwidth/23.2,dheight/0.59)
                dcanvas.coords("ipentry8",dwidth/23.2,dheight/0.525)
                dcanvas.coords("ipentry9",dwidth/23.2,dheight/0.43)
                dcanvas.coords("ipentry10",dwidth/23.2,dheight/0.394)
                dcanvas.coords("ipentry11",dwidth/23.2,dheight/0.344)

                dcanvas.coords("ipcombo1",dwidth/23.2,dheight/0.83)
                dcanvas.coords("ipcombo2",dwidth/23.2,dheight/0.654)
                dcanvas.coords("ipcombo3",dwidth/1.9,dheight/0.525)
                dcanvas.coords("ipcombo4",dwidth/23.2,dheight/0.474)
                dcanvas.coords("ipcombo5",dwidth/1.89,dheight/0.394)
                dcanvas.coords("ipcombo6",dwidth/23.2,dheight/0.364)
                dcanvas.coords("ipcombo7",dwidth/1.89,dheight/0.344)

                dcanvas.coords("ipcbutton1",dwidth/23.2,dheight/0.51)
                dcanvas.coords("ipcbutton2",dwidth/23.2,dheight/0.385)

                dcanvas.coords("ipbutton2",dwidth/2.45,dheight/0.654)
                dcanvas.coords("ipbutton3",dwidth/2.45,dheight/0.474)
                dcanvas.coords("ipbutton4",dwidth/2.45,dheight/0.364)
                dcanvas.coords("ipbutton5",dwidth/2.38,dheight/0.325)

                dcanvas.coords("iphline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)

                try:
                    dcanvas.coords("ipdate1",dwidth/2.9,dheight/0.73)
                except:
                    pass


            p_canvas_2=Canvas(pro_frame_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

            pro_frame_2.grid_columnconfigure(0,weight=1)
            pro_frame_2.grid_rowconfigure(0,weight=1)
        
            vertibar=Scrollbar(pro_frame_2, orient=VERTICAL)
            vertibar.grid(row=0,column=1,sticky='ns')
            vertibar.config(command=p_canvas_2.yview)

            p_canvas_2.bind("<Configure>", pro_responsive_widgets_2)
            p_canvas_2.config(yscrollcommand=vertibar.set)
            p_canvas_2.grid(row=0,column=0,sticky='nsew')


            p_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('ippoly1'))

            label_1 = Label(p_canvas_2,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel1'))

            p_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iphline'))

            p_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('ippoly2'))

            p_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('ippoly3'))

            label_1 = Label(p_canvas_2,width=10,height=2,text="INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel2'))

            btn_item_1=Button(p_canvas_2,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
            window_btn_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=btn_item_1, tags=('ipbutton1'))

            label_1 = Label(p_canvas_2,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel3'))

            entry_inv_item_1=Entry(p_canvas_2,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_1, tags=('ipentry1'))

            label_1 = Label(p_canvas_2,width=4,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel4'))

            str_inv_item_1 = StringVar()
            entry_inv_item_2=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_inv_item_1)
            str_inv_item_1.set('  Eg: N41554')
            window_entry_entry_inv_item_2 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_2, tags=('ipentry2'))

            label_1 = Label(p_canvas_2,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel5'))

            entry_inv_item_2=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_2 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_2, tags=('ipentry3'))

            label_1 = Label(p_canvas_2,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel6'))

            label_1 = Label(p_canvas_2,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel7'))

            comb_inv_item_1 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_1['values'] = ("Choose...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards",)
            comb_inv_item_1.current(0)
            window_comb_inv_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_1, tags=('ipcombo1'))

            label_1 = Label(p_canvas_2,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel8'))

            entry_inv_item_3=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_3 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_3,tags=('ipentry4'))

            label_1 = Label(p_canvas_2,width=24,height=1,text="Initial quantity on hand", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel9'))

            entry_inv_item_4=Entry(p_canvas_2,width=60,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_4 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_4,tags=('ipentry5'))

            label_1 = Label(p_canvas_2,width=10,height=1,text="As of date", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel10'))
  
            label_1 = Label(p_canvas_2,width=14,height=1,text="Low stock alert", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel11'))

            entry_inv_item_6=Entry(p_canvas_2,width=60,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_6 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_6,tags=('ipentry6'))

            label_1 = Label(p_canvas_2,width=22,height=1,text="Inventory asset account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(35, 910, anchor="nw", window=label_1,tags=('iplabel12'))

            comb_inv_item_2 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_2['values'] = ("Inventory Asset",)
            comb_inv_item_2.current(0)
            window_comb_inv_item_2 = p_canvas_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_item_2,tags=('ipcombo2'))

            def inv_acc_create_1():
                pro_frame_2.grid_forget()
                pro_frame_2_1 = Frame(tab3_4)
                pro_frame_2_1.grid(row=0,column=0,sticky='nsew')
                def pro_responsive_widgets_2_1(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
                
                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/1.021
                    y1 = dheight/14 
                    y2 = dheight/3.505

                    dcanvas.coords("iapoly1",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    dcanvas.coords("ialabel1",dwidth/3,dheight/8.24)
                    dcanvas.coords("iahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                    r2 = 25
                    x11 = dwidth/63
                    x21 = dwidth/1.021
                    y11 = dheight/2.8
                    y21 = dheight/0.52


                    dcanvas.coords("iapoly2",x11 + r2,y11,
                    x11 + r2,y11,
                    x21 - r2,y11,
                    x21 - r2,y11,     
                    x21,y11,     
                    #--------------------
                    x21,y11 + r2,     
                    x21,y11 + r2,     
                    x21,y21 - r2,     
                    x21,y21 - r2,     
                    x21,y21,
                    #--------------------
                    x21 - r2,y21,     
                    x21 - r2,y21,     
                    x11 + r2,y21,
                    x11 + r2,y21,
                    x11,y21,
                    #--------------------
                    x11,y21 - r2,
                    x11,y21 - r2,
                    x11,y11 + r2,
                    x11,y11 + r2,
                    x11,y11,
                    )

                    dcanvas.coords("iabutton3",dwidth/23,dheight/3.415)

                    dcanvas.coords("ialabel2",dwidth/23,dheight/1.91)
                    dcanvas.coords("ialabel3",dwidth/1.9,dheight/1.91)
                    dcanvas.coords("ialabel4",dwidth/23.3,dheight/1.41)
                    dcanvas.coords("ialabel5",dwidth/1.9,dheight/1.41)
                    dcanvas.coords("ialabel6",dwidth/1.9,dheight/0.95)

                    dcanvas.coords("iaentry1",dwidth/1.9,dheight/1.74)
                    dcanvas.coords("iaentry2",dwidth/1.9,dheight/1.32)

                    dcanvas.coords("iacombo1",dwidth/23,dheight/1.74)
                    dcanvas.coords("iacombo2",dwidth/23,dheight/1.32)
                    dcanvas.coords("iacombo3",dwidth/1.9,dheight/1.09)
                    dcanvas.coords("iacombo4",dwidth/1.9,dheight/0.91)

                    dcanvas.coords("iatext1",dwidth/23,dheight/1.15)
                    dcanvas.coords("iacheck1",dwidth/1.9,dheight/1.155)

                    dcanvas.coords("iabutton1",dwidth/2.3,dheight/0.73)

                p_canvas_2_1=Canvas(pro_frame_2_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                pro_frame_2_1.grid_columnconfigure(0,weight=1)
                pro_frame_2_1.grid_rowconfigure(0,weight=1)
                
                vertibar=Scrollbar(pro_frame_2_1, orient=VERTICAL)
                vertibar.grid(row=0,column=1,sticky='ns')
                vertibar.config(command=p_canvas_2_1.yview)

                p_canvas_2_1.bind("<Configure>", pro_responsive_widgets_2_1)
                p_canvas_2_1.config(yscrollcommand=vertibar.set)
                p_canvas_2_1.grid(row=0,column=0,sticky='nsew')


                p_canvas_2_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly1'))

                label_1 = Label(p_canvas_2_1,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ialabel1'))

                p_canvas_2_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iahline'))

                p_canvas_2_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly2'))

                label_1 = Label(p_canvas_2_1,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel2'))

                comb_inv_1_1 = ttk.Combobox(p_canvas_2_1, font=('arial 10'),foreground="white")
                comb_inv_1_1['values'] = ("Current Assets",)
                comb_inv_1_1.current(0)
                window_comb_inv_1_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_1_1,tags=('iacombo1'))

                label_1 = Label(p_canvas_2_1,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel3'))

                entry_inv_1_2=Entry(p_canvas_2_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_inv_1_2 = p_canvas_2_1.create_window(0, 0, anchor="nw", height=30,window=entry_inv_1_2,tags=('iaentry1'))

                label_1 = Label(p_canvas_2_1,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel4'))

                comb_inv_1_2 = ttk.Combobox(p_canvas_2_1, font=('arial 10'),foreground="white")
                comb_inv_1_2['values'] = ("Inventory",)
                comb_inv_1_2.current(0)
                window_comb_inv_1_2 = p_canvas_2_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_1_2,tags=('iacombo2'))

                label_1 = Label(p_canvas_2_1,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel5'))

                entry_inv_1_4=Entry(p_canvas_2_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_inv_1_4 = p_canvas_2_1.create_window(0, 0, anchor="nw", height=30,window=entry_inv_1_4,tags=('iaentry2'))

                inv_text_1 = Text(p_canvas_2_1,width=67, height=14, background='black',foreground='white')
                inv_text_1.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_inv_text_1 = p_canvas_2_1.create_window(0, 0, anchor="nw",window=inv_text_1,tags=('iatext1'))

                chk_str_inv_1_1 = StringVar()
                chkbtn_inv_1_1 = Checkbutton(p_canvas_2_1, text = "Is sub-account", variable = chk_str_inv_1_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_inv_1_1.select()
                window_chkbtn_inv_1_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=chkbtn_inv_1_1,tags=('iacheck1'))

                comb_inv_1_3 = ttk.Combobox(p_canvas_2_1, font=('arial 10'),foreground="white")
                comb_inv_1_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_inv_1_3.current(0)
                window_comb_inv_1_3 = p_canvas_2_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_1_3,tags=('iacombo3'))

                label_1 = Label(p_canvas_2_1,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel6'))

                comb_inv_1_4 = ttk.Combobox(p_canvas_2_1, font=('arial 10'),foreground="white")
                comb_inv_1_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                comb_inv_1_4.current(0)
                window_comb_inv_1_4 = p_canvas_2_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_1_4,tags=('iacombo4'))


                inv_sub_btn_1_1=Button(p_canvas_2_1,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_inv_sub_btn_1_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=inv_sub_btn_1_1,tags=('iabutton1'))

                def i_back_1_():
                    pro_frame_2_1.grid_forget()
                    pro_frame_2.grid(row=0,column=0,sticky='nsew')

                bck_btn1=Button(p_canvas_2_1,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=i_back_1_)
                window_bck_btn1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('iabutton3'))

                

            asset_btn=Button(p_canvas_2,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_acc_create_1)
            window_asset_btn = p_canvas_2.create_window(0, 0, anchor="nw", window=asset_btn,tags=('ipbutton2'))

            label_1 = Label(p_canvas_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel13'))

            entry_inv_item_7=Entry(p_canvas_2,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_7 = p_canvas_2.create_window(0, 0, anchor="nw", height=60,window=entry_inv_item_7,tags=('ipentry7'))

            label_1 = Label(p_canvas_2,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel14'))
            
            entry_inv_item_8=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_8 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_8,tags=('ipentry8'))

            chk_str_inv_item = StringVar()
            chkbtn_inv_item_1 = Checkbutton(p_canvas_2, text = "Inclusive of tax", variable = chk_str_inv_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
            chkbtn_inv_item_1.select()
            window_chkbtn_inv_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=chkbtn_inv_item_1,tags=('ipcbutton1'))

            label_1 = Label(p_canvas_2,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel15'))

            comb_inv_item_3 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_inv_item_3.current(0)
            window_comb_inv_item_3 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_3,tags=('ipcombo3'))

            label_1 = Label(p_canvas_2,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel16'))

            comb_inv_item_4 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_4['values'] = ("Choose...","Billable Expense Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales of Product Income","Uncategorised Income",)
            comb_inv_item_4.current(0)
            window_comb_inv_item_4 = p_canvas_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_item_4,tags=('ipcombo4'))

            def inv_inc_acc_1():
                pro_frame_2.grid_forget()
                pro_frame_2_2 = Frame(tab3_4)
                pro_frame_2_2.grid(row=0,column=0,sticky='nsew')

                def pro_responsive_widgets_2_2(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
                
                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/1.021
                    y1 = dheight/14 
                    y2 = dheight/3.505

                    dcanvas.coords("iapoly1",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    dcanvas.coords("ialabel1",dwidth/3,dheight/8.24)
                    dcanvas.coords("iahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                    r2 = 25
                    x11 = dwidth/63
                    x21 = dwidth/1.021
                    y11 = dheight/2.8
                    y21 = dheight/0.52


                    dcanvas.coords("iapoly2",x11 + r2,y11,
                    x11 + r2,y11,
                    x21 - r2,y11,
                    x21 - r2,y11,     
                    x21,y11,     
                    #--------------------
                    x21,y11 + r2,     
                    x21,y11 + r2,     
                    x21,y21 - r2,     
                    x21,y21 - r2,     
                    x21,y21,
                    #--------------------
                    x21 - r2,y21,     
                    x21 - r2,y21,     
                    x11 + r2,y21,
                    x11 + r2,y21,
                    x11,y21,
                    #--------------------
                    x11,y21 - r2,
                    x11,y21 - r2,
                    x11,y11 + r2,
                    x11,y11 + r2,
                    x11,y11,
                    )

                    dcanvas.coords("iabutton3",dwidth/23,dheight/3.415)

                    dcanvas.coords("ialabel2",dwidth/23,dheight/1.91)
                    dcanvas.coords("ialabel3",dwidth/1.9,dheight/1.91)
                    dcanvas.coords("ialabel4",dwidth/23.3,dheight/1.41)
                    dcanvas.coords("ialabel5",dwidth/1.9,dheight/1.41)
                    dcanvas.coords("ialabel6",dwidth/1.9,dheight/0.95)

                    dcanvas.coords("iaentry1",dwidth/1.9,dheight/1.74)
                    dcanvas.coords("iaentry2",dwidth/1.9,dheight/1.32)

                    dcanvas.coords("iacombo1",dwidth/23,dheight/1.74)
                    dcanvas.coords("iacombo2",dwidth/23,dheight/1.32)
                    dcanvas.coords("iacombo3",dwidth/1.9,dheight/1.09)
                    dcanvas.coords("iacombo4",dwidth/1.9,dheight/0.91)

                    dcanvas.coords("iatext1",dwidth/23,dheight/1.15)
                    dcanvas.coords("iacheck1",dwidth/1.9,dheight/1.155)

                    dcanvas.coords("iabutton1",dwidth/2.3,dheight/0.73)

                p_canvas_2_2=Canvas(pro_frame_2_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                pro_frame_2_2.grid_columnconfigure(0,weight=1)
                pro_frame_2_2.grid_rowconfigure(0,weight=1)
                
                vertibar=Scrollbar(pro_frame_2_2, orient=VERTICAL)
                vertibar.grid(row=0,column=1,sticky='ns')
                vertibar.config(command=p_canvas_2_2.yview)

                p_canvas_2_2.bind("<Configure>", pro_responsive_widgets_2_2)
                p_canvas_2_2.config(yscrollcommand=vertibar.set)
                p_canvas_2_2.grid(row=0,column=0,sticky='nsew')


                p_canvas_2_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly1'))

                label_1 = Label(p_canvas_2_2,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1, tags=('ialabel1'))

                p_canvas_2_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iahline'))

                p_canvas_2_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly2'))

                label_1 = Label(p_canvas_2_2,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel2'))

                comb_inv_2_1 = ttk.Combobox(p_canvas_2_2, font=('arial 10'),foreground="white")
                comb_inv_2_1['values'] = ("Income",)
                comb_inv_2_1.current(0)
                window_comb_inv_2_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_2_1,tags=('iacombo1'))

                label_1 = Label(p_canvas_2_2,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel3'))

                entry_inv_2_2=Entry(p_canvas_2_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_inv_2_2 = p_canvas_2_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_2_2,tags=('iaentry1'))

                label_1 = Label(p_canvas_2_2,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel4'))

                comb_inv_2_2 = ttk.Combobox(p_canvas_2_2, font=('arial 10'),foreground="white")
                comb_inv_2_2['values'] = ("Sales of Product Income",)
                comb_inv_2_2.current(0)
                window_comb_inv_2_2 = p_canvas_2_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_2_2,tags=('iacombo2'))

                label_1 = Label(p_canvas_2_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel5'))

                entry_inv_2_4=Entry(p_canvas_2_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_inv_2_4 = p_canvas_2_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_2_4,tags=('iaentry2'))

                inv_text_2 = Text(p_canvas_2_2,width=67, height=14, background='black',foreground='white')
                inv_text_2.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_inv_text_2 = p_canvas_2_2.create_window(0, 0, anchor="nw",window=inv_text_2,tags=('iatext1'))

                chk_str_inv_2_1 = StringVar()
                chkbtn_inv_2_1 = Checkbutton(p_canvas_2_2, text = "Is sub-account", variable = chk_str_inv_2_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_inv_2_1.select()
                window_chkbtn_inv_2_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=chkbtn_inv_2_1,tags=('iacheck1'))

                comb_inv_2_3 = ttk.Combobox(p_canvas_2_2, font=('arial 10'),foreground="white")
                comb_inv_2_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_inv_2_3.current(0)
                window_comb_inv_2_3 = p_canvas_2_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_2_3,tags=('iacombo3'))

                label_1 = Label(p_canvas_2_2,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel6'))

                comb_inv_2_4 = ttk.Combobox(p_canvas_2_2, font=('arial 10'),foreground="white")
                comb_inv_2_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                comb_inv_2_4.current(0)
                window_comb_inv_2_4 = p_canvas_2_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_2_4,tags=('iacombo4'))

                inv_sub_btn_2_1=Button(p_canvas_2_2,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_inv_sub_btn_2_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=inv_sub_btn_2_1,tags=('iabutton1'))

                def i_back_2_():
                    pro_frame_2_2.grid_forget()
                    pro_frame_2.grid(row=0,column=0,sticky='nsew')

                bck_btn1=Button(p_canvas_2_2,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=i_back_2_)
                window_bck_btn1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('iabutton3'))


            account_btn=Button(p_canvas_2,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_inc_acc_1)
            window_account_btn = p_canvas_2.create_window(0, 0, anchor="nw", window=account_btn,tags=('ipbutton3'))

            p_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iphline1'))

            label_1 = Label(p_canvas_2,width=22,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel17'))

            entry_inv_item_9=Entry(p_canvas_2,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_9 = p_canvas_2.create_window(0, 0, anchor="nw", height=60,window=entry_inv_item_9,tags=('ipentry9'))

            label_1 = Label(p_canvas_2,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel18'))
            
            entry_inv_item_10=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_10 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_10,tags=('ipentry10'))

            chk_str_inv_item_1 = StringVar()
            chkbtn_inv_item_2 = Checkbutton(p_canvas_2, text = "Inclusive of purchase tax", variable = chk_str_inv_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
            chkbtn_inv_item_2.select()
            window_chkbtn_inv_item_2 = p_canvas_2.create_window(0, 0, anchor="nw", window=chkbtn_inv_item_2,tags=('ipcbutton2'))

            label_1 = Label(p_canvas_2,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(700, 1530, anchor="nw", window=label_1,tags=('iplabel19'))

            comb_inv_item_5 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_inv_item_5.current(0)
            window_comb_inv_item_5 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_5,tags=('ipcombo5'))

            label_1 = Label(p_canvas_2,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel20'))

            comb_inv_item_6 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_6['values'] = ("Cost of sales",)
            comb_inv_item_6.current(0)
            window_comb_inv_item_6 = p_canvas_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_item_6,tags=('ipcombo6'))

            def inv_exp_acc_1():
                pro_frame_2.grid_forget()
                pro_frame_2_3 = Frame(tab3_4)
                pro_frame_2_3.grid(row=0,column=0,sticky='nsew')

                def pro_responsive_widgets_2_3(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
                
                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/1.021
                    y1 = dheight/14 
                    y2 = dheight/3.505

                    dcanvas.coords("iapoly1",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    dcanvas.coords("ialabel1",dwidth/3,dheight/8.24)
                    dcanvas.coords("iahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                    r2 = 25
                    x11 = dwidth/63
                    x21 = dwidth/1.021
                    y11 = dheight/2.8
                    y21 = dheight/0.52


                    dcanvas.coords("iapoly2",x11 + r2,y11,
                    x11 + r2,y11,
                    x21 - r2,y11,
                    x21 - r2,y11,     
                    x21,y11,     
                    #--------------------
                    x21,y11 + r2,     
                    x21,y11 + r2,     
                    x21,y21 - r2,     
                    x21,y21 - r2,     
                    x21,y21,
                    #--------------------
                    x21 - r2,y21,     
                    x21 - r2,y21,     
                    x11 + r2,y21,
                    x11 + r2,y21,
                    x11,y21,
                    #--------------------
                    x11,y21 - r2,
                    x11,y21 - r2,
                    x11,y11 + r2,
                    x11,y11 + r2,
                    x11,y11,
                    )

                    dcanvas.coords("iabutton3",dwidth/23,dheight/3.415)

                    dcanvas.coords("ialabel2",dwidth/23,dheight/1.91)
                    dcanvas.coords("ialabel3",dwidth/1.9,dheight/1.91)
                    dcanvas.coords("ialabel4",dwidth/23.3,dheight/1.41)
                    dcanvas.coords("ialabel5",dwidth/1.9,dheight/1.41)
                    dcanvas.coords("ialabel6",dwidth/1.9,dheight/0.95)

                    dcanvas.coords("iaentry1",dwidth/1.9,dheight/1.74)
                    dcanvas.coords("iaentry2",dwidth/1.9,dheight/1.32)

                    dcanvas.coords("iacombo1",dwidth/23,dheight/1.74)
                    dcanvas.coords("iacombo2",dwidth/23,dheight/1.32)
                    dcanvas.coords("iacombo3",dwidth/1.9,dheight/1.09)
                    dcanvas.coords("iacombo4",dwidth/1.9,dheight/0.91)

                    dcanvas.coords("iatext1",dwidth/23,dheight/1.15)
                    dcanvas.coords("iacheck1",dwidth/1.9,dheight/1.155)

                    dcanvas.coords("iabutton1",dwidth/2.3,dheight/0.73)

                p_canvas_2_3=Canvas(pro_frame_2_3, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
                
                pro_frame_2_3.grid_columnconfigure(0,weight=1)
                pro_frame_2_3.grid_rowconfigure(0,weight=1)

                vertibar=Scrollbar(pro_frame_2_3, orient=VERTICAL)
                vertibar.grid(row=0,column=1,sticky='ns')
                vertibar.config(command=p_canvas_2_3.yview)

                p_canvas_2_3.bind("<Configure>", pro_responsive_widgets_2_3)
                p_canvas_2_3.config(yscrollcommand=vertibar.set)
                p_canvas_2_3.grid(row=0,column=0,sticky='nsew')


                p_canvas_2_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly1'))

                label_1 = Label(p_canvas_2_3,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1, tags=('ialabel1'))

                p_canvas_2_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iahline'))

                p_canvas_2_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly2'))

                label_1 = Label(p_canvas_2_3,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel2'))

                comb_inv_3_1 = ttk.Combobox(p_canvas_2_3, font=('arial 10'),foreground="white")
                comb_inv_3_1['values'] = ("Cost of Goods Sold",)
                comb_inv_3_1.current(0)
                window_comb_inv_3_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_3_1,tags=('iacombo1'))

                label_1 = Label(p_canvas_2_3,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel3'))

                entry_inv_3_2=Entry(p_canvas_2_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_inv_3_2 = p_canvas_2_3.create_window(0, 0, anchor="nw", height=30,window=entry_inv_3_2,tags=('iaentry1'))

                label_1 = Label(p_canvas_2_3,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel4'))

                comb_inv_3_2 = ttk.Combobox(p_canvas_2_3, font=('arial 10'),foreground="white")
                comb_inv_3_2['values'] = ("Suppliers and Materials-COS",)
                comb_inv_3_2.current(0)
                window_comb_inv_3_2 = p_canvas_2_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_3_2,tags=('iacombo2'))

                label_1 = Label(p_canvas_2_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel5'))

                entry_inv_3_4=Entry(p_canvas_2_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_inv_3_4 = p_canvas_2_3.create_window(0, 0, anchor="nw", height=30,window=entry_inv_3_4,tags=('iaentry2'))

                inv_text_3 = Text(p_canvas_2_3,width=67, height=14, background='black',foreground='white')
                inv_text_3.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_inv_text_3 = p_canvas_2_3.create_window(0, 0, anchor="nw",window=inv_text_3,tags=('iatext1'))

                chk_str_inv_3_1 = StringVar()
                chkbtn_inv_3_1 = Checkbutton(p_canvas_2_3, text = "Is sub-account", variable = chk_str_inv_3_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_inv_3_1.select()
                window_chkbtn_inv_3_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=chkbtn_inv_3_1,tags=('iacheck1'))

                comb_inv_3_3 = ttk.Combobox(p_canvas_2_3, font=('arial 10'),foreground="white")
                comb_inv_3_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_inv_3_3.current(0)
                window_comb_inv_3_3 = p_canvas_2_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_3_3,tags=('iacombo3'))

                label_1 = Label(p_canvas_2_3,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel6'))

                comb_inv_3_4 = ttk.Combobox(p_canvas_2_3, font=('arial 10'),foreground="white")
                comb_inv_3_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                comb_inv_3_4.current(0)
                window_comb_inv_3_4 = p_canvas_2_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_3_4,tags=('iacombo4'))

                inv_sub_btn_3_1=Button(p_canvas_2_3,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_inv_sub_btn_3_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=inv_sub_btn_3_1,tags=('iabutton1'))

                def i_back_3_():
                    pro_frame_2_3.grid_forget()
                    pro_frame_2.grid(row=0,column=0,sticky='nsew')

                bck_btn3=Button(p_canvas_2_3,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=i_back_3_)
                window_bck_btn3 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=bck_btn3,tags=('iabutton3'))


            expense_btn=Button(p_canvas_2,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_exp_acc_1)
            window_expense_btn = p_canvas_2.create_window(0, 0, anchor="nw", window=expense_btn,tags=('ipbutton4'))

            label_1 = Label(p_canvas_2,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel21'))

            str_inv_item_2 = StringVar()
            entry_inv_item_11=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_inv_item_2)
            str_inv_item_2.set(' 0')
            window_entry_entry_inv_item_11 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_11,tags=('ipentry11'))

            label_1 = Label(p_canvas_2,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel22'))

            comb_inv_item_7 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_7['values'] = ("Select Supplier",)
            comb_inv_item_7.current(0)
            window_comb_inv_item_7 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_7,tags=('ipcombo7'))

            inv_sub_btn1=Button(p_canvas_2,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_inv_sub_btn1 = p_canvas_2.create_window(0, 0, anchor="nw", window=inv_sub_btn1,tags=('ipbutton5'))

            entry_inv_item_5=DateEntry(p_canvas_2,width=60,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_5 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_5,tags=('ipdate1'))


        p_btn_1=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=inv_add_item)
        window_p_btn_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_1,tags=('apbutton1'))

        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly4"))

        label_1 = Label(p_canvas_1,width=11,height=1,text="Non-Inventory", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel4'))

        label_1 = Label(p_canvas_1,width=46,height=2,text="A non-inventory is a type of product that is procured, sold, \nconsumed in production but we do not keep inventories for it.", font=('arial 12'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel5'))

        def non_add_item():
            pro_frame_1.grid_forget()
            pro_frame_3 = Frame(tab3_4)
            pro_frame_3.grid(row=0,column=0,sticky='nsew')
            def pro_responsive_widgets_3(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
            
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("nppoly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("nplabel1",dwidth/3,dheight/8.24)
                dcanvas.coords("nphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.29


                dcanvas.coords("nppoly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                r2 = 25
                x11 = dwidth/24
                x21 = dwidth/1.050
                y11 = dheight/2.1
                y21 = dheight/1.35


                dcanvas.coords("nppoly3",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("nplabel2",dwidth/3,dheight/1.77)
                dcanvas.coords("npbutton1",dwidth/1.8,dheight/1.77)

                dcanvas.coords("nplabel3",dwidth/23.2,dheight/1.23)
                dcanvas.coords("nplabel4",dwidth/23.3,dheight/1.02)
                dcanvas.coords("nplabel5",dwidth/1.9,dheight/1.02)
                dcanvas.coords("nplabel6",dwidth/1.9,dheight/0.92)
                dcanvas.coords("nplabel7",dwidth/27,dheight/0.865)
                dcanvas.coords("nplabel8",dwidth/1.915,dheight/0.865)
                dcanvas.coords("nplabel12",dwidth/26,dheight/0.675)
                dcanvas.coords("nplabel13",dwidth/26.8,dheight/0.606)
                dcanvas.coords("nplabel14",dwidth/28.3,dheight/0.538)
                dcanvas.coords("nplabel15",dwidth/1.9,dheight/0.538)
                dcanvas.coords("nplabel16",dwidth/28.4,dheight/0.485)
                dcanvas.coords("nplabel17",dwidth/50,dheight/0.438)
                dcanvas.coords("nplabel18",dwidth/26,dheight/0.420)
                dcanvas.coords("nplabel20",dwidth/28,dheight/0.368)
                dcanvas.coords("nplabel21",dwidth/2.6,dheight/0.368)
                dcanvas.coords("nplabel22",dwidth/1.5,dheight/0.368)

                dcanvas.coords("nplabel9",dwidth/23.2,dheight/0.392)
                dcanvas.coords("nplabel10",dwidth/1.9,dheight/0.392)


                dcanvas.coords("npentry1",dwidth/23.2,dheight/1.165)
                dcanvas.coords("npentry2",dwidth/23.2,dheight/0.975)
                dcanvas.coords("npentry3",dwidth/1.9,dheight/0.975)
                dcanvas.coords("npentry4",dwidth/1.9,dheight/0.83)
                dcanvas.coords("npentry7",dwidth/23.2,dheight/0.59)
                dcanvas.coords("npentry8",dwidth/23.2,dheight/0.525)
                dcanvas.coords("npentry9",dwidth/23.2,dheight/0.43)
                dcanvas.coords("npentry10",dwidth/23.2,dheight/0.412)
                dcanvas.coords("npentry11",dwidth/2.6,dheight/0.362)

                dcanvas.coords("npcentry2",dwidth/23.2,dheight/0.385)
                dcanvas.coords("npcentry3",dwidth/1.9,dheight/0.385)

                dcanvas.coords("npcombo1",dwidth/23.2,dheight/0.83)
                dcanvas.coords("npcombo3",dwidth/1.9,dheight/0.525)
                dcanvas.coords("npcombo4",dwidth/23.2,dheight/0.474)
                dcanvas.coords("npcombo6",dwidth/23.2,dheight/0.362)
                dcanvas.coords("npcombo7",dwidth/1.5,dheight/0.362)

                dcanvas.coords("npbutton2",dwidth/23.2,dheight/0.654)
                dcanvas.coords("npbutton3",dwidth/2.45,dheight/0.474)
                dcanvas.coords("npbutton4",dwidth/3.37,dheight/0.362)
                dcanvas.coords("npbutton5",dwidth/2.38,dheight/0.345)

                dcanvas.coords("npcbutton1",dwidth/23.2,dheight/0.51)
                dcanvas.coords("npcbutton2",dwidth/23.2,dheight/0.378)

                dcanvas.coords("npline1",dwidth/21,dheight/0.73,dwidth/1.055,dheight/0.73)
                dcanvas.coords("nphline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)


            p_canvas_3=Canvas(pro_frame_3, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

            pro_frame_3.grid_columnconfigure(0,weight=1)
            pro_frame_3.grid_rowconfigure(0,weight=1)
          
            vertibar=Scrollbar(pro_frame_3, orient=VERTICAL)
            vertibar.grid(row=0,column=1,sticky='ns')
            vertibar.config(command=p_canvas_3.yview)

            p_canvas_3.bind("<Configure>", pro_responsive_widgets_3)
            p_canvas_3.config(yscrollcommand=vertibar.set)
            p_canvas_3.grid(row=0,column=0,sticky='nsew')

            p_canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('nppoly1'))

            label_1 = Label(p_canvas_3,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel1'))

            p_canvas_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('nphline'))

            p_canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('nppoly2'))

            p_canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('nppoly3'))

            label_1 = Label(p_canvas_3,width=15,height=2,text="NON-INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel2'))

            btn_non_item_2=Button(p_canvas_3,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
            window_btn_non_item_2 = p_canvas_3.create_window(0, 0, anchor="nw", window=btn_non_item_2, tags=('npbutton1'))

            label_1 = Label(p_canvas_3,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel3'))

            entry_non_item_1=Entry(p_canvas_3,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_1 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_1, tags=('npentry1'))

            label_1 = Label(p_canvas_3,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel4'))

            str_non_item_1 = StringVar()
            entry_non_iitem_2=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_non_item_1)
            str_non_item_1.set('  Eg: N41554')
            window_entry_non_iitem_2 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_iitem_2, tags=('npentry2'))

            label_1 = Label(p_canvas_3,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel5'))

            entry_non_item_2=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_2 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_2, tags=('npentry3'))

            label_non_1 = Label(p_canvas_3,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
            window_label_non_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_non_1, tags=('nplabel6'))

            label_1 = Label(p_canvas_3,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel7'))

            comb_inv_item_1 = ttk.Combobox(p_canvas_3, font=('arial 10'),foreground="white")
            comb_inv_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards","OTH Others",)
            comb_inv_item_1.current(0)
            window_comb_inv_item_1 = p_canvas_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_1, tags=('npcombo1'))

            label_1 = Label(p_canvas_3,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel8'))

            entry_non_item_3=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_inv_item_3 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_3,tags=('npentry4'))

            p_canvas_3.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('npline1'))

            label_1 = Label(p_canvas_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel12'))

            chk_str_non_item = StringVar()
            chkbtn_non_item = Checkbutton(p_canvas_3, text = "I sell this product/service to my customers.", variable = chk_str_non_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
            window_chkbtn_non_item = p_canvas_3.create_window(0, 0, anchor="nw", window=chkbtn_non_item,tags=('npbutton2'))

            label_1 = Label(p_canvas_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel13'))

            entry_non_item_7=Entry(p_canvas_3,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_7 = p_canvas_3.create_window(0, 0, anchor="nw", height=60,window=entry_non_item_7,tags=('npentry7'))

            label_1 = Label(p_canvas_3,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel14'))
            
            entry_non_item_8=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_8 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_8,tags=('npentry8'))

            chk_str_non_item_1 = StringVar()
            chkbtn_non_item_1 = Checkbutton(p_canvas_3, text = "Inclusive of tax", variable = chk_str_non_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
            chkbtn_non_item_1.select()
            window_chkbtn_non_item_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=chkbtn_non_item_1,tags=('npcbutton1'))

            label_1 = Label(p_canvas_3,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel15'))

            comb_non_item_3 = ttk.Combobox(p_canvas_3, font=('arial 10'),foreground="white")
            comb_non_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_non_item_3.current(0)
            window_comb_non_item_3 = p_canvas_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_item_3,tags=('npcombo3'))

            label_1 = Label(p_canvas_3,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel16'))

            comb_non_item_4 = ttk.Combobox(p_canvas_3, font=('arial 10'),foreground="white")
            comb_non_item_4['values'] = ("Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discount","Sales of Product Income","Services","Unapplied Cash Payment Income","Uncategorised Income",)
            comb_non_item_4.current(0)
            window_comb_non_item_4 = p_canvas_3.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_non_item_4,tags=('npcombo4'))

            def non_inc_acc_1():
                pro_frame_3.grid_forget()
                pro_frame_3_1 = Frame(tab3_4)
                pro_frame_3_1.grid(row=0,column=0,sticky='nsew')

                def pro_responsive_widgets_non_1(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
                
                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/1.021
                    y1 = dheight/14 
                    y2 = dheight/3.505

                    dcanvas.coords("napoly1",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    dcanvas.coords("nalabel1",dwidth/3,dheight/8.24)
                    dcanvas.coords("nahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                    r2 = 25
                    x11 = dwidth/63
                    x21 = dwidth/1.021
                    y11 = dheight/2.8
                    y21 = dheight/0.52


                    dcanvas.coords("napoly2",x11 + r2,y11,
                    x11 + r2,y11,
                    x21 - r2,y11,
                    x21 - r2,y11,     
                    x21,y11,     
                    #--------------------
                    x21,y11 + r2,     
                    x21,y11 + r2,     
                    x21,y21 - r2,     
                    x21,y21 - r2,     
                    x21,y21,
                    #--------------------
                    x21 - r2,y21,     
                    x21 - r2,y21,     
                    x11 + r2,y21,
                    x11 + r2,y21,
                    x11,y21,
                    #--------------------
                    x11,y21 - r2,
                    x11,y21 - r2,
                    x11,y11 + r2,
                    x11,y11 + r2,
                    x11,y11,
                    )

                    dcanvas.coords("nabutton3",dwidth/23,dheight/3.415)

                    dcanvas.coords("nalabel2",dwidth/23,dheight/1.91)
                    dcanvas.coords("nalabel3",dwidth/1.9,dheight/1.91)
                    dcanvas.coords("nalabel4",dwidth/23.3,dheight/1.41)
                    dcanvas.coords("nalabel5",dwidth/1.9,dheight/1.41)
                    dcanvas.coords("nalabel6",dwidth/1.9,dheight/0.95)

                    dcanvas.coords("naentry1",dwidth/1.9,dheight/1.74)
                    dcanvas.coords("naentry2",dwidth/1.9,dheight/1.32)

                    dcanvas.coords("nacombo1",dwidth/23,dheight/1.74)
                    dcanvas.coords("nacombo2",dwidth/23,dheight/1.32)
                    dcanvas.coords("nacombo3",dwidth/1.9,dheight/1.09)
                    dcanvas.coords("nacombo4",dwidth/1.9,dheight/0.91)

                    dcanvas.coords("natext1",dwidth/23,dheight/1.15)
                    dcanvas.coords("nacheck1",dwidth/1.9,dheight/1.155)

                    dcanvas.coords("nabutton1",dwidth/2.3,dheight/0.73)

                p_canvas_3_1=Canvas(pro_frame_3_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                pro_frame_3_1.grid_columnconfigure(0,weight=1)
                pro_frame_3_1.grid_rowconfigure(0,weight=1)
                
                vertibar=Scrollbar(pro_frame_3_1, orient=VERTICAL)
                vertibar.grid(row=0,column=1,sticky='ns')
                vertibar.config(command=p_canvas_3_1.yview)

                p_canvas_3_1.bind("<Configure>", pro_responsive_widgets_non_1)
                p_canvas_3_1.config(yscrollcommand=vertibar.set)
                p_canvas_3_1.grid(row=0,column=0,sticky='nsew')

                
                p_canvas_3_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('napoly1'))

                label_1 = Label(p_canvas_3_1,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1, tags=('nalabel1'))

                p_canvas_3_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('nahline'))

                p_canvas_3_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('napoly2'))

                label_1 = Label(p_canvas_3_1,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel2'))

                comb_non_2_1 = ttk.Combobox(p_canvas_3_1, font=('arial 10'),foreground="white")
                comb_non_2_1['values'] = ("Income",)
                comb_non_2_1.current(0)
                window_comb_non_2_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_2_1,tags=('nacombo1'))

                label_1 = Label(p_canvas_3_1,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel3'))

                entry_non_2_2=Entry(p_canvas_3_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_non_2_2 = p_canvas_3_1.create_window(0, 0, anchor="nw", height=30,window=entry_non_2_2,tags=('naentry1'))

                label_1 = Label(p_canvas_3_1,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel4'))

                comb_non_2_2 = ttk.Combobox(p_canvas_3_1, font=('arial 10'),foreground="white")
                comb_non_2_2['values'] = ("Discounts/Refunds Given","Non-Profit Income","Other Primary Income","Revenue-General","Sales-Retail","Sales-Wholesale","Sales of Product Income","Service/Fee Income","Unapplied Cash Payment Inncome",)
                comb_non_2_2.current(0)
                window_comb_non_2_2 = p_canvas_3_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_2_2,tags=('nacombo2'))

                label_1 = Label(p_canvas_3_1,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel5'))

                entry_non_2_4=Entry(p_canvas_3_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_non_2_4 = p_canvas_3_1.create_window(0, 0, anchor="nw", height=30,window=entry_non_2_4,tags=('naentry2'))

                non_text_2 = Text(p_canvas_3_1,width=67, height=14, background='black',foreground='white')
                non_text_2.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_non_text_2 = p_canvas_3_1.create_window(0, 0, anchor="nw",window=non_text_2,tags=('natext1'))

                chk_str_non_2_1 = StringVar()
                chkbtn_non_2_1 = Checkbutton(p_canvas_3_1, text = "Is sub-account", variable = chk_str_non_2_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_non_2_1.select()
                window_chkbtn_non_2_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=chkbtn_non_2_1,tags=('nacheck1'))

                comb_non_2_3 = ttk.Combobox(p_canvas_3_1, font=('arial 10'),foreground="white")
                comb_non_2_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_non_2_3.current(0)
                window_comb_non_2_3 = p_canvas_3_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_2_3,tags=('nacombo3'))

                label_1 = Label(p_canvas_3_1,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel6'))

                comb_non_2_4 = ttk.Combobox(p_canvas_3_1, font=('arial 10'),foreground="white")
                comb_non_2_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                comb_non_2_4.current(0)
                window_comb_non_2_4 = p_canvas_3_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_2_4,tags=('nacombo4'))

                non_sub_btn_2_1=Button(p_canvas_3_1,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_non_sub_btn_2_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=non_sub_btn_2_1,tags=('nabutton1'))

                def n_back_1_():
                    pro_frame_3_1.grid_forget()
                    pro_frame_3.grid(row=0,column=0,sticky='nsew')

                nbck_btn1=Button(p_canvas_3_1,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=n_back_1_)
                window_nbck_btn1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=nbck_btn1,tags=('nabutton3'))

            account_non_btn=Button(p_canvas_3,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=non_inc_acc_1)
            window_account_non_btn = p_canvas_3.create_window(0, 0, anchor="nw", window=account_non_btn,tags=('npbutton3'))

            p_canvas_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('nphline1'))

            label_1 = Label(p_canvas_3,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(26, 1300, anchor="nw", window=label_1,tags=('nplabel17'))

            chk_str_non_pitem = StringVar()
            chkbtn_non_pitem = Checkbutton(p_canvas_3, text = "I Purchase this product/service from Supplier.", variable = chk_str_non_pitem, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
            window_chkbtn_non_pitem = p_canvas_3.create_window(0, 0, anchor="nw", window=chkbtn_non_pitem,tags=('npentry9'))


            label_1 = Label(p_canvas_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel18'))

            entry_non_item_9=Entry(p_canvas_3,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_9 = p_canvas_3.create_window(0, 0, anchor="nw", height=60,window=entry_non_item_9,tags=('npentry10'))

            label_1 = Label(p_canvas_3,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel9'))
            
            entry_non_item_10=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_10 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_10,tags=('npcentry2'))

            chk_str_non_item_2 = StringVar()
            chkbtn_non_item_2 = Checkbutton(p_canvas_3, text = "Inclusive of purchase tax", variable = chk_str_non_item_2, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
            chkbtn_non_item_2.select()
            window_chkbtn_non_item_2 = p_canvas_3.create_window(0, 0, anchor="nw", window=chkbtn_non_item_2,tags=('npcbutton2'))

            label_1 = Label(p_canvas_3,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel10'))

            comb_non_item_5 = ttk.Combobox(p_canvas_3, font=('arial 10'),foreground="white")
            comb_non_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_non_item_5.current(0)
            window_comb_non_item_5 = p_canvas_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_item_5,tags=('npcentry3'))

            label_1 = Label(p_canvas_3,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel20'))

            comb_non_item_6 = ttk.Combobox(p_canvas_3, font=('arial 10'),foreground="white")
            comb_non_item_6['values'] = ("Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities",)
            comb_non_item_6.current(0)
            window_comb_non_item_6 = p_canvas_3.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_non_item_6,tags=('npcombo6'))

            def non_exp_acc_1():
                pro_frame_3.grid_forget()
                pro_frame_3_2 = Frame(tab3_4)
                pro_frame_3_2.grid(row=0,column=0,sticky='nsew')

                def pro_responsive_widgets_non_2(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
                
                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/1.021
                    y1 = dheight/14 
                    y2 = dheight/3.505

                    dcanvas.coords("eapoly1",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    dcanvas.coords("ealabel1",dwidth/3,dheight/8.24)
                    dcanvas.coords("eahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                    r2 = 25
                    x11 = dwidth/63
                    x21 = dwidth/1.021
                    y11 = dheight/2.8
                    y21 = dheight/0.52


                    dcanvas.coords("eapoly2",x11 + r2,y11,
                    x11 + r2,y11,
                    x21 - r2,y11,
                    x21 - r2,y11,     
                    x21,y11,     
                    #--------------------
                    x21,y11 + r2,     
                    x21,y11 + r2,     
                    x21,y21 - r2,     
                    x21,y21 - r2,     
                    x21,y21,
                    #--------------------
                    x21 - r2,y21,     
                    x21 - r2,y21,     
                    x11 + r2,y21,
                    x11 + r2,y21,
                    x11,y21,
                    #--------------------
                    x11,y21 - r2,
                    x11,y21 - r2,
                    x11,y11 + r2,
                    x11,y11 + r2,
                    x11,y11,
                    )

                    dcanvas.coords("eabutton3",dwidth/23,dheight/3.415)

                    dcanvas.coords("ealabel2",dwidth/23,dheight/1.91)
                    dcanvas.coords("ealabel3",dwidth/1.9,dheight/1.91)
                    dcanvas.coords("ealabel4",dwidth/23.3,dheight/1.41)
                    dcanvas.coords("ealabel5",dwidth/1.9,dheight/1.41)
                    dcanvas.coords("ealabel6",dwidth/1.9,dheight/0.95)

                    dcanvas.coords("eaentry1",dwidth/1.9,dheight/1.74)
                    dcanvas.coords("eaentry2",dwidth/1.9,dheight/1.32)

                    dcanvas.coords("eacombo1",dwidth/23,dheight/1.74)
                    dcanvas.coords("eacombo2",dwidth/23,dheight/1.32)
                    dcanvas.coords("eacombo3",dwidth/1.9,dheight/1.09)
                    dcanvas.coords("eacombo4",dwidth/1.9,dheight/0.91)

                    dcanvas.coords("eatext1",dwidth/23,dheight/1.15)
                    dcanvas.coords("eacheck1",dwidth/1.9,dheight/1.155)

                    dcanvas.coords("eabutton1",dwidth/2.3,dheight/0.73)

                p_canvas_3_2=Canvas(pro_frame_3_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                pro_frame_3_2.grid_columnconfigure(0,weight=1)
                pro_frame_3_2.grid_rowconfigure(0,weight=1)
                
                vertibar=Scrollbar(pro_frame_3_2, orient=VERTICAL)
                vertibar.grid(row=0,column=1,sticky='ns')
                vertibar.config(command=p_canvas_3_2.yview)

                p_canvas_3_2.bind("<Configure>", pro_responsive_widgets_non_2)
                p_canvas_3_2.config(yscrollcommand=vertibar.set)
                p_canvas_3_2.grid(row=0,column=0,sticky='nsew')


                p_canvas_3_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('eapoly1'))

                label_1 = Label(p_canvas_3_2,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1, tags=('ealabel1'))

                p_canvas_3_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('eahline'))

                p_canvas_3_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('eapoly2'))

                label_1 = Label(p_canvas_3_2,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel2'))

                comb_non_3_1 = ttk.Combobox(p_canvas_3_2, font=('arial 10'),foreground="white")
                comb_non_3_1['values'] = ("Expense",)
                comb_non_3_1.current(0)
                window_comb_non_3_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_3_1,tags=('eacombo1'))

                label_1 = Label(p_canvas_3_2,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel3'))

                entry_non_3_2=Entry(p_canvas_3_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_non_3_2 = p_canvas_3_2.create_window(0, 0, anchor="nw", height=30,window=entry_non_3_2,tags=('eaentry1'))

                label_1 = Label(p_canvas_3_2,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel4'))

                comb_non_3_2 = ttk.Combobox(p_canvas_3_2, font=('arial 10'),foreground="white")
                comb_non_3_2['values'] = ("Advertising/Promotional","Amortisation Expense","Auto","Bad Debts","Bank Charges","Borrowing Cost","Charitable Contributions","Commision and Fees","Cost of Labour","Dues and Subscriptions","Equipment Rental","Finance Costs","Income Tax Expense","Insurance","Interest Paid","Legal and Professional Fees","Loss on Discontinued Operations, Net of Tax","Management Compensation","Meals and Entertainment","Office/General Administrative Expenses","Other Miscellaneous Service Cost","Other Selling Expenses","Payroll Expenses","Rent or Lease of Building","Repair and Maintanance","Shipping and Delivery Expense","Shipping, Freight and Delivery","Supplies and Materials","Taxes Paid","Travel Expenses-Gereral and Admin Expenses","Travel Expenses-Selling Expense","Unapplied Cash Bill Payment Expense","Utilities",)
                comb_non_3_2.current(0)
                window_comb_non_3_2 = p_canvas_3_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_3_2,tags=('eacombo2'))

                label_1 = Label(p_canvas_3_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel5'))

                entry_non_3_4=Entry(p_canvas_3_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_non_3_4 = p_canvas_3_2.create_window(0, 0, anchor="nw", height=30,window=entry_non_3_4,tags=('eaentry2'))

                non_text_3 = Text(p_canvas_3_2,width=67, height=14, background='black',foreground='white')
                non_text_3.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_non_text_3 = p_canvas_3_2.create_window(0, 0, anchor="nw",window=non_text_3,tags=('eatext1'))

                chk_str_non_3_1 = StringVar()
                chkbtn_non_3_1 = Checkbutton(p_canvas_3_2, text = "Is sub-account", variable = chk_str_non_3_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_non_3_1.select()
                window_chkbtn_non_3_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=chkbtn_non_3_1,tags=('eacheck1'))

                comb_non_3_3 = ttk.Combobox(p_canvas_3_2, font=('arial 10'),foreground="white")
                comb_non_3_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_non_3_3.current(0)
                window_comb_non_3_3 = p_canvas_3_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_3_3,tags=('eacombo3'))

                label_1 = Label(p_canvas_3_2,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel6'))

                comb_non_3_4 = ttk.Combobox(p_canvas_3_2, font=('arial 10'),foreground="white")
                comb_non_3_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                comb_non_3_4.current(0)
                window_comb_non_3_4 = p_canvas_3_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_3_4,tags=('eacombo4'))

                non_sub_btn_3_1=Button(p_canvas_3_2,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_non_sub_btn_3_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=non_sub_btn_3_1,tags=('eabutton1'))

                def n_back_2_():
                    pro_frame_3_2.grid_forget()
                    pro_frame_3.grid(row=0,column=0,sticky='nsew')

                ebck_btn1=Button(p_canvas_3_2,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=n_back_2_)
                window_ebck_btn1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=ebck_btn1,tags=('eabutton3'))

            expense_non_btn=Button(p_canvas_3,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=non_exp_acc_1)
            window_expense_non_btn = p_canvas_3.create_window(0, 0, anchor="nw", window=expense_non_btn,tags=('npbutton4'))

            label_1 = Label(p_canvas_3,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel21'))

            str_non_item_2 = StringVar()
            entry_non_item_11=Entry(p_canvas_3,width=50,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_non_item_2)
            str_non_item_2.set(' 0')
            window_entry_non_item_11 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_11,tags=('npentry11'))

            label_1 = Label(p_canvas_3,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel22'))

            comb_non_item_7 = ttk.Combobox(p_canvas_3, font=('arial 10'),foreground="white")
            comb_non_item_7['values'] = ("Select Supplier",)
            comb_non_item_7.current(0)
            window_comb_non_item_7 = p_canvas_3.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_non_item_7,tags=('npcombo7'))

            non_sub_btn1=Button(p_canvas_3,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_non_sub_btn1 = p_canvas_3.create_window(0, 0, anchor="nw", window=non_sub_btn1,tags=('npbutton5'))

        p_btn_2=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=non_add_item)
        window_p_btn_2 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_2,tags=('apbutton2'))

        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly5"))

        label_1 = Label(p_canvas_1,width=10,height=1,text="Services", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel6'))

        label_1 = Label(p_canvas_1,width=45,height=2,text="A service is a transaction in which no physical goods are \ntransferred from the seller to the buyer.", font=('arial 12'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel7'))

        def ser_add_item():
            pro_frame_1.grid_forget()
            pro_frame_4 = Frame(tab3_4)
            pro_frame_4.grid(row=0,column=0,sticky='nsew')

            def pro_responsive_widgets_4(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
            
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("sppoly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("splabel1",dwidth/3,dheight/8.24)
                dcanvas.coords("sphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.29


                dcanvas.coords("sppoly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                r2 = 25
                x11 = dwidth/24
                x21 = dwidth/1.050
                y11 = dheight/2.1
                y21 = dheight/1.35


                dcanvas.coords("sppoly3",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("splabel2",dwidth/3,dheight/1.77)
                dcanvas.coords("spbutton1",dwidth/1.8,dheight/1.77)

                dcanvas.coords("splabel3",dwidth/23.2,dheight/1.23)
                dcanvas.coords("splabel4",dwidth/23.3,dheight/1.02)
                dcanvas.coords("splabel5",dwidth/1.9,dheight/1.02)
                dcanvas.coords("splabel7",dwidth/27,dheight/0.865)
                dcanvas.coords("splabel8",dwidth/1.915,dheight/0.865)
                dcanvas.coords("splabel12",dwidth/26,dheight/0.675)
                dcanvas.coords("splabel13",dwidth/26.8,dheight/0.606)
                dcanvas.coords("splabel14",dwidth/28.3,dheight/0.538)
                dcanvas.coords("splabel15",dwidth/1.9,dheight/0.538)
                dcanvas.coords("splabel16",dwidth/28.4,dheight/0.485)
                dcanvas.coords("splabel17",dwidth/50,dheight/0.438)
                dcanvas.coords("splabel18",dwidth/26,dheight/0.420)
                dcanvas.coords("splabel9",dwidth/23.2,dheight/0.392)
                dcanvas.coords("splabel10",dwidth/1.9,dheight/0.392)
                dcanvas.coords("splabel20",dwidth/28,dheight/0.368)
                dcanvas.coords("splabel21",dwidth/2.6,dheight/0.368)
                dcanvas.coords("splabel22",dwidth/1.5,dheight/0.368)

                dcanvas.coords("splabel23",dwidth/2.6,dheight/0.485)

                dcanvas.coords("splabel24",dwidth/1.53,dheight/0.485)
                

                dcanvas.coords("spentry1",dwidth/23.2,dheight/1.165)
                dcanvas.coords("spentry2",dwidth/23.2,dheight/0.975)
                dcanvas.coords("spentry3",dwidth/1.9,dheight/0.975)
                dcanvas.coords("spentry4",dwidth/1.9,dheight/0.83)
                dcanvas.coords("spentry7",dwidth/23.2,dheight/0.59)
                dcanvas.coords("spentry8",dwidth/23.2,dheight/0.525)
                dcanvas.coords("spentry9",dwidth/23.2,dheight/0.43)
                dcanvas.coords("spentry10",dwidth/23.2,dheight/0.412)
                dcanvas.coords("spentry11",dwidth/2.6,dheight/0.362)

                dcanvas.coords("spentry12",dwidth/2.6,dheight/0.474)

                dcanvas.coords("spcentry2",dwidth/23.2,dheight/0.385)
                dcanvas.coords("spcentry3",dwidth/1.9,dheight/0.385)

                dcanvas.coords("spcombo1",dwidth/23.2,dheight/0.83)
                dcanvas.coords("spcombo3",dwidth/1.9,dheight/0.525)
                dcanvas.coords("spcombo4",dwidth/23.2,dheight/0.474)
                dcanvas.coords("spcombo6",dwidth/23.2,dheight/0.362)
                dcanvas.coords("spcombo7",dwidth/1.5,dheight/0.362)

                dcanvas.coords("spcombo8",dwidth/1.5,dheight/0.474)

                dcanvas.coords("spbutton2",dwidth/23.2,dheight/0.654)
                dcanvas.coords("spbutton3",dwidth/3.37,dheight/0.474)
                dcanvas.coords("spbutton4",dwidth/3.37,dheight/0.362)
                dcanvas.coords("spbutton5",dwidth/2.38,dheight/0.345)

                dcanvas.coords("spcbutton1",dwidth/23.2,dheight/0.51)
                dcanvas.coords("spcbutton2",dwidth/23.2,dheight/0.378)

                dcanvas.coords("spline1",dwidth/21,dheight/0.73,dwidth/1.055,dheight/0.73)

                dcanvas.coords("sphline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)

            p_canvas_4=Canvas(pro_frame_4, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

            pro_frame_4.grid_columnconfigure(0,weight=1)
            pro_frame_4.grid_rowconfigure(0,weight=1)
     
            vertibar=Scrollbar(pro_frame_4, orient=VERTICAL)
            vertibar.grid(row=0,column=1,sticky='ns')
            vertibar.config(command=p_canvas_4.yview)

            p_canvas_4.bind("<Configure>", pro_responsive_widgets_4)
            p_canvas_4.config(yscrollcommand=vertibar.set)
            p_canvas_4.grid(row=0,column=0,sticky='nsew')


            p_canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sppoly1'))

            label_1 = Label(p_canvas_4,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel1'))

            p_canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sphline'))

            p_canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sppoly2'))

            p_canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('sppoly3'))

            label_1 = Label(p_canvas_4,width=15,height=2,text="SERVICES", font=('arial 20'),background="#2f516f",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel2'))

            btn_ser_item_2=Button(p_canvas_4,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
            window_btn_ser_item_2 = p_canvas_4.create_window(0, 0, anchor="nw", window=btn_ser_item_2, tags=('spbutton1'))

            label_1 = Label(p_canvas_4,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel3'))

            entry_ser_item_1=Entry(p_canvas_4,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ser_item_1 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_item_1, tags=('spentry1'))

            label_1 = Label(p_canvas_4,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel4'))

            str_ser_item_1 = StringVar()
            entry_ser_iitem_2=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_ser_item_1)
            str_ser_item_1.set('  Eg: N41554')
            window_entry_ser_iitem_2 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_iitem_2, tags=('spentry2'))

            label_1 = Label(p_canvas_4,width=9,height=1,text="SAC Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel5'))

            str_ser_iitem_1 = StringVar()
            entry_ser_item_2=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_ser_iitem_1)
            str_ser_iitem_1.set(' Eg: 998841-Coke and refined petroleum product manufacturing services')
            window_entry_ser_item_2 = p_canvas_4.create_window(710, 630, anchor="nw", height=30,window=entry_ser_item_2, tags=('spentry3'))


            label_1 = Label(p_canvas_4,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel7'))

            comb_ser_item_1 = ttk.Combobox(p_canvas_4, font=('arial 10'),foreground="white")
            comb_ser_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG-BAGS","BAL-BALE","BDL-BUNDLES","BKL-BUCKLES","BOX-BOX","BOU-BILLIONS OF UNITS","BTL-BOTTLES","BUN-BUNCHES","CAN-CANS","CBM-CUBIC METER","CMS-CENTIMETER","CCM-CUBIC CENTIMETER","CTN-CARTONS","DOZ-DOZEN","DRM-DRUM","GGR-GREAT GROSS","GMS-GRAMS","GRS-GROSS","GYD-GRODD YARDS","KGS-KILOGRAMS","KLR-KILOLITER","KME-KILOMETRE","MTS-METRIC TON","MLT-MILLILITRE","MTR-METERS","NOS-NUMBER","PAC-PACKS","PCS-PIECES","PRS-PAIRS","QTL-QUINTAL","ROL-ROLLS","SQF-SQUARE FEET","SET-SETS","SQM-SQUARE METERS","SQY-SQUARE YARDS","TBS-TABLETS","TGM-TEN GROSS","THD-THOUSAND","TON-TONNES","TUB-TUBES","UGS-US GALLONS","UNT-UNITS","YDS-YARDS","OTH-OTHERS",)
            comb_ser_item_1.current(0)
            window_comb_ser_item_1 = p_canvas_4.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_item_1, tags=('spcombo1'))

            label_1 = Label(p_canvas_4,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(705, 710, anchor="nw", window=label_1,tags=('splabel8'))

            entry_ser_item_3=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ser_item_3 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_item_3,tags=('spentry4'))

            p_canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('spline1'))


            label_1 = Label(p_canvas_4,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel12'))

            chk_str_ser_item = StringVar()
            chkbtn_ser_item = Checkbutton(p_canvas_4, text = "I sell this product/service to my customers.", variable = chk_str_ser_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
            window_chkbtn_ser_item = p_canvas_4.create_window(0, 0, anchor="nw", window=chkbtn_ser_item,tags=('spbutton2'))

            label_1 = Label(p_canvas_4,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel13'))

            entry_ser_item_7=Entry(p_canvas_4,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ser_item_7 = p_canvas_4.create_window(0, 0, anchor="nw", height=60,window=entry_ser_item_7,tags=('spentry7'))

            label_1 = Label(p_canvas_4,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel14'))
            
            entry_non_item_8=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_8 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_8,tags=('spentry8'))

            chk_str_ser_item_1 = StringVar()
            chkbtn_ser_item_1 = Checkbutton(p_canvas_4, text = "Inclusive of tax", variable = chk_str_ser_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
            chkbtn_ser_item_1.select()
            window_chkbtn_ser_item_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=chkbtn_ser_item_1,tags=('spcbutton1'))

            label_1 = Label(p_canvas_4,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel15'))

            comb_ser_item_3 = ttk.Combobox(p_canvas_4, font=('arial 10'),foreground="white")
            comb_ser_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_ser_item_3.current(0)
            window_comb_ser_item_3 = p_canvas_4.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_item_3,tags=('spcombo3'))

            label_1 = Label(p_canvas_4,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel16'))

            
            comb_ser_item_6 = ttk.Combobox(p_canvas_4, font=('arial 10'),foreground="white")
            comb_ser_item_6['values'] = ("Choose...","Billable Expense income","Product Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discounts","Sales of Product Income","Cost of sales","Equipment Rental for Jobs","Uncategorised Income","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Depreciation Expense","Dues and Subscriptions","Housekeeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Internet Expenses","Meals and Enetrtainments","Office Suppliers","Postage and Delivery","Printing and Reprooduction","Professional Fees","Purchases","Rent Expense","Repair and Maintananace","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities","Finance charge Income","Insurance Proceeds Received","Interest Income","Proceeds From Sale os Assets","Shipping and delivery Income","Ask My Accountant","CGST Write-off","GST Write-off","IGST Write-off","Miscellaneous Expense","Political Contributions","Reconcilation Discrepancies","SGST Write-off","Vehicles","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi kalyan Cess","Input Krishi kalyan Cess RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Krishi Kalyan Cess Payable","Input VAT 5%","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output SGST Tax RCM","Output Service Tax","Output Service Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","SGST Payable","Service Tax Payable","Srvice Tax Suspense","Swachh Barath Cess Payable","TDS Payable","VAT Payable","VAT Suspense","Deferred CGST","Deferred GST Input credit","Deferred IGST","Deferred SGST","Deferred Service Tax Input Credit","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Sevice Tax Refund","TDS Receivable","Uncategorised Asset","Undeposited Fund","Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and maintanance","Sales Discount","Sales of Product Income","Uncategorised Income","accumulated Depreciation","Building and Improvements","Furniture and Equipments","Land","Leasehold Improvements","Vehicles","Retained Earnings","Cost of Sales","Equipment Rental for Jobs","Freight and Shipping Costs","Merchant Account Fees","Purchases-Hardware for Resales","Purchases-Software for Resales","Subcontracted Services","Tools and Craft Suppliers",)
            comb_ser_item_6.current(0)
            window_comb_ser_item_6 = p_canvas_4.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_ser_item_6,tags=('spcombo4'))

            def ser_inc_acc_1():
                pro_frame_4.grid_forget()
                pro_frame_4_1 = Frame(tab3_4)
                pro_frame_4_1.grid(row=0,column=0,sticky='nsew')

                def pro_responsive_widgets_4_1(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
                
                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/1.021
                    y1 = dheight/14 
                    y2 = dheight/3.505

                    dcanvas.coords("sapoly1",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    dcanvas.coords("salabel1",dwidth/3,dheight/8.24)
                    dcanvas.coords("sahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                    r2 = 25
                    x11 = dwidth/63
                    x21 = dwidth/1.021
                    y11 = dheight/2.8
                    y21 = dheight/0.52


                    dcanvas.coords("sapoly2",x11 + r2,y11,
                    x11 + r2,y11,
                    x21 - r2,y11,
                    x21 - r2,y11,     
                    x21,y11,     
                    #--------------------
                    x21,y11 + r2,     
                    x21,y11 + r2,     
                    x21,y21 - r2,     
                    x21,y21 - r2,     
                    x21,y21,
                    #--------------------
                    x21 - r2,y21,     
                    x21 - r2,y21,     
                    x11 + r2,y21,
                    x11 + r2,y21,
                    x11,y21,
                    #--------------------
                    x11,y21 - r2,
                    x11,y21 - r2,
                    x11,y11 + r2,
                    x11,y11 + r2,
                    x11,y11,
                    )

                    dcanvas.coords("sabutton3",dwidth/23,dheight/3.415)

                    dcanvas.coords("salabel2",dwidth/23,dheight/1.91)
                    dcanvas.coords("salabel3",dwidth/1.9,dheight/1.91)
                    dcanvas.coords("salabel4",dwidth/23.3,dheight/1.41)
                    dcanvas.coords("salabel5",dwidth/1.9,dheight/1.41)
                    dcanvas.coords("salabel6",dwidth/1.9,dheight/0.95)

                    dcanvas.coords("saentry1",dwidth/1.9,dheight/1.74)
                    dcanvas.coords("saentry2",dwidth/1.9,dheight/1.32)

                    dcanvas.coords("sacombo1",dwidth/23,dheight/1.74)
                    dcanvas.coords("sacombo2",dwidth/23,dheight/1.32)
                    dcanvas.coords("sacombo3",dwidth/1.9,dheight/1.09)
                    dcanvas.coords("sacombo4",dwidth/1.9,dheight/0.91)

                    dcanvas.coords("satext1",dwidth/23,dheight/1.15)
                    dcanvas.coords("sacheck1",dwidth/1.9,dheight/1.155)

                    dcanvas.coords("sabutton1",dwidth/2.3,dheight/0.73)

                p_canvas_4_1=Canvas(pro_frame_4_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                pro_frame_4_1.grid_columnconfigure(0,weight=1)
                pro_frame_4_1.grid_rowconfigure(0,weight=1)
                
                vertibar=Scrollbar(pro_frame_4_1, orient=VERTICAL)
                vertibar.grid(row=0,column=1,sticky='ns')
                vertibar.config(command=p_canvas_4_1.yview)

                p_canvas_4_1.bind("<Configure>", pro_responsive_widgets_4_1)
                p_canvas_4_1.config(yscrollcommand=vertibar.set)
                p_canvas_4_1.grid(row=0,column=0,sticky='nsew')


                p_canvas_4_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sapoly1'))

                label_1 = Label(p_canvas_4_1,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1, tags=('salabel1'))

                p_canvas_4_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sahline'))

                p_canvas_4_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sapoly2'))

                label_1 = Label(p_canvas_4_1,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel2'))

                comb_ser_2_1 = ttk.Combobox(p_canvas_4_1, font=('arial 10'),foreground="white")
                comb_ser_2_1['values'] = ("Account Receivable(Debtors)","Current Assets","Bank","Fixed Assets","Non-Current Assets","Accounts Payable(Creditors)","Credit Card","Current Liabilities","Non-Current Liabilities","Equity","Income","Other Income","Cost of Goods Sold","Expenses","Other Expenses",)
                comb_ser_2_1.current(0)
                window_comb_ser_2_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_2_1,tags=('sacombo1'))

                label_1 = Label(p_canvas_4_1,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel3'))

                entry_ser_2_2=Entry(p_canvas_4_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_ser_2_2 = p_canvas_4_1.create_window(0, 0, anchor="nw", height=30,window=entry_ser_2_2,tags=('saentry1'))

                label_1 = Label(p_canvas_4_1,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel4'))

                comb_ser_2_2 = ttk.Combobox(p_canvas_4_1, font=('arial 10'),foreground="white")
                comb_ser_2_2['values'] = ("Account Receivable(Debtors)",)
                comb_ser_2_2.current(0)
                window_comb_ser_2_2 = p_canvas_4_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_2_2,tags=('sacombo2'))

                label_1 = Label(p_canvas_4_1,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel5'))

                entry_ser_2_4=Entry(p_canvas_4_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_ser_2_4 = p_canvas_4_1.create_window(0, 0, anchor="nw", height=30,window=entry_ser_2_4,tags=('saentry2'))

                ser_text_2 = Text(p_canvas_4_1,width=67, height=14, background='black',foreground='white')
                ser_text_2.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_ser_text_2 = p_canvas_4_1.create_window(0, 0, anchor="nw",window=ser_text_2,tags=('satext1'))

                chk_str_ser_2_1 = StringVar()
                chkbtn_ser_2_1 = Checkbutton(p_canvas_4_1, text = "Is sub-account", variable = chk_str_ser_2_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_ser_2_1.select()
                window_chkbtn_ser_2_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=chkbtn_ser_2_1,tags=('sacheck1'))

                comb_ser_2_3 = ttk.Combobox(p_canvas_4_1, font=('arial 10'),foreground="white")
                comb_ser_2_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_ser_2_3.current(0)
                window_comb_ser_2_3 = p_canvas_4_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_2_3,tags=('sacombo3'))

                label_1 = Label(p_canvas_4_1,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel6'))

                comb_ser_2_4 = ttk.Combobox(p_canvas_4_1, font=('arial 10'),foreground="white")
                comb_ser_2_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                comb_ser_2_4.current(0)
                window_comb_ser_2_4 = p_canvas_4_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_2_4,tags=('sacombo4'))

                ser_sub_btn_2_1=Button(p_canvas_4_1,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_ser_sub_btn_2_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=ser_sub_btn_2_1,tags=('sabutton1'))

                def s_back_1_():
                    pro_frame_4_1.grid_forget()
                    pro_frame_4.grid(row=0,column=0,sticky='nsew')

                bck_btn1=Button(p_canvas_4_1,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=s_back_1_)
                window_bck_btn1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('sabutton3'))

            income_ser_btn=Button(p_canvas_4,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=ser_inc_acc_1)
            window_income_ser_btn = p_canvas_4.create_window(0, 0, anchor="nw", window=income_ser_btn,tags=('spbutton3'))

            label_1 = Label(p_canvas_4,width=10,height=1,text="Abatement %", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel23'))

            str_ser_iitem_2 = StringVar()
            entry_ser_iitem_11=Entry(p_canvas_4,width=50,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_ser_iitem_2)
            str_ser_iitem_2.set(' 0')
            window_entry_ser_iitem_11 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_iitem_11,tags=('spentry12'))

            label_1 = Label(p_canvas_4,width=14,height=1,text="Service Type", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel24'))

            comb_ser_iitem_7 = ttk.Combobox(p_canvas_4, font=('arial 10'),foreground="white")
            comb_ser_iitem_7['values'] = ("Choose...","Stock Broking","Genral Insurance","Courier","Advertsing Agency","Consulting Engineer","Custom House Agent","Steamer Agent","Clearing and Forwarding","Man power Recruiting","Air Travel Agent","Tour operator","Rent a Cab","Architect","Interior Director","Management Consultment","Chartered Accountant","Cost Accountant","Company Scretary","Real Estate Agent","Security Agency","Credit Rating Agency","Market Research Agency","Underwriter","Beauty Parlor","Cargo Handling","Cable Operators","Dry Cleaning","Event Management","Fashion Designer","Life Insurance","Scientific and Technical Consultancy","Photography","Convention Services","Video Tape Production","Sound Recording","Broadcating","Insurance Auxilary Service","banking and Other Financial","Port Services","Authorised Service Station","Health Club and Fitness Centres","Rail Travel Agent","Storage and Warehousing","Business Auxilary","Commercial Coaching","Erection or Installation","Franchise Service","Internet Cafe","Maintanance or Repair","Technical Testing","Technical Inspection","Foreign Exchange Broking","Port","Airport Services","Air Transport","Business Exhibition","Goods Transport","Construction of Commerce Complex","Intellectual Property Service","Opinion Poll Service","Outdoor Catering","Television and Radio Program Production","Survey and Exploration of Minerals","Pandal and Shamiana","Travel Agent","Forward Contract Brokerage","Transport Through Pipeline","Site Preparation","Dredging","Survey and Map Making","Cleaning Service","Clubs and Association Service","Packaging Service","Mailing List Compilation","Residential Complex Construction","Share Transfer Agent","ATM Maintanance","Recovery Agent","Sale of Space for Advertisement","Sponsorship","International Air Travel","Containerised Rail Transport","Business Support Service","Action Service","Public Relation Management","Ship Management","Internet Telephony","Cruise Ship Tour","Credit Card","Telecommunication Service","Mining of Minerals, Oil or Gas","Recting Immovable Property","Works Contract","Development of Consent","Asset Management","Design Services","Information Technology Services","ULIP Management","Stock Exchange Service","Service for Transaction in Goods","Clearing House Services","Supply of Tangiable","Online Inforamtion Retrieval","Mandap keeper",)
            comb_ser_iitem_7.current(0)
            window_comb_ser_iitem_7 = p_canvas_4.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_ser_iitem_7,tags=('spcombo8'))

            p_canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sphline1'))

            label_1 = Label(p_canvas_4,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel17'))

            chk_str_ser_pitem = StringVar()
            chkbtn_ser_pitem = Checkbutton(p_canvas_4, text = "I Purchase this product/service from Supplier.", variable = chk_str_ser_pitem, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
            window_chkbtn_ser_pitem = p_canvas_4.create_window(0, 0, anchor="nw", window=chkbtn_ser_pitem,tags=('spentry9'))


            label_1 = Label(p_canvas_4,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel18'))

            entry_ser_item_9=Entry(p_canvas_4,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ser_item_9 = p_canvas_4.create_window(0, 0, anchor="nw", height=60,window=entry_ser_item_9,tags=('spentry10'))

            label_1 = Label(p_canvas_4,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel9'))
            
            entry_ser_item_10=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ser_item_10 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_item_10,tags=('spcentry2'))

            chk_str_sser_item_2 = StringVar()
            chkbtn_sser_item_2 = Checkbutton(p_canvas_4, text = "Inclusive of Tax", variable = chk_str_sser_item_2, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
            chkbtn_sser_item_2.select()
            window_chkbtn_sser_item_2 = p_canvas_4.create_window(0, 0, anchor="nw", window=chkbtn_sser_item_2,tags=('spcbutton2'))

            label_1 = Label(p_canvas_4,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel10'))

            comb_ser_item_5 = ttk.Combobox(p_canvas_4, font=('arial 10'),foreground="white")
            comb_ser_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_ser_item_5.current(0)
            window_comb_ser_item_5 = p_canvas_4.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_item_5,tags=('spcentry3'))

            label_1 = Label(p_canvas_4,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel20'))

            comb_ser_item_6 = ttk.Combobox(p_canvas_4, font=('arial 10'),foreground="white")
            comb_ser_item_6['values'] = ("Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities",)
            comb_ser_item_6.current(0)
            window_comb_ser_item_6 = p_canvas_4.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_ser_item_6,tags=('spcombo6'))

            def ser_exp_acc_1():
                pro_frame_4.grid_forget()
                pro_frame_4_2 = Frame(tab3_4)
                pro_frame_4_2.grid(row=0,column=0,sticky='nsew')

                def pro_responsive_widgets_4_2(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
                
                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/1.021
                    y1 = dheight/14 
                    y2 = dheight/3.505

                    dcanvas.coords("xapoly1",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    dcanvas.coords("xalabel1",dwidth/3,dheight/8.24)
                    dcanvas.coords("xahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                    r2 = 25
                    x11 = dwidth/63
                    x21 = dwidth/1.021
                    y11 = dheight/2.8
                    y21 = dheight/0.52


                    dcanvas.coords("xapoly2",x11 + r2,y11,
                    x11 + r2,y11,
                    x21 - r2,y11,
                    x21 - r2,y11,     
                    x21,y11,     
                    #--------------------
                    x21,y11 + r2,     
                    x21,y11 + r2,     
                    x21,y21 - r2,     
                    x21,y21 - r2,     
                    x21,y21,
                    #--------------------
                    x21 - r2,y21,     
                    x21 - r2,y21,     
                    x11 + r2,y21,
                    x11 + r2,y21,
                    x11,y21,
                    #--------------------
                    x11,y21 - r2,
                    x11,y21 - r2,
                    x11,y11 + r2,
                    x11,y11 + r2,
                    x11,y11,
                    )

                    dcanvas.coords("xabutton3",dwidth/23,dheight/3.415)

                    dcanvas.coords("xalabel2",dwidth/23,dheight/1.91)
                    dcanvas.coords("xalabel3",dwidth/1.9,dheight/1.91)
                    dcanvas.coords("xalabel4",dwidth/23.3,dheight/1.41)
                    dcanvas.coords("xalabel5",dwidth/1.9,dheight/1.41)
                    dcanvas.coords("xalabel6",dwidth/1.9,dheight/0.95)

                    dcanvas.coords("xaentry1",dwidth/1.9,dheight/1.74)
                    dcanvas.coords("xaentry2",dwidth/1.9,dheight/1.32)

                    dcanvas.coords("xacombo1",dwidth/23,dheight/1.74)
                    dcanvas.coords("xacombo2",dwidth/23,dheight/1.32)
                    dcanvas.coords("xacombo3",dwidth/1.9,dheight/1.09)
                    dcanvas.coords("xacombo4",dwidth/1.9,dheight/0.91)

                    dcanvas.coords("xatext1",dwidth/23,dheight/1.15)
                    dcanvas.coords("xacheck1",dwidth/1.9,dheight/1.155)

                    dcanvas.coords("xabutton1",dwidth/2.3,dheight/0.73)

                p_canvas_4_2=Canvas(pro_frame_4_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                pro_frame_4_2.grid_columnconfigure(0,weight=1)
                pro_frame_4_2.grid_rowconfigure(0,weight=1)
                
                vertibar=Scrollbar(pro_frame_4_2, orient=VERTICAL)
                vertibar.grid(row=0,column=1,sticky='ns')
                vertibar.config(command=p_canvas_4_2.yview)

                p_canvas_4_2.bind("<Configure>", pro_responsive_widgets_4_2)
                p_canvas_4_2.config(yscrollcommand=vertibar.set)
                p_canvas_4_2.grid(row=0,column=0,sticky='nsew')


                p_canvas_4_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('xapoly1'))

                label_1 = Label(p_canvas_4_2,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1, tags=('xalabel1'))

                p_canvas_4_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('xahline'))

                p_canvas_4_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('xapoly2'))

                label_1 = Label(p_canvas_4_2,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel2'))

                comb_ser_3_1 = ttk.Combobox(p_canvas_4_2, font=('arial 10'),foreground="white")
                comb_ser_3_1['values'] = ("Account Receivable(Debtors)","Current Assets","Bank","Fixed Assets","Non-Current Assets","Accounts Payable(Creditors)","Credit Card","Current Liabilities","Non-Current Liabilities","Equity","Income","Other Income","Cost of Goods Sold","Expenses","Other Expenses",)
                comb_ser_3_1.current(0)
                window_comb_ser_3_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_3_1,tags=('xacombo1'))

                label_1 = Label(p_canvas_4_2,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel3'))

                entry_ser_3_2=Entry(p_canvas_4_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_ser_3_2 = p_canvas_4_2.create_window(0, 0, anchor="nw", height=30,window=entry_ser_3_2,tags=('xaentry1'))

                label_1 = Label(p_canvas_4_2,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel4'))

                comb_ser_3_2 = ttk.Combobox(p_canvas_4_2, font=('arial 10'),foreground="white")
                comb_ser_3_2['values'] = ("Account Receivable(Debtors)",)
                comb_ser_3_2.current(0)
                window_comb_ser_3_2 = p_canvas_4_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_3_2,tags=('xacombo2'))

                label_1 = Label(p_canvas_4_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel5'))

                entry_ser_3_4=Entry(p_canvas_4_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_ser_3_4 = p_canvas_4_2.create_window(0, 0, anchor="nw", height=30,window=entry_ser_3_4,tags=('xaentry2'))

                ser_text_3 = Text(p_canvas_4_2,width=67, height=14, background='black',foreground='white')
                ser_text_3.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_ser_text_3 = p_canvas_4_2.create_window(0, 0, anchor="nw",window=ser_text_3,tags=('xatext1'))

                chk_str_ser_3_1 = StringVar()
                chkbtn_ser_3_1 = Checkbutton(p_canvas_4_2, text = "Is sub-account", variable = chk_str_ser_3_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_ser_3_1.select()
                window_chkbtn_ser_3_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=chkbtn_ser_3_1,tags=('xacheck1'))

                comb_ser_3_3 = ttk.Combobox(p_canvas_4_2, font=('arial 10'),foreground="white")
                comb_ser_3_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_ser_3_3.current(0)
                window_comb_ser_3_3 = p_canvas_4_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_3_3,tags=('xacombo3'))

                label_1 = Label(p_canvas_4_2,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel6'))

                comb_ser_3_4 = ttk.Combobox(p_canvas_4_2, font=('arial 10'),foreground="white")
                comb_ser_3_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                comb_ser_3_4.current(0)
                window_comb_ser_3_4 = p_canvas_4_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_3_4,tags=('xacombo4'))

                ser_sub_btn_3_1=Button(p_canvas_4_2,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_ser_sub_btn_3_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=ser_sub_btn_3_1,tags=('xabutton1'))

                def s_back_2_():
                    pro_frame_4_2.grid_forget()
                    pro_frame_4.grid(row=0,column=0,sticky='nsew')

                sbck_btn2=Button(p_canvas_4_2,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=s_back_2_)
                window_sbck_btn2 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=sbck_btn2,tags=('xabutton3'))

            expense_ser_btn=Button(p_canvas_4,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=ser_exp_acc_1)
            window_expense_ser_btn = p_canvas_4.create_window(0, 0, anchor="nw", window=expense_ser_btn,tags=('spbutton4'))

            label_1 = Label(p_canvas_4,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel21'))

            str_sser_iitem_2 = StringVar()
            entry_sser_item_11=Entry(p_canvas_4,width=50,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_sser_iitem_2)
            str_sser_iitem_2.set(' 0')
            window_entry_sser_item_11 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_sser_item_11,tags=('spentry11'))

            label_1 = Label(p_canvas_4,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel22'))

            comb_ser_item_7 = ttk.Combobox(p_canvas_4, font=('arial 10'),foreground="white")
            comb_ser_item_7['values'] = ("Select Supplier",)
            comb_ser_item_7.current(0)
            window_comb_ser_item_7 = p_canvas_4.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_ser_item_7,tags=('spcombo7'))

            ser_sub_btn1=Button(p_canvas_4,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_ser_sub_btn1 = p_canvas_4.create_window(0, 0, anchor="nw", window=ser_sub_btn1,tags=('spbutton5'))

        p_btn_3=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=ser_add_item)
        window_p_btn_3 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_3,tags=('apbutton3'))

        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly6"))

        label_1 = Label(p_canvas_1,width=10,height=1,text="Bundle", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel8'))

        label_1 = Label(p_canvas_1,width=46,height=2,text="A bundle is a group of software programs or hardware \ndevices that are grouped together and sold as one.", font=('arial 12'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel9'))

        def bun_add_item():
            pro_frame_1.grid_forget()
            pro_frame_5 = Frame(tab3_4)
            pro_frame_5.grid(row=0,column=0,sticky='nsew')
            
            def pro_responsive_widgets_5(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
            
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("bppoly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("bplabel1",dwidth/3,dheight/8.24)
                dcanvas.coords("bphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.29


                dcanvas.coords("bppoly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                r2 = 25
                x11 = dwidth/24
                x21 = dwidth/1.050
                y11 = dheight/2.1
                y21 = dheight/1.35


                dcanvas.coords("bppoly3",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("bplabel2",dwidth/3,dheight/1.77)
                dcanvas.coords("bpbutton1",dwidth/1.8,dheight/1.77)

                dcanvas.coords("bplabel3",dwidth/23.2,dheight/1.23)
                dcanvas.coords("bplabel4",dwidth/1.9,dheight/1.23)
                dcanvas.coords("bplabel5",dwidth/25,dheight/1.02)
                dcanvas.coords("bplabel6",dwidth/23,dheight/0.8)


                dcanvas.coords("bpentry1",dwidth/23.2,dheight/1.165)
                dcanvas.coords("bpentry2",dwidth/1.9,dheight/1.165)
                dcanvas.coords("bpentry3",dwidth/23.2,dheight/0.97)

            p_canvas_5=Canvas(pro_frame_5, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

            pro_frame_5.grid_columnconfigure(0,weight=1)
            pro_frame_5.grid_rowconfigure(0,weight=1)
            
            vertibar=Scrollbar(pro_frame_5, orient=VERTICAL)
            vertibar.grid(row=0,column=1,sticky='ns')
            vertibar.config(command=p_canvas_5.yview)

            p_canvas_5.bind("<Configure>", pro_responsive_widgets_5)
            p_canvas_5.config(yscrollcommand=vertibar.set)
            p_canvas_5.grid(row=0,column=0,sticky='nsew')


            p_canvas_5.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('bppoly1'))

            label_1 = Label(p_canvas_5,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel1'))

            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('bphline'))

            p_canvas_5.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('bppoly2'))

            p_canvas_5.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('bppoly3'))
            
            label_1 = Label(p_canvas_5,width=15,height=2,text="BUNDLE", font=('arial 20'),background="#2f516f",fg="white") 
            window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel2'))

            btn_bun_item_2=Button(p_canvas_5,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
            window_btn_bun_item_2 = p_canvas_5.create_window(0, 0, anchor="nw", window=btn_bun_item_2, tags=('bpbutton1'))

            label_1 = Label(p_canvas_5,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel3'))

            entry_bun_item_1=Entry(p_canvas_5,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_bun_item_1 = p_canvas_5.create_window(55, 530, anchor="nw", height=30,window=entry_bun_item_1, tags=('bpentry1'))

            label_1 = Label(p_canvas_5,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel4'))

            str_bun_item_1 = StringVar()
            entry_bun_iitem_2=Entry(p_canvas_5,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_item_1)
            str_bun_item_1.set('  Eg: N41554')
            window_entry_bun_iitem_2 = p_canvas_5.create_window(0, 0, anchor="nw", height=30,window=entry_bun_iitem_2, tags=('bpentry2'))

            label_1 = Label(p_canvas_5,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel5'))

            entry_bun_item_7=Entry(p_canvas_5,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_bun_item_7 = p_canvas_5.create_window(0, 0, anchor="nw", height=60,window=entry_bun_item_7, tags=('bpentry3'))

            label_1 = Label(p_canvas_5,width=30,height=1,text="Products/services included in the bundle", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel6'))

            p_canvas_5.create_line(60, 800, 1250, 800, fill='gray',width=1)
            p_canvas_5.create_line(60, 850, 1250, 850, fill='gray',width=1)
            p_canvas_5.create_line(60, 925, 1250, 925, fill='gray',width=1)
            p_canvas_5.create_line(60, 800, 60, 925, fill='gray',width=1)
            p_canvas_5.create_line(275, 800, 275, 925, fill='gray',width=1)
            p_canvas_5.create_line(500, 800, 500, 925, fill='gray',width=1)
            p_canvas_5.create_line(735, 800, 735, 925, fill='gray',width=1)
            p_canvas_5.create_line(850, 800, 850, 925, fill='gray',width=1)
            p_canvas_5.create_line(980, 800, 980, 925, fill='gray',width=1)
            p_canvas_5.create_line(1110, 800, 1110, 925, fill='gray',width=1)
            p_canvas_5.create_line(1250, 800, 1250, 925, fill='gray',width=1)
            p_canvas_5.create_line(60, 1000, 1250, 1000, fill='gray',width=1)
            p_canvas_5.create_line(60, 1075, 1250, 1075, fill='gray',width=1)
            p_canvas_5.create_line(60, 1150, 1250, 1150, fill='gray',width=1)
            p_canvas_5.create_line(60, 925, 60, 1150, fill='gray',width=1)
            p_canvas_5.create_line(275, 925, 275, 1150, fill='gray',width=1)
            p_canvas_5.create_line(500, 925, 500, 1150, fill='gray',width=1)
            p_canvas_5.create_line(735, 925, 735, 1150, fill='gray',width=1)
            p_canvas_5.create_line(850, 925, 850, 1150, fill='gray',width=1)
            p_canvas_5.create_line(980, 925, 980, 1150, fill='gray',width=1)
            p_canvas_5.create_line(1110, 925, 1110, 1150, fill='gray',width=1)
            p_canvas_5.create_line(1250, 925, 1250, 1150, fill='gray',width=1)

            label_3 = Label(p_canvas_5,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_3 = p_canvas_5.create_window(105, 815, anchor="nw", window=label_3)

            label_4 = Label(p_canvas_5,width=10,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = p_canvas_5.create_window(340, 815, anchor="nw", window=label_4)

            label_4 = Label(p_canvas_5,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = p_canvas_5.create_window(570, 815, anchor="nw", window=label_4)

            label_4 = Label(p_canvas_5,width=5,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = p_canvas_5.create_window(770, 815, anchor="nw", window=label_4)

            label_4 = Label(p_canvas_5,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = p_canvas_5.create_window(880, 815, anchor="nw", window=label_4)

            label_4 = Label(p_canvas_5,width=8,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = p_canvas_5.create_window(1005, 815, anchor="nw", window=label_4)

            label_4 = Label(p_canvas_5,width=8,height=1,text="TAX", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = p_canvas_5.create_window(1150, 815, anchor="nw", window=label_4)

            bun_comb_1 = ttk.Combobox(p_canvas_5, font=('arial 10'),foreground="white")
            bun_comb_1['values'] = ("Choose",)
            bun_comb_1.current(0)
            window_bun_comb_1 = p_canvas_5.create_window(80, 870, anchor="nw", width=180, height=30,window=bun_comb_1)

            bun_comb_2 = ttk.Combobox(p_canvas_5, font=('arial 10'),foreground="white")
            bun_comb_2['values'] = ("Choose",)
            bun_comb_2.current(0)
            window_bun_comb_2 = p_canvas_5.create_window(80, 945, anchor="nw", width=180, height=30,window=bun_comb_2)

            bun_comb_3 = ttk.Combobox(p_canvas_5, font=('arial 10'),foreground="white")
            bun_comb_3['values'] = ("Choose",)
            bun_comb_3.current(0)
            window_bun_comb_3 = p_canvas_5.create_window(80, 1020, anchor="nw", width=180, height=30,window=bun_comb_3)

            bun_comb_4 = ttk.Combobox(p_canvas_5, font=('arial 10'),foreground="white")
            bun_comb_4['values'] = ("Choose",)
            bun_comb_4.current(0)
            window_bun_comb_4 = p_canvas_5.create_window(80, 1095, anchor="nw", width=180, height=30,window=bun_comb_4)

            bun_entry_1=Entry(p_canvas_5,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_1 = p_canvas_5.create_window(295, 870, anchor="nw", height=30, window=bun_entry_1)

            bun_entry_2=Entry(p_canvas_5,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_2 = p_canvas_5.create_window(295, 945, anchor="nw", height=30, window=bun_entry_2)

            bun_entry_3=Entry(p_canvas_5,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_3 = p_canvas_5.create_window(295, 1020, anchor="nw", height=30, window=bun_entry_3)

            bun_entry_4=Entry(p_canvas_5,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_4 = p_canvas_5.create_window(295, 1095, anchor="nw", height=30, window=bun_entry_4)

            bun_entry_5=Entry(p_canvas_5,width=32,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_5 = p_canvas_5.create_window(520, 870, anchor="nw", height=30, window=bun_entry_5)

            bun_entry_6=Entry(p_canvas_5,width=32,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_6 = p_canvas_5.create_window(520, 945, anchor="nw", height=30, window=bun_entry_6)

            bun_entry_7=Entry(p_canvas_5,width=32,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_7 = p_canvas_5.create_window(520, 1020, anchor="nw", height=30, window=bun_entry_7)

            bun_entry_8=Entry(p_canvas_5,width=32,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_8 = p_canvas_5.create_window(520, 1095, anchor="nw", height=30, window=bun_entry_8)

            str_bun_entry_9 = StringVar()
            bun_entry_9=Entry(p_canvas_5,width=15,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_9)
            str_bun_entry_9.set(' 0')
            window_bun_entry_9 = p_canvas_5.create_window(745, 870, anchor="nw", height=30, window=bun_entry_9)

            str_bun_entry_10 = StringVar()
            bun_entry_10=Entry(p_canvas_5,width=15,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_10)
            str_bun_entry_10.set(' 0')
            window_bun_entry_10 = p_canvas_5.create_window(745, 945, anchor="nw", height=30, window=bun_entry_10)

            str_bun_entry_11 = StringVar()
            bun_entry_11=Entry(p_canvas_5,width=15,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_11)
            str_bun_entry_11.set(' 0')
            window_bun_entry_11 = p_canvas_5.create_window(745, 1020, anchor="nw", height=30, window=bun_entry_11)

            str_bun_entry_12 = StringVar()
            bun_entry_12=Entry(p_canvas_5,width=15,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_12)
            str_bun_entry_12.set(' 0')
            window_bun_entry_12 = p_canvas_5.create_window(745, 1095, anchor="nw", height=30, window=bun_entry_12)

            str_bun_entry_13 = StringVar()
            bun_entry_13=Entry(p_canvas_5,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_13)
            str_bun_entry_13.set(' 0.0')
            window_bun_entry_13 = p_canvas_5.create_window(860, 870, anchor="nw", height=30, window=bun_entry_13)

            str_bun_entry_14 = StringVar()
            bun_entry_14=Entry(p_canvas_5,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_14)
            str_bun_entry_14.set(' 0.0')
            window_bun_entry_14 = p_canvas_5.create_window(860, 945, anchor="nw", height=30, window=bun_entry_14)

            str_bun_entry_15 = StringVar()
            bun_entry_15=Entry(p_canvas_5,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_15)
            str_bun_entry_15.set(' 0.0')
            window_bun_entry_15 = p_canvas_5.create_window(860, 1020, anchor="nw", height=30, window=bun_entry_15)

            str_bun_entry_16 = StringVar()
            bun_entry_16=Entry(p_canvas_5,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_16)
            str_bun_entry_16.set(' 0.0')
            window_bun_entry_16 = p_canvas_5.create_window(860, 1095, anchor="nw", height=30, window=bun_entry_16)

            str_bun_entry_17 = StringVar()
            bun_entry_17=Entry(p_canvas_5,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_17)
            str_bun_entry_17.set(' 0.0')
            window_bun_entry_17 = p_canvas_5.create_window(990, 870, anchor="nw", height=30, window=bun_entry_17)

            str_bun_entry_18 = StringVar()
            bun_entry_18=Entry(p_canvas_5,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_18)
            str_bun_entry_18.set(' 0.0')
            window_bun_entry_18 = p_canvas_5.create_window(990, 945, anchor="nw", height=30, window=bun_entry_18)

            str_bun_entry_19 = StringVar()
            bun_entry_19=Entry(p_canvas_5,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_19)
            str_bun_entry_19.set(' 0.0')
            window_bun_entry_19 = p_canvas_5.create_window(990, 1020, anchor="nw", height=30, window=bun_entry_19)

            str_bun_entry_20 = StringVar()
            bun_entry_20=Entry(p_canvas_5,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_20)
            str_bun_entry_20.set(' 0.0')
            window_bun_entry_20 = p_canvas_5.create_window(990, 1095, anchor="nw", height=30, window=bun_entry_20)

            str_bun_entry_21 = StringVar()
            bun_entry_21=Entry(p_canvas_5,width=19,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_21)
            str_bun_entry_21.set(' 0.0')
            window_bun_entry_21 = p_canvas_5.create_window(1120, 870, anchor="nw", height=30, window=bun_entry_21)

            str_bun_entry_22 = StringVar()
            bun_entry_22=Entry(p_canvas_5,width=19,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_22)
            str_bun_entry_22.set(' 0.0')
            window_bun_entry_22 = p_canvas_5.create_window(1120, 945, anchor="nw", height=30, window=bun_entry_22)

            str_bun_entry_23 = StringVar()
            bun_entry_23=Entry(p_canvas_5,width=19,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_23)
            str_bun_entry_23.set(' 0.0')
            window_bun_entry_23 = p_canvas_5.create_window(1120, 1020, anchor="nw", height=30, window=bun_entry_23)

            str_bun_entry_24 = StringVar()
            bun_entry_24=Entry(p_canvas_5,width=19,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_24)
            str_bun_entry_24.set(' 0.0')
            window_bun_entry_24 = p_canvas_5.create_window(1120, 1095, anchor="nw", height=30, window=bun_entry_24)


            bun_sub_btn1=Button(p_canvas_5,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_bun_sub_btn1 = p_canvas_5.create_window(575, 1200, anchor="nw", window=bun_sub_btn1)


        p_btn_4=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=bun_add_item)
        window_p_btn_4 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_4,tags=('apbutton4'))

        def pro_back_1():
            pro_frame_1.grid_forget()
            pro_frame.grid(row=0,column=0,sticky='nsew')

        pbck_btn1=Button(p_canvas_1,text='??? Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=pro_back_1)
        window_pbck_btn1 = p_canvas_1.create_window(0, 0, anchor="nw", window=pbck_btn1,tags=('apbutton5'))


    pbtn1=Button(pro_canvas,text='Add Products', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_product)
    window_pbtn1 = pro_canvas.create_window(0, 0, anchor="nw", window=pbtn1,tags=('pbutton1'))

    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Expenses Tab}
    tab_exp = ttk.Notebook(tab4)
    tab4_1 =  ttk.Frame(tab_exp)
    tab4_2=  ttk.Frame(tab_exp)
    tab_exp.add(tab4_1,compound = LEFT, text ='Expenses')
    tab_exp.add(tab4_2,compound = LEFT, text ='Supliers')
    tab_exp.pack(expand = 1, fill ="both")
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333{Pay Roll Tab}
    tab_payroll = ttk.Notebook(tab5)
    tab5_1 =  ttk.Frame(tab_payroll)
    tab5_2=  ttk.Frame(tab_payroll)
     
    tab_payroll.add(tab5_1,compound = LEFT, text ='Employee')
    tab_payroll.add(tab5_2,compound = LEFT, text ='Payslip')

    tab_payroll.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Report Tab}

    tab_report = ttk.Notebook(tab6)
    tab6_1 =  ttk.Frame(tab_report)
    tab6_2=  ttk.Frame(tab_report)
    tab6_3 = ttk.Frame(tab_report)
    tab6_4=  ttk.Frame(tab_report)

    
        
    tab_report.add(tab6_1,compound = LEFT, text ='Profit & Loss')
    tab_report.add(tab6_2,compound = LEFT, text ='Balance Sheet')
    tab_report.add(tab6_3,compound = LEFT, text ='Accounts Receivables')
    tab_report.add(tab6_4,compound = LEFT, text ='Accounts Payables')
 
    tab_report.pack(expand = 1, fill ="both")

    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Taxes}

    tab_tax = ttk.Notebook(tab7)
    tab7_1 =  ttk.Frame(tab_tax)
    tab7_2=  ttk.Frame(tab_tax)

    tab_tax.add(tab7_1,compound = LEFT, text ='GST')
    tab_tax.add(tab7_2,compound = LEFT, text ='New')

    tab_tax.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Accounting}
    tab_account = ttk.Notebook(tab8)
    tab8_1 =  ttk.Frame(tab_account)
    tab8_2=  ttk.Frame(tab_account)

    tab_account.add(tab8_1,compound = LEFT, text ='Chart Of Accounts')
    tab_account.add(tab8_2,compound = LEFT, text ='Reconcile')
   
 
    tab_account.pack(expand = 1, fill ="both")
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Cash Management}
    tab_cash = ttk.Notebook(tab10)
    
    tab10_1 =  ttk.Frame(tab_cash)
    tab10_2=  ttk.Frame(tab_cash)
    tab10_3 = ttk.Frame(tab_cash)

    tab_cash.add(tab10_1,compound = LEFT, text ='Cash Position')
    tab_cash.add(tab10_2,compound = LEFT, text ='Cash Flow Analyzer')
    tab_cash.add(tab10_3,compound = LEFT, text ='Check Cash Flow')

    tab_cash.pack(expand = 1, fill ="both")
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{My Account}
    Sys_mains_frame=Frame(tab9, height=750,bg="#2f516f")
    Sys_mains_frame.pack(fill=X)

#---------------------------------------------------------------------------------------------------------------Company Second Portion
def cmpny_crt2():
    main_frame_cmpny.pack_forget()
    global main_frame_cmpny2
    main_frame_cmpny2=Frame(root, height=750,bg="#213b52")
    main_frame_cmpny2.pack(fill=X,)

    cmpny_dt_frm2=Frame(main_frame_cmpny2, height=650, width=500,bg="white")
    cmpny_dt_frm2.pack(pady=105)

    def responsive_wid_cmp2(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("cmpny_hd1",dwidth/40,dheight/15)
        dcanvas.coords("nm_nm2",dwidth/6,dheight/5)
        dcanvas.coords("cmpny_cntry",dwidth/6,dheight/3.2)
        dcanvas.coords("cmpny_cntry2",dwidth/6,dheight/2.35)
        dcanvas.coords("r1",dwidth/2.2,dheight/1.8)
        dcanvas.coords("r2",dwidth/2.2,dheight/1.6)
        dcanvas.coords("cmpny_cntry3",dwidth/6,dheight/1.38)
        dcanvas.coords("button_cmp2",dwidth/4.3,dheight/1.2)
        dcanvas.coords("button_cmp3",dwidth/1.9,dheight/1.2)

        dcanvas.coords("cmp_lbl1",dwidth/6,dheight/3.8)
        dcanvas.coords("cmp_lbl2",dwidth/6,dheight/2.7)
        dcanvas.coords("cmp_lbl3",dwidth/6,dheight/2)
        dcanvas.coords("cmp_lbl4",dwidth/6,dheight/1.46)
        

    lf_cmpy2= Canvas(cmpny_dt_frm2,height=650, width=500)
    lf_cmpy2.bind("<Configure>", responsive_wid_cmp2)
    lf_cmpy2.pack(fill=X)

    def name_ent2(event):
        if nm_nm2.get()=="Legal Business Name":
            nm_nm2.delete(0,END)
        else:
            pass


    cmpny_hd1=Label(lf_cmpy2, text="Let's Start Building Your FinsYs",font=('Calibri 28 bold'), fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_hd1, tag=("cmpny_hd1"))

    

    nm_nm2 = Entry(cmpny_dt_frm2, width=30, font=('Calibri 16'),borderwidth=2)
    nm_nm2.insert(0,"Legal Business Name")
    nm_nm2.bind("<Button-1>",name_ent2)
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=nm_nm2, tag=("nm_nm2"))

    cmp_lbl1=Label(cmpny_dt_frm2, text="Your Industry",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl1, tag=("cmp_lbl1"))

    invset_bg_var = StringVar()
    cmpny_cntry = ttk.Combobox(cmpny_dt_frm2,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
    
    cmpny_cntry['values'] = ('Accounting Services','Consultants, doctors, Lawyers and similar','Information Tecnology','Manufacturing','Professional, Scientific and Technical Services','Restaurant/Bar and similar','Retail and Smilar','Other Finanacial Services')
    cmpny_cntry.current(0)
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry, tag=("cmpny_cntry"))

    cmp_lbl2=Label(cmpny_dt_frm2, text="Company type",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl2, tag=("cmp_lbl2"))

    invset_bg_var = StringVar()
    cmpny_cntry2 = ttk.Combobox(cmpny_dt_frm2,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
    
    cmpny_cntry['values'] = ('Private Limited Company','Public Limited Company','Joint-Venture Company','Partnership Firm Company','One Person Company','Branch Office Company','Non Government Organization')
    cmpny_cntry.current(0)
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry2, tag=("cmpny_cntry2"))
    
    cmp_lbl3=Label(cmpny_dt_frm2, text="Do you have an Accountant, Bookkeeper or Tax Pro ?",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl3, tag=("cmp_lbl3"))

    bs_cus_ct=StringVar()
    r1=Radiobutton(cmpny_dt_frm2, text = "Yes", variable = bs_cus_ct, value ="Yes",font=('Calibri 16'))
    r1.select()
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=r1, tag=("r1"))

    r2=Radiobutton(cmpny_dt_frm2, text = "No", variable = bs_cus_ct, value ="No",font=('Calibri 16'))
    r2.select()
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=r2, tag=("r2"))


    cmp_lbl4=Label(cmpny_dt_frm2, text="How do you like to get paid?",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl4, tag=("cmp_lbl4"))
    
    invset_bg_var = StringVar()
    cmpny_cntry3 = ttk.Combobox(cmpny_dt_frm2,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
    
    cmpny_cntry['values'] = ('Cash','Cheque','Credit card/Debit card','Bank Transfer','Paypal/Other service')
    cmpny_cntry.current(0)
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry3, tag=("cmpny_cntry3"))

    button_cmp2 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=cmpny_crt1,text="Previous",bg="#213b52")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=button_cmp2, tag=("button_cmp2"))
    button_cmp3 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=fun_sign_in,text="Submit",bg="#213b52")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=button_cmp3, tag=("button_cmp3"))
#-------------------------------------------------------------------------------------------------------------------company creation
def cmpny_crt1():
    try:
        main_frame_cmpny2.pack_forget()
    except:
        pass
    try:
        main_frame_signup.pack_forget()
    except:
        pass
    global main_frame_cmpny
    main_frame_cmpny=Frame(root, height=750,bg="#213b52")
    main_frame_cmpny.pack(fill=X,)

    cmpny_dt_frm=Frame(main_frame_cmpny, height=650, width=500,bg="white")
    cmpny_dt_frm.pack(pady=50)

    def name_ent(event):
        if nm_nm.get()=="Company Name":
            nm_nm.delete(0,END)
        else:
            pass

    def cmp_add(event):
        if cmp_cmpn.get()=="Company Address":
                cmp_cmpn.delete(0,END)
        else:
            pass
    def cty_ent(event):
        if cmp_cty.get()=="City":
            cmp_cty.delete(0,END)
        else:
            pass

    def em_ent(event):
        if cmp_email.get()=="Email":
                cmp_email.delete(0,END)
        else:
            pass
    def ph_ent(event):
        if cmp_ph.get()=="Phone Number":
            cmp_ph.delete(0,END)
        else:
            pass

    def fil_ent(event):
        
        cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
        
        cmp_files.delete(0,END)
        cmp_files.insert(0,cmp_logo)
    
    def responsive_wid_cmp1(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("cmpny_hd",dwidth/2,dheight/13)
        dcanvas.coords("nm_nm",dwidth/2,dheight/5)
        dcanvas.coords("cmp_cmpn",dwidth/2,dheight/3.5)
        dcanvas.coords("cmp_cty",dwidth/2,dheight/2.7)
        dcanvas.coords("cmpny_cntry",dwidth/2,dheight/2.2)
        dcanvas.coords("cmp_pin",dwidth/2,dheight/1.85)
        dcanvas.coords("cmp_email",dwidth/2,dheight/1.6)
        dcanvas.coords("cmp_ph",dwidth/2,dheight/1.4)
        dcanvas.coords("cmp_files",dwidth/2,dheight/1.25)
        dcanvas.coords("button_cmp",dwidth/2,dheight/1.1)


    lf_cmpy1= Canvas(cmpny_dt_frm,height=650, width=500)
    lf_cmpy1.bind("<Configure>", responsive_wid_cmp1)
    lf_cmpy1.pack(fill=X)

    cmpny_hd=Label(lf_cmpy1, text="We're Happy you're Here!",font=('Calibri 30 bold'), fg="black")
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_hd, tag=("cmpny_hd"))


    nm_nm = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
    nm_nm.insert(0,"Company Name")
    nm_nm.bind("<Button-1>",name_ent)
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=nm_nm, tag=("nm_nm"))

    cmp_cmpn = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_cmpn.insert(0,"Company Address")
    cmp_cmpn.bind("<Button-1>",cmp_add)
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cmpn, tag=("cmp_cmpn"))

    cmp_cty = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_cty.insert(0,"City")
    cmp_cty.bind("<Button-1>",cty_ent)
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cty, tag=("cmp_cty"))

    invset_bg_var = StringVar()
    cmpny_cntry = ttk.Combobox(lf_cmpy1,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_cntry, tag=("cmpny_cntry"))
    cmpny_cntry['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
    cmpny_cntry.current(0)

    cmp_pin = Spinbox(lf_cmpy1,from_=1,to=1000000,width=29, font=('Calibri 16'),borderwidth=2)
    cmp_pin.delete(0,END)
    cmp_pin.insert(0,"Pincode")
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_pin, tag=("cmp_pin"))
   

    cmp_email = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_email.insert(0,"Email")
    cmp_email.bind("<Button-1>",em_ent)
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_email, tag=("cmp_email"))

    cmp_ph = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_ph.insert(0,"Phone Number")
    cmp_ph.bind("<Button-1>",ph_ent)
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_ph, tag=("cmp_ph"))

    cmp_files = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_files.insert(0,"No file Chosen")
    cmp_files.bind("<Button-1>",fil_ent)
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_files, tag=("cmp_files"))

    button_cmp = customtkinter.CTkButton(master=lf_cmpy1,command=cmpny_crt2,text="Next",bg="#213b52")
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=button_cmp, tag=("button_cmp"))
    
#--------------------------------------------------------------------------------------------------------Sign in frame in signup section
def fun_sign_in():
    print("haii")
    try:
        main_frame_signup.pack_forget()
    except:
        pass
    try:
        main_frame_cmpny2.pack_forget()
    except:
        pass

    main_frame_signin.pack(fill=X,)
    


#---------------------------------------------------------------------------------------------------------------------Sign Up Section
def func_sign_up():
    
    global main_frame_signup
    main_frame_signin.pack_forget()

    main_frame_signup=Frame(root, height=750)
    main_frame_signup.pack(fill=X,)

    def responsive_wid_signup(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("round_signup",dwidth/2,-dheight/.5,dwidth/.7,dheight/.5)
        dcanvas.coords("sign_in_lb",dwidth/6,dheight/12)
        dcanvas.coords("fst_nm",dwidth/8.5,dheight/5)
        dcanvas.coords("lst_nm",dwidth/8.5,dheight/3.5)
        dcanvas.coords("sys_em",dwidth/8.5,dheight/2.7)
        dcanvas.coords("sys_usr",dwidth/8.5,dheight/2.2)
        dcanvas.coords("sys_pass",dwidth/8.5,dheight/1.85)
        dcanvas.coords("sys_cf",dwidth/8.5,dheight/1.6)
        dcanvas.coords("button_sign",dwidth/6,dheight/1.4)
        dcanvas.coords("lft_lab",dwidth/1.4,dheight/18)
        dcanvas.coords("lft_lab2",dwidth/1.52,dheight/10)
        dcanvas.coords("btn_signup2",dwidth/1.36,dheight/6.6)
        dcanvas.coords("label_img",dwidth/1.8,dheight/5)
        
        


    lf_signup= Canvas(main_frame_signup,width=1500, height=1500)
    lf_signup.bind("<Configure>", responsive_wid_signup)
    lf_signup.pack(fill=X)

    lf_signup.create_oval(0,0,0,0,fill="#213b52", tag=("round_signup"))

    # #--------------------------------------------------------------------------------sign up section
    sign_in_lb=Label(lf_signup, text="Sign Up",font=('Calibri 30 bold'), fg="black")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sign_in_lb, tag=("sign_in_lb"))

    def nme(event):
        if fst_nm.get()=="Firstname":
            fst_nm.delete(0,END)
        else:
            pass

    def nme1(event):
        if lst_nm.get()=="Lastname":
            lst_nm.delete(0,END)
        else:
            pass
        
    def nme2(event):
        if sys_em.get()=="Email":
            sys_em.delete(0,END)
        else:
            pass
        
        
    def nme3(event):
        if sys_usr.get()=="Username":
            sys_usr.delete(0,END)
        else:
            pass
        
    def nme4(event):
        if sys_pass.get()=="Password":
            sys_pass.delete(0,END)
        else:
            pass
    
    def nme5(event):
        if sys_cf.get()=="Confirm Password":
            sys_cf.delete(0,END)
        else:
            pass
    
    

    fst_nm = Entry(lf_signup, width=25, font=('Calibri 16'))
    fst_nm.insert(0,"Firstname")
    fst_nm.bind("<Button-1>",nme)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=fst_nm, tag=("fst_nm"))

    lst_nm = Entry(lf_signup,  width=25, font=('Calibri 16'))
    lst_nm.insert(0,"Lastname")
    lst_nm.bind("<Button-1>",nme1)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lst_nm, tag=("lst_nm"))

    sys_em = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_em.insert(0,"Email")
    sys_em.bind("<Button-1>",nme2)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_em, tag=("sys_em"))

    sys_usr = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_usr.insert(0,"Username")
    sys_usr.bind("<Button-1>",nme3)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_usr, tag=("sys_usr"))

    sys_pass = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_pass.insert(0,"Password")
    sys_pass.bind("<Button-1>",nme4)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_pass, tag=("sys_pass"))

    sys_cf = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_cf.insert(0,"Confirm Password")
    sys_cf.bind("<Button-1>",nme5)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_cf, tag=("sys_cf"))

    button_sign = customtkinter.CTkButton(master=lf_signup, command=cmpny_crt1,text="Sign Up",bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=button_sign, tag=("button_sign"))

    label_img = Label(lf_signup, image = sign_up,bg="#213b52", width=800,anchor="w")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=label_img, tag=("label_img"))
    
    

    lft_lab=Label(lf_signup, text="One of us ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab, tag=("lft_lab"))
    lft_lab2=Label(lf_signup, text="click here for work with FinsYs.",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab2, tag=("lft_lab2"))

    btn_signup2 = Button(lf_signup, text='Sign In', command=fun_sign_in, bg="white", fg="black",borderwidth = 3,height=1,width=10)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=btn_signup2, tag=("btn_signup2"))


main_frame_signin=Frame(root, height=750)
main_frame_signin.pack(fill=X,)
# main_frame_signin=Frame(root)
# main_frame_signin.grid(row=0,column=0,sticky='nsew')
# main_frame_signin.grid_rowconfigure(0,weight=1)
# main_frame_signin.grid_columnconfigure(0,weight=1)



def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

def sig_pass(event):
        if pass_ent.get()=="Password":
            pass_ent.delete(0,END)
        else:
            pass


def responsive_wid_login(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("sign_inlb",dwidth/1.4,dheight/4)

        dcanvas.coords("nm_ent",dwidth/1.5,dheight/2.7)
        dcanvas.coords("pass_ent",dwidth/1.5,dheight/2.2)
        dcanvas.coords("button",dwidth/1.4,dheight/1.8)
        dcanvas.coords("round_login",-dwidth/2,-dheight/.5,dwidth/2,dheight/.5)
        dcanvas.coords("lft_lab",dwidth/4,dheight/18)
        dcanvas.coords("lft_lab2",dwidth/6,dheight/10)
        dcanvas.coords("btn2",dwidth/3.7,dheight/6.6)
        dcanvas.coords("img",dwidth/16,dheight/5.5)
    

lf_signup= Canvas(main_frame_signin,width=1366,height=750)
lf_signup.bind("<Configure>", responsive_wid_login)
lf_signup.pack(fill=X)

sign_inlb=Label(lf_signup, text="Sign In",font=('Calibri 30 bold'), fg="black")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sign_inlb, tag=("sign_inlb"))

nm_ent = Entry(lf_signup, width=25, font=('Calibri 16'))
nm_ent.insert(0,"Username")
nm_ent.bind("<Button-1>",sig_nm)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=nm_ent, tag=("nm_ent"))

pass_ent = Entry(lf_signup, width=25, font=('Calibri 16'))
pass_ent.insert(0,"Password")
pass_ent.bind("<Button-1>",sig_pass)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=pass_ent, tag=("pass_ent"))

button = customtkinter.CTkButton(master=main_frame_signin,command=main_sign_in,text="Log In",bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=button, tag=("button"))

# #------------------------------------------------------------------------------------------------------------------------left canvas

lf_signup.create_oval(0,0,0,0,fill="#213b52", tag=("round_login"))

img = Label(lf_signup, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=img, tag=("img"))

lft_lab=Label(lf_signup, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab, tag=("lft_lab"))
lft_lab2=Label(lf_signup, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab2, tag=("lft_lab2"))

btn2 = Button(main_frame_signin, text = 'Sign Up', command = func_sign_up, bg="white", fg="black",borderwidth = 3,height=1,width=10)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=btn2, tag=("btn2"))

root.mainloop()