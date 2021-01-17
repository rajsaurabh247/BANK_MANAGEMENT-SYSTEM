
import sqlite3
from tkinter import messagebox


try:
    from Tkinter import *
except ImportError:
    from tkinter import *



class New_Toplevel:

    def __init__(self):
        def closeacc():
            self.data = str(self.accno.get())

            if self.data.isdigit() == True and len(self.data) != 0:

                connt = sqlite3.connect('database.db')
                c = connt.cursor()

                c.execute("SELECT * from customer WHERE account = " + self.accno.get())
                row=c.fetchone()
                if row is None:
                    messagebox.showinfo("SORRY!","Account Doesn't Exist")
                else:
                    c.execute("DELETE FROM customer WHERE account = " + self.accno.get())
                    connt.commit()
                    connt.close()
                    messagebox.showinfo("SUCCESS!", " Account Closed")




            else:
                self.Text1.delete(1.0, END)
                self.Text1.insert(INSERT, "INVALID INPUT! PLEASE INPUT A VALID ACC NO.""\n")

        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 23 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 24 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1063x749+0+0")
        root.title("ACCOUNT CLOSING")
        root.configure(background="black")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.04, rely=0.04, relheight=0.91, relwidth=0.91)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="yellow")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.14, rely=0.12, height=46, width=442)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="yellow")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="blue")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''ENTER THE ACC NO.   ''')

        self.Entry1 = Entry(self.Frame1)
        self.accno=StringVar()
        self.Entry1.place(relx=0.67, rely=0.12,height=44, relwidth=0.17)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#bfbfbf")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#ffffff")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#e6e6e6")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=self.accno)







        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.05, rely=0.54, relheight=0.4, relwidth=0.89)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=824)
        self.Text1.configure(wrap=WORD)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.34, rely=0.28, height=93, width=286)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="blue")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''CLOSE ACCOUNT''')
        self.Button1.configure(command=closeacc)
        root.mainloop()



if __name__ == '__main__':
    out=New_Toplevel()
