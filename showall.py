
import sqlite3

try:
    from Tkinter import *
except ImportError:
    from tkinter import *






class BANK_MANAGEMENT_checkin:
    def __init__(self):
        root = Tk()

        connt = sqlite3.connect('database.db')
        cursor = connt.cursor()
        cursor.execute('SELECT * FROM customer')

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font11 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Times New Roman} -size 16 -weight bold " \
                 "-slant roman -underline 0 -overstrike 0"

        root.geometry("1363x749+0+0")
        root.title("ALL ACCOUNTS DETAILS")
        root.configure(background="black")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")



        self.Labelframe1 = LabelFrame(root)
        self.Labelframe1.place(relx=0.01, rely=0.04, relheight=0.95
                , relwidth=0.97)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font11)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''DETAILS OF ALL CUSTOMERS''')
        self.Labelframe1.configure(background="yellow")
        self.Labelframe1.configure(highlightbackground="#ffffff")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=760)

        self.Frame1 = Frame(self.Labelframe1)
        self.Frame1.place(relx=0, rely=0.1, relheight=0.86, relwidth=1
                , y=-31, h=15)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="yellow")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=355)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0, rely=0.1, height=37, width=105)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="blue")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="Padauk")
        self.Label1.configure(foreground="white")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''A/C NO''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.081, rely=0.1, height=37, width=224)
        self.Label2.configure(activebackground="#ffffff")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="blue")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="Padauk")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#ffffff")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''NAME''')

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.252, rely=0.1, height=37, width=115)
        self.Label3.configure(activebackground="#ffffff")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="blue")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="Padauk")
        self.Label3.configure(foreground="white")
        self.Label3.configure(highlightbackground="#ffffff")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''GENDER''')

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.34, rely=0.1, height=37, width=53)
        self.Label4.configure(activebackground="#ffffff")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="blue")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="Padauk")
        self.Label4.configure(foreground="white")
        self.Label4.configure(highlightbackground="#ffffff")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''AGE''')

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.381, rely=0.1, height=37, width=365)
        self.Label5.configure(activebackground="#ffffff")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="blue")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="Padauk")
        self.Label5.configure(foreground="white")
        self.Label5.configure(highlightbackground="#ffffff")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''ADDRESS''')

        self.Label6 = Label(self.Frame1)
        self.Label6.place(relx=0.66, rely=0.1, height=37, width=118)
        self.Label6.configure(activebackground="#ffffff")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="blue")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="Padauk")
        self.Label6.configure(foreground="white")
        self.Label6.configure(highlightbackground="#ffffff")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''MOBILE''')

        self.Label7 = Label(self.Frame1)
        self.Label7.place(relx=0.75, rely=0.1, height=37, width=145)
        self.Label7.configure(activebackground="#ffffff")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="blue")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="Padauk")
        self.Label7.configure(foreground="white")
        self.Label7.configure(highlightbackground="#ffffff")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''ADHAAR NO''')

        self.Label8 = Label(self.Frame1)
        self.Label8.place(relx=0.8615, rely=0.1, height=37, width=90)
        self.Label8.configure(activebackground="#ffffff")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="blue")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="Padauk")
        self.Label8.configure(foreground="white")
        self.Label8.configure(highlightbackground="#ffffff")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''AMOUNT''')

        self.Label9 = Label(self.Frame1)
        self.Label9.place(relx=0.931, rely=0.1, height=37, width=92)
        self.Label9.configure(activebackground="#ffffff")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="blue")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="Padauk")
        self.Label9.configure(foreground="white")
        self.Label9.configure(highlightbackground="#ffffff")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''TYPE''')

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0, rely=0.16, relheight=0.8, relwidth=0.08)
        self.Text1.configure(background="white")
        self.Text1.configure(font="Verdana")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=314)
        self.Text1.configure(wrap=WORD)

        self.Text2 = Text(self.Frame1)
        self.Text2.place(relx=0.08, rely=0.16, relheight=0.8, relwidth=0.17)
        self.Text2.configure(background="white")
        self.Text2.configure(font="Verdana")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=314)
        self.Text2.configure(wrap=WORD)

        self.Text3 = Text(self.Frame1)
        self.Text3.place(relx=0.25, rely=0.16, relheight=0.8, relwidth=0.1)
        self.Text3.configure(background="white")
        self.Text3.configure(font="Verdana")
        self.Text3.configure(foreground="black")
        self.Text3.configure(highlightbackground="#d9d9d9")
        self.Text3.configure(highlightcolor="black")
        self.Text3.configure(insertbackground="black")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(selectforeground="black")
        self.Text3.configure(width=314)
        self.Text3.configure(wrap=WORD)

        self.Text4 = Text(self.Frame1)
        self.Text4.place(relx=0.34, rely=0.16, relheight=0.8, relwidth=0.04)
        self.Text4.configure(background="white")
        self.Text4.configure(font="Verdana")
        self.Text4.configure(foreground="black")
        self.Text4.configure(highlightbackground="#d9d9d9")
        self.Text4.configure(highlightcolor="black")
        self.Text4.configure(insertbackground="black")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(selectforeground="black")
        self.Text4.configure(width=314)
        self.Text4.configure(wrap=WORD)

        self.Text5 = Text(self.Frame1)
        self.Text5.place(relx=0.38, rely=0.16, relheight=0.8, relwidth=0.28)
        self.Text5.configure(background="white")
        self.Text5.configure(font="Verdana")
        self.Text5.configure(foreground="black")
        self.Text5.configure(highlightbackground="#d9d9d9")
        self.Text5.configure(highlightcolor="black")
        self.Text5.configure(insertbackground="black")
        self.Text5.configure(selectbackground="#c4c4c4")
        self.Text5.configure(selectforeground="black")
        self.Text5.configure(width=314)
        self.Text5.configure(wrap=WORD)

        self.Text6 = Text(self.Frame1)
        self.Text6.place(relx=0.66, rely=0.16, relheight=0.8, relwidth=0.1)
        self.Text6.configure(background="white")
        self.Text6.configure(font="Verdana")
        self.Text6.configure(foreground="black")
        self.Text6.configure(highlightbackground="#d9d9d9")
        self.Text6.configure(highlightcolor="black")
        self.Text6.configure(insertbackground="black")
        self.Text6.configure(selectbackground="#c4c4c4")
        self.Text6.configure(selectforeground="black")
        self.Text6.configure(width=314)
        self.Text6.configure(wrap=WORD)

        self.Text7 = Text(self.Frame1)
        self.Text7.place(relx=0.75, rely=0.16, relheight=0.8, relwidth=0.11)
        self.Text7.configure(background="white")
        self.Text7.configure(font="Verdana")
        self.Text7.configure(foreground="black")
        self.Text7.configure(highlightbackground="#d9d9d9")
        self.Text7.configure(highlightcolor="black")
        self.Text7.configure(insertbackground="black")
        self.Text7.configure(selectbackground="#c4c4c4")
        self.Text7.configure(selectforeground="black")
        self.Text7.configure(width=314)
        self.Text7.configure(wrap=WORD)

        self.Text8 = Text(self.Frame1)
        self.Text8.place(relx=0.86, rely=0.16, relheight=0.8, relwidth=0.07)
        self.Text8.configure(background="white")
        self.Text8.configure(font="Verdana")
        self.Text8.configure(foreground="black")
        self.Text8.configure(highlightbackground="#d9d9d9")
        self.Text8.configure(highlightcolor="black")
        self.Text8.configure(insertbackground="black")
        self.Text8.configure(selectbackground="#c4c4c4")
        self.Text8.configure(selectforeground="black")
        self.Text8.configure(width=314)
        self.Text8.configure(wrap=WORD)

        self.Text9 = Text(self.Frame1)
        self.Text9.place(relx=0.93, rely=0.16, relheight=0.8, relwidth=0.28)
        self.Text9.configure(background="white")
        self.Text9.configure(font="Verdana")
        self.Text9.configure(foreground="black")
        self.Text9.configure(highlightbackground="#d9d9d9")
        self.Text9.configure(highlightcolor="black")
        self.Text9.configure(insertbackground="black")
        self.Text9.configure(selectbackground="#c4c4c4")
        self.Text9.configure(selectforeground="black")
        self.Text9.configure(width=314)
        self.Text9.configure(wrap=WORD)



        for row in cursor.fetchall():
            self.Text1.insert(INSERT, ""+str(row[0])+"\n")
            self.Text2.insert(INSERT, "" + row[1] + "\n")
            self.Text3.insert(INSERT, "" + str(row[2]) + "\n")
            self.Text4.insert(INSERT, "" + str(row[3]) + "\n")
            self.Text5.insert(INSERT, "" + str(row[4]) + "\n")
            self.Text6.insert(INSERT, "" + str(row[5]) + "\n")
            self.Text7.insert(INSERT, "" + str(row[6]) + "\n")
            self.Text8.insert(INSERT, "" + str(row[7]) + "\n")
            self.Text9.insert(INSERT, "" + str(row[8]) + "\n")




        root.mainloop()


if __name__ == '__main__':

    bank=BANK_MANAGEMENT_checkin()
