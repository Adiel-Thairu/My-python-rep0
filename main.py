from tkinter import *
from pil import Image, ImageTk
from employee import employeeClass
from customer import customerClass
from category import categoryClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Kimbo Inventory Management System")
        self.root.config(bg="white")

        # ---------------title----------------
        self.icon_title = PhotoImage(file="images/buy.png")
        title = Label(self.root, text="Kimbo Inventory Management System", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=100)

        # --------btn logout -------------
        btn_logout = Button(self.root, text="Logout",command=self.logout, font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)
        # ---------clock--------------------
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-YYYY\t\t Time: HH:MM:SS", font=("times new roman", 15, "bold"), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # --------------left menu-------------------------
        self.MenuLogo = Image.open("images/management.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.ANTIALIAS)
        self.MenuLogo = ImageTk, PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        self.icon_side=PhotoImage(file="images/smallicon10.png")

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20, "bold"), bg="#009688").pack(side=TOP, fill=X)

        btn_employee = Button(LeftMenu, text="Employee", command=self.employee, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,
                                                                                                         fill=X)
        btn_customer = Button(LeftMenu, text="Supplier", command=self.customer, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,
                                                                                                           fill=X)
        btn_product = Button(LeftMenu, text="Product", command=self.product, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,
                                                                                                           fill=X)
        btn_sales = Button(LeftMenu, text="Sales",command=self.sales, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,
                                                                                                           fill=X)
        btn_category = Button(LeftMenu, text="Category", command=self.category, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,
                                                                                                           fill=X)
        btn_exit = Button(LeftMenu, text="Exit",command=self.root.destroy, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,
                                                                                                           fill=X)
        
        # --------------------------content-------------------------------------

        self.lbl_employee= Label(self.root,text="Total Employees\n[ 0 ]",bd=5, relief=RIDGE,  bg="#00008B", fg="white", font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_customer = Label(self.root, text="Total Customers\n[ 0 ]", bd=5, relief=RIDGE, bg="#4A708B",
                                  fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_customer.place(x=650, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Products\n[ 0 ]", bd=5, relief=RIDGE, bg="#8B3626",
                                  fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=1000, y=120, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE, bg="#00EE00",
                                  fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=300, y=300, height=150, width=300)

        self.lbl_categories = Label(self.root, text="Total Categories\n[ 0 ]", bd=5, relief=RIDGE, bg="#8B8B00",
                                  fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_categories.place(x=650, y=300, height=150, width=300)




        # ---------footer--------------------
        lbl_footer = Label(self.root, text="IMS-inventory Management System", font=("times new roman", 15), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)

        self.update_content()

# ----------------------------------------------------------

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def customer(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = customerClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[{str(len(product))}]')

            cur.execute("select * from customer")
            customer = cur.fetchall()
            self.lbl_customer.config(text=f'Total Suppliers\n[{str(len(customer))}]')

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_categories.config(text=f'Total Categories\n[{str(len(category))}]')

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n[{str(len(employee))}]')
            bill = len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n [{str(bill)}]')

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(
            text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200, self.update_content)
        except Exception as ex:
               messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python loginn.py")


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
