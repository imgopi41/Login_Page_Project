from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox



# Defining a class

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


# defining variables

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_cfpass=StringVar()


# Background image

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\eshwar\Desktop\Gopinath Files\Visual Studio files\GopiVSCodePython\Loginpage\Background_image.jpg")
        bg_lb1 = Label(self.root,image=self.bg)
        bg_lb1.place(x=0,y=0,relwidth=1,relheight=1)

# Main Frame

        # self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\eshwar\Desktop\Gopinath Files\Visual Studio files\GopiVSCodePython\Loginpage\Background_image2.jpg")
        # left_lb1 = Label(self.root,image=self.bg1)
        # left_lb1.place(x=50,y=100,width=470,height=550)

        register_lbl=Label(text="REGISTER HERE", font=("times new roman",20,"bold"),fg="green")
        register_lbl.place(x=20,y=20)


# Labelling  first and last name


        fname=Label(text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.txt_fname=ttk.Entry(textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txt_fname.place(x=50,y=130,width=250)


        lname=Label(text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

# Labelling contact number and email id

        contact=Label(text="Contact Number",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)


        
        Email_lbl=Label(text="Email Id",font=("times new roman",15,"bold"),bg="white",fg="black")
        Email_lbl.place(x=370,y=170)


        self.Emailbl=ttk.Entry(textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.Emailbl.place(x=370,y=200,width=250)


# Labelling Security section


        security_lbl=Label(text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_lbl.place(x=50,y=270)

        self.combo_security_lbl=ttk.Combobox(textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_lbl["values"]=("Select","Food name","Place name","Pet name")
        self.combo_security_lbl.place(x=50,y=300,width=250)
        self.combo_security_lbl.current(0)



        security_a=Label(text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_a.place(x=370,y=269)


        self.txt_security=ttk.Entry(textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=300,width=250)      


# Labelling Password and confirm password

        psw_lbl=Label(text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")  
        psw_lbl.place(x=50,y=380)

        self.txt_psw_lbl=Entry(textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_psw_lbl.place(x=50,y=410,width=250)


        cpsw_lbl=Label(text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")  
        cpsw_lbl.place(x=370,y=380)

        self.txt_cpsw_lbl=ttk.Entry(textvariable=self.var_cfpass,font=("times new roman",15,"bold"))
        self.txt_cpsw_lbl.place(x=370,y=410,width=250)  


# Check Button

        self.var_check=IntVar()
        chkbtn = Checkbutton(variable=self.var_check,text="I Agree Terms and Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        chkbtn.place(x=50,y=455)

# Button 

        img=Image.open(r"C:\Users\eshwar\Desktop\Gopinath Files\Visual Studio files\GopiVSCodePython\Loginpage\Registernow_button.jpg")
        img=img.resize((100,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=50,y=510,width=90)

        img1=Image.open(r"C:\Users\eshwar\Desktop\Gopinath Files\Visual Studio files\GopiVSCodePython\Loginpage\Loginnow_image.jpg")
        img1=img1.resize((100,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=350,y=510,width=100)


# Function declarition


    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_cfpass.get():
                messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
                messagebox.showerror("Error","Please Agree our Terms and Condition")
        else: 
                messagebox.showinfo("Success","Welcome Dear user") 


 


if __name__ == "__main__":
    root=Tk()
    app = Register(root)
    root.mainloop()





#     self.var_fname=StringVar()
#         self.var_lname=StringVar()
#         self.var_contact=StringVar()
#         self.var_email=StringVar()
#         self.var_securityQ=StringVar()
#         self.var_securityA=StringVar()
#         self.var_pass=StringVar()
#         self.var_cfpass=StringVar()

# command=self.register_data,