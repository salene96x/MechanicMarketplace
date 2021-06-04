from tkinter import *
from sqlite3 import *
from tkinter import messagebox
def root_page():
    root = Tk()
    root.title("Mechanic Marketplace")
    root.resizable(0,0)
    root.geometry("800x600")
    root.option_add("*bg", "lightblue")
    root.configure(bg='lightblue')
    return root

def login_page(root):
    global usr_entry, pwd_entry
    usr_var = StringVar()
    pwd_var = StringVar()

    logo = PhotoImage(file="images/logo.png")

    login_frame = Frame(root, bg="lightblue")
    login_frame.place(relheight=1, relwidth=1, x=0, y=0)
    login_frame.option_add("*background", "lightblue")
    login_frame.option_add("*font", "Garamond 16")
    login_frame.rowconfigure((1,4,5),weight=0)
    login_frame.rowconfigure((0,2,3,6),weight=1)
    login_frame.columnconfigure((0,1),weight=1)

    Label(login_frame, text="Welcome to Mechanic Marketplace", font="Garamond 24 bold").grid(row=1, columnspan=2)
    # Label(login_frame, image=logo, bg='black').grid(row=0, columnspan=2)
    Label(login_frame, text="Username : ").grid(row=2, column=0, sticky='se', padx=15, pady=15)
    Label(login_frame, text="Password : ").grid(row=3, column=0, stick='ne', padx=15, pady=15)
    Label(login_frame, text="Don't have an account?, Click on the signup button.").grid(row=5, columnspan=2)

    usr_entry = Entry(login_frame, width=20, textvariable=usr_var)
    usr_entry.grid(row=2, column=1, sticky='sw', padx=15, pady=15)
    pwd_entry = Entry(login_frame, width=20, textvariable=pwd_var, show="*")
    pwd_entry.grid(row=3, column=1, sticky='nw', padx=15, pady=15)

    btn_login = Button(login_frame, text='Log-in', width=25, height=3, command=login_click)
    btn_login.grid(row=4, columnspan=2, sticky='n', pady=25)

    btn_signup = Button(login_frame, text="Sign up", height=3, width=25, command=signup_page)
    btn_signup.grid(row=6, columnspan=2, sticky='n')

    return pwd_var, usr_var, login_frame

def signup_page():
    global usr_var, pwd_var, con_pwd_var, f_name_var, l_name_var, tel_var, usr_type_var, amphoe_var, prov_var, frame_signup
    usr_var = StringVar()
    pwd_var = StringVar()
    con_pwd_var = StringVar()
    f_name_var = StringVar()
    l_name_var = StringVar()
    tel_var = StringVar()
    usr_type_var = StringVar()
    amphoe_var = StringVar()
    prov_var = StringVar()

    frame_signup = Frame(root, bg='lightyellow')
    frame_signup.option_add("*background", "lightyellow")
    frame_signup.option_add("*font", "Garamond 16")
    frame_signup.place(x=0, y=0, relheight=1, relwidth=1)

    frame_signup.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)
    frame_signup.columnconfigure((0,1), weight=1)

    Label(frame_signup, text="Signing up process", font="Garamond 24").grid(row=0, columnspan=2, sticky='s')
    Label(frame_signup, text="Please fill data in the below fields to proceed signing up process.", font="Garamond 18").grid(row=1, columnspan=2, sticky='n')
    Label(frame_signup, text="Username : ").grid(row=2, column=0, sticky='e')
    Label(frame_signup, text="Password : ").grid(row=3, column=0, sticky='e')
    Label(frame_signup, text="Confirmed Password : ").grid(row=4, column=0, sticky='e')
    Label(frame_signup, text="First name : ").grid(row=5, column=0, sticky='e')
    Label(frame_signup, text="Last name : ").grid(row=6, column=0, sticky='e')
    Label(frame_signup, text="Telephone No. : ").grid(row=7, column=0, sticky='e')
    Label(frame_signup, text="User type : ").grid(row=8, column=0, sticky='e')
    Label(frame_signup, text="Amphoe : ").grid(row=9, column=0, sticky='e')
    Label(frame_signup, text="Province : ").grid(row=10, column=0, sticky='e')

    Entry(frame_signup, width=20, textvariable=usr_var).grid(row=2, column=1, sticky='w')
    Entry(frame_signup, width=20, textvariable=pwd_var, show="*").grid(row=3, column=1, sticky='w')
    Entry(frame_signup, width=20, textvariable=con_pwd_var, show="*").grid(row=4, column=1, sticky='w')
    Entry(frame_signup, width=20, textvariable=f_name_var).grid(row=5, column=1, sticky='w')
    Entry(frame_signup, width=20, textvariable=l_name_var).grid(row=6, column=1, sticky='w')
    Entry(frame_signup, width=20, textvariable=tel_var).grid(row=7, column=1, sticky='w')
    Entry(frame_signup, width=20, textvariable=amphoe_var).grid(row=9, column=1, sticky='w')
    Entry(frame_signup, width=20, textvariable=prov_var).grid(row=10, column=1, sticky='w')

    Radiobutton(frame_signup, text="General", variable=usr_type_var, value="General").grid(row=8, column=1, sticky='w')
    Radiobutton(frame_signup, text="Mechanic", variable=usr_type_var, value="Mechanic").grid(row=8, column=1)

    btn_confirm = Button(frame_signup, text="Confirm", width=25, height=3, command=signup_clicked)
    btn_confirm.grid(row=11, column=0, sticky='e', padx=20)
    btn_cancel = Button(frame_signup, text="Cancel", width=25, height=3, command=frame_signup.destroy)
    btn_cancel.grid(row=11, column=1, sticky='w', padx=20)

def signup_clicked():
    cursor.execute("select ln_usr from login where ln_usr = ?",[usr_var.get()])
    result = cursor.fetchall()
    if result:
        messagebox.showerror("Sign up : ", "Duplicated Username")
    else :
        if pwd_var.get() == con_pwd_var.get():
            if usr_type_var == "General":
                sql = "insert into general_users values (?,?,?,?,?)"
                cursor.execute(sql, [usr_var.get(), pwd_var.get(),f_name_var.get(),l_name_var.get(),tel_var.get()])
            else : 
                sql = "insert into mechanic_users values (?,?,?,?,?,?,?)"
                cursor.execute(sql, [usr_var.get(), pwd_var.get(),f_name_var.get(),l_name_var.get(),tel_var.get(), amphoe_var.get(), prov_var.get()])
            conn.commit()
            sql = "insert into login values (?,?)"
            cursor.execute(sql,[usr_var.get(), pwd_var.get()])
            conn.commit()
            conn.close()
            messagebox.showinfo("Sign up : ", "Successfully signed up for an account")
            frame_signup.destroy()
            usr_entry.focus_force()
        else :
            messagebox.showerror("Sign up : ", "The confirmation and normal are not the same.")

def main_page():
    global upper_frame, left_frame
    root.rowconfigure((0,1), weight=0)
    root.rowconfigure((2), weight=1)
    root.columnconfigure(0, weight=0)
    root.columnconfigure(1, weight=1)
    root.configure(bg="lightgrey")

    upper_frame = Frame(root, bg='blue')
    upper_frame.option_add("*background", "blue")
    upper_frame.grid(row=0, columnspan=2, column=0, sticky='news')
    left_frame = Frame(root, bg='blue')
    left_frame.grid(row=1, rowspan=2, column=0, sticky='news')

    Label(upper_frame, text="=                      Mechanic Marketplace", font="Garamond 30 bold", fg='white').pack()

    btn_locate_location = Button(left_frame, text="Current location locating", width=30, height=3, command=current_location_click)
    btn_locate_location.pack(pady=20)
    btn_locate_location = Button(left_frame, text="Electrical Mechanic", width=30, height=3, command=electric_click)
    btn_locate_location.pack(pady=20)
    btn_locate_location = Button(left_frame, text="Car Mechanic", width=30, height=3, command=car_click)
    btn_locate_location.pack(pady=20)
    btn_locate_location = Button(left_frame, text="Others Mechanic", width=30, height=3, command=others_click)
    btn_locate_location.pack(pady=20)
    btn_trouble_report = Button(left_frame, text="Trouble reporting", width=30, height=3, command=trouble_click)
    btn_trouble_report.pack(pady=20)
    btn_trouble_report = Button(left_frame, text="Contact Us", width=30, height=3, command=contact_click)
    btn_trouble_report.pack(pady=20)
    btn_exit = Button(left_frame, text="Exitting Application", width=30, height=3, command=quit)
    btn_exit.pack(pady=20)

def electric_click():
    frame_electric = Frame(root, bg="lightyellow")
    frame_electric.grid(row=2, column=1, sticky='news')
    frame_electric.option_add("*background", "lightyellow")
    frame_electric.option_add("*font", "Garamond 16")
    frame_electric.columnconfigure((0,1,2,3), weight=1)

    Label(frame_electric, text="Electrical Mechanics", font='Garamond 30 bold').grid(columnspan=4, row=0)
    Label(frame_electric, text='No.').grid(row=1, column=0)
    Label(frame_electric, text="Mechanic's Name").grid(row=1, column=1)
    Label(frame_electric, text="Province").grid(row=1, column=2)
    Label(frame_electric, text="Telephone No.").grid(row=1, column=3)

    sql = 'select mu_fname, mu_surname, mu_province, mu_tel from mechanic_users where mu_type = ?'
    cursor.execute(sql,['electric'])
    result = cursor.fetchall()

    cnt = 2
    for x in result:
        Label(frame_electric, text=cnt-1).grid(row=cnt, column=0)
        Label(frame_electric, text=x[0]+" "+x[1]).grid(row=cnt, column=1)
        Label(frame_electric, text=x[2]).grid(row=cnt, column=2)
        Label(frame_electric, text=x[3]).grid(row=cnt, column=3)
        cnt += 1

def others_click():
    frame_electric = Frame(root, bg="lightyellow")
    frame_electric.grid(row=2, column=1, sticky='news')
    frame_electric.option_add("*background", "lightyellow")
    frame_electric.option_add("*font", "Garamond 16")
    frame_electric.columnconfigure((0,1,2,3), weight=1)

    Label(frame_electric, text="Other types Mechanics", font='Garamond 30 bold').grid(columnspan=4, row=0)
    Label(frame_electric, text='No.').grid(row=1, column=0)
    Label(frame_electric, text="Mechanic's Name").grid(row=1, column=1)
    Label(frame_electric, text="Province").grid(row=1, column=2)
    Label(frame_electric, text="Telephone No.").grid(row=1, column=3)

    sql = 'select mu_fname, mu_surname, mu_province, mu_tel from mechanic_users where mu_type = ?'
    cursor.execute(sql,['others'])
    result = cursor.fetchall()

    cnt = 2
    for x in result:
        Label(frame_electric, text=cnt-1).grid(row=cnt, column=0)
        Label(frame_electric, text=x[0]+" "+x[1]).grid(row=cnt, column=1)
        Label(frame_electric, text=x[2]).grid(row=cnt, column=2)
        Label(frame_electric, text=x[3]).grid(row=cnt, column=3)
        cnt += 1

def car_click():
    frame_electric = Frame(root, bg="lightyellow")
    frame_electric.grid(row=2, column=1, sticky='news')
    frame_electric.option_add("*background", "lightyellow")
    frame_electric.option_add("*font", "Garamond 16")
    frame_electric.columnconfigure((0,1,2,3), weight=1)

    Label(frame_electric, text="Car Mechanics", font='Garamond 30 bold').grid(columnspan=4, row=0)
    Label(frame_electric, text='No.').grid(row=1, column=0)
    Label(frame_electric, text="Mechanic's Name").grid(row=1, column=1)
    Label(frame_electric, text="Province").grid(row=1, column=2)
    Label(frame_electric, text="Telephone No.").grid(row=1, column=3)

    sql = 'select mu_fname, mu_surname, mu_province, mu_tel from mechanic_users where mu_type = ?'
    cursor.execute(sql,['car'])
    result = cursor.fetchall()

    cnt = 2
    for x in result:
        Label(frame_electric, text=cnt-1).grid(row=cnt, column=0)
        Label(frame_electric, text=x[0]+" "+x[1]).grid(row=cnt, column=1)
        Label(frame_electric, text=x[2]).grid(row=cnt, column=2)
        Label(frame_electric, text=x[3]).grid(row=cnt, column=3)
        cnt += 1

def contact_click():
    frame_contact = Frame(root, bg='lightgreen')
    frame_contact.grid(row=2, column=1, sticky='news')
    frame_contact.option_add("*background", "lightgreen")
    frame_contact.option_add("*font", "Garamond 16")
    frame_contact.columnconfigure((0,1), weight=1)

    avatar = PhotoImage("images/avatar.png")

    Label(frame_contact, text="Contact Detail", font="Garamond 30 bold").grid(row=0, columnspan=2)
    # Label(frame_contact, image=avatar).grid(row=1, columnspan=2)
    Label(frame_contact, text="Name : ").grid(row=2, column=0, sticky='e')
    Label(frame_contact, text="Kittituch Promligoon (North)").grid(row=2, column=1, sticky='w')
    Label(frame_contact, text="Detail : ").grid(row=3, column=0, sticky='e')
    Label(frame_contact, text="Developer of this application\nif you want to contact me just direct emailing or calling").grid(row=3, column=1, sticky='w')
    Label(frame_contact, text="Telephone No. : ").grid(row=4, column=0, sticky='e')
    Label(frame_contact, text="082-464-9887").grid(row=4, column=1, sticky='w')

def current_location_click():
    global loc, type
    type = StringVar()
    loc = StringVar()
    frame_main = Frame(root, bg='lightgrey')
    frame_main.grid(row=1, column=1, sticky='news')

    frame_main.option_add("*font", "Garamond 16")
    frame_main.option_add("*background", "lightgrey")
    frame_main.columnconfigure((0,1),weight=1)
    frame_main.rowconfigure((0,1,2), weight=1)

    Label(frame_main, text="Fill your current location (Province) : ").grid(column=0,row=0,pady=20, sticky='e')
    Label(frame_main, text="Fill a mechanic type : ").grid(column=0,row=1,pady=20, sticky='e')

    Entry(frame_main, width=20, textvariable=loc).grid(column=1,row=0, pady=20, sticky='w')
    Entry(frame_main, width=20, textvariable=type).grid(column=1,row=1, pady=20, sticky='w')

    btn_find = Button(frame_main, text='Find a mechanic', width=30, height=3, command=find_click)
    btn_find.grid(row=2, columnspan=2, pady=20)
    

def find_click():
    frame_display = Frame(root, bg='lightyellow')
    frame_display.grid(row=2, column=1, sticky='news')
    frame_display.columnconfigure((0,1,2,3), weight=1)
    frame_display.option_add("*background", "lightyellow")

    Label(frame_display, text="No.").grid(row=0, column=0)
    Label(frame_display, text="Mechanic's Name").grid(row=0, column=1)
    Label(frame_display, text="Amphoe in province").grid(row=0, column=2)
    Label(frame_display, text="Telephone No.").grid(row=0, column=3)

    sql = "select mu_fname, mu_surname, mu_amphoe, mu_tel from mechanic_users where mu_province = ? and mu_type = ?"
    cursor.execute(sql, [loc.get(), type.get()])
    result = cursor.fetchall()

    cnt = 1
    for x in result:
        Label(frame_display, text=cnt).grid(row=cnt, column=0)
        Label(frame_display, text=x[0]+" "+x[1]).grid(row=cnt, column=1)
        Label(frame_display, text=x[2]).grid(row=cnt, column=2)
        Label(frame_display, text=x[3]).grid(row=cnt, column=3)
        cnt += 1

def trouble_click():
    global message, frame_report
    message = StringVar()
    frame_report = Frame(root, bg='lightyellow')
    frame_report.grid(row=2, column=1, sticky='news')
    frame_report.option_add("*background", "lightyellow")
    frame_report.columnconfigure((0,1),weight=1)
    frame_report.option_add("*font", "Garamond 16")

    Label(frame_report, text="Trouble Reporting", font="Garamond 30 bold").grid(row=0, columnspan=2)
    Label(frame_report, text="Messages : ").grid(row=1, column=0, sticky='e')

    Entry(frame_report, width=50, textvariable=message).grid(row=1, column=1, sticky='w')

    btn_send = Button(frame_report, text="Send", command=send_click, width=30)
    btn_send.grid(row=2, columnspan=2)

def send_click():
    sql = "insert into troubles values (?)"
    cursor.execute(sql, [message.get()])
    messagebox.showinfo("Trouble Reporting", "Report has been sent, Thank you for your reporting")
    frame_report.destroy()

def login_click():
    login_frame.destroy()
    sql = "select * from login where ln_usr = ?"
    cursor.execute(sql, [usr_var.get()])
    result = cursor.fetchall()
    if result:
        main_page()
        messagebox.showinfo("Login : ", "Successfully login\nWelcome !")
    else :
        messagebox.showerror("Login : ", "Incorrect username or password")

def connection():
    conn = connect("project_app.db")
    cursor = conn.cursor()
    return conn, cursor

if __name__ == "__main__":
    conn, cursor = connection()
    root = root_page()
    pwd_var, usr_var, login_frame = login_page(root)
    root.mainloop()