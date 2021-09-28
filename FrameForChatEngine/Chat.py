import tkinter as tk
from tkinter import ttk
import requests
from FrameForChatEngine.CanvasWindow import Canvas
from cryptography.fernet import Fernet

#Symmetric CryptoGraphy
KEY=Fernet.generate_key()
#fkey = open('FILE_KEY.txt', 'wb')
#fkey.write(KEY)
with open('FILE_KEY.txt', 'rb') as fkey:
    KEY = fkey.read()
class Chat(ttk.Frame):
    def __init__(self ,Container,User_Name, background, darkstyle, **kwargs):
        super().__init__(Container, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.Get_User_Name=User_Name

        self.messages = [{"message": f"Hey There {self.Get_User_Name} ! Welcome to Shantanu's Chat Engine . Start A Chat!", "date":1620323455.620137 }]

        self.message_labels= []

        self.darkstyle=darkstyle
        self.background=background

        self.Button_Container = ttk.Frame(self, padding=10, style="Controls.TFrame")
        self.Button_Container.grid(row=1, column=0, sticky="EW")

        self.message_input = tk.Text(self.Button_Container, height=5, width=1, highlightcolor="#51ff00",
                                     relief="sunken", highlightthickness=1, font=("Segoe UI", 10, "bold"))
        self.message_input.pack(fill="both", side="left", expand=True, padx=(0, 10))

        #self.key = Fernet.generate_key()
        global KEY
        global fkey

        self.cipher = Fernet(KEY)
        self.Fetch_Button = ttk.Button(self.Button_Container, text="Fetch", command=self.get_messages, padding=(15, 7),
                                       style="FetchButton.TButton", cursor="hand2")
        self.Send_Button = ttk.Button(self.Button_Container, text="Send", command=self.post_messages, padding=(15, 7),
                                      style="SendButton.TButton", cursor="hand2")

        self.Send_Button.pack(pady=(0, 6))
        self.Fetch_Button.pack(pady=(5, 5))

        self.message_input.bind("<Return>", self.post_messages)
        self.message_input.bind("<KP_Enter>", self.post_messages)

        self.message_window = Canvas(self,self.cipher,background=background)  # tk widgets do not have a style
        self.message_window.grid(row=0, column=0, sticky="NSEW", pady=5)
        self.Encrypted_M=bytes
        self.message_window.update_message_widgets(self.messages, self.message_labels,self.Encrypted_M)
    def post_messages(self, *args):
        self.getmessages = self.message_input.get("1.0", "end").strip().encode('iso-8859-15')
        # print(self.getmessages)
        self.Encrypted_M=self.cipher.encrypt(self.getmessages)
        #print(self.Encrypted_Message)
        body = str(self.Encrypted_M)
        requests.post("http://167.99.63.70/message", json={"message": body})
        self.message_input.delete("1.0", "end")
        self.get_messages()
    def get_messages(self):
        self.messages = requests.get("http://167.99.63.70/messages").json()
        self.message_window.update_message_widgets(self.messages,self.message_labels,self.Encrypted_M)
        self.message_window.on_Scroll_again()
        self.after(50, lambda: self.message_window.yview_moveto(1.0))



