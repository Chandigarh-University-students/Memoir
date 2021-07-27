from tkinter import *
import pyrebase
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from ToolTip import CreateToolTip
import FirebaseAuth

class Diary:
    def __init__(self,root):
        self.root=root
        self.diaryPage()
        #self.login()
        self.firebase = pyrebase.initialize_app(FirebaseAuth.firebaseConfig)
        
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

        self.forget_pass = Button(self.root, text="Forget password?", fg="red",bg="white", font="Arial 9", cursor="hand2", command=self.forgetPass)
        self.forget_pass.place(x = 390, y = 210, width = 120)

        self.login_button = Button(self.root, text="LOGIN", bg="skyblue", font=self.font, relief=RAISED, border = 4, cursor="hand2", command=self.Signin)
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

        self.register_new = Button(self.root, text="Register",bg="#ADD8E6", font=self.font, relief=RAISED, border = 4,cursor="hand2", command=self.Signup)
        self.register_new.place(x = 510, y = 210, width = 100)
        
        self.login_button = Button(self.root, text="Already Have a Account", bg="skyblue", font=self.font, relief=RAISED, border = 4, cursor="hand2", command=self.login)
        self.login_button.place(x = 475, y = 290, width = 180, height = 30)

    def showPass(self):
        if self.pass_chk.get()==1:
            self.password_entry.config(show='')
        else:
            self.bullet = "\u2022"
            self.password_entry.config(show=self.bullet)

    def Signin(self):
        if self.password_entry.get()=='' or self.username_entry.get()=='':
            messagebox.showerror("Error !", "All Fields are Required !", parent=self.root)
            return

        try:
            self.email = self.username_entry.get()
            self.password = self.password_entry.get()
            self.auth = self.firebase.auth()
            self.login = self.auth.sign_in_with_email_and_password(self.email, self.password)
            messagebox.showinfo("Success", "Signed In!")
            self.diaryPage()
        except Exception as e:
            messagebox.showerror("Error !", str(e), parent=self.root)

    def Signup(self):
        if self.password_entry.get()=='' or self.username_entry.get()=='':
            messagebox.showerror("Error !", "All Fields are Required !", parent=self.root)
            return

        try:
            self.email = self.username_entry.get()
            self.password = self.password_entry.get()
            self.auth = self.firebase.auth()
            self.login = self.auth.create_user_with_email_and_password(self.email, self.password)
            messagebox.showinfo("Success", "Signed Up!")
            self.diaryPage()
        except Exception as e:
            messagebox.showerror("Error !", str(e), parent=self.root)

    def forgetPass(self):
        if self.username_entry.get()=='':
            messagebox.showerror('Error !','Enter email', parent=self.root)
            return
        try:
            self.email = self.username_entry.get()
            if messagebox.askyesno('Confirm',f'Is your mail {self.email} correct?', parent=self.root):
                self.auth = self.firebase.auth()
                self.auth.send_password_reset_email(self.email)
                messagebox.showinfo('Info',f'A password reset email is sent to {self.email}', parent=self.root)
            else:
                messagebox.showinfo('Info','Provide us with your email',parent=self.root)
        except Exception as e:
            messagebox.showerror('Error !',str(e),parent=self.root)

    def diaryPage(self):
        self.page = Toplevel(self.root)
        self.page.title('Your Page')
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.page.geometry('1000x600')
        self.icon = Image.open('images/diary.png')
        self.photo = ImageTk.PhotoImage(self.icon)
        self.page.wm_iconphoto(False, self.photo)
        self.font = ["Helvetica", 15, "bold"]

        #top frame
        self.topframe = Frame(self.page, bg='#ECECEC', padx=15, pady=5)
        self.topframe.pack(expand='no', fill='x')
        self.diarylabel = Label(self.topframe, text='Your Memories', fg='#28282B',bg='#ECECEC', font=self.font)
        self.diarylabel.pack(side='left')

        self.play = ImageTk.PhotoImage(file='images/play.png')
        self.previous = ImageTk.PhotoImage(file='images/previous.png')
        self.next = ImageTk.PhotoImage(file='images/next.png')

        self.next_button = Button(self.topframe, image=self.next,bg='#ECECEC',border=0, cursor='hand2')
        self.next_button.pack(side='right')
        self.next_button_ttp = CreateToolTip(self.next_button, 'Next')
        
        self.play_button = Button(self.topframe, image=self.play,bg='#ECECEC',border=0, cursor='hand2')
        self.play_button.pack(side='right')
        self.play_button_ttp = CreateToolTip(self.play_button, 'Play/Pause')
        
        self.previous_button = Button(self.topframe, image=self.previous,bg='#ECECEC',border=0, cursor='hand2')
        self.previous_button.pack(side='right')
        self.previous_button_ttp = CreateToolTip(self.previous_button, 'Previous')

        self.musiclabel = Label(self.topframe, text = 'Let the Music play     ',fg='#28282B',bg='#ECECEC', font=self.font)
        self.musiclabel.pack(side='right')
        
        #middle frame
        self.pw = PanedWindow(self.page, borderwidth=2, width = 100)
        self.pw.pack(fill=BOTH, expand=True)

        self.nowlabel = Label(self.pw, text='Now', fg='#28282B',bg='#90CCF4')
        self.pw.add(self.nowlabel)

        self.pw2 = PanedWindow(self.page, borderwidth=2, width = 100)
        self.pw.add(self.pw2)

        self.oldlabel = Label(self.pw2, text='Old', fg='#28282B',bg='#F78888')
        self.pw2.add(self.oldlabel)

        #bottom frame
        self.bottomframe = Frame(self.page, bg='#F3D250', padx=15, pady=5)
        self.bottomframe.pack(expand='no', fill='x', side='bottom')

        self.delete_account = Button(self.bottomframe,text='Delete', bg='red', fg='white', font='Arial 12 bold', cursor='hand2',width=10)
        self.delete_account.pack(side='right')
        
        self.theme_image = ImageTk.PhotoImage(file='images/theme.png')
        self.theme_button = Button(self.bottomframe, image=self.theme_image, bg='#F3d250', cursor='hand2', border=0)
        self.theme_button.pack(side='right')
        self.theme_button_ttp = CreateToolTip(self.theme_button,'Themes')

        self.add_button = Button(self.bottomframe,text='Add', bg='green', fg='white', font='Arial 12 bold', cursor='hand2',width=10)
        self.add_button.pack(side='left')

        self.clear_button = Button(self.bottomframe,text='Clear', bg='#ECECEC', fg='black', font='Arial 12 bold', cursor='hand2',width=10)
        self.clear_button.pack(side='left')

        self.reset_button = Button(self.bottomframe,text='Reset', bg='#ECECEC', fg='black', font='Arial 12 bold', cursor='hand2',width=10)
        self.reset_button.pack(side='left')
        

root = Tk()
obj = Diary(root)
root.mainloop()
