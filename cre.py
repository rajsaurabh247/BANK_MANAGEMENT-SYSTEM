


from tkinter import messagebox
import sqlite3
try:
    from Tkinter import *
except ImportError:
    from tkinter import *







class BANK_MANAGEMENT_create:


    def __init__(self):


        def chk_acc():
            while True:

                self.l = str(self.acc.get())

                if self.l.isdigit() == True and len(self.l) != 0:
                    self.Text1.delete(1.0, END)

                    self.Text1.insert(INSERT, "A/C NUMBER HAS BEEN ENTERED""\n")
                    break
                else:
                    self.Text1.delete(1.0, END)
                    self.Text1.insert(INSERT, "INVALID INPUT! PLEASE ENTER RELEVENT ACCOUNT NUMBER""\n")
                    break


        def chk_name():
            while True:

                self.k = str(self.name.get())


                if len(self.k) != 0 and self.k.isdigit() != True and self.k.isspace()!= True:
                    self.Text1.delete(1.0, END)

                    self.Text1.insert(INSERT, "NAME HAS BEEN ENTERED""\n")
                    break
                else:
                    self.Text1.delete(1.0, END)
                    self.Text1.insert(INSERT, "INVALID INPUT! PLEASE ENTER A VALID NAME""\n")

                    break


        def chk_age():
            while True:
                self.a=str(self.age.get())
                if len(self.a)!=0 and self.a.isdigit()==True:
                    if int(self.a)>=18:
                        self.Text1.delete(1.0, END)
                        self.Text1.insert(INSERT, "AGE HAS BEEN ENTERED""\n")
                        break
                    elif int(self.a) < 18:
                        messagebox.showinfo("WARNING!", "CUSTOMER SHOULD BE ATLEAST 18 YEARS OLD")
                        break
                    break



                else:

                    self.Text1.delete(1.0, END)
                    self.Text1.insert(INSERT, "INVALID INPUT! ""\n")

                    break

        def chk_add():
            while True:
                self.g = str(self.addr.get())

                ak = self.g.isdigit()
                if len(self.g) != 0 and ak != True:
                    self.Text1.delete(1.0, END)

                    self.Text1.insert(INSERT, "ADDRESS HAS BEEN ENTERED""\n")
                    break
                else:
                    self.Text1.delete(1.0, END)
                    self.Text1.insert(INSERT, "INVALID INPUT! PLEASE ENTER A VALID ADDRESS""\n")

                    break

        def chk_mo():
            while True:

                self.h = str(self.mobile.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    self.Text1.delete(1.0, END)

                    self.Text1.insert(INSERT, "MOBILE NUMBER HAS BEEN ENTERED""\n")
                    break

                elif len(self.h)>10 or len(self.h)<10:
                    self.Text1.delete(1.0, END)
                    messagebox.showinfo("WARNING!", "MOBILE NUMBER SHOULD BE OF 10 DIGITS")
                    break

                else:
                    self.Text1.delete(1.0, END)
                    self.Text1.insert(INSERT, "INVALID INPUT! PLEASE ENTER A VALID MOBILE NUMBER""\n")
                break

        def adhr_upd():
            while True:

                self.au = str(self.adhaar.get())

                if self.au.isdigit() == True and len(self.au) != 0 and len(self.au) == 12:
                    self.Text1.delete(1.0, END)

                    self.Text1.insert(INSERT, "ADHAAR NUMBER HAS BEEN ENTERED""\n")
                    break

                elif len(self.au)>12 or len(self.au)<12:
                    self.Text1.delete(1.0, END)
                    messagebox.showinfo("WARNING!", "ADHAAR NUMBER SHOULD BE OF 12 DIGITS")
                    break

                else:
                    self.Text1.delete(1.0, END)
                    self.Text1.insert(INSERT, "INVALID INPUT! PLEASE ENTER VALID ADHAAR NO ""\n")
                    break








        def amt_upd():


                while True:

                    self.y = str(self.amount.get())

                    if len(self.y) != 0  :

                        self.Text1.delete(1.0, END)

                        self.Text1.insert(INSERT, "AMOUNT HAS BEEN ENTERED  ""\n")
                        break
                    else:
                        self.Text1.delete(1.0, END)
                        self.Text1.insert(INSERT, "ENTER GREATER AMOUNT  ""\n")

                        break





        def enter(self,x):
            account1 = self.acc.get()
            name1=self.name.get()
            gender1=self.var
            age1=self.age.get()
            address1=self.addr.get()
            mobile1=self.mobile.get()
            adhaar1 = self.adhaar.get()
            amount1=self.amount.get()
            self.y=x
            if self.y==1:
                acctype1="CURRENT"
            else:
                acctype1 = "SAVING"
            if self.var.get()==1:
                gender1="MALE"
            else:
                gender1 = "FEMALE"


            if len(str(self.amount.get())) != 0 and len(str(self.name.get())) != 0 and len(str(self.addr.get())) != 0 and len(str(self.mobile.get())) != 0 and len(str(self.acc.get())) != 0 and len(str(self.adhaar.get())) != 0 and len(str(self.age.get())) != 0:


                with db:
                    cursor=db.cursor()
                    try:

                        cursor.execute('INSERT INTO customer(account,name,gender,age,address,mobile,adhaar,amount,acctype) VALUES(?,?,?,?,?,?,?,?,?)',(account1,name1,gender1,age1,address1,mobile1,adhaar1,amount1,acctype1))
                        if self.y==1:

                            messagebox.showinfo("SUCCESS!", "CURRENT ACCOUNT CREATED")
                        else:

                            messagebox.showinfo("SUCCESS!", "SAVING ACCOUNT CREATED")

                    except:
                        messagebox.showinfo("SORRY!", "ACCOUNT NO. ALREADY EXISTS")

                    db.commit()
            else:
                 messagebox.showinfo("ERROR!","FILL ALL THE FIELDS CORRECTLY")




        def submit_clicked():

            if self.var1.get()==1  and self.var2.get()==0 :
                x=1


                enter(self,x)





            elif self.var1.get() == 0 and self.var2.get() == 1:

                x=0
                if int(self.amount.get())>=1000:
                    enter(self,x)
                else:
                    messagebox.showinfo("ERROR!", "MINIMUM BALANCE FOR SAVING A/C MUST BE Rs.1000")




            else:
                self.Text1.insert(INSERT, "FILL ALL THE FIELDS CORRECTLY""\n")

        root = Tk()
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS customer(account INTEGER UNIQUE, name TEXT, gender TEXT, age INTEGER, address TEXT, mobile INTEGER,adhaar INTEGER UNIQUE, amount INTEGER, acctype TEXT)")
        db.commit()


        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 30 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 16 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 19 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1363x749+0+0")
        root.title("ACCOUNT CREATION")
        root.configure(background="yellow")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")

        self.Text1 = Text(root)
        self.Text1.place(relx=0.03, rely=0.82, relheight=0.11, relwidth=0.93)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=994)
        self.Text1.configure(wrap=WORD)

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.03, rely=0.01, relheight=0.12, relwidth=0.93)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="blue")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=995)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.04, rely=0.11, relheight=0.84, relwidth=0.5)
        self.Message1.configure(background="blue")
        self.Message1.configure(font=font11)
        self.Message1.configure(foreground="white")
        self.Message1.configure(highlightbackground="#ffffff")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''SELECTED CHOICE''')
        self.Message1.configure(width=496)

        self.Message2 = Message(self.Frame1)
        self.Message2.place(relx=0.52, rely=0.11, relheight=0.84, relwidth=0.07)
        self.Message2.configure(background="blue")
        self.Message2.configure(font=font11)
        self.Message2.configure(foreground="white")
        self.Message2.configure(highlightbackground="#ffffff")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text=''':''')
        self.Message2.configure(width=66)

        self.Message3 = Message(self.Frame1)
        self.Message3.place(relx=0.57, rely=0.11, relheight=0.84, relwidth=0.38)
        self.Message3.configure(background="blue")
        self.Message3.configure(font=font11)
        self.Message3.configure(foreground="white")
        self.Message3.configure(highlightbackground="#ffffff")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''CREATE ACCOUNT''')
        self.Message3.configure(width=366)

        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

        self.Frame2 = Frame(root)
        self.Frame2.place(relx=0.03, rely=0.15, relheight=0.66, relwidth=0.93)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="yellow")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=995)


        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0, rely=0.001, height=44, width=380)
        self.Label1.configure(background="yellow")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="blue")
        self.Label1.configure(text='''ENTER A/C NUMBER''')


        self.Entry1 = Entry(self.Frame2)
        self.acc=StringVar()
        self.Entry1.place(relx=0.47, rely=0.01, height=34, relwidth=0.43)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#bfbfbf")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=424)
        self.Entry1.configure(textvariable=self.acc)


        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.91, rely=0.01, height=33, width=43)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OK''')
        self.Button1.configure(command=chk_acc)


        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0, rely=0.09, height=47, width=380)
        self.Label2.configure(activebackground="#ffffff")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="yellow")
        self.Label2.configure(disabledforeground="#bfbfbf")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="blue")
        self.Label2.configure(highlightbackground="#ffffff")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''ENTER CUSTOMER NAME''')


        self.Entry2 = Entry(self.Frame2)
        self.name=StringVar()
        self.Entry2.place(relx=0.47, rely=0.095,height=34, relwidth=0.43)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#bfbfbf")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="black")
        self.Entry2.configure(highlightbackground="#ffffff")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#e6e6e6")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(textvariable=self.name)


        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.91, rely=0.095, height=33, width=43)
        self.Button2.configure(activebackground="#ffffff")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#ffffff")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''OK''')
        self.Button2.configure(command=chk_name)


        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0, rely=0.18, height=47, width=380)
        self.Label3.configure(activebackground="#ffffff")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="yellow")
        self.Label3.configure(disabledforeground="#bfbfbf")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="blue")
        self.Label3.configure(highlightbackground="#ffffff")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''SELECT GENDER''')










        self.Frame3 = Frame(root)
        self.Frame3.place(relx=0.4651, rely=0.275, height=34)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="0")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="yellow")
        self.Frame3.configure(highlightbackground="#ffffff")
        self.Frame3.configure(highlightcolor="black")
        self.Frame3.configure(width=395)

        self.var=IntVar()
        r1=Radiobutton(self.Frame3,anchor=W,text="Male",value=1,variable=self.var,width=16)
        r1.pack(anchor=W,side=LEFT,ipadx=10)
        r1.configure(background="yellow")
        r2=Radiobutton(self.Frame3,text="Female",value=2,variable=self.var,width=16)
        r2.pack(anchor=W,side=LEFT)
        r2.configure(background="yellow")


        self.Label4 = Label(self.Frame2)
        self.Label4.place(relx=0, rely=0.27, height=47, width=380)
        self.Label4.configure(activebackground="#ffffff")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="yellow")
        self.Label4.configure(disabledforeground="#bfbfbf")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="blue")
        self.Label4.configure(highlightbackground="#ffffff")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''ENTER AGE''')

        self.Entry4 = Entry(self.Frame2)
        self.age = StringVar()
        self.Entry4.place(relx=0.47, rely=0.28,height=34, relwidth=0.43)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#bfbfbf")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="black")
        self.Entry4.configure(highlightbackground="#ffffff")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#e6e6e6")
        self.Entry4.configure(selectforeground="black")
        self.Entry4.configure(textvariable=self.age)

        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.91, rely=0.28, height=33, width=43)
        self.Button4.configure(activebackground="#ffffff")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#ffffff")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#ffffff")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''OK''')
        self.Button4.configure(command=chk_age)


        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0, rely=0.36, height=47, width=380)
        self.Label5.configure(activebackground="#ffffff")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="yellow")
        self.Label5.configure(disabledforeground="#bfbfbf")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="blue")
        self.Label5.configure(highlightbackground="#ffffff")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''ENTER THE ADDRESS''')


        self.Entry5 = Entry(self.Frame2)
        self.addr = StringVar()
        self.Entry5.place(relx=0.47, rely=0.37,height=34, relwidth=0.43)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#bfbfbf")
        self.Entry5.configure(font=font10)
        self.Entry5.configure(foreground="black")
        self.Entry5.configure(highlightbackground="#ffffff")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="#e6e6e6")
        self.Entry5.configure(selectforeground="black")
        self.Entry5.configure(textvariable=self.addr)

        self.Button5 = Button(self.Frame2)
        self.Button5.place(relx=0.91, rely=0.37, height=33, width=43)
        self.Button5.configure(activebackground="#ffffff")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#ffffff")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#ffffff")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''OK''')
        self.Button5.configure(command=chk_add)



        self.Label6 = Label(self.Frame2)
        self.Label6.place(relx=0, rely=0.46, height=40, width=380)
        self.Label6.configure(activebackground="#ffffff")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="yellow")
        self.Label6.configure(disabledforeground="#bfbfbf")
        self.Label6.configure(font=font12)
        self.Label6.configure(foreground="blue")
        self.Label6.configure(highlightbackground="#ffffff")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''ENTER MOB NUMBER''')





        self.Entry6 = Entry(self.Frame2)
        self.mobile=StringVar()
        self.Entry6.place(relx=0.47, rely=0.46,height=34, relwidth=0.43)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#bfbfbf")
        self.Entry6.configure(font=font10)
        self.Entry6.configure(foreground="black")
        self.Entry6.configure(highlightbackground="#ffffff")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="#e6e6e6")
        self.Entry6.configure(selectforeground="black")
        self.Entry6.configure(textvariable=self.mobile)


        self.Button6 = Button(self.Frame2)
        self.Button6.place(relx=0.91, rely=0.46, height=33, width=43)
        self.Button6.configure(activebackground="#ffffff")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#ffffff")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#ffffff")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''OK''')
        self.Button6.configure(command=chk_mo)




        self.Label7 = Label(self.Frame2)
        self.Label7.place(relx=0, rely=0.54, height=47, width=380)
        self.Label7.configure(activebackground="#ffffff")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="yellow")
        self.Label7.configure(disabledforeground="#bfbfbf")
        self.Label7.configure(font=font12)
        self.Label7.configure(foreground="blue")
        self.Label7.configure(highlightbackground="#ffffff")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''ENTER AADHAR NUMBER''')

        self.Entry7 = Entry(self.Frame2)
        self.adhaar = StringVar()
        self.Entry7.place(relx=0.47, rely=0.55, height=34, relwidth=0.43)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#bfbfbf")
        self.Entry7.configure(font=font10)
        self.Entry7.configure(foreground="black")
        self.Entry7.configure(highlightbackground="#ffffff")
        self.Entry7.configure(highlightcolor="black")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(selectbackground="#e6e6e6")
        self.Entry7.configure(selectforeground="black")
        self.Entry7.configure(textvariable=self.adhaar)

        self.Button7 = Button(self.Frame2)
        self.Button7.place(relx=0.91, rely=0.55, height=33, width=43)
        self.Button7.configure(activebackground="#ffffff")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#ffffff")
        self.Button7.configure(disabledforeground="#bfbfbf")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#ffffff")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''OK''')
        self.Button7.configure(command=adhr_upd)



        self.Label8 = Label(self.Frame2)
        self.Label8.place(relx=0, rely=0.64, height=42, width=380)
        self.Label8.configure(activebackground="#ffffff")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="yellow")
        self.Label8.configure(disabledforeground="#bfbfbf")
        self.Label8.configure(font=font12)
        self.Label8.configure(foreground="blue")
        self.Label8.configure(highlightbackground="#ffffff")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''ENTER INITIAL AMOUNT''')

        self.Entry8 = Entry(self.Frame2)
        self.amount = StringVar()
        self.Entry8.place(relx=0.47, rely=0.64, height=34, relwidth=0.43)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#bfbfbf")
        self.Entry8.configure(font=font10)
        self.Entry8.configure(foreground="black")
        self.Entry8.configure(highlightbackground="#ffffff")
        self.Entry8.configure(highlightcolor="black")
        self.Entry8.configure(insertbackground="black")
        self.Entry8.configure(selectbackground="#e6e6e6")
        self.Entry8.configure(selectforeground="black")
        self.Entry8.configure(textvariable=self.amount)

        self.Button8 = Button(self.Frame2)
        self.Button8.place(relx=0.91, rely=0.64, height=33, width=43)
        self.Button8.configure(activebackground="#ffffff")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#ffffff")
        self.Button8.configure(disabledforeground="#bfbfbf")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#ffffff")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''OK''')
        self.Button8.configure(command=amt_upd)












        self.Label9 = Label(self.Frame2)
        self.Label9.place(relx=0.28, rely=0.75, height=48, width=296)
        self.Label9.configure(activebackground="#ffffff")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="yellow")
        self.Label9.configure(disabledforeground="#bfbfbf")
        self.Label9.configure(font=font13)
        self.Label9.configure(foreground="black")
        self.Label9.configure(highlightbackground="#ffffff")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text=''' CHOOSE ACCOUNT TYPE :''')



        self.Checkbutton1 = Checkbutton(self.Frame2)
        self.var1 = IntVar()
        self.Checkbutton1.place(relx=0.15, rely=0.8, relheight=0.17
                , relwidth=0.14)
        self.Checkbutton1.configure(activebackground="#ffffff")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="yellow")
        self.Checkbutton1.configure(disabledforeground="#bfbfbf")
        self.Checkbutton1.configure(font=font14)
        self.Checkbutton1.configure(foreground="black")
        self.Checkbutton1.configure(highlightbackground="#ffffff")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''CURRENT''')
        self.Checkbutton1.configure(variable=self.var1)






        self.Checkbutton2 = Checkbutton(self.Frame2)
        self.var2 = IntVar()
        self.Checkbutton2.place(relx=0.5, rely=0.82, relheight=0.11
                , relwidth=0.16)
        self.Checkbutton2.configure(activebackground="#ffffff")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="yellow")
        self.Checkbutton2.configure(disabledforeground="#bfbfbf")
        self.Checkbutton2.configure(font=font13)
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#ffffff")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''SAVING''')
        self.Checkbutton2.configure(variable=self.var2)











        self.Button9 = Button(self.Frame2)
        self.Button9.place(relx=0.75, rely=0.77, height=83, width=156)
        self.Button9.configure(activebackground="#ffffff")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="blue")
        self.Button9.configure(disabledforeground="#bfbfbf")
        self.Button9.configure(font=font16)
        self.Button9.configure(foreground="white")
        self.Button9.configure(highlightbackground="#ffffff")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''SUBMIT''')
        self.Button9.configure(command=submit_clicked)






        root.mainloop()


if __name__ == '__main__':
    bank=BANK_MANAGEMENT_create()






