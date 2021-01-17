import os
from subprocess import call

import sqlite3
try:
    from Tkinter import *
except ImportError:
    from tkinter import *



def new_account():
    call(["python", "cre.py"])
def show_all():
    call(["python", "showall.py"])
def close():
    call(["python", "close.py"])
def enquiry():
    call(["python","enquiry.py"])
def deposit():
    call(["python","deposit.py"])
def withdraw():
    call(["python","withdraw.py"])


class BANK_MANAGEMENT:
    def __init__(self):
        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1063x749+0+0")

        root.maxsize(1063,749)
        root.title("BANK MANAGEMENT")
        root.configure(background="black")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")



        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="yellow")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.03, rely=0.01, relheight=0.15, relwidth=0.86)
        self.Message1.configure(background="yellow")
        self.Message1.configure(font=font16)
        self.Message1.configure(foreground="black")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="white")
        self.Message1.configure(text='''WELCOME TO OUR BANK''')
        self.Message1.configure(width=791)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.18, rely=0.17, height=50,width=566)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="blue")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font14)
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''CREATE NEW ACCOUNT''')
        self.Button1.configure(width=566)
        self.Button1.configure(command=new_account)


        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.18, rely=0.26, height=50, width=566)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="blue")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="white")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''DEPOSIT AMOUNT''')
        self.Button2.configure(width=566)
        self.Button2.configure(command=deposit)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.18, rely=0.35, height=50, width=566)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="blue")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="white")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''WITHDRAW AMOUNT''')
        self.Button3.configure(width=566)
        self.Button3.configure(command=withdraw)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.18, rely=0.44, height=50, width=566)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="blue")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="white")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''SHOW ALL ACCOUNTS''')
        self.Button4.configure(width=566)
        self.Button4.configure(command=show_all)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.18, rely=0.53, height=50, width=566)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="blue")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="white")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''CLOSE AN ACCOUNT''')
        self.Button5.configure(width=566)
        self.Button5.configure(command=close)

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.18, rely=0.62, height=50, width=566)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="blue")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=font14)
        self.Button6.configure(foreground="white")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''ENQUIRY''')
        self.Button6.configure(width=566)
        self.Button6.configure(command=enquiry)

        self.Button7 = Button(self.Frame1)
        self.Button7.place(relx=0.18, rely=0.71, height=50, width=566)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="blue")
        self.Button7.configure(disabledforeground="#bfbfbf")
        self.Button7.configure(font=font14)
        self.Button7.configure(foreground="white")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''EXIT''')
        self.Button7.configure(width=566)
        self.Button7.configure(command=quit)


        root.mainloop()


if __name__ == '__main__':
    GUUEST=BANK_MANAGEMENT()


