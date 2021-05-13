text = """Greetings! Welcome to the Engine I made with Python! Thank you for using the program.
If I will talk a little bit about the program:
You can name your project with the Project Name section.
-You can color the default earring or the earring you have created.
-You can create multiple projects.

Thank youuuu."""

turkishText = """Selamlar! Python ile yaptığım Motora hoşgeldiniz! Programı kullandığınız için teşekkür ederim.
Programdan biraz bahsedecek olursam: 
-Project Name kısmı ile projene isim verebilirsin.
-Varsayılan küpe veya kendi yarattığın küpe renk verebilirsin.
-Birden çok proje oluşturabilirsin.

Teşekkürlerrrrr."""
from tkinter import * 

class main:
    def __init__(self,title = "About",geometry = "700x500",color = "black"):
        self.title = title
        self.geometry = geometry
        self.color = color
    def mainnn(self):
        self.root = Tk()
        self.root.title(self.title)
        self.root.geometry(self.geometry)
        self.root.configure(bg = self.color)
        #------------------------------------
        self.text = Label(self.root,text = text,bg = "black",fg = "white",font = ("Times New Roman",12))
        self.text.pack()
        self.text.place(x=45,y=0)
        #------------------------------------
        self.cizgi = Label(self.root,text ="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg = "black",fg = "white")
        self.cizgi.pack()
        self.cizgi.place(x = 0,y = 135)
        #-----------------------------------
        self.turkishText = Label(self.root,text = turkishText,bg = "black",fg = "white",font = ("Times New Roman",12))
        self.turkishText.pack()
        self.turkishText.place(x=45,y=155)
        self.root.mainloop()
