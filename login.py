from tkinter import *
from tkinter import ttk
from pil import Image, ImageTk
from main import IMS


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # bg image
        self.bg = ImageTk.PhotoImage(file="image/b3.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        # Left image
        self.left = ImageTk.PhotoImage(file="image/inscription.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        # Register Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="purple"
                      ).place(x=50, y=30)
        # ---------------row 1--------------------

        f_name = Label(frame1, text="First Name", font=("times new roman", 20, "bold"), bg="white",
                       fg="grey").place(x=50, y=100)
        txt_frame = Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 20, "bold"), bg="white",
                       fg="grey").place(x=370, y=100)
        txt_frame = Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=370, y=130, width=250)

        # ----------------row 2------------------
        contact = Label(frame1, text="Contact No.", font=("times new roman", 20, "bold"), bg="white",
                       fg="grey").place(x=50, y=170)
        txt_frame = Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 20, "bold"), bg="white",
                       fg="grey").place(x=370, y=170)
        txt_frame = Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=370, y=200, width=250)

        # --------------------row3--------------
        question = Label(frame1, text="Security Question", font=("times new roman", 20, "bold"), bg="white",
                        fg="grey").place(x=50, y=240)
        cmb_quest = ttk.Combobox(frame1, font=("times new roman", 13), state="readonly", justify=CENTER)
        cmb_quest['values'] = ("select", "Your First Pet Name", "Your Birth County place", "Your Best Meal")
        cmb_quest.place(x=50, y=270, width=250)
        cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 20, "bold"), bg="white",
                      fg="grey").place(x=370, y=240)
        txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=370, y=270, width=250)

        # ----------------row 2------------------
        password = Label(frame1, text="Password", font=("times new roman", 20, "bold"), bg="white",
                        fg="grey").place(x=50, y=310)
        txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=50, y=340, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 20, "bold"), bg="white",
                      fg="grey").place(x=370, y=310)
        txt_cpassword= Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=370, y=340, width=250)

        # -------------------------terms
        chk = Checkbutton(frame1, text="I Agree To The Terms & Conditions", onvalue=1, offvalue=0, bg="white", font=("times new roman", 12,)).place(x=50, y=380)
        self.btn_img = ImageTk.PhotoImage(file="image/register.png")

        btn = Button(frame1, image=self.btn_img, bd=0, cursor="hand2", command=self.main).place(x=50, y=420, width=260, height=60)
        btn_login = Button(self.root, text="Sign In", command=self.login2, font=("times new roman", 20), bd=0, bg="#EEC591", cursor="hand2").place(x=380, y=550)

    def main(self):
        self.new_win = Toplevel(self.root)
        self.new_obj =IMS(self.new_win)


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
