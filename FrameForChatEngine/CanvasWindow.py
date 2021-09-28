import sys
from os import path
import tkinter as Tk
from tkinter import ttk,StringVar
import datetime
from PIL import Image, ImageTk

max_width=800
Switch=0
class Canvas(Tk.Canvas):
    def __init__(self, controller,Cipher ,*args, **kwargs):
        super().__init__(controller, *args, **kwargs, highlightthickness=0)

        self.controller=controller
        self.cipher=Cipher
        self.ChangeModeButtonText=StringVar(value="G o  D a r k")
        self.bundle_dir=getattr(sys,"_MEIPASS",path.abspath(path.dirname(__file__)))
        self.path_to_item=path.join(self.bundle_dir,"ChatAssets","Message.png")
        self.path_to_item2=path.join(self.bundle_dir,"ChatAssets","ChatAvatar.png")
        self.MessageImage = Image.open(self.path_to_item).resize((1800, 40))
        self.MessagePhoto = ImageTk.PhotoImage(self.MessageImage)


        self.message_frame = ttk.Frame(self,style="Messages.TFrame")
        self.message_frame.columnconfigure(0, weight=1)
        self.ChangeModeButton = ttk.Button(controller.Button_Container, textvariable=self.ChangeModeButtonText, command=self.show_DarkMode
                                           , padding=(15, 7), cursor="hand2", style="DGODARK.TButton")
        self.ChangeModeButton.pack(pady=(6, 0))
        self.scrollable_window = self.create_window((0, 0), window=self.message_frame, anchor="nw")

        def configure_scrollable_window_width_for_not_moving_in_x_axis(event):  # if anything wants to get bound we put an event
            self.itemconfig(self.scrollable_window,width=self.winfo_width())  # as self.scrollable_window is not a tk widget its an id

        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))

        self.bind("<Configure>", configure_scrollable_window_width_for_not_moving_in_x_axis)
        self.message_frame.bind("<Configure>", configure_scroll_region)

        scrollbar = ttk.Scrollbar(controller, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")
        self['yscrollcommand']=scrollbar.set                                   #self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)       # move to the bottom of the scrollable area,contents stay on the screen when you open it
        #self.on_Scroll_again()

    def on_Scroll_again(self):
        self.bind_all("<MouseWheel>", self.on_Scroll)

    def on_Scroll(self, event):
        self.yview_scroll(-int(event.delta / 120), "units")

    def update_message_widgets(self, messages, message_labels,En):
        existing_labels = [(self.getencryptedmessages, time["text"]) for message, time in message_labels]
        for message in messages:
            self.message_time = datetime.datetime.fromtimestamp(message["date"]).strftime("%d-%m-%Y %H:%M:%S")
            self.getencryptedmessages = message['message']
            self.replaceditem1 = self.getencryptedmessages
            print(self.replaceditem1)
            if("'" in self.replaceditem1):
                self.replaceitem2 = self.replaceditem1.replace("'", '')[1:]
                print(self.replaceitem2)
                self.decoded = self.replaceitem2.encode('iso-8859-15')
                print(self.decoded)
                if self.decoded == En:
                    self.D = self.cipher.decrypt(self.decoded)
                    self.Decrypted_Message = self.D.decode()
                    self.strDecryptedMessage = str(self.Decrypted_Message)
                    #print(self.DDD)

                    if (self.strDecryptedMessage, self.message_time) not in existing_labels:
                        self._create_message_container(self.strDecryptedMessage, self.message_time, message_labels)
                else:
                    if (self.getencryptedmessages, self.message_time) not in existing_labels:
                        self._create_message_container(self.getencryptedmessages, self.message_time, message_labels)


    def _create_message_container(self, message_content, message_time, message_labels):
        self.container = ttk.Frame(self.message_frame,style="Messages.TFrame")
        self.container.grid(sticky="EW", padx=(10, 50), pady=10)
        self.container.columnconfigure(1, weight=1)


        def reconfigure_message_label(event):
            for label,tt in message_labels:
                label.configure(wraplength=min(self.container.winfo_width()-100,max_width))
                tt['wraplength']=min(self.container.winfo_width()-100,max_width)

        self.container.bind("<Configure>", reconfigure_message_label)

        self._create_message_bubble(self.container, message_content, message_time, message_labels)

    def _create_message_bubble(self, container, message_content, message_time, message_labels):
        avatar_image = Image.open(self.path_to_item2).resize((60,60))
        avatar_photo = ImageTk.PhotoImage(avatar_image)
        image_label = ttk.Label(container, image=avatar_photo,style="Avatar.TLabel")
        image_label.grid(row=0, column=0, rowspan=2, sticky="NEW", padx=(0, 10), pady=(5, 0))
        image_label.image = avatar_photo
        self.time_label = ttk.Label(container, text=message_time,style="Time.TLabel")
        self.time_label.grid(row=0, column=1, sticky="NEW")
        self.message_label2 = ttk.Label(container, text=message_content, anchor="w", justify="left", wraplength=900,style="Message.TLabel")
        self.message_label2.grid(row=1, column=1, sticky="NSEW")
        message_labels.append((self.message_label2, self.time_label))


    def show_DarkMode(self):
        self.controller.configure(style="DMessages.TFrame")
        self.controller.Button_Container.configure(style="DControls.TFrame")
        self.configure(background=self.controller.darkstyle)
        self.controller.message_input.configure(bg="#272430", fg="#ffffff", highlightcolor="#4000ff")
        self.message_frame.configure(style="DMessages.TFrame")
        self.controller.Send_Button.configure(style="DSendButton.TButton")
        self.controller.Fetch_Button.configure(style="DFetchButton.TButton")
        self.message_label2.configure(relief="raised", style="DMessage.TLabel", borderwidth=0, padding=5)
        self.time_label.configure(image=self.MessagePhoto, compound="center", style="DTime.TLabel",
                                  relief="raised",
                                  borderwidth=0, padding=(0, 1))
        self.container.configure(style="DMessages.TFrame")
        def changemessage(event):
            for i, j in self.controller.message_labels:
                i.configure(relief="raised", style="DMessage.TLabel", borderwidth=0, padding=5)
                j.configure(image=self.MessagePhoto, compound="center", style="DTime.TLabel", relief="raised",
                            borderwidth=0, padding=(0, 1))

            for k in self.message_frame.winfo_children():
                k.configure(style="DMessages.TFrame")
        self.container.bind_all("<Configure>", changemessage)          #bind to configure forever and change whole setting beforhand
        self.ChangeModeButton.configure(style="DGOLIGHT.TButton")
        self.ChangeModeButtonText.set(value="G o  L i g h t")
        self.ChangeModeButton.configure(command=self.Show_Light)
        self.yview_moveto(1.0)

    def Show_Light(self):
        self.controller.configure(style="Messages.TFrame")
        self.controller.Button_Container.configure(style="Controls.TFrame")
        self.configure(background=self.controller.background)
        self.controller.message_input.configure(bg="#ffffff", fg="#000000", highlightcolor="#51ff00")
        self.message_frame.configure(style="Messages.TFrame")
        self.controller.Send_Button.configure(style="SendButton.TButton")
        self.controller.Fetch_Button.configure(style="FetchButton.TButton")
        self.message_label2.configure(relief="raised", style="Message.TLabel", borderwidth=0, padding=5)
        self.time_label.configure(image='', style="Time.TLabel", padding=9)
        self.container.configure(style="Messages.TFrame")
        def changemessage(event):
            for i, j in self.controller.message_labels:
                i.configure(relief="raised", style="Message.TLabel", borderwidth=0, padding=5)
                j.configure(image='', style="Time.TLabel", padding=9)
            for k in self.message_frame.winfo_children():
                k.configure(style="Messages.TFrame")
        self.container.bind_all("<Configure>", changemessage)
        self.ChangeModeButton.configure(style="DGODARK.TButton")
        self.ChangeModeButtonText.set(value="G o  D a r k")
        self.ChangeModeButton.configure(command=self.show_DarkMode)
        self.yview_moveto(1.0)





