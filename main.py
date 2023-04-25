from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


# Defining a class

class Login_page:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background Image

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\eshwar\Desktop\Gopinath Files\Login_page\Background_image.jpg")  # copy path image from your system

        label_bg = Label(self.root, image=self.bg)
        label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Logo work

        img1 = Image.open(r"C:\Users\eshwar\Desktop\Gopinath Files\Login_page\LoginPage_Logo.jpg")  # copy path image from your system
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        label_img1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        label_img1.place(x=730, y=175, width=100, height=100)

        text_work = Label(frame, text="Login Page", font=('times new roman', 20, "bold"), fg="white", bg="black")
        text_work.place(x=100, y=110)

        # labelling for username and password

        username = lb1 = Label(frame, text="Username", font=('times new roman', 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=('times new roman', 15, 'bold'))
        self.txtuser.place(x=40, y=180, width=270)

        password = lb2 = Label(frame, text="Password", font=('times new roman', 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpsw = ttk.Entry(frame, show='*', font=('times new roman', 15, 'bold'))
        self.txtpsw.place(x=40, y=250, width=270)

        # Icon / button / Username

        img2 = Image.open(r"C:\Users\eshwar\Desktop\Gopinath Files\Login_page\Username_image.png")  # copy path image from your system
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        label_img2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        label_img2.place(x=650, y=323, width=25, height=25)

        # Password

        img3 = Image.open(r"C:\Users\eshwar\Desktop\Gopinath Files\Login_page\Password_image.png")  # copy path image from your system
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        label_img3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        label_img3.place(x=650, y=393, width=25, height=25)

        # Login button

        loginbtn = Button(frame, command=self.login, text="Login", font=('times new roman', 15, 'bold'), bd=3,
                          relief=RIDGE, fg="white", bg="black")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register button


        # Defining a function

    def login(self):
        if self.txtuser.get() == "" or self.txtpsw.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "Gopinath" and self.txtpsw.get() == "gopi_19":
            messagebox.showinfo("Success", "Login Successfull")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")


# Calling a main function

if __name__ == "__main__":
    root = Tk()
    app = Login_page(root)
    root.mainloop()




