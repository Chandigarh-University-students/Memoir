from tkinter import *
import pyrebase
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

global password_entry
global pass_chk

class Diary:
    def __init__(self,root):
        self.root=root
        self.login()
        
    def login(self):
        self.root.destroy()
        self.root = Tk()
        self.app_width = 800
        self.app_height = 480

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2 ) - (self.app_height / 2)

        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')
        self.root.resizable(0,0)
        self.root.config(bg="white")
        self.root.title("Your Diary")
        
        self.icon = Image.open('images/diary.png')
        self.photo = ImageTk.PhotoImage(self.icon)
        self.root.wm_iconphoto(False, self.photo)
        
        self.bg = ImageTk.PhotoImage(file="images/login.png")
        self.Background = Label(self.root, image = self.bg)
        self.Background.place(x = 0, y = 0, relwidth=1, relheight=1)

        self.font = ["Helvetica", 10, "bold"]
        self.username_label = Label(self.root, text="Email", font=self.font, bg="white")
        self.username_label.place(x = 390, y = 130, height = 23)

        self.username_entry = Entry(self.root, font=self.font)
        self.username_entry.place(x = 465, y = 130, width = 250, height = 23)

        self.password_label = Label(self.root, text="Password", font=self.font, bg="white")
        self.password_label.place(x = 390, y = 170, height = 23)

        self.bullet = "\u2022"
        self.password_entry = Entry(self.root, font=self.font, show=self.bullet)
        self.password_entry.place(x = 465, y = 170, width = 225, height = 23)
        
        self.pass_chk = IntVar()
        self.show_pass = Checkbutton(self.root, bg='white', cursor='hand2', border=0, variable=self.pass_chk, command=self.showPass)
        self.show_pass.place(x = 690, y = 170, height = 23)

        self.forget_pass = Button(self.root, text="Forget password?", fg="red",bg="white", font="Arial 9", cursor="hand2")
        self.forget_pass.place(x = 390, y = 210, width = 120)

        self.login_button = Button(self.root, text="LOGIN", bg="skyblue", font=self.font, relief=RAISED, border = 4, cursor="hand2", command=self.diaryPage)
        self.login_button.place(x = 510, y = 250, width = 90, height = 30)

        self.register_new = Button(self.root, text="Register New Account",bg="#ADD8E6", font=self.font, relief=RAISED, border = 4, command=self.register, cursor="hand2")
        self.register_new.place(x = 475, y = 330, width = 160)

    def register(self):
        self.root.destroy()
        self.root = Tk()
        self.app_width = 800
        self.app_height = 480

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2 ) - (self.app_height / 2)

        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')
        self.root.resizable(0,0)
        self.root.config(bg="white")
        self.root.title("Your Diary")
        
        self.icon = Image.open('images/diary.png')
        self.photo = ImageTk.PhotoImage(self.icon)
        self.root.wm_iconphoto(False, self.photo)

        self.bg1 = ImageTk.PhotoImage(file="images/register.png")
        self.Background = Label(self.root, image = self.bg1)
        self.Background.place(x = 0, y = 0, relwidth=1, relheight=1)

        self.font = ["Helvetica", 10, "bold"]
        self.username_label = Label(self.root, text="Email", font=self.font, bg="white")
        self.username_label.place(x = 390, y = 130, height = 23)

        self.username_entry = Entry(self.root, font=self.font)
        self.username_entry.place(x = 465, y = 130, width = 250, height = 23)

        self.password_label = Label(self.root, text="Password", font=self.font, bg="white")
        self.password_label.place(x = 390, y = 170, height = 23)

        self.bullet = "\u2022"
        self.password_entry = Entry(self.root, font=self.font, show=self.bullet)
        self.password_entry.place(x = 465, y = 170, width = 225, height = 23)

        self.pass_chk = IntVar()
        self.show_pass = Checkbutton(self.root, bg='white', cursor='hand2', border=0, variable=self.pass_chk, command=self.showPass)
        self.show_pass.place(x = 690, y = 170, height = 23)

        self.register_new = Button(self.root, text="Register",bg="#ADD8E6", font=self.font, relief=RAISED, border = 4,cursor="hand2", command=self.diaryPage)
        self.register_new.place(x = 510, y = 210, width = 100)
        
        self.login_button = Button(self.root, text="Already Have a Account", bg="skyblue", font=self.font, relief=RAISED, border = 4, cursor="hand2", command=self.login)
        self.login_button.place(x = 475, y = 290, width = 180, height = 30)

    def showPass(self):
        if self.pass_chk.get()==1:
            self.password_entry.config(show='')
        else:
            self.bullet = "\u2022"
            self.password_entry.config(show=self.bullet)

    def diaryPage(self):
        if self.password_entry.get()=='' or self.username_entry.get()=='':
            messagebox.showerror("Error !", "All Fields are Required !", parent=self.root)
            return
        self.page = Toplevel(self.root)
        self.page.title('Your Page')
        self.icon = Image.open('images/diary.png')
        self.photo = ImageTk.PhotoImage(self.icon)
        self.page.wm_iconphoto(False, self.photo)

root = Tk()
obj = Diary(root)
root.mainloop()
