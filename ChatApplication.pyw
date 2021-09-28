#from colour import Color
from tkinter import *
from tkinter import font,ttk,Tk,messagebox
from FrameForChatEngine.Chat import Chat
from Windows import setprocessdpi
from PIL import Image,ImageTk
import sys
from os import path
setprocessdpi()

#for light mode
COLOUR_LIGHT_BACKGROUND_1 = "#fff"
COLOUR_LIGHT_BACKGROUND_2 = "#f2f3f5"
COLOUR_LIGHT_BACKGROUND_3 = "#e3e5e8"
COLOUR_BACKGROUND_4="#0013ff"
COLOUR_LIGHT_TEXT = "#aaa"
COLOR_GODARK_BUTTON="#272430"
DCOLOR="#2f2a34"

COLOR_BUTTON_5="#0051ff"
COLOR_BUTTON_6="#5359aa"
COLOUR_BUTTON_NORMAL = "#5fba7d"
COLOUR_BUTTON_ACTIVE = "#58c77c"
COLOUR_BUTTON_PRESSED = "#44e378"

#for dark mode
Dcolors = "#4d495f"
DC="#a26ac7"
DC1="#cf88ff"
DCOLOUR_LIGHT_BACKGROUND_1 = "#272430"
DCOLOUR_LIGHT_BACKGROUND_2 = "#210927"
DCOLOUR_LIGHT_BACKGROUND_3 = "#2d0c34"
DCOLOUR_LIGHT_BACKGROUND_4 = "#5500ff"
DCOLOUR_LIGHT_TEXT1="#ffffff"
DCOLOUR_BACKGROUND_4="#a6942a"
DCOLOUR_LIGHT_TEXT = "#aaa"
DCOLOR_GOLIGHT_BUTTON="#ffffff"
DCOLOUR_GOLIGHT_BUTTON_FOREGROUND="#000000"
#for Entry
COLORBUTTON="#661290"
COLORBUTTONHIGHLIGHT="#aa00ff"

DCOLOR_BUTTON_5="#ffd900"
DCOLOR_BUTTON_6="#d3bc3a"
DCOLOUR_BUTTON_NORMAL = "#a32461"
DCOLOUR_BUTTON_ACTIVE = "#ff0068"
DCOLOUR_BUTTON_PRESSED = "#4d0623"

class ChatApp(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        bundle_dir = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
        self.path1 = path.join(bundle_dir, "../CryptChat/NewChatAssets", "Virgin America.png")
        self.path2 = path.join(bundle_dir, "../CryptChat/NewChatAssets", "Entry.png")
        self.NameImage=Image.open(self.path1).resize((1200,600))
        self.NamePhoto=ImageTk.PhotoImage(self.NameImage)

        self.EntryImage=Image.open(self.path2).resize((150,150))
        self.EntryPhoto=ImageTk.PhotoImage(self.EntryImage)

        self.frames=dict()

        self.title("CHAT ENGINE")
        self.geometry("1200x600")
        self.minsize(800,600)
        self.maxsize(1200,500)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)


        self.ImageLabel=ttk.Label(self,image=self.NamePhoto,borderwidth=0)
        self.ImageLabel.grid(row=0,column=0,sticky="NSEW")

        self.EnterFrame=ttk.Frame(self,style="DMessages.TFrame")
        self.EnterFrame.grid(row=0,column=0,sticky="NSEW",padx=150,pady=80)


        self.EntryImageLabel=ttk.Label(self.EnterFrame,image=self.EntryPhoto,borderwidth=0,style="EnterLabel.TLabel")
        self.EntryImageLabel.grid(row=0,column=0,padx=390,pady=(30,0))

        self.EntryText=ttk.Label(self.EnterFrame,text="ENTER YOUR NAME TO CONTINUE",style="textlabel.TLabel")
        self.EntryText.grid(row=2,column=0,pady=20)

        self.EnterName=Entry(self.EnterFrame,width=20,border=0,bg="#272430",fg="white")
        self.EnterName.config(font=('Century Gothic',17))
        self.EnterName.grid(row=3,column=0,pady=10)

        Frame(self.EnterFrame, width=320, height=3, bg='#141414').place(x=305, y=299)

        self.EnterButton=ttk.Button(self.EnterFrame,text="E  N  T  E  R",padding=(20,5),style="EnterButton.TButton",command=self.EnterCondition)
        self.EnterButton.grid(row=4,column=0,pady=40)

    def EnterCondition(self):
        if self.EnterName.get()=="" or self.EnterName.get().isdigit():
            messagebox.showerror("ENTRY FAILED","        PLEASE ENTER YOUR NAME        ")
        else:
            messagebox.showinfo("ENTRY SUCCESSFULL",f"         W E L C O M E  {self.EnterName.get()}      ")
            self.ChatFrame = Chat(self,self.EnterName.get(), background=COLOUR_LIGHT_BACKGROUND_1, darkstyle=DCOLOUR_LIGHT_BACKGROUND_1,
                                  style="Messages.TFrame")
            self.ChatFrame.grid(row=0, column=0, sticky="NSEW")
root = ChatApp()
ChangeFont=font.nametofont("TkDefaultFont")
style=ttk.Style(root)
style.theme_use("clam")
#for EntryPage
style.configure("EnterButton.TButton", borderwidth=0, background=COLORBUTTON,font=("Segoe UI",14,))
style.map("EnterButton.TButton",background=[("pressed",COLOUR_LIGHT_BACKGROUND_1 ), ("active",COLORBUTTONHIGHLIGHT )],)
style.configure("textlabel.TLabel", background=DCOLOUR_LIGHT_BACKGROUND_1,font=("Century Gothic",15,"bold"))
style.configure("EnterLabel.TLabel", background=DCOLOUR_LIGHT_BACKGROUND_1)
style.configure("EnterFrameMessages.TFrame", background=COLOUR_LIGHT_BACKGROUND_1)
#for light mode
style.configure("Messages.TFrame", background=COLOUR_LIGHT_BACKGROUND_3)
style.configure("Controls.TFrame", background=COLOUR_LIGHT_BACKGROUND_2)
style.configure("SendButton.TButton", borderwidth=0, background=COLOUR_BUTTON_NORMAL,font=("Bodoni",14,"bold"))
style.map("SendButton.TButton",background=[("pressed",COLOUR_BUTTON_ACTIVE ), ("active",COLOUR_BUTTON_PRESSED )],)
style.configure("FetchButton.TButton", background=COLOR_BUTTON_6, borderwidth=0,font=("Bodoni",14,"bold"))
style.map("FetchButton.TButton",background=[("pressed",COLOUR_BACKGROUND_4),("active",COLOR_BUTTON_5)],)
style.configure("Time.TLabel",padding=5,background=COLOUR_LIGHT_BACKGROUND_1,foreground=COLOUR_LIGHT_TEXT,font=8)
style.configure("Avatar.TLabel", background=COLOUR_LIGHT_BACKGROUND_3)
style.configure("Message.TLabel", background=COLOUR_LIGHT_BACKGROUND_2)
style.configure("DGODARK.TButton",background=COLOUR_LIGHT_BACKGROUND_2, borderwidth=0,font=("Century Gothic",14,"bold"))
style.map("DGODARK.TButton",background=[("active",COLOR_GODARK_BUTTON)],foreground=[("active",COLOUR_LIGHT_BACKGROUND_1)])
ChangeFont.configure(family="Bodoni", size=14)
#for dark mode
style.configure("DMessages.TFrame", background=DCOLOUR_LIGHT_BACKGROUND_1)
style.configure("DControls.TFrame", background=DCOLOUR_LIGHT_BACKGROUND_1)
style.configure("DSendButton.TButton", borderwidth=0,background=DCOLOUR_BUTTON_NORMAL,font=("Century Gothic",14,"bold"))
style.map("DSendButton.TButton",background=[("pressed",DCOLOUR_BUTTON_PRESSED ), ("active",DCOLOUR_BUTTON_ACTIVE )],)
style.configure("DFetchButton.TButton", background=DC, borderwidth=0,font=("Century Gothic",14,"bold"))
style.map("DFetchButton.TButton",background=[("pressed",DC),("active",DC1)],)
style.configure("DTime.TLabel",padding=5,background=DCOLOUR_LIGHT_BACKGROUND_1,foreground=DCOLOUR_LIGHT_TEXT1,font=8)
style.configure("DAvatar.TLabel", background=COLOUR_LIGHT_BACKGROUND_3)
style.configure("DMessage.TLabel", background=Dcolors,foreground=DCOLOUR_LIGHT_TEXT1)
style.configure("DGOLIGHT.TButton",background=DCOLOUR_LIGHT_BACKGROUND_1, borderwidth=0,font=("Century Gothic",14,"bold"),foreground=COLOUR_LIGHT_BACKGROUND_2)
style.map("DGOLIGHT.TButton",background=[("active",DCOLOR_GOLIGHT_BUTTON)],foreground=[("active",DCOLOUR_GOLIGHT_BUTTON_FOREGROUND)])

root.mainloop()
