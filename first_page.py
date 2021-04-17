from tkinter import *
def close(e=1):
    root.destroy()
root=Tk()


Label(root,text='Project Title:Phonebook',font="Arial 20").grid(row=0,column=0)
root.geometry('750x750')
Label(root,text='Project of Python and Database',font="Arial 20").grid(row=1,column=1)

Label(root,text="Developed by: ANANTA PANDEY\n -----------------------",font="Arial 15",fg="blue").grid(row=2,column=1)
Label(root,text="make mouse movement over this window to close",fg="red").grid(row=3,column=1)
root.bind('<Motion>', close)
root.mainloop()
