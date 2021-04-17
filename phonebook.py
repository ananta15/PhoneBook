from first_page import *
import sqlite3
from tkinter import *
from tkinter import messagebox
import re
con=sqlite3.Connection("phone")
cur=con.cursor()
cur.execute('create table if not exists contact(sno integer primary key autoincrement,fname text,mname text,lname text,comp text,address text,city text,pincode text,web text,dob text)')
cur.execute('create table if not exists phone(sno integer ,ptype text,num text,foreign key(sno) references contact(sno) on delete cascade,primary key(sno,num))')
cur.execute('create table if not exists email(sno integer,etype text,mail text,foreign key(sno) references contact(sno) on delete cascade,primary key(sno,mail))')

def check_email(s):
    c1=s.count('@')
    c2=s.count('.com')
    if c1==1 and c2==1:
        i=s.index('@')
        s1=s[:i]
        if s1.isalnum() or s1.isalpha():
            return 1
        else:
            return 0
    else:
        return 0

    
    
def insert():
    pt=""
    et=""
    if v1.get()==1:
        pt="Office"
    elif v1.get()==2:
        pt="Home"
    elif v1.get()==3:
        pt="Mobile"
    else:
        pt=""

    if v2.get()==1:
        et="Office"
    elif v2.get()==2:
        et="Home"
    else:
        et=""
        
##    if not (re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",s,re.IGNORECASE)):
##        showinfo("WRONG INPUT","INVALID E-MAIL")

    if ( fn.get()==mn.get() and fn.get()!='' and mn.get()!='' ) or fn.get()=='' or ( ln.get()==mn.get() and ln.get()!='' and mn.get()!='') or ( fn.get()==ln.get() and fn.get()!='' and ln.get()!=''):
        showinfo("WRONG INPUT","INVALID NAME")
    elif len(pno.get())!=10:
        showinfo("WRONG INPUT","INVALID PHONE NUMBER")
    elif not (re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",s,re.IGNORECASE)):
        showinfo("WRONG INPUT","INVALID E-MAIL")
    else:
        cur.execute('''insert into contact(fname,mname,lname,comp,address,city,pincode,web,dob) values(?,?,?,?,?,?,?,?,?)''',(fn.get(),mn.get(),ln.get(),comp.get(),add.get(),city.get(),pin.get(),web.get(),dob.get()))
        cur.execute('''insert into phone values((select max(sno) from contact),?,?)''',(pt,pno.get()))
        cur.execute('''insert into email values((select max(sno) from contact),?,?)''',(et,email.get()))
        cur.execute('''select * from contact''')
        print(cur.fetchall())
        cur.execute('''select * from phone''')
        print(cur.fetchall())
        cur.execute('''select * from email''')
        print(cur.fetchall())
        con.commit()
        showinfo("saved","Entry successful!")
        clear()
    

def clear():
    fn.delete(0,END)
    mn.delete(0,END)
    ln.delete(0,END)
    comp.delete(0,END)
    add.delete(0,END)
    city.delete(0,END)
    pin.delete(0,END)
    web.delete(0,END)
    dob.delete(0,END)
    pno.delete(0,END)
    email.delete(0,END)
    
def search():
    def func(event1):
        a=lb.curselection()
        if(a==()):
            return 
        else:
            def edit():
                def upd():
                    phonetype=""
                    if(m3.get()==1):
                        phonetype="office"
                    elif(m3.get()==2):
                        phonetype="Home"
                    elif(m3.get()==3):
                        phonetype="Mobile"
                    else:
                        phonetype="not specified"
                    emailtype=""
                    if(m4.get()==1):
                        emailtype="office"
                    elif(m4.get()==2):
                        emailtype="Personal"
                    else:
                        emailtype="not specified"
                    cur.execute('select sno from contact where fname=? and mname=? and lname=?',k)
                    cid=cur.fetchall()
                    cid=cid[0][0]
                    cur.execute('update contact set fname=?,mname=?,lname=?,comp=?,address=?,city=?,pincode=?,web=?,dob=? where sno=?',(fn.get(),mn.get(),ln.get(),comp.get(),add.get(),city.get(),pin.get(),web.get(),dob.get(),cid))
                    cur.execute('update phone set ptype=?,num=? where sno=?',(phonetype,pno.get(),cid))
                    cur.execute('update email set etype=?,mail=? where sno=?',(emailtype,email.get(),cid))
                    
                    showinfo("updated","Database updated")
                    root5.destroy()
                    root2.destroy()
                    root1.destroy()
                    con.commit()

                def close_2():
                    root5.destroy()
                    root2.destroy()
                    root1.destroy() 

                root5=Tk()
                root5.geometry('550x550')
                cur.execute('''select fname,mname,lname,comp,address,city,pincode,web,dob,ptype,num,etype,mail from detail where fname=? and mname=? and lname=?''',k)
                a=cur.fetchall()
                a=a[0]
                Label(root5,text="First Name").grid(row=1,column=0)
                first_name=Entry(root5)
                first_name.grid(row=1,column=1)
                first_name.insert(0,a[0])
                
                Label(root5,text="Middle Name").grid(row=2,column=0)
                middle_name=Entry(root5)
                middle_name.grid(row=2,column=1)
                middle_name.insert(0,a[1])
                
                Label(root5,text="Last Name").grid(row=3,column=0)
                last_name=Entry(root5)
                last_name.grid(row=3,column=1)
                last_name.insert(0,a[2])
                
                Label(root5,text="Company Name").grid(row=4,column=0)
                company_name=Entry(root5)
                company_name.grid(row=4,column=1)
                company_name.insert(0,a[3])
                
                Label(root5,text="Address").grid(row=5,column=0)
                address=Entry(root5)
                address.grid(row=5,column=1)
                address.insert(0,a[4])
                
                Label(root5,text="City").grid(row=6,column=0)
                city=Entry(root5)
                city.grid(row=6,column=1)
                city.insert(0,a[5])
                
                Label(root5,text="Pin code").grid(row=7,column=0)
                pin=Entry(root5)
                pin.grid(row=7,column=1)
                pin.insert(0,a[6])
                
                Label(root5,text="Website Url").grid(row=8,column=0)
                website_url=Entry(root5)
                website_url.grid(row=8,column=1)
                website_url.insert(0,a[7])
                
                Label(root5,text="Date of Birth").grid(row=9,column=0)
                dob=Entry(root5)
                dob.grid(row=9,column=1)
                dob.insert(0,a[8])
                
                Label(root5,text="Select Phone Type",font="Arial 10",fg="blue").grid(row=10,column=0)
                m3=IntVar()
                Radiobutton(root5,text="Office",variable=m3,value=1).grid(row=10,column=1)
                Radiobutton(root5,text="Home",variable=m3,value=2).grid(row=10,column=2)
                Radiobutton(root5,text="Mobile",variable=m3,value=3).grid(row=10,column=3)
                
                Label(root5,text="Phone Number").grid(row=11,column=0)
                phone_number=Entry(root5)
                phone_number.grid(row=11,column=1)
                phone_number.insert(0, a[10])
                
                Label(root5,text="Select Email Type",font="Arial 10",fg="blue").grid(row=12,column=0)
                m4=IntVar()
                Radiobutton(root5,text="Office",variable=m4,value=1).grid(row=12,column=1)
                Radiobutton(root5,text="Personal",variable=m4,value=2).grid(row=12,column=2)
                
                Label(root5,text="Email id").grid(row=13,column=0)
                email_id=Entry(root5)
                email_id.grid(row=13,column=1)
                email_id.insert(0, a[12])
                
                Button(root5,text="Update",command=upd).grid(row=14,column=0)
                Button(root5,text="Close",command=close_2).grid(row=14,column=1)
                root5.mainloop()


                
            def close_1():
                root2.destroy()
                root1.destroy()
            def delete_rec():
                cur.execute('select sno from contact c where c.fname=? and c.mname=? and c.lname=?',k)
                t=cur.fetchall()
                t=t[0][0]
                cur.execute('delete from contact c where c.sno=?',(t,))
                showinfo("Delete","Record successfully deleted")
                con.commit()
                root2.destroy()
                root1.destroy()
            root2=Tk()
            root2.geometry('300x400')
            k=lb.get(a[0])
            print(k)
            cur.execute('select fname,mname,lname,comp,address,city,pincode,web,dob,ptype,num,etype,mail from contact c,phone p,email e where c.fname=? and c.mname=? and c.lname=? and c.sno=p.sno and c.sno=e.sno' ,k)
            m=cur.fetchall()
            m=m[0]          
            lo=Listbox(root2,height=15,width=50)
            lo.pack()
            lo.insert(0,"First Name: "+m[0])
            lo.insert(1,"Middle Name: "+m[1])
            lo.insert(2,"Last Name:"+m[2])
            lo.insert(3,"Company Name:"+m[3])
            lo.insert(4,"Address:"+m[4])
            lo.insert(5,"City:"+m[5])
            lo.insert(6,"Pin:"+str(m[6]))
            lo.insert(7,"Website:"+m[7])
            lo.insert(8,"DOB: "+m[8])
            lo.insert(9,"Contact Type:"+m[9])
            lo.insert(10,"Phone no.:"+str(m[10]))
            lo.insert(11,"Email Type:"+m[11])
            lo.insert(12,"Email id:"+m[12])
            Button(root2,text="Close",command=close_1).pack()
            Button(root2,text="Delete",command=delete_rec).pack()
            Button(root2,text="Edit",command=edit).pack()
            root2.mainloop()
            root2.mainloop()
            
    
    def get_text(event):
        lb.delete(0, END)
        #print m1.get()
        cur.execute('select fname,mname, lname from contact where fname like "%'+ m1.get()+'%" or mname like " %'+ m1.get()+'%" or lname like " %'+m1.get()+'%" ')
        
        res=cur.fetchall()
        for item in range(len(res)):
            lb.insert(item,res[item])

    root1=Tk()
    root1.geometry('600x600')
    root1.bind('<Button-1>', func)
    Label(root1,text="Searching Phone Book",font="Arial 15",bg="light blue").grid(row=0,column=0)
    Label(root1,text="Enter Your Name").grid(row=1,column=0)
    m1=Entry(root1)
    m1.grid(row=2,column=0)
    m1.bind('<KeyRelease>',get_text)
    lb=Listbox(root1,height=30,width=90,fg="red",selectmode=SINGLE)
    lb.grid(row=3,column=0)
    Button(root1,text="Close",command=root1.destroy).grid(row=5,column=0)
    root1.mainloop()

def close():
    root.destroy()
def add_phone_num():
    
    pt=""    
    if v1.get()==1:
        pt="Office"
    elif v1.get()==2:
        pt="Home"
    elif v1.get()==3:
        pt="Mobile"
    else:
        pt=""

    cur.execute('''insert into phone values((select max(sno) from contact)+1,?,?)''',(pt,pno.get()))
    pno.delete(0,END)
#GUI
root=Tk()
root.geometry("550x700")
photo = PhotoImage(file = r"images.gif")
Label(root,image=photo).grid(row=0,column=1)
#fname
Label(root,text="First Name : ",font="Arial 12").grid(row=2,column=0)
fn=Entry(root)
fn.grid(row=2,column=1)
#mname
Label(root,text="Middle Name : ",font="Arial 12").grid(row=4,column=0)
mn=Entry(root)
mn.grid(row=4,column=1)
#lname
Label(root,text="Last Name : ",font="Arial 12").grid(row=6,column=0)
ln=Entry(root)
ln.grid(row=6,column=1)    

#company name
Label(root,text="Company Name : ",font="Arial 12").grid(row=8,column=0)
comp=Entry(root)
comp.grid(row=8,column=1)
#address
Label(root,text="Address : ",font="Arial 12").grid(row=10,column=0)
add=Entry(root)
add.grid(row=10,column=1)
#city
Label(root,text="City : ",font="Arial 12").grid(row=12,column=0)
city=Entry(root)
city.grid(row=12,column=1)
#pincode
Label(root,text="Pincode : ",font="Arial 12").grid(row=14,column=0)
pin=Entry(root)
pin.grid(row=14,column=1)
#website
Label(root,text="Website URL : ",font="Arial 12").grid(row=16,column=0)
web=Entry(root)
web.grid(row=16,column=1)
#Date of birth
Label(root,text="Date Of Birth : ",font="Arial 12").grid(row=18,column=0)
dob=Entry(root)
dob.grid(row=18,column=1)
Label(root,text="( dd-mm-yyyy )",font="Arial 8").grid(row=18,column=2)

#phone type
Label(root,text="Select Phone Type",font="Arial 15",fg="blue").grid(row=20,column=0)
#phone radiobutton
v1=IntVar()
p1=Radiobutton(root,text="Office",variable=v1,value=1)
p1.grid(row=20,column=1)
p2=Radiobutton(root,text="Home",variable=v1,value=2)
p2.grid(row=20,column=2)
p3=Radiobutton(root,text="Mobile",variable=v1,value=3)
p3.grid(row=20,column=3)
#phone number
Label(root,text="Phone Number : ",font="Arial 12").grid(row=22,column=0)
pno=Entry(root)
pno.grid(row=22,column=1)
Button(root,text="+",command=add_phone_num).grid(row=22,column=2)
#email tyope
Label(root,text="Select Email Type",font="Arial 15",fg="blue").grid(row=24,column=0)
#email radiobutton
v2=IntVar()
e1=Radiobutton(root,text="Office",variable=v2,value=1)
e1.grid(row=26,column=1)
e2=Radiobutton(root,text="Home",variable=v2,value=2)
e2.grid(row=26,column=2)
#email
Label(root,text="E.Mail : ",font="Arial 12").grid(row=28,column=0)
email=Entry(root)
email.grid(row=28,column=1)
Button(root,text="+",command=root.bell).grid(row=28,column=2)
#buttons
Label(root,text="").grid(row=30,column=0)
Button(root,text="Save",command=insert,width=7).grid(row=31,column=0)
Button(root,text="Search",command=search,width=7).grid(row=31,column=1)
Button(root,text="Close",command=close,width=7).grid(row=31,column=2)

root.mainloop()
