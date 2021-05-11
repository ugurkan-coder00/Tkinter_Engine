from tkinter import *
from tkinter import ttk
import random
bruh = ('snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
        'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
        'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
        'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
        'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
        'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
        'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
        'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
        'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
        'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
        'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
        'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
        'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
        'indian red', 'saddle brown', 'sandy brown',
        'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
        'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
        'pale violet red', 'maroon', 'medium violet red', 'violet red',
        'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
        'thistle', 'snow2', 'snow3',
        'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
        'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
        'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
        'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
        'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
        'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
        'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
        'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
        'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
        'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
        'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
        'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
        'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
        'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
        'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
        'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
        'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
        'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
        'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
        'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
        'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
        'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
        'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
        'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
        'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
        'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
        'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
        'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
        'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
        'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
        'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
        'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
        'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
        'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
        'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
        'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
        'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
        'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
        'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
        'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
        'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
        'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
        'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
        'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
        'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
        'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
        'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
        'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
        'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
        'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
        'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
        'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
        'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
        'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
        'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
        'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
        'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99')

rand = random.randint(1,437)
rand2 = random.randint(1,461)

class main:
    def __init__(self,title = "Engine",geometry = "700x500",rootColor = "black",defaultColor = "red",defaultName = "",createColor = "black"):
        self.title = title
        self.geometry = geometry
        self.rootColor = rootColor
        self.defaultColor = defaultColor
        self.defaultName = defaultName
        self.createColor = createColor
    def root(self):
        self.root = Tk()
        self.root.title(self.title)
        self.root.geometry(self.geometry)
        self.root.configure(bg = self.rootColor)
    def Cube(self):
        self.kup = Label(self.root,bg = self.defaultColor)
        self.kup.pack()
        self.kup.place(height = 40,width = 40)
    #Command
    def SaveCommand(self):
        if self.box.get() == "" or self.box.get() == " ":
            self.kup.configure(text = "",bg = self.defaultColor,font = ("Times New Roman",10,"bold"))
        else:
            self.kup.configure(text = "",bg = self.box.get(),font = ("Times New Roman",10,"bold"))
        self.label = Label(self.root,text=self.nameEntry.get(),bg = "black",fg = "white",font = ("Times New Roman",13,"bold"))
        self.label.pack()
        self.label.place(x = 212,y = 0)
    def xx(self,_=None):
        self.kup.place(x=self.Xayar.get(),y=self.Yayar.get())
    def yy(self,_=None):
        self.kup.place(x=self.Xayar.get(),y=self.Yayar.get())
    #EndCommand
    def name(self):
        self.nameText = Label(self.root,text = "Project Name:",bg = "gray8",fg = "white",font = ("Times New Roman",10,"bold"))
        self.nameText.pack()
        self.nameText.place(x = 525,y = 2)
        self.nameEntry = Entry(self.root,bg = "gray8",fg = "yellow",font = ("Times New Roman",9,"bold"))
        self.nameEntry.pack()
        self.nameEntry.place(x = 525,y = 20)
    def color(self):
        self.boxText = Label(self.root,text = "Color the cube:",bg = "gray8",fg = "white",font = ("Times New Roman",10,"bold"))
        self.boxText.pack()
        self.boxText.place(x=525,y=42)
        n = StringVar()
        self.box = ttk.Combobox(self.root, width = 27, textvariable = n)
        self.box['values'] = (bruh)
        self.box.pack()
        self.box.place(x=525,y=60,width = 126)
    def panel(self):
        self.panell = Label(self.root,bg = "gray8")
        self.panell.pack()
        self.panell.place(x = 475,y =0,height = 500,width = 225)
    def X(self):
        self.Xayar = Scale(self.root,from_=0.0, to=437.0,resolution=1.0,length = 111,fg="white", bg="black",orient = "horizontal",command = self.xx)
        self.Xayar.pack()
        self.Xayar.place(x=525,y=100,height = 38,width = 126)
        self.XayarText = Label(self.root,text = "X",bg = "gray8",fg = "white",font = ("Times New Roman",9))
        self.XayarText.pack()
        self.XayarText.place(x=580,y=82)
    def Y(self):
        self.Yayar = Scale(self.root,from_=0.0, to=461.0,resolution=1.0,length = 111,fg="white", bg="black",orient = "horizontal",command = self.yy)
        self.Yayar.pack()
        self.Yayar.place(x=525,y=160,height = 38,width = 126)
        self.YayarText = Label(self.root,text = "Y",bg = "gray8",fg = "white",font = ("Times New Roman",9))
        self.YayarText.pack()
        self.YayarText.place(x=580,y=142)
    def SaveButton(self):
        self.save = Button(self.root,text = "SAVE",bg = "black",fg = "white",font = ("Times New Roman",9),command = self.SaveCommand)
        self.save.pack()
        self.save.place(x = 558,y = 210)
    def cizgi(self):
        self.cizgii = Label(self.root,bg = "gray8",fg = "white",text = "-------------------------------------------------------")
        self.cizgii.pack()
        self.cizgii.place(x=475,y=240)
    def menuBar(self):
        self.bar = Menu(self.root,bg = "black",fg = "white")
        self.file = Menu(self.bar,tearoff = False,bg = "red")
        self.edit = Menu(self.bar,tearoff = False,bg = "red")
        self.file.add_command(label="Exit",command = self.root.quit)
        self.edit.add_command(label="Create",command = self.CreateMain)
        self.edit.add_command(label="Close",command = self.CreateClosing)
        self.bar.add_cascade(label="File",menu=self.file)
        self.bar.add_cascade(label="Edit",menu=self.edit)
        self.root.config(menu=self.bar)
    #Create Partition
    def CreateCommandButton(self):
        self.kup2.configure(bg = self.box2.get())
        self.kup2.pack()
        self.kup2.place(x = rand,y = rand2,height = 40,width = 40)
    def CreateCommandScaleX(self,_=None):
        self.kup2.place(x = self.Xayar2.get(),y = self.Yayar2.get())
    def CreateCommandScaleY(self,_=None):
        self.kup2.place(x = self.Xayar2.get(),y = self.Yayar2.get())
    #-----------------------------------------
    def CreateMain(self):
        self.kup2 = Label(self.root,bg = self.createColor)
        #-----------------------------------------
        self.partitionName = Label(self.root,text = "Create",bg = "gray8",fg = "white",font = ("Times New Roman",13,"bold"))
        self.partitionName.pack()
        self.partitionName.place(x = 561,y = 252)
        #-----------------------------------------
        self.boxText2 = Label(self.root,text = "Color the cube:",bg = "gray8",fg = "white",font = ("Times New Roman",10,"bold"))
        self.boxText2.pack()
        self.boxText2.place(x=525,y=278)
        n2 = StringVar()
        self.box2 = ttk.Combobox(self.root, width = 27, textvariable = n2)
        self.box2['values'] = (bruh)
        self.box2.pack()
        self.box2.place(x=525,y=298,width = 126)
        #-----------------------------------------
        self.Xayar2 = Scale(self.root,from_=0.0, to=437.0,resolution=1.0,length = 111,fg="white", bg="black",orient = "horizontal",command = self.CreateCommandScaleX)
        self.Xayar2.set(rand)
        self.Xayar2.pack()
        self.Xayar2.place(x=525,y=338,height = 38,width = 126)
        self.XayarText2 = Label(self.root,text = "X",bg = "gray8",fg = "white",font = ("Times New Roman",9))
        self.XayarText2.pack()
        self.XayarText2.place(x=580,y=320)
        #-----------------------------------------
        self.Yayar2 = Scale(self.root,from_=0.0, to=461.0,resolution=1.0,length = 111,fg="white", bg="black",orient = "horizontal",command = self.CreateCommandScaleY)
        self.Yayar2.set(rand2)
        self.Yayar2.pack()
        self.Yayar2.place(x=525,y=398,height = 38,width = 126)
        self.YayarText2 = Label(self.root,text = "Y",bg = "gray8",fg = "white",font = ("Times New Roman",9))
        self.YayarText2.pack()
        self.YayarText2.place(x=580,y=380)
        #-----------------------------------------
        self.save2 = Button(self.root,text = "CREATE",bg = "black",fg = "white",font = ("Times New Roman",9),command = self.CreateCommandButton)
        self.save2.pack()
        self.save2.place(x = 552,y = 460)
    def CreateClosing(self):
        self.partitionName.destroy()
        self.box2.destroy()
        self.boxText2.destroy()
        self.Xayar2.destroy()
        self.XayarText2.destroy()
        self.Yayar2.destroy()
        self.YayarText2.destroy()
        self.save2.destroy()
    #End Partition
    def mainloop(self):
        self.mainloop = mainloop()
 
classs = main()
classs.root()
classs.Cube()
classs.panel()
classs.color()
classs.name()
classs.X()
classs.Y()
classs.cizgi()
classs.menuBar()
classs.SaveButton()
classs.mainloop()
