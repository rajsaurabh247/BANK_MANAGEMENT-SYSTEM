
import sqlite3

from tkinter import messagebox
try:
    from Tkinter import *
except ImportError:
    from tkinter import *




class BANK_MANAGEMENT:
    def __init__(self):
        def info():
            self.accinfo = str(self.getaccount.get())
            self.amtinfo = str(self.getamount.get())




            if self.accinfo.isdigit() == True and len(self.accinfo) != 0 and self.amtinfo.isdigit() == True and len(self.amtinfo) != 0 and int(self.amtinfo)!=0:


                connt = sqlite3.connect('database.db')
                c = connt.cursor()

                c.execute("SELECT * from customer WHERE account = " + self.accinfo)
                row=c.fetchone()
                if row is None:
                    messagebox.showinfo("SORRY!","Account Doesn't Exist")
                else:


                    c.execute("UPDATE customer SET amount = amount+? WHERE account = ?" ,(self.amtinfo,self.accinfo))
                    connt.commit()
                    connt.close()
                    messagebox.showinfo("SUCCESS!", " Account UPDATED!")


            else:
                messagebox.showinfo("ERROR!", "INVALID ENTRY!")







        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 28 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 23 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        root.geometry("1063x749+0+0")
        root.title("DEPOSIT AMOUNT")
        root.configure(background="black")



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.87, relwidth=0.94)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="yellow")
        self.Frame1.configure(width=825)



        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.12, rely=0.21, height=28, width=377)
        self.Label1.configure(background="yellow")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="blue")
        self.Label1.configure(text='''ENTER THE A/C NO.   ''')

        self.Entry1 = Entry(self.Frame1)
        self.getaccount=StringVar()
        self.Entry1.place(relx=0.65, rely=0.21,height=40, relwidth=0.3)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=84)
        self.Entry1.configure(textvariable=self.getaccount)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.12, rely=0.34, height=48, width=377)
        self.Label2.configure(background="yellow")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="blue")
        self.Label2.configure(text='''ENTER THE AMOUNT   ''')

        self.Entry2 = Entry(self.Frame1)
        self.getamount =StringVar()
        self.Entry2.place(relx=0.65, rely=0.34, height=40, relwidth=0.3)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=84)
        self.Entry2.configure(textvariable=self.getamount)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.42, rely=0.51, height=74, width=197)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="blue")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SUBMIT''')
        self.Button1.configure(width=197)
        self.Button1.configure(command=info)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0, rely=0.02, relheight=0.12, relwidth=1)
        self.Message1.configure(background="blue")
        self.Message1.configure(font=font11)
        self.Message1.configure(foreground="white")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''DEPOSIT AMOUNT...!!!''')
        self.Message1.configure(width=460)
        root.mainloop()






if __name__ == '__main__':
    GETINFO=BANK_MANAGEMENT()
