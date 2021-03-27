# important packages
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
import passgen
import requests,json
import re

class PassMan():
    def __init__(self):

        # creating root window and the gui
        self.root=tk.Tk()
        self.root.title("Password Manager")
        self.root.geometry("410x560+400+100")


        # initializing important instance variable
        self.BASE_URL = "http://localhost:8000/"
        self.ENDPOINT = "api/user/"
        self.ACCOUNT_ENDPOINT  = "api/account"
        self.hidden = True
        self.counter = self.pk =0
        
        self.website_entry = self.user_entry = self.password_entry = self.tree  =  self.manager_tab_signup = self.manager_tab_login= None
        
        # important variable and their datatypes to hold the value of checkbox
        self.lower_alpha = tk.IntVar()
        self.upper_alpha = tk.IntVar()
        self.numeric = tk.IntVar()
        self.special_symbol = tk.IntVar()

        # important variablt and their datatypes to hold the valur of forms
        self.email = tk.StringVar()
        self.password =  tk.StringVar()
        self.generated_password = tk.StringVar()
        self.remember_me = tk.IntVar()
        self.name = tk.StringVar()
        self.repeat_password = tk.StringVar()
        self.dml_website = tk.StringVar()
        self.dml_email = tk.StringVar()
        self.dml_password = tk.StringVar()





        # tabs
        tabs=ttk.Notebook(self.root)
        self.manager_tabs=ttk.Frame(tabs)
        self.generator_tab=ttk.Frame(tabs)
        self.about_tab=ttk.Frame(tabs)
        tabs.add(self.manager_tabs,text="Manager")
        tabs.add(self.generator_tab,text="Generator")
        tabs.add(self.about_tab,text="About")
        tabs.pack(expand=True,fill='both')



        # creating different gui
        self.about_tab_config()
        self.generator_tab_config()
        self.login()


        # launching window and disabling resizing facility of window
        self.root.resizable(False,False)
        self.root.mainloop()


    # creating gui for about tab
    def about_tab_config(self):
        about_label=ttk.Label(self.about_tab,text="About the Developer:\n\nfollow me on Github : github.com/altaf7740\nfollow me on Linkedin : linkedin.com/in/altaf7740\n\n\n   THANK YOU :)")
        about_label.grid(row=0,column=0)


    # creating gui for generator tab
    def generator_tab_config(self):
        heading_label = ttk.Label(self.generator_tab,text="Password Generator",font=("verdana",20,"bold"))
        heading_label.place(x=30,y=20)

        length_label = ttk.Label(self.generator_tab,text="Length : ",font=("verdana",10))
        length_label.place(x=45,y=110)

        self.spin_box = ttk.Spinbox(self.generator_tab,width=23,to=50,font=("verdana",10))
        self.spin_box.place(x=115,y=110)


        complexity_label = ttk.Label(self.generator_tab,text="Complexity :",font=("verdana",10))
        complexity_label.place(x=45,y=170)

        lower_alpha_checkbox = tk.Checkbutton(self.generator_tab,text="Lower Alphabhet",variable=self.lower_alpha, offvalue=0, onvalue=1,font=("verdana",10))
        lower_alpha_checkbox.place(x=50,y=220)

        upper_alpha_checkbox = tk.Checkbutton(self.generator_tab,text="Upper Alphabhet",variable=self.upper_alpha, offvalue=0, onvalue=1,font=("verdana",10))
        upper_alpha_checkbox.place(x=220,y=220)

        numeric_checkbox = tk.Checkbutton(self.generator_tab,text="Numbers",variable=self.numeric, offvalue=0, onvalue=1,font=("verdana",10))
        numeric_checkbox.place(x=50,y=260)

        special_symbol_checkbox = tk.Checkbutton(self.generator_tab,text="Special Symbols",variable=self.special_symbol, offvalue=0, onvalue=1,font=("verdana",10))
        special_symbol_checkbox.place(x=220,y=260)

        generate_button = tk.Button(self.generator_tab,text="Generate", bg="blue",fg="white",command=self.password_generator,font=("verdana",14))
        generate_button.place(x=31,y=350,width=340)

        
        self.generated_edit_box = ttk.Entry(self.generator_tab,width=25,textvariable=self.generated_password,font=("helvitika",15,"bold"))
        self.generated_edit_box.place(x=31,y=420)

        copy_button = tk.Button(self.generator_tab,text="⎘", bg="white", command=self.clipboard_copy,fg="black",font=('verdana',15))
        copy_button.place(x=320,y=410,width=40)







    # ---------------creating gui for manager tab-----------------

    # 1. *************creating login form in manager tab*************
    def login(self):
        if self.manager_tab_signup:
            self.manager_tab_signup.destroy()
        self.manager_tab_login = ttk.Frame(self.manager_tabs)
        self.manager_tab_login.pack(expand=True,fill='both')
        # 
        # writing in manager tab
        heading_label = ttk.Label(self.manager_tab_login,text="Login",font=("verdana",20,"bold"))
        heading_label.place(x=30,y=30)

        for_registration_label = ttk.Label(self.manager_tab_login,text="Doesn't have an account yet?",font=("verdana",10))
        for_registration_label.place(x=32,y=65)

        signup_label=ttk.Label(self.manager_tab_login,foreground="blue",cursor="hand2",text = "Sign Up",font =("verdana",10))
        signup_label.place(x=240,y=65)
        signup_label.bind("<Button-1>", lambda e: self.signup())

        email_label = ttk.Label(self.manager_tab_login,text="Email Address",font=("verdana",10,"bold"))
        email_label.place(x=31,y=100)

        password_label = ttk.Label(self.manager_tab_login,text="Password",font=("verdana",10,"bold"))
        password_label.place(x=31,y=170)

        forgot_password_label=ttk.Label(self.manager_tab_login,foreground="blue",cursor="hand2",text = "Forgot Password?",font =("verdana",10))
        forgot_password_label.place(x=250,y=170)
        forgot_password_label.bind("<Button-1>", lambda e: self.recover_password())

        login_with_label=ttk.Label(self.manager_tab_login,foreground="grey",text = "  or login with  ".center(50,"-"),font =("verdana",10))
        login_with_label.place(x=31,y=360)

        # entry box in manager tab
        email_entry = tk.Entry(self.manager_tab_login,width=30,textvariable=self.email,font=("helvitika",15,"bold"))
        email_entry.place(x=34,y=125)
        email_entry.focus()

        self.password_entry = tk.Entry(self.manager_tab_login,width=30,textvariable=self.password,font=("helvitika",15,"bold"),show="*")
        self.password_entry.place(x=34,y=195)
        self.password_entry.bind("<Return>",self.login_functionality)


        # checkbox
        remember_me_checkbox = tk.Checkbutton(self.manager_tab_login,text="Remember Me",variable=self.remember_me, offvalue=0, onvalue=1,font=("verdana",10))
        remember_me_checkbox.place(x=31,y=240)


        # login button
        login_button = tk.Button(self.manager_tab_login,text="LOGIN", bg="blue",fg="white",command=self.login_functionality,font=("verdana",14))
        login_button.place(x=31,y=290,width=340)

        google_login_button = tk.Button(self.manager_tab_login,text="Google", bg="#FF3E30",fg="white",command=exit,font=("verdana",14))
        google_login_button.place(x=31,y=405,width=150)

        facebook_login_button = tk.Button(self.manager_tab_login,text="Facebook", bg="#3B5998",fg="white",command=exit,font=("verdana",14))
        facebook_login_button.place(x=220,y=405,width=150)




    # 2. *************creating signup form in manager tab*****************
    def signup(self):
        self.manager_tab_login.destroy()
        self.manager_tab_signup = ttk.Frame(self.manager_tabs)
        self.manager_tab_signup.pack(expand=True,fill='both')

        heading_label = ttk.Label(self.manager_tab_signup,text="Signup",font=("verdana",20,"bold"))
        heading_label.place(x=30,y=5)

        signin_label2 = ttk.Label(self.manager_tab_signup,text="Already registered ",font=("verdana",10))
        signin_label2.place(x=190,y=400)

        signin_label=ttk.Label(self.manager_tab_signup,foreground="blue",cursor="hand2",text = "Sign in?",font =("verdana",10))
        signin_label.place(x=320,y=400)
        signin_label.bind("<Button-1>", lambda e: self.login())

        name_label = ttk.Label(self.manager_tab_signup,text="Name",font=("verdana",10,"bold"))
        name_label.place(x=31,y=65)


        email_label = ttk.Label(self.manager_tab_signup,text="Email Address",font=("verdana",10,"bold"))
        email_label.place(x=31,y=135)

        password_label = ttk.Label(self.manager_tab_signup,text="Password",font=("verdana",10,"bold"))
        password_label.place(x=31,y=205)

        repeat_password_label = ttk.Label(self.manager_tab_signup,text="Confirm Password",font=("verdana",10,"bold"))
        repeat_password_label.place(x=31,y=275)

        login_with_label=ttk.Label(self.manager_tab_signup,foreground="grey",text = "  or signup with  ".center(50,"-"),font =("verdana",10))
        login_with_label.place(x=31,y=440)

        # entry box in manager tab
        name_entry = tk.Entry(self.manager_tab_signup,width=30,textvariable=self.name,font=("helvitika",15,"bold"))
        name_entry.place(x=34,y=90)


        email_entry = tk.Entry(self.manager_tab_signup,width=30,textvariable=self.email,font=("helvitika",15,"bold"))
        email_entry.place(x=34,y=160)
        email_entry.delete(0,tk.END)
        

        self.password_entry = tk.Entry(self.manager_tab_signup,width=30,textvariable=self.password,font=("helvitika",15,"bold"),show="*")
        self.password_entry.place(x=34,y=230)
        self.password_entry.delete(0,tk.END)

        password_repeat_entry = tk.Entry(self.manager_tab_signup,width=30,textvariable=self.repeat_password,font=("helvitika",15,"bold"),show="*")
        password_repeat_entry.place(x=34,y=300)


        signup_button = tk.Button(self.manager_tab_signup,text="CREATE ACCOUNT", bg="blue",fg="white",command=self.signup_functionality,font=("verdana",14))
        signup_button.place(x=31,y=360,width=340)

        google_signup_button = tk.Button(self.manager_tab_signup,text="Google", bg="#FF3E30",fg="white",command=exit,font=("verdana",14))
        google_signup_button.place(x=31,y=480,width=150)

        facebook_signup_button = tk.Button(self.manager_tab_signup,text="Facebook", bg="#3B5998",fg="white",command=exit,font=("verdana",14))
        facebook_signup_button.place(x=220,y=480,width=150)



    # 3. *******************creating password manager in manager_tab***********************
    def password_manager(self,response):
        if self.manager_tab_login:
            self.manager_tab_login.destroy()
        else:
            self.manager_tab_signup.destroy()
        
        self.manager_tab_manager = ttk.Frame(self.manager_tabs)
        self.manager_tab_manager.pack(expand=True,fill='both')

        # styling the treeview
        style = ttk.Style()
        style.configure("Treeview",background="white", foreground="black", rowheight=30,font=('TkFixedFont',10))
        style.map('Treeview',background=[('selected','green')])

        self.tree = ttk.Treeview(self.manager_tab_manager,columns=("website","username","password"),)
        self.tree.heading("#0",text="counter")
        self.tree.heading("website",text="Website")
        self.tree.heading("username",text="Username")
        self.tree.heading("password",text="Password")
        self.tree.pack()
        self.tree.column('#0', width=0,minwidth=0)
        self.tree.column('#1', width=195, anchor=tk.W)
        self.tree.column('#2',anchor=tk.W,width=195)
        self.tree.column('#3',width=0  ,minwidth=0)
        self.tree.tag_configure('oddrow', background="white")
        self.tree.tag_configure('evenrow',background="#FFFF66")
        for data in response:
            if self.counter %2==0:
                self.tree.insert(parent='',index='end',iid=data['pk'],text="",values=(data['website'],data['username'],data['password']),tags=('evenrow'))
            else:
                self.tree.insert(parent='',index='end',iid=data['pk'],text="",values=(data['website'],data['username'],data['password']),tags=('oddrow'))
            self.counter+=1
            self.pk=data['pk']

        # binding double click feature
        self.tree.bind("<Double-1>",self.bind_data)


        # tree.bind("<Button-1>", disableEvent)    

        website_label = ttk.Label(self.manager_tab_manager,text="Website : ",font=("verdana",10))
        website_label.place(x=35,y=340)

        self.website_entry = tk.Entry(self.manager_tab_manager,width=20,textvariable=self.dml_website,font=("helvitika",15,"bold"))
        self.website_entry.place(x=140,y=335)

        user_label = ttk.Label(self.manager_tab_manager,text="Username : ",font=("verdana",10))
        user_label.place(x=35,y=380)

        self.user_entry = tk.Entry(self.manager_tab_manager,width=20,textvariable=self.dml_email,font=("helvitika",15,"bold"))
        self.user_entry.place(x=140,y=375)

        password_label = ttk.Label(self.manager_tab_manager,text="Password : ",font=("verdana",10))
        password_label.place(x=35,y=420)

        self.password_entry = tk.Entry(self.manager_tab_manager,width=15,textvariable=self.dml_password,font=("helvitika",15,"bold"))
        self.password_entry.place(x=140,y=415)
        

        show_hide_button = tk.Button(self.manager_tab_manager,text="👁", bg="white",fg="black",command=self.show_hide_password,font=("verdana",15))
        show_hide_button.place(x=310,y=408,width=30)

        copy_button = tk.Button(self.manager_tab_manager,text="⎘", bg="white",fg="black",command=self.clipboard_creds,font=("verdana",15))
        copy_button.place(x=360,y=408,width=40)


        insert_button = tk.Button(self.manager_tab_manager,text="INSERT", bg="blue",fg="white",command=self.insert_data,font=("verdana",14))
        insert_button.place(x=10,y=480,width=100)

        update_button = tk.Button(self.manager_tab_manager,text="UPDATE", bg="green",fg="white",command=self.update_data,font=("verdana",14))
        update_button.place(x=160,y=480,width=100)

        delete_button = tk.Button(self.manager_tab_manager,text="DELETE", bg="red",fg="white",command=self.delete_data,font=("verdana",14))
        delete_button.place(x=300,y=480,width=100)












    # -------important methods--------

    # copy generated password to clipboard
    def clipboard_copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.generated_password.get())
        self.root.update() 
        m_box.showinfo("Success","Coppied to clipboard!")

    # password recovery logic
    def recover_password(self):
        if self.email.get()  != "":
            # do what ever you want 
            # help 
            print(self.email.get())
        else:
            m_box.showerror("error","please provide valid email")

    # business logic for signup
    def signup_functionality(self):
        if self.email.get() !="" and self.name.get() != "" and self.password.get() != "" and self.repeat_password.get()!= "":
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email.get()):
                m_box.showerror("error","invalid email  !")
                return None
            if self.password.get() != self.repeat_password.get():
                m_box.showerror("error","password not matched !")
            else:
                # write the logic here further
                response = requests.post(self.BASE_URL+self.ACCOUNT_ENDPOINT,data=json.dumps({"name":self.name.get(),"email":self.email.get(),"master_key":self.password.get()}))
                if response.status_code == 200:
                    m_box.showinfo("success","accounts successfully created, Login to Enjoy the features")
                    self.login()
                else:
                    m_box.showerror("error","something went wrong !")

        else:
            m_box.showerror("error","fill the form completely")

    # business logic for login
    def login_functionality(self,event=None):
        if  self.email.get() ==  "" or  self.password.get() ==  "":
            m_box.showerror("error","fill the form correctly")
        else:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email.get()):
                m_box.showerror("error","invalid email  !")
                return None
            response = requests.get(self.BASE_URL+self.ACCOUNT_ENDPOINT,data=json.dumps({"email":self.email.get(),"master_key":self.password.get()}))
            if response.status_code == 200:
                creds = {"email":self.email.get(),"password":self.password.get()}      
                response = requests.get(self.BASE_URL+self.ENDPOINT,data=json.dumps(creds))        
                self.password_manager(response.json())
            else:
                m_box.showerror("error","user id or password is incorrect !")

    # business logic to clean the creds form
    def clean_cred_form(self):
        self.user_entry.delete(0,tk.END)
        self.password_entry.delete(0,tk.END)
        self.website_entry.delete(0,tk.END)
        

    # insert data in form automatically when double clicked on any element of treeview
    def bind_data(self,e):
        data = self.tree.focus()
        values=self.tree.item(data,'values')
        self.clean_cred_form()
        self.user_entry.insert(0,values[1])
        self.website_entry.insert(0,values[0])
        self.password_entry.insert(0,values[2])
        self.password_entry.config(show="*")
        self.hidden=True

    # logic to show or hide password (plain text password / )
    def show_hide_password(self):
        if self.hidden:
            self.password_entry.config(show='')
            self.hidden = False
        else:
            self.password_entry.config(show="*")
            self.hidden = True


    # copy the user_creds_password to clipboard
    def clipboard_creds(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.dml_password.get())
        self.root.update() 
        m_box.showinfo("Success","Coppied to clipboard!")

    # business logic to update the user creds
    def update_data(self):
        selected = self.tree.focus()
        creds = {"email":self.email.get(),"password":self.password.get(),"cred_user":self.dml_email.get(),"cred_password":self.dml_password.get(),"cred_website":self.dml_website.get(), "id":selected}
        response = requests.put(self.BASE_URL+self.ENDPOINT, data=json.dumps(creds))
        print(response.status_code)
        if response.status_code == 200:
            self.tree.item(selected,text="",values=(self.dml_website.get(),self.dml_email.get(),self.dml_password.get()))
            self.clean_cred_form()
        else:
            m_box.showerror("error","something went wrong")

    # business logic to delete the user creds
    def delete_data(self):    
        data = {"email":self.email.get(),"password":self.password.get(),"id":self.tree.selection()[0]}
        response = requests.delete(self.BASE_URL+self.ENDPOINT,data=json.dumps(data))
        if response.status_code ==200:
            self.tree.delete(self.tree.selection()[0])
            self.clean_cred_form()
        else:
            m_box.showerror("error","something went wrong")


    # business logic to insert the user creds
    def insert_data(self):
        creds = {"email":self.email.get(),"password":self.password.get(),"cred_user":self.dml_email.get(),"cred_password":self.dml_password.get(),"cred_website":self.dml_website.get()}
        response = requests.post(self.BASE_URL+self.ENDPOINT,data=json.dumps(creds))
        if response.status_code ==200:
            self.pk+=1
            if self.counter %2==0:
                self.tree.insert(parent='',index='end',iid=self.pk,text="",values=(self.dml_website.get(),self.dml_email.get(),self.dml_password.get()),tags=('evenrow'))
            else:
                self.tree.insert(parent='',index='end',iid=self.pk,text="",values=(self.dml_website.get(),self.dml_email.get(),self.dml_password.get()),tags=('oddrow'))
            self.counter+=1     
            self.clean_cred_form()
        else:
            m_box.showerror("error","Failed to insert data")

    def password_generator(self):
        try:
            spin_data  = int(self.spin_box.get())
        except Exception as e:
            m_box.showerror("Not a Number",e)
        else:
            if 0<int(self.spin_box.get())<50:
                if self.lower_alpha.get() and self.upper_alpha.get() and self.special_symbol.get() and self.numeric.get():
                    password =  passgen.get_complex_password(int(self.spin_box.get()))
                
                elif self.lower_alpha.get()and self.upper_alpha.get() and self.special_symbol.get() and not self.numeric.get():
                    password =  passgen.get_alpha_special_password(int(self.spin_box.get()))
                    
                elif self.lower_alpha.get()and self.upper_alpha.get() and not self.special_symbol.get() and self.numeric.get():
                    password =  passgen.get_alphanumeric_password(int(self.spin_box.get()))
                    
                elif  self.lower_alpha.get()and not self.upper_alpha.get() and self.special_symbol.get() and self.numeric.get():
                    password =  passgen.get_lower_alpha_numeric_special_password(int(self.spin_box.get()))
                    
                elif not self.lower_alpha.get()and self.upper_alpha.get() and self.special_symbol.get() and not self.numeric.get():
                    password =  passgen.get_special_upper_password(int(self.spin_box.get()))
                    
                elif self.lower_alpha.get()and self.upper_alpha.get() and not self.special_symbol.get() and not self.numeric.get():
                    password =  passgen.get_alpha_password(int(self.spin_box.get()))
                    
                elif self.lower_alpha.get()and not self.upper_alpha.get() and not self.special_symbol.get() and self.numeric.get():
                    password =  passgen.get_lower_alpha_numeric_password(int(self.spin_box.get()))
                    
                elif not self.lower_alpha.get()and not self.upper_alpha.get() and self.special_symbol.get() and self.numeric.get():
                    password =  passgen.get_special_numeric_password(int(self.spin_box.get()))
                    
                elif not self.lower_alpha.get()and self.upper_alpha.get() and self.special_symbol.get() and not self.numeric.get():
                    password =  passgen.get_special_upper_password(int(self.spin_box.get()))
                    
                elif self.lower_alpha.get()and self.upper_alpha.get() and not self.special_symbol.get() and self.numeric.get():
                    password =  passgen.get_upper_alpha_numeric_password(int(self.spin_box.get()))

                elif self.lower_alpha.get()and not  self.upper_alpha.get() and self.special_symbol.get() and not self.numeric.get():
                    password =  passgen.get_special_lower_password(int(self.spin_box.get()))
                    
                elif not self.lower_alpha.get()and self.upper_alpha.get() and not self.special_symbol.get() and self.numeric.get():
                    password =  passgen.get_upper_alpha_numeric_password(int(self.spin_box.get()))
                    
                elif not self.lower_alpha.get()and not self.upper_alpha.get() and self.special_symbol.get() and not self.numeric.get():
                    password =  passgen.get_special_only_password(int(self.spin_box.get()))
                    
                elif not self.lower_alpha.get()and self.upper_alpha.get() and not self.special_symbol.get() and not self.numeric.get():
                    password =  passgen.get_upper_alpha_password(int(self.spin_box.get()))
                    
                elif self.lower_alpha.get()and not self.upper_alpha.get() and not self.special_symbol.get() and not self.numeric.get():
                    password =  passgen.get_lower_alpha_password(int(self.spin_box.get()))
                    
                elif not self.lower_alpha.get()and not self.upper_alpha.get() and not self.special_symbol.get() and  self.numeric.get():
                    password =  passgen.get_numeric_password(int(self.spin_box.get()))

                self.generated_edit_box.delete(0,tk.END)
                self.generated_edit_box.insert(0,password)


# creating object
obj=PassMan()