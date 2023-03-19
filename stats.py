#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 12, 2018 10:39:51 AM IST  platform: Linux

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import stats_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    stats_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    stats_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x450+650+150")
        top.title("New Toplevel")



        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.35, rely=0.222,height=23, relwidth=0.277)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

        self.Button1 = Button(top)
        self.Button1.place(relx=0.383, rely=0.311, height=29, width=129)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Next''')
        self.Button1.configure(width=129)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.35, rely=0.044, height=21, width=169)
        self.Label1.configure(text='''Player Statistics''')
        self.Label1.configure(width=169)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.35, rely=0.133, height=21, width=169)
        self.Label2.configure(text='''Enter Player Name''')
        self.Label2.configure(width=169)

        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.067, rely=0.4, relheight=0.567
                , relwidth=0.9)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(text='''Statistics''')
        self.Labelframe1.configure(width=540)






if __name__ == '__main__':
    vp_start_gui()


