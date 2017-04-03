import threading
from Tkinter import *
import tkMessageBox
import socket
import time
import os


class InformationOfUsers:
    login = None
    password = None
    friend_login = None


class Provider:
    s = None
    s_to_message = None
    server_address = None
    server_address2 = None
    top = None
    text = None
    message = None


class MainWindow(Provider):
    def __init__(self):
        #socket connection
        Provider.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Provider.s_to_message = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 11000)
        self.server_address2 = ('localhost', 11001)

        self.s_to_message.connect(self.server_address2)
        self.s.connect(self.server_address)

        #MainWindow
        Provider.top = Tk()
        self.top.title("Gadu Gadu")
        self.top.geometry('{}x{}'.format(300, 500))

        self.password = StringVar()
        self.login = StringVar()

        L1 = Label(self.top, text="Login")
        L1.place(relx=0.29, rely=0.33)
        E1 = Entry(self.top, textvariable=self.login)
        E1.place(relx=0.29, rely=0.37)

        L2 = Label(self.top, text="Password")
        L2.place(relx=0.29, rely=0.41)
        E2 = Entry(self.top, show="*", textvariable=self.password)
        E2.place(relx=0.29, rely=0.45)

        B = Button(self.top, bd=1, text="Log in", command=self.log_in, width=7)
        B2 = Button(self.top, bd=1, text="Register", command=self.register, width=7)

        B.place(relx=0.29, rely=0.5)
        B2.place(relx=0.51, rely=0.5)

        self.top.mainloop()

    def log_in(self):
        self.s.send("log " + self.login.get() + " " + self.password.get())

        if self.s.recv(1024) == "Login successful":
            InformationOfUsers.login = self.login.get()
            InformationOfUsers.password = self.password.get()

            self.top.destroy()
            AfterLoginWindow()
        else:
            tkMessageBox.showinfo("Login", "Wrong login or password")

    def register(self):
        self.s.send("register " + self.login.get() + " " + self.password.get())

        if self.s.recv(1024) == "Registration successful":
            tkMessageBox.showinfo("Registration", "Registration successful")
            print "account register"
            print self.password.get()
            print self.login.get()
        else:
            tkMessageBox.showinfo("Registration", "This login is unavailable")


class AfterLoginWindow(Provider):
    def __init__(self):
        self.top = Tk()
        self.top.title("Gadu Gadu" + " - " + InformationOfUsers.login)
        self.top.geometry('{}x{}'.format(300, 500))
        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)

        menubar = Menu(self.top)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Logout", command=self.logout)
        filemenu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Online", command=lambda: self.status("Online"))
        editmenu.add_command(label="Away", command=lambda: self.status("Away"))
        editmenu.add_command(label="Invisible", command=lambda: self.status("Invisible"))
        editmenu.add_command(label="Offline", command=lambda: self.status("Offline"))
        menubar.add_cascade(label="Status", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Set Description", command=self.set_description)
        menubar.add_cascade(label="Description", menu=helpmenu)

        self.top.config(menu=menubar)

        self.search_name = StringVar(self.top)
        E1 = Entry(self.top, textvariable=self.search_name)
        E1.place(relx=0.04, rely=0.02, width=200)

        B = Button(self.top, bd=1, text="Search", command=self.search, width=8)
        B.place(relx=0.75, rely=0.0147)

        #friends = self.show_friends

        print_friends = PrintFriends(self.top, self.show_friends, self.chat)
        print_friends.start()

        #self.top.mainloop()

    def on_closing(self):
        if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
            self.s.send("status " + "Offline")
            os._exit(1)

    def status(self, status):
        if status == "Offline":
            self.s.send("status " + status)
            self.top.destroy()
            MainWindow()
        else:
            self.s.send("status " + status)

    def logout(self):
        self.s.send("status " + "Offline")
        self.top.destroy()
        MainWindow()

    def exit(self):
        self.s.send("status " + "Offline")
        self.top.destroy()

    def chat(self, friend):
        chat_window = Toplevel(self.top)
        chat_window.title(friend)
        chat_window.geometry('{}x{}'.format(500, 300))
        chat_window.protocol("WM_DELETE_WINDOW", lambda: self.chat_closingg(chat_window))

        InformationOfUsers.friend_login = friend

        scrollbar = Scrollbar(chat_window)
        scrollbar.pack(side=RIGHT, fill=Y)

        text = Text(chat_window, width=65, height=15, wrap=WORD, yscrollcommand=scrollbar.set)
        text.config(state=DISABLED)
        text.pack()

        self.receive = ReceiveMessage(chat_window, text, self.top)
        self.receive.start()

        scrollbar.config(command=text.yview)

        message = StringVar(chat_window)
        E3 = Entry(chat_window, bd=2, width=79, textvariable=message)
        E3.place(relx=0, rely=0.80)

        B = Button(chat_window, bd=1, text="Send", command=lambda: self.just_do_it(text, message), width=10)
        B.place(relx=0.78, rely=0.89)

    def chat_closingg(self, chat_window):
        self.receive.stop()
        chat_window.destroy()

    def just_do_it(self, text, message):
        message = message.get()

        text.config(state=NORMAL)
        text.insert(END, InformationOfUsers.login + ":\n" + message + "\n\n")
        text.config(state=DISABLED)
        text.pack()

        self.s.send("send " + InformationOfUsers.friend_login + " " + InformationOfUsers.login + " " + message)

    def search(self):
        self.s.send("search " + self.search_name.get())

        if self.s.recv(1024) == "Search successful":
            result = tkMessageBox.askquestion("Search", "Search successful, do you want to add to friends this person?")

            if result == "yes":
                self.s.send("add " + self.search_name.get())

                if self.s.recv(1024) == "You are already friends with him":
                    tkMessageBox.showinfo("Search", "You are already friends with " + self.search_name.get())
                else:
                    pass#print_friends = PrintFriends(self.top, self.show_friends, self.chat)
                    #print_friends.start()
            else:
                pass
        else:
            tkMessageBox.showinfo("Search", "There are no person of this name")

    def show_friends(self):
        self.s.send("show")
        data = ""

        while True:
            data += self.s.recv(1024)
            if data[-5:] == "<EOF>":
                break
            else:
                continue

        if data[-6] == " ":
            data = data[:-6]
        else:
            data = data[:-5]

        if data == "There are no friends of you":
            return
        else:
            return data

    def set_description(self):
        enter_description_window = Toplevel(self.top)
        enter_description_window.geometry('{}x{}'.format(230, 100))
        enter_description_window.title("Set Description")

        value = StringVar(enter_description_window)

        ent = Entry(enter_description_window, textvariable=value)
        ent.place(relx=0.06, rely=0.25, width=200)

        B = Button(enter_description_window, bd=1, text="Set", command=lambda: self.set(value.get(), enter_description_window), width=8)
        B.place(relx=0.35, rely=0.55)

    def set(self, value, window):
        self.s.send("set " + value)
        window.destroy()


class ReceiveMessage(threading.Thread, Provider):
    def __init__(self, chat_window, text, main_window):
        threading.Thread.__init__(self)
        self._stop = threading.Event()
        self.chat_window = chat_window
        self.text = text
        self.main_window = main_window

    def run(self):
        while not self.stopped():
            message = self.s_to_message.recv(1024)

            self.text.config(state=NORMAL)
            self.text.insert(INSERT, InformationOfUsers.friend_login + ":\n" + message + "\n")
            self.text.config(state=DISABLED)
            self.text.pack()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()


class PrintFriends(threading.Thread):
    def __init__(self, window, friends, chat):
        threading.Thread.__init__(self)
        self.stop = False
        self.window = window
        self.friends = friends
        self.chat = chat

    def run(self):
        while True:
            all_friends = self.friends()

            if all_friends:
                all_friends = all_friends.split(" ' ")
            else:
                time.sleep(1)
                continue

            buttons = []

            for friend in all_friends:
                button_name = friend
                buttons.append(Button(self.window, bd=1, justify=LEFT, text=button_name,
                                      command=lambda name=friend.split(" ")[1]: self.chat(name), width=38))

            y = 0.14

            for i in buttons:
                i.place(relx=0.04, rely=y)
                y += 0.07

            time.sleep(1)


MainWindow()
