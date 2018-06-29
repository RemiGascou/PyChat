from tkinter import * 
from tkinter.messagebox import *
import socket

from threading import Thread

list_commands = ['/name ']
global pseudo
pseudo = """Unnamed"""

global currentstatut
currentstatut = 0

class PyChat:
    def version():
        return "PyChat V.1.2.1"
        
    def credits():
        return "© Rémi GASCOU"

def about():
    about_window = Toplevel()
    about_window.title("About PyChat")
    about_window.geometry("350x120")
    about_window.resizable(width=False, height=False)
    about_window.focus()
    
    label = Label(about_window, text="Version :")
    label.pack()
    label = Label(about_window, text=PyChat.version())
    label.pack()
    label = Label(about_window, text=" ")
    label.pack()
    label = Label(about_window, text="Credits :")
    label.pack()
    label = Label(about_window, text=PyChat.credits())
    label.pack()


def debug_window():
    serverName = """"""
    password = ""
    var_entry_password_checkbutton = 0
    
    def quit_debug_window():
        quit_debug_window.quit()
        quit_debug_window.destroy()
    
    def none():
        return 0
    
    debug_window = Tk()
    debug_window.title("debug_window")
    debug_window.geometry("350x200")
    debug_window.resizable(width=False, height=False)
    debug_window.focus_force()
    
    graphical_debug = LabelFrame(debug_window, text="Graphical debug")
    graphical_debug.pack(fill="both", expand="yes", padx=5, pady=5)
    pseudo_params = LabelFrame(debug_window, text="Deeper debug")
    pseudo_params.pack(fill="both", expand="yes", padx=5, pady=5)

    
    debug_window = Label(graphical_debug, text="Connection statuts")
    debug_window.grid(sticky=E, padx=5, pady=5)
    Button(graphical_debug, text="0", command= lambda: status(0), height = 1, width = 3).grid(row=0, column=1, padx=5, pady=5)
    Button(graphical_debug, text="1", command= lambda: status(1), height = 1, width = 3).grid(row=0, column=2, padx=5, pady=5)
    Button(graphical_debug, text="2", command= lambda: status(2), height = 1, width = 3).grid(row=0, column=3, padx=5, pady=5)
    
    debug_window.mainloop()


def connectToServer_window():
    serverip = """"""
    
    def quit_connectToServer_window():
        global pseudo
        if connectToServer_window_serverip_entry.get() != """""" and isIPAdress(connectToServer_window_serverip_entry.get()):
            port = connectToServer_window_serverport_entry.get()
            if connectToServer_window_serverport_entry.get() == """""":
                port = 12800
            serverip = connectToServer_window_serverip_entry.get()
            if connectToServer_window_clientpseudo_entry.get() != """""":
                oldpseudo = pseudo
                pseudo = connectToServer_window_clientpseudo_entry.get()
                infochangenametext = oldpseudo + " changed name to " + pseudo
                chatbox.configure(state = NORMAL)
                chatbox.insert(INSERT, infochangenametext + "\n", END)
                chatbox.insert(INSERT, "Trying to connect to : " + serverip + " ...\n", END)
                chatbox.configure(state = DISABLED)
                chatbox.pack(padx=5, pady=5)
                pseudoBox.config(text=pseudo)
                pseudoBox.pack(side=LEFT, padx=5, pady=0)
            thread_clientinit = clientinit(serverip,int(port))
            thread_clientinit.start()
            connectToServer_window.quit()
            connectToServer_window.destroy()
        else :
            if connectToServer_window_serverip_entry.get() == """""" or not isIPAdress(connectToServer_window_serverip_entry.get()):
                connectToServer_window_serverip_entry.configure(highlightbackground="red", highlightcolor="red",highlightthickness=1)
            else :
                connectToServer_window_serverip_entry.configure(highlightbackground="red", highlightcolor="red",highlightthickness=0)
                
    def none():
        return 0
        
    def isIPAdress(ip):
        if type(ip) == str and len(ip) < 16:
            liste = ip.split(".")
            check = 0
            for element in liste:
                for subelement in element:
                    if subelement not in ['1','2','3','4','5','6','7','8','9','0']:
                        return False 
                if int(element) >= 0 and int(element) < 256:
                    check = check + 1
            if check == 4:
                return True
            return False 
        return False 

    
    connectToServer_window = Toplevel()
    connectToServer_window.title("Connexion à un serveur")
    connectToServer_window.geometry("350x200")
    connectToServer_window.resizable(width=False, height=False)
    connectToServer_window.focus_force()
    
    co_params = LabelFrame(connectToServer_window, text="Paramètres de connexion")
    co_params.pack(fill="both", expand="yes", padx=5, pady=5)
    pseudo_params = LabelFrame(connectToServer_window, text="Pseudonyme")
    pseudo_params.pack(fill="both", expand="yes", padx=5, pady=5)
    
    
    connectToServer_window_serverip_label = Label(co_params, text="IP du serveur").grid(sticky=E, padx=5, pady=5)
    connectToServer_window_serverip_entry = Entry(co_params, width = 38, borderwidth = 2)
    connectToServer_window_serverip_entry.grid(row=0, column=1)
    connectToServer_window_serverport_label = Label(co_params, text="Port du serveur").grid(sticky=E, padx=5, pady=5)
    connectToServer_window_serverport_entry = Entry(co_params, width = 38, borderwidth = 2)
    connectToServer_window_serverport_entry.grid(row=1, column=1)
    connectToServer_window_serverport_entry.insert(0, 12800)
    
    connectToServer_window_clientpseudo_label = Label(pseudo_params, text="   Pseudonyme")
    connectToServer_window_clientpseudo_label.grid(sticky=E, padx=5, pady=5)
    connectToServer_window_clientpseudo_entry = Entry(pseudo_params, width = 38, borderwidth = 2)
    connectToServer_window_clientpseudo_entry.grid(row=0, column=1)

    connectToServer_window_connectToServer_button = Button(connectToServer_window, text="Connexion au serveur", command=quit_connectToServer_window, height = 1, width = 16)
    connectToServer_window_connectToServer_button.pack(side=RIGHT, padx=5, pady=5, ipadx=2, ipady=2)
    
    connectToServer_window.mainloop()

def createServer_window():
    serverName = """"""
    password = ""
    var_entry_password_checkbutton = 0
    
    def quit_createServer_window():
        if createServer_window_entry_servername_entry.get() != """""":
            if var_entry_password_checkbutton.get() == 1 and createServer_window_entry_password_entry.get() != """""":
                serverName = createServer_window_entry_servername_entry.get()
                password = createServer_window_entry_password_entry.get()
                createServer_window.quit()
                createServer_window.destroy()
            if var_entry_password_checkbutton.get() == 0:
                serverName = createServer_window_entry_servername_entry.get()
                print("serverName =",serverName)
                createServer_window.quit()
                createServer_window.destroy()
        else:
            if createServer_window_entry_servername_entry.get() == """""":
                createServer_window_entry_servername_entry.configure(highlightbackground="red", highlightcolor="red",highlightthickness=1)
            else :
                createServer_window_entry_servername_entry.configure(highlightbackground="red", highlightcolor="red",highlightthickness=0)
            if var_entry_password_checkbutton.get() == 1 and createServer_window_entry_password_entry.get() == """""":
                createServer_window_entry_password_entry.configure(highlightbackground="red", highlightcolor="red",highlightthickness=1)
            else :
                createServer_window_entry_password_entry.configure(highlightbackground="red", highlightcolor="red",highlightthickness=0)
            #contour rouge si vide?
    
    def toggle_password_entry():
        if var_entry_password_checkbutton.get() == 0:
            createServer_window_entry_password_entry.config(state='disabled')
        elif var_entry_password_checkbutton.get() == 1:
            createServer_window_entry_password_entry.config(state='normal')
    
    def none():
        return 0
    
    createServer_window = Tk()
    createServer_window.title("Créer serveur")
    createServer_window.geometry("350x160")
    createServer_window.resizable(width=False, height=False)
    createServer_window.focus()
    
    main_params = LabelFrame(createServer_window, text="Paramètres principaux")
    main_params.pack(fill="both", expand="yes", padx=5, pady=5)
    advanced_params = LabelFrame(createServer_window, text="Paramètres avancés")
    advanced_params.pack(fill="both", expand="yes", padx=5, pady=5)
    
    
    createServer_window_entry_servername_label = Label(main_params, text="Nom du serveur")
    createServer_window_entry_servername_label.pack(side=LEFT, padx=5, pady=5)
    createServer_window_entry_servername_entry = Entry(main_params, width = 30, borderwidth = 2)
    createServer_window_entry_servername_entry.pack(side=RIGHT, padx=5, pady=5)
    
    var_entry_password_checkbutton=IntVar()
    createServer_window_entry_password_checkbutton = Checkbutton(advanced_params, variable=var_entry_password_checkbutton, command=toggle_password_entry ,text="Mot de passe")
    createServer_window_entry_password_checkbutton.pack(side=LEFT, padx=5, pady=5)
    createServer_window_entry_password_entry = Entry(advanced_params, width = 30, borderwidth = 2, state='disabled')
    createServer_window_entry_password_entry.pack(side=RIGHT, padx=5, pady=5)
    
    
    createServer_window_button_createserver = Button(createServer_window, text="Créer serveur", command=quit_createServer_window, height = 1, width = 10)
    createServer_window_button_createserver.pack(side=RIGHT, padx=5, pady=5, ipadx=2, ipady=2)
    
    createServer_window.mainloop()

def quit_window():
    if askyesno(PyChat.version(), 'Êtes-vous sûr de vouloir quitter ?'):
        root.quit()
        root.destroy()
        sys.exit()

def none():
    return 0

def onHitReturn(event):
    global pseudo
    msg = champ_message.get()
    champ_message.delete(0, END)
    if currentstatut == 1 or currentstatut == 2:
        if msg != """""" and not msg.startswith("/"):
            print("You hit return. This message will be sent to server : " + "<" + pseudo + "> " + msg)
            chatbox.configure(state = NORMAL)
            chatbox.insert(INSERT, "<" + pseudo + "> " + msg + "\n", END)
            chatbox.configure(state = DISABLED)
            chatbox.pack(padx=5, pady=5)
    if msg.startswith("""/name """):
        infochangenametext = pseudo + " changed name to " + msg[6:len(msg)]
        chatbox.configure(state = NORMAL)
        chatbox.insert(INSERT, infochangenametext + "\n", END)
        chatbox.configure(state = DISABLED)
        chatbox.pack(padx=5, pady=5)
        champ_message.delete(0, END)
        print(msg[6:len(msg)])
        pseudo = msg[6:len(msg)]
        pseudoBox.config(text=pseudo)
        pseudoBox.pack(side=LEFT, padx=5, pady=0)


def onClickSend():
    global pseudo
    msg = champ_message.get()
    champ_message.delete(0, END)
    if currentstatut == 1 or currentstatut == 2:
        if msg != """""" and not msg.startswith("/"):
            print("You clicked send button. This message will be sent to server : " + msg)
            chatbox.configure(state = NORMAL)
            chatbox.insert(INSERT, "<" + pseudo + "> " + msg + "\n", END)
            chatbox.configure(state = DISABLED)
            chatbox.pack(padx=5, pady=5)
    if msg.startswith("""/name """):
        infochangenametext = pseudo + " changed name to " + msg[6:len(msg)]
        chatbox.configure(state = NORMAL)
        chatbox.insert(INSERT, infochangenametext + "\n", END)
        chatbox.configure(state = DISABLED)
        chatbox.pack(padx=5, pady=5)
        champ_message.delete(0, END)
        print(msg[6:len(msg)])
        pseudo = msg[6:len(msg)]
        pseudoBox.config(text=pseudo)
        pseudoBox.pack(side=LEFT, padx=5, pady=0)

def createMenus():
    #Creation des menus
    menubar = Menu(root)
    
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Connexion à un serveur", command=connectToServer_window)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=quit_window)
    menubar.add_cascade(label="Client", menu=menu1)
    
    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="Créer un serveur", command=createServer_window)
    menubar.add_cascade(label="Serveur", menu=menu2)
    
    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos", command=about)
    menubar.add_cascade(label="Aide", menu=menu3)
    menu3.add_separator()
    menu3.add_command(label="Debug", command=debug_window)
    
    root.config(menu = menubar)
    

def status(n):
    global currentstatut
    if n == 0:
        currentstatut = 0
        statusLight = w.create_rectangle(0, 0, 10, 10, fill="red")
        statutsBox.config(text="Disconnected")
        chatbox.configure(state = NORMAL)
        chatbox.insert(INSERT, pseudo + " has disconnected." + "\n", END)
        chatbox.pack(padx=5, pady=5)
        chatbox.configure(state = DISABLED)
    if n == 1:
        currentstatut = 1
        statusLight = w.create_rectangle(0, 0, 10, 10, fill="lightgreen")
        statutsBox.config(text="Connected")
        chatbox.configure(state = NORMAL)
        chatbox.insert(INSERT, pseudo + " has connected." + "\n", END)
        chatbox.pack(padx=5, pady=5)
        chatbox.configure(state = DISABLED)
    if n == 2:
        currentstatut = 2
        statusLight = w.create_rectangle(0, 0, 10, 10, fill="orange")
        statutsBox.config(text="Serveur")
        chatbox.configure(state = NORMAL)
        chatbox.insert(INSERT, pseudo + " is running a server." + "\n", END)
        chatbox.pack(padx=5, pady=5)
        chatbox.configure(state = DISABLED)

class clientinit(Thread):
    def __init__(self,ip,port): #Constructeur
        Thread.__init__(self)
        self.ip = ip
        self.port = port
    
    def run(self):
        global client

        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.ip, self.port))
            chatbox.configure(state = NORMAL)
            chatbox.insert(INSERT, "Connexion établie avec le serveur sur le port {}" + self.ip + ":" + self.port + "\n", END)
            chatbox.configure(state = DISABLED)
        except (ConnectionRefusedError, OSError) :
            chatbox.configure(state = NORMAL)
            chatbox.insert(INSERT, "Connection refused." + "\n", END)
            chatbox.configure(state = DISABLED)
        except (TimeoutError) :
            chatbox.configure(state = NORMAL)
            chatbox.insert(INSERT, "Connection timed out." + "\n", END)
            chatbox.configure(state = DISABLED)

class clientreceive(Thread):
    def __init__(self): #Constructeur
        Thread.__init__(self)
    
    def run(self):
        while msg_received != "": #Will be used nextly for deconnexion
            msg_received = client.recv(1024)
            chatbox.configure(state = NORMAL)
            chatbox.insert(INSERT, msg_received + "\n", END)
            chatbox.configure(state = DISABLED)
        

def clientsend(Thread):
    def __init__(self): #Constructeur
        Thread.__init__(self)
        self.pseudo = pseudo
    
    def run(self,ip,port = 12800):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        print("Connexion établie avec le serveur sur le port {}".format(port))
        msg = msg.encode()
        client.send(msg)

#Création de la fenetre main
root = Tk()
#root.iconbitmap("pychat") #Not WrKing
root.title(PyChat.version())
root.geometry("450x512")
root.resizable(width=False, height=False)
root.focus_force()

createMenus()


#Initialisation du client

#thread_receivemessages = Thread(target=client.receive())

#Initialisation du serveur


#Creation de la statutsBox and pseudoBox
statusFrame = Frame(root)
statusFrame.pack(fill="both", padx=5, pady=0)
# . . . -Statuts
w = Canvas(statusFrame, width=10, height=10)
w.pack(side=RIGHT, padx=3)
statusLight = w.create_rectangle(0, 0, 10, 10, fill="red")
statutsBox = Label(statusFrame, text="Disconnected", bd =1)
statutsBox.pack(side=RIGHT, padx=5, pady=0)
# . . . -Pseudo
pseudoBox = Label(statusFrame, text=pseudo)
pseudoBox.pack(side=LEFT, padx=5, pady=0)


#Creation de la ChatBox
global chatbox
chatbox = Text(root)
text = "Welcome to PyChat !\nCurrent version : " + PyChat.version() + "\n"
chatbox.insert(INSERT, text + "\n", END)
chatbox.configure(background='lightgrey',height = 28, width = 54, state = DISABLED, bd =1)
chatbox.pack(padx=5, pady=5)

send_message = """ """
champ_message = Entry(root, width=61, textvariable=send_message, bd =2)
champ_message.pack(side = LEFT, padx=7, pady=5)
champ_message.bind('<Return>', onHitReturn)

send_button = Button(root, text="Envoyer", command=onClickSend, height = 1, width = 6)
send_button.pack(side=RIGHT, padx=5, pady=5, ipadx=4, ipady=4)



root.mainloop()