from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from data import Data

root = Tk()

data1 = []
root.geometry('900x700')
root.title("Registration Programer Form")

form = Frame(root)
form.pack(side="left", fill="both", expand="yes")
label_0 = Label(form, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)


label_1 = Label(form, text="FullName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
nama = StringVar()

entry_1 = Entry(form, textvariable=nama)
entry_1.place(x=240, y=130)

label_2 = Label(form, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)
email = StringVar()

entry_2 = Entry(form, textvariable=email)
entry_2.place(x=240, y=180)

label_3 = Label(form, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)
var = StringVar()
ttk.Radiobutton(form, text="Male", variable=var,
                value="Male").place(x=235, y=230)
ttk.Radiobutton(form, text="Female",
                variable=var, value="Female").place(x=300, y=230)


label_4 = Label(form, text="country", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

list1 = ['Indonesia', 'Japan', 'UK', 'Portugal', 'Argentina', 'South Africa']
c = StringVar()
droplist = OptionMenu(form, c, *list1)
droplist.config(width=15)
c.set('select your country')
droplist.place(x=240, y=280)

label_4 = Label(form, text="Programming", width=20, font=("bold", 10))
label_4.place(x=85, y=330)
var1 = IntVar()
Checkbutton(form, text="java", variable=var1).place(x=235, y=330)
var2 = IntVar()
Checkbutton(form, text="python", variable=var2).place(x=290, y=330)
# Celstial Object image

lb_openImg = LabelFrame(form, text="Open Image",
                        width=20, height=20, padx=2, pady=2)
lb_openImg.place(x=80, y=400)
f_img = Frame(lb_openImg, height=200, width=400)
f_img.pack(side="left", padx=10, pady=10)
f_img.pack_propagate(0)
lb_img = Label(f_img, background="Grey")
lb_img.pack(fill="both", expand="yes")


def getImg():
    # get image 
    root.filename = filedialog.askopenfilename(initialdir="~",
                                               title="Select a File",
                                               filetypes=(
                                                   ("Images", "*.jpg *.jpeg *.png"), ("all files", "*.*"))
                                               )
    # image preview
    load = Image.open(root.filename)
    render = ImageTk.PhotoImage(load.resize((400, 200), Image.ANTIALIAS))
    lb_img.configure(image=render)
    lb_img.image = render
    root.image = render
    load.close()


bt_openImg = Button(lb_openImg, text="Browse...", command=getImg, fg="black")
bt_openImg.pack(side=TOP, padx=10, pady=10)


# submit


def submitObject():
    if((nama.get() == "")
       or (email.get() == "")
       or (var.get() != "Male" and var.get() != "Female")
       or (c.get() == "")
       or (var1.get() == "")
       or (var2.get() == "")
       or (root.image == None)
       ):
        print("var value= "+var.get())
        messagebox.showwarning(title="Incomplete input",
                               message="Please insert all the data")

        pass
    else:
        # insert new object 
        data1.append(Data(nama.get(), email.get(), var.get(), c.get(),
                     var1.get(), var2.get(), root.filename, root.image))
        # reset form
        nama.set("")
        email.set("")
        c.set("")
        var.set("")
        var1.set(0)
        var2.set(0)
        root.image = None
        lb_img.configure(image="")
        pass


Button(form, text='Submit', width=20, bg='brown',
       fg='black', command=submitObject).place(x=180, y=380)

# App Menu
appMenu = Frame(root)
appMenu.pack(side="right", padx=10, pady=10, fill="y")

lb_appName = Label(appMenu, text="Competition\nProgrammer",
                   borderwidth=0, anchor="w", justify=LEFT)
lb_appName.grid(row=0, column=0)
lb_appName.configure(font=("Helvetica", 36, "bold"))


def input():
    top = Toplevel()
    top.title("Submissions")
    top.focus()
    f = Frame(top)
    f.pack(fill="both", expand="yes")
    # Table 
    lb_hd_nama = Label(f, text="Nama",
                       borderwidth=1, relief="solid")
    lb_hd_nama.grid(row=0, column=0, sticky="news", ipadx=5, rowspan=2)

    lb_hd_email = Label(f, text="Email",
                        borderwidth=1, relief="solid")
    lb_hd_email.grid(row=0, column=1, sticky="news", ipadx=5, rowspan=2)

    lb_hd_gender = Label(f, text="Gender", borderwidth=1, relief="solid")
    lb_hd_gender.grid(row=0, column=2, sticky="news", ipadx=5, rowspan=2)

    lb_hd_country = Label(f, text="Country", borderwidth=1, relief="solid")
    lb_hd_country.grid(row=0, column=3, sticky="news", ipadx=5, rowspan=2)

    lb_hd_progamming = Label(f, text="Progamming",
                             borderwidth=1, relief="solid")
    lb_hd_progamming.grid(row=0, column=4, columnspan=2,
                          sticky="news", ipadx=5)

    lb_hd_java = Label(f, text="Java", borderwidth=1, relief="solid")
    lb_hd_java.grid(row=1, column=4, sticky="news", ipadx=5)

    lb_hd_python = Label(f, text="Python", borderwidth=1, relief="solid")
    lb_hd_python.grid(row=1, column=5, sticky="news", ipadx=5)

    lb_hd_img = Label(f, text="Image", borderwidth=1,
                      relief="solid", width=40)
    lb_hd_img.grid(row=0, column=6, sticky="news", rowspan=2)

    for i, data in enumerate(data1):
        lb_hd_nama = Label(
            f, text=data.nama, borderwidth=1, relief="solid")
        lb_hd_nama.grid(row=i+2, column=0, sticky="nesw", ipadx=5)

        lb_hd_email = Label(
            f, text=data.email, borderwidth=1, relief="solid")
        lb_hd_email.grid(row=i+2, column=1, sticky="nesw", ipadx=5)

        lb_hd_gender = Label(
            f, text=data.var, borderwidth=1, relief="solid")
        lb_hd_gender.grid(row=i+2, column=2, sticky="nesw", ipadx=5)

        lb_hd_country = Label(
            f, text=data.c, borderwidth=1, relief="solid")
        lb_hd_country.grid(row=i+2, column=3, sticky="nesw", ipadx=5)

        lb_hd_progamming = Label(
            f, text=data.var1, borderwidth=1, relief="solid")
        lb_hd_progamming.grid(row=i+2, column=4, sticky="nesw", ipadx=5)
        lb_hd_progamming = Label(
            f, text=data.var2, borderwidth=1, relief="solid")
        lb_hd_progamming.grid(row=i+2, column=5, sticky="nesw", ipadx=5)

        lb_cb_img = Label(f, image=data.image,
                          borderwidth=1, relief="solid")
        lb_cb_img.grid(row=i+2, column=6, sticky="nesw")

    def exit_btn():
        top.destroy()
        top.update()
    bt_exit = Button(f, text="Exit", width=10, command=exit_btn)
    bt_exit.grid(row=3+len(data1), column=0,
                 columnspan=7, pady=20, ipadx=5)
    pass


bt_see = Button(appMenu, text="SEE ALL SUBMISSIONS", command=input)

bt_see.grid(row=1, column=0, sticky="new", padx=1, pady=5)


def clearSubmissions():
    confirm = messagebox.askokcancel(
        title="Confirm Clear Submissions", message="Do you want to clear all submissions?")
    if confirm == True:
        data1.clear()
        messagebox.showinfo(title="Submissions Cleared",
                            message="All submissions have been cleared")


bt_clear = Button(appMenu, text="CLEAR ALL SUBMISSIONS",
                  command=clearSubmissions)
bt_clear.grid(row=2, column=0, sticky="new", padx=1, pady=5)


def about():
    top = Toplevel()
    top.title("About")
    f = Frame(top)
    f.pack(fill="both", expand="yes", ipadx=5, ipady=5)
    lb_title = Label(f, text="Competition Progamming", anchor="w")
    lb_title.grid(row=0, column=0, sticky="w")
    lb_desc = Label(f, text="Aplikasi ini merekam data programmer dari beberapa negara\nyang memiliki gambar untuk profile picture. Data termasuk nama,email,gender,country,bahasa pemograman  dan gambar.", anchor="w")
    lb_desc.grid(row=1, column=0, sticky="w")
    lb_nama = Label(
        f, text="Nama: Arrozy Adi Falaqi\nNIM: 1908853", anchor="w")
    lb_nama.grid(row=2, column=0, sticky="w")

    def exit_btn():
        top.destroy()
        top.update()
    bt_exit = Button(f, text="Exit", width=10, command=exit_btn)
    bt_exit.grid(row=3, column=0, pady=5)
    pass


bt_about = Button(appMenu, text="ABOUT", command=about)
bt_about.grid(row=3, column=0, sticky="new", padx=1, pady=5)


def exit():
    confirm = messagebox.askyesno("Confirm exit", "Do you want to exit?")
    if confirm == True:
        root.quit()


bt_exit = Button(appMenu, text="EXIT", command=exit)
bt_exit.grid(row=10, column=0, sticky="sew", padx=1, pady=5)
root.mainloop()
