# School Version

# จัดทำโดย
# นายกันตวิชญ์ ฤทธาเกริกไกล ม.4/1 เลขที่ 1
# นายวุฒิภัทร กันชนะ ม.4/1 เลขที่ 3
# นายภูมิรพี ยาวิชัย ม.4/1 เลขที่ 6


try: #python 2
    from Tkinter import *
    from Tkinter.messagebox import *
    from Tkinter.colorchooser import *

except: #python 3
    from tkinter import *
    from tkinter.messagebox import *
    from tkinter.colorchooser import *

#startup theme
try:
    startupTheme = open("StartupTheme.txt","r",encoding="utf-8")
    Theme = int(startupTheme.read(1))

    startupTheme.close()
except:
    startupTheme = open("StartupTheme.txt","w",encoding="utf-8")
    startupTheme.write("0")

    startupTheme = open("StartupTheme.txt","r",encoding="utf-8")
    Theme = int(startupTheme.read(1))

    startupTheme.close()

#app
app = Tk()
app.title("Calculator Pro Max 2.0 Ultra Beta")
app.geometry("+200+100")
app.resizable(width=False, height=False)
#app.iconbitmap("calculator.ico")

#exit
def closeApp():
    try:custom.destroy()
    except:pass

    try:showaf.destroy()
    except:pass

    try:showvf.destroy()
    except:pass

    app.destroy()

#theme def
def lightTheme():
    setLightTheme = open("StartupTheme.txt","w",encoding="utf-8")
    setLightTheme.writelines("0")
    setLightTheme.close()

    try:custom.destroy()
    except:pass

    clnumber = "#ebebeb"
    clsymbol = "#dfdfdf"
    clequal = "#148fff"

    app.configure(bg="white")

    displayScreen.config(fg="black",bg="white")
    resultScreen.config(fg="black",bg="white")

    bt7.config(fg="black",bg=clnumber)
    bt8.config(fg="black",bg=clnumber)
    bt9.config(fg="black",bg=clnumber)
    btdevide.config(fg="black",bg=clsymbol)

    bt4.config(fg="black",bg=clnumber)
    bt5.config(fg="black",bg=clnumber)
    bt6.config(fg="black",bg=clnumber)
    bttimes.config(fg="black",bg=clsymbol)

    bt1.config(fg="black",bg=clnumber)
    bt2.config(fg="black",bg=clnumber)
    bt3.config(fg="black",bg=clnumber)
    btminus.config(fg="black",bg=clsymbol)

    btback.config(fg="red",bg=clnumber)
    bt0.config(fg="black",bg=clnumber)
    btdel.config(fg="red",bg=clnumber)
    btplus.config(fg="black",bg=clsymbol)

    btbracketopen.config(fg="black",bg=clsymbol)
    btbracketclose.config(fg="black",bg=clsymbol)
    btdot.config(fg="black",bg=clsymbol)
    btequal.config(fg="black",bg=clequal)

def darkTheme():         
    setDarkTheme = open("StartupTheme.txt","w",encoding="utf-8")
    setDarkTheme.writelines("1")
    setDarkTheme.close()

    try:custom.destroy()
    except:pass
            
    cldisplay = "#3c3c3c"
    clnumber = "#2d2d2d"
    clsymbol = "#232323"
    clequal = "#0073dc"
    
    app.configure(bg="#3c3c3c")

    displayScreen.config(fg="white",bg=cldisplay)
    resultScreen.config(fg="white",bg=cldisplay)

    bt7.config(fg="white",bg=clnumber)
    bt8.config(fg="white",bg=clnumber)
    bt9.config(fg="white",bg=clnumber)
    btdevide.config(fg="white",bg=clsymbol)

    bt4.config(fg="white",bg=clnumber)
    bt5.config(fg="white",bg=clnumber)
    bt6.config(fg="white",bg=clnumber)
    bttimes.config(fg="white",bg=clsymbol)

    bt1.config(fg="white",bg=clnumber)
    bt2.config(fg="white",bg=clnumber)
    bt3.config(fg="white",bg=clnumber)
    btminus.config(fg="white",bg=clsymbol)

    btback.config(fg="red",bg=clnumber)
    bt0.config(fg="white",bg=clnumber)
    btdel.config(fg="red",bg=clnumber)
    btplus.config(fg="white",bg=clsymbol)

    btbracketopen.config(fg="white",bg=clsymbol)
    btbracketclose.config(fg="white",bg=clsymbol)
    btdot.config(fg="white",bg=clsymbol)
    btequal.config(fg="white",bg=clequal)

def setBgColor():
    global line
    global displayScreen,resultScreen,bt7,bt8,bt9,btdevide,bt4,bt5,bt6,bttimes,bt1,bt2,bt3,btminus,btdot,bt0,btdel,btplus,btbracketopen,btbracketclose,btequal,btback
    
    startupTheme = open("StartupTheme.txt","w",encoding="utf-8")
    startupTheme.writelines("2")
    startupTheme.close()

    try:
        customThemeData = open("CustomThemeData.txt","r",encoding="utf-8")
        customThemeData.close()
    except:
        customThemeData = open("CustomThemeData.txt","w",encoding="utf-8")
        for line in range(30):
            customThemeData.write("#ffffff\n")
        customThemeData.close()

        setBgColor()

    try:
        displayScreen.config(fg="black")
        resultScreen.config(fg="black")

        bt7.config(fg="black")
        bt8.config(fg="black")
        bt9.config(fg="black")
        btdevide.config(fg="black")

        bt4.config(fg="black")
        bt5.config(fg="black")
        bt6.config(fg="black")
        bttimes.config(fg="black")

        bt1.config(fg="black")
        bt2.config(fg="black")
        bt3.config(fg="black")
        btminus.config(fg="black")

        btback.config(fg="red")
        bt0.config(fg="black")
        btdel.config(fg="red")
        btplus.config(fg="black")

        btbracketopen.config(fg="black")
        btbracketclose.config(fg="black")
        btdot.config(fg="black")
        btequal.config(fg="black")

        for x in range(0,28):
            readline = open("CustomThemeData.txt", "r",encoding="utf-8")
            
            try:
                getColor = readline.readlines()[x]
                Color = getColor[0:7]
            except:
                pass

            try:
                if x == 0:
                    app.configure(bg=Color)
                    displayScreen.configure(bg=Color)
                    resultScreen.configure(bg=Color)
                elif x == 2:
                    bt0.configure(bg=Color)
                elif x == 3:
                    bt1.configure(bg=Color)
                elif x == 4:
                    bt2.configure(bg=Color)
                elif x == 5:
                    bt3.configure(bg=Color)
                elif x == 6:
                    bt4.configure(bg=Color)
                elif x == 7:
                    bt5.configure(bg=Color)
                elif x == 8:
                    bt6.configure(bg=Color)
                elif x == 9:
                    bt7.configure(bg=Color)
                elif x == 10:
                    bt8.configure(bg=Color)
                elif x == 11:
                    bt9.configure(bg=Color)
                elif x == 13:
                    btplus.configure(bg=Color)
                elif x == 14:
                    btminus.configure(bg=Color)
                elif x == 15:
                    bttimes.configure(bg=Color)
                elif x == 16:
                    btdevide.configure(bg=Color)
                elif x == 18:
                    btbracketopen.configure(bg=Color)
                elif x == 19:
                    btbracketclose.configure(bg=Color)
                elif x == 20:
                    btdot.configure(bg=Color)
                elif x == 22:
                    btdel.configure(bg=Color)
                elif x == 23:
                    btback.configure(bg=Color)
                elif x == 25:
                    btequal.config(bg=Color)
                readline.close()
            except:
                pass
    except:
        pass

def customTheme():
    global custom

    custom = Tk()
    custom.title("Custom Theme Setting")
    custom.geometry("+800+100")
    custom.resizable(width=False, height=False)
    #custom.iconbitmap("calculator.ico")

    startupTheme = open("StartupTheme.txt","w",encoding="utf-8")
    startupTheme.writelines("2")
    startupTheme.close()

    try:
        customThemeData = open("CustomThemeData.txt","r",encoding="utf-8")
        customThemeData.close()
    except:
        customThemeData = open("CustomThemeData.txt","w",encoding="utf-8")
        for i in range(30):
            customThemeData.write("#ffffff\n")
        customThemeData.close()

        setBgColor()

    def chooseBgColor(cbtn):
        global line

        ccolor = askcolor()

        try:
            if cbtn == "display":
                line = 0

            elif cbtn == 0:
                line = 2
            elif cbtn == 1:
                line = 3
            elif cbtn == 2:
                line = 4
            elif cbtn == 3:
                line = 5
            elif cbtn == 4:
                line = 6
            elif cbtn == 5:
                line = 7
            elif cbtn == 6:
                line = 8
            elif cbtn == 7:
                line = 9
            elif cbtn == 8:
                line = 10
            elif cbtn == 9:
                line = 11

            elif cbtn == "+":
                line = 13
            elif cbtn == "-":
                line = 14
            elif cbtn == "x":
                line = 15
            elif cbtn == "÷":
                line = 16

            elif cbtn == "(":
                line = 18
            elif cbtn == ")":
                line = 19
            elif cbtn == ".":
                line = 20

            elif cbtn == "C":
                line = 22
            elif cbtn == "⌫":
                line = 23

            elif cbtn == "=":
                line = 25
        except:
            pass

        with open("CustomThemeData.txt","r",encoding="utf-8") as file:
            data = file.readlines()

        data[line] = ccolor[1]+"\n"

        with open("CustomThemeData.txt","w",encoding="utf-8") as file:
            file.writelines(data)

            file.close()

        setBgColor()

    def customThemeFile():
        import subprocess
        subprocess.call("notepad CustomThemeData.txt")

    def setDefault():
        import os

        ask = askquestion("Warning","Your saved data will be deleted and replace with default value, do you want to continue?")
        if ask == "yes":
            os.remove("CustomThemeData.txt")

            customThemeData = open("CustomThemeData.txt","w",encoding="utf-8")
            for line in range(30):
                customThemeData.write("#ffffff\n")
            customThemeData.close()

            setBgColor()

    cMenu = Menu(custom)
    custom.config(menu=cMenu)
    cMenu.add_command(label="Edit File",command=customThemeFile)
    cMenu.add_command(label="Reload File",command=setBgColor)
    cMenu.add_command(label="Set Default",command=setDefault)

    #screen
    cdisplayScreen = Button(custom,font=('arial',20),borderwidth=0,text="Display Screen",command=lambda:chooseBgColor("display"))
    cdisplayScreen.grid(row=0,column=0,rowspan=2,columnspan=4,sticky=E)

    #button
    #row2
    cbt7 = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="7",command=lambda:chooseBgColor(7),padx=30,pady=10)
    cbt8 = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="8",command=lambda:chooseBgColor(8),padx=30,pady=10)
    cbt9 = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="9",command=lambda:chooseBgColor(9),padx=32,pady=10)

    cbtdevide = Button(custom,font=('arial',30),borderwidth=0,text="÷",command=lambda:chooseBgColor("÷"),padx=33,pady=11)

    #row3
    cbt4 = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="4",command=lambda:chooseBgColor(4),padx=30,pady=10)
    cbt5 = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="5",command=lambda:chooseBgColor(5),padx=30,pady=10)
    cbt6 = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="6",command=lambda:chooseBgColor(6),padx=32,pady=10)

    cbttimes = Button(custom,font=('arial',30),borderwidth=0,text="x",command=lambda:chooseBgColor("x"),padx=35,pady=11)

    #row4
    cbt1 = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="1",command=lambda:chooseBgColor(1),padx=30,pady=10)
    cbt2 = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="2",command=lambda:chooseBgColor(2),padx=30,pady=10)
    cbt3 = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="3",command=lambda:chooseBgColor(3),padx=32,pady=10)

    cbtminus = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="-",command=lambda:chooseBgColor("-"),padx=37,pady=10)

    #row5
    cbtdel = Button(custom,font=('arial',25,'bold'),borderwidth=0,text="C",command=lambda:chooseBgColor("C"),padx=32,pady=19)

    cbt0 = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="0",command=lambda:chooseBgColor(0),padx=30,pady=12)

    cbtback = Button(custom,font=('arial',23,'bold'),borderwidth=0,text="⌫",command=lambda:chooseBgColor("⌫"),padx=26,pady=21)
    cbtplus = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="+",command=lambda:chooseBgColor("+"),padx=32,pady=12)

    #row6
    cbtbracketopen = Button(custom,font=('arial',30),borderwidth=0,text="(",command=lambda:chooseBgColor("("),padx=35,pady=11)
    cbtbracketclose = Button(custom,font=('arial',30),borderwidth=0,text=")",command=lambda:chooseBgColor(")"),padx=35,pady=11)
    cbtdot = Button(custom,font=('arial',30),borderwidth=0,text=".",command=lambda:chooseBgColor("."),padx=38,pady=11)
    cbtequal = Button(custom,font=('arial',30,'bold'),borderwidth=0,text="=",command=lambda:chooseBgColor("="),padx=32,pady=10)

    #set button position
    cbt7.grid(row=2,column=0,sticky=W)
    cbt8.grid(row=2,column=1,sticky=W)
    cbt9.grid(row=2,column=2,sticky=W)
    cbtdevide.grid(row=2,column=3,sticky=W)

    cbt4.grid(row=3,column=0,sticky=W)
    cbt5.grid(row=3,column=1,sticky=W)
    cbt6.grid(row=3,column=2,sticky=W)
    cbttimes.grid(row=3,column=3,sticky=W)

    cbt1.grid(row=4,column=0,sticky=W)
    cbt2.grid(row=4,column=1,sticky=W)
    cbt3.grid(row=4,column=2,sticky=W)
    cbtminus.grid(row=4,column=3,sticky=W)

    cbtdel.grid(row=5,column=0,sticky=W)
    cbt0.grid(row=5,column=1,sticky=W)
    cbtback.grid(row=5,column=2,sticky=W)
    cbtplus.grid(row=5,column=3,sticky=W)

    cbtbracketopen.grid(row=6,column=0,sticky=W)
    cbtbracketclose.grid(row=6,column=1,sticky=W)
    cbtdot.grid(row=6,column=2,sticky=W)
    cbtequal.grid(row=6,column=3,sticky=W)

    custom.mainloop()

def checkCustomWindow():
    global custom

    try:
        custom.state()
        setBgColor()
        #showerror("Cannot Open Window","You already open Custom Theme Setting's window.")
        return
    except:
        setBgColor()
        customTheme()

#menu def
def about():
    showinfo("About","จัดทำโดย\nนายกันตวิชญ์ ฤทธาเกริกไกล ม.4/1 เลขที่ 1\nนายวุฒิภัทร กันชนะ ม.4/1 เลขที่ 3\nนายภูมิรพี ยาวิชัย ม.4/1 เลขที่ 6")

#menu item
#option
option = Menu(app,tearoff=0)
option.add_command(label="About",command=about)
option.add_command(label="Exit",command=closeApp)

#theme
theme = Menu(app,tearoff=0)
theme.add_command(label="Light",command=lightTheme)
theme.add_command(label="Dark",command=darkTheme)
theme.add_separator()

csub = Menu(theme, tearoff=0)
csub.add_command(label="Apply",command=setBgColor)
csub.add_command(label="Edit",command=checkCustomWindow)

theme.add_cascade(label="Custom",command=checkCustomWindow,menu=csub)

def showFormulaArea():
    global showaf
    showaf = Tk()
    showaf.title("Area Formula")
    showaf.geometry("450x250+800+100")
    showaf.resizable(width=False,height=False)

    Label(showaf,text="Area of ...",font=('Arial',30)).grid(row=0,column=0,sticky=W)
    Label(showaf,text="\nSquare (สี่เหลี่ยมจัตุรัส)",font=('Arial',15)).grid(row=1,column=0,sticky=W)
    Label(showaf,text="Rectangle (สี่เหลี่ยมผืนผ้า)",font=('Arial',15)).grid(row=2,column=0,sticky=W)
    Label(showaf,text="Triangle (สามเหลี่ยม)",font=('Arial',15)).grid(row=3,column=0,sticky=W)
    Label(showaf,text="Circle (วงกลม)",font=('Arial',15)).grid(row=4,column=0,sticky=W)

    Label(showaf,text="\n= Side x Side",font=('Arial',15)).grid(row=1,column=1,sticky=W)
    Label(showaf,text="= Width x Length",font=('Arial',15)).grid(row=2,column=1,sticky=W)
    Label(showaf,text="= 1/2 x Base x Height",font=('Arial',15)).grid(row=3,column=1,sticky=W)
    Label(showaf,text="= πr²",font=('Arial',15)).grid(row=4,column=1,sticky=W)

    showaf.mainloop()

def showFormulaVolume():
    global showvf
    showvf = Tk()
    showvf.title("Volume Formula")
    showvf.geometry("450x250+800+100")
    showvf.resizable(width=False,height=False)

    Label(showvf,text="Volume of ...",font=('Arial',30)).grid(row=0,column=0,sticky=W)
    Label(showvf,text="\nCube (ลูกบาศก์)",font=('Arial',15)).grid(row=1,column=0,sticky=W)
    Label(showvf,text="Prism (ปริซึม)",font=('Arial',15)).grid(row=2,column=0,sticky=W)
    Label(showvf,text="Cylinder (ทรงกระบอก)",font=('Arial',15)).grid(row=3,column=0,sticky=W)
    Label(showvf,text="Cone (ทรงกรวย)",font=('Arial',15)).grid(row=4,column=0,sticky=W)
    Label(showvf,text="Pyramid (พีรามิด)",font=('Arial',15)).grid(row=5,column=0,sticky=W)

    Label(showvf,text="\n= Side x Side x Side",font=('Arial',15)).grid(row=1,column=1,sticky=W)
    Label(showvf,text="= Base Area x Height",font=('Arial',15)).grid(row=2,column=1,sticky=W)
    Label(showvf,text="= πr²h",font=('Arial',15)).grid(row=3,column=1,sticky=W)
    Label(showvf,text="= (1/3)πr²h",font=('Arial',15)).grid(row=4,column=1,sticky=W)
    Label(showvf,text="= (1/3)(Base Area)h",font=('Arial',15)).grid(row=5,column=1,sticky=W)

    showvf.mainloop()

#formula
formula = Menu(app,tearoff=0)
formula.add_command(label="Area",command=showFormulaArea)
formula.add_command(label="Volume",command=showFormulaVolume)

#menu
appMenu = Menu(app)
app.config(menu=appMenu)

appMenu.add_cascade(label="Option",menu=option)
appMenu.add_cascade(label="Theme",menu=theme)
appMenu.add_cascade(label="Formula",menu=formula)

#calculation
content = ""
txtInput = StringVar()

txtOutput = StringVar(value="0")

#calculation def
def btnInput(number):
    global content

    if len(content) >= 65:
        txtOutput.set("Max Characters Limit")
    else:
        content += str(number)
        txtInput.set(content)

    displayTextSize()

def equal():
    global content
    global result

    if content != "":
        calculate = content

        calculate = calculate.replace("x","*")
        calculate = calculate.replace("÷","/")

        try:
            result = float(eval(calculate))

            displayTextSize()
            txtOutput.set(result)
        except ZeroDivisionError:
            txtOutput.set("Cannot divide by zero")
        except:
            txtOutput.set("Error")

def backspace():
    global content

    content = content[:-1]

    txtInput.set(content)
    displayTextSize()

def clear():
    global content
    global calculate
    global result

    content = ""
    calculate = ""
    result = 0.0
    txtInput.set("")
    txtOutput.set("0")
    displayTextSize()

#text size
def displayTextSize():
    global content
    global calculate
    global result

    #display
    if len(content) >= 0 and len(content) < 30:
        displayScreen.config(font=('arial',20))

    elif len(content) >= 30 and len(content) < 41:
        displayScreen.config(font=('arial',15))

    elif len(content) >= 41 and len(content) < 65:
        displayScreen.config(font=('arial',10))

    #result
    try:
        if len(str(result)) >= 0 and len(str(result)) < 15:
            resultScreen.config(font=('arial',35))

        elif len(str(result)) >= 15 and len(str(result)) < 30:
            resultScreen.config(font=('arial',25))
    except:
        pass

#display screen
displayScreen = Label(app,font=('arial',20),height=1,borderwidth=0,textvariable=txtInput)
displayScreen.grid(row=0,column=0,columnspan=4,sticky=E)

#result screen
resultScreen = Label(app,font=('arial',35),height=1,borderwidth=0,textvariable=txtOutput)
resultScreen.grid(row=1,column=0,columnspan=4,sticky=E)

#button
#row2
bt7 = Button(app,font=('arial',30,'bold'),borderwidth=0,text="7",command=lambda:btnInput(7),padx=30,pady=10)
bt8 = Button(app,font=('arial',30,'bold'),borderwidth=0,text="8",command=lambda:btnInput(8),padx=30,pady=10)
bt9 = Button(app,font=('arial',30,'bold'),borderwidth=0,text="9",command=lambda:btnInput(9),padx=32,pady=10)

btdevide = Button(app,font=('arial',30),borderwidth=0,text="÷",command=lambda:btnInput("÷"),padx=33,pady=11)

#row3
bt4 = Button(app,font=('arial',30,'bold'),borderwidth=0,text="4",command=lambda:btnInput(4),padx=30,pady=10)
bt5 = Button(app,font=('arial',30,'bold'),borderwidth=0,text="5",command=lambda:btnInput(5),padx=30,pady=10)
bt6 = Button(app,font=('arial',30,'bold'),borderwidth=0,text="6",command=lambda:btnInput(6),padx=32,pady=10)

bttimes = Button(app,font=('arial',30),borderwidth=0,text="x",command=lambda:btnInput("x"),padx=35,pady=11)

#row4
bt1 = Button(app,font=('arial',30,'bold'),borderwidth=0,text="1",command=lambda:btnInput(1),padx=30,pady=10)
bt2 = Button(app,font=('arial',30,'bold'),borderwidth=0,text="2",command=lambda:btnInput(2),padx=30,pady=10)
bt3 = Button(app,font=('arial',30,'bold'),borderwidth=0,text="3",command=lambda:btnInput(3),padx=32,pady=10)

btminus = Button(app,font=('arial',30,'bold'),borderwidth=0,text="-",command=lambda:btnInput("-"),padx=37,pady=10)

#row5
btdel = Button(app,font=('arial',25,'bold'),borderwidth=0,text="C",command=clear,padx=32,pady=19)

bt0 = Button(app,font=('arial',30,'bold'),borderwidth=0,text="0",command=lambda:btnInput(0),padx=30,pady=12)

btback = Button(app,font=('arial',23,'bold'),borderwidth=0,text="⌫",command=backspace,padx=26,pady=21)
btplus = Button(app,font=('arial',30,'bold'),borderwidth=0,text="+",command=lambda:btnInput("+"),padx=32,pady=12)

#row6
btbracketopen = Button(app,font=('arial',30),borderwidth=0,text="(",command=lambda:btnInput("("),padx=35,pady=11)
btbracketclose = Button(app,font=('arial',30),borderwidth=0,text=")",command=lambda:btnInput(")"),padx=35,pady=11)
btdot = Button(app,font=('arial',30),borderwidth=0,text=".",command=lambda:btnInput("."),padx=38,pady=11)
btequal = Button(app,font=('arial',30,'bold'),borderwidth=0,text="=",command=equal,padx=32,pady=10)

#set theme

if Theme == 0:
    lightTheme()
if Theme == 1:
    darkTheme()
if Theme == 2:
    setBgColor()
    

#set button position
bt7.grid(row=2,column=0,sticky=W)
bt8.grid(row=2,column=1,sticky=W)
bt9.grid(row=2,column=2,sticky=W)
btdevide.grid(row=2,column=3,sticky=W)

bt4.grid(row=3,column=0,sticky=W)
bt5.grid(row=3,column=1,sticky=W)
bt6.grid(row=3,column=2,sticky=W)
bttimes.grid(row=3,column=3,sticky=W)

bt1.grid(row=4,column=0,sticky=W)
bt2.grid(row=4,column=1,sticky=W)
bt3.grid(row=4,column=2,sticky=W)
btminus.grid(row=4,column=3,sticky=W)

btdel.grid(row=5,column=0,sticky=W)
bt0.grid(row=5,column=1,sticky=W)
btback.grid(row=5,column=2,sticky=W)
btplus.grid(row=5,column=3,sticky=W)

btbracketopen.grid(row=6,column=0,sticky=W)
btbracketclose.grid(row=6,column=1,sticky=W)
btdot.grid(row=6,column=2,sticky=W)
btequal.grid(row=6,column=3,sticky=W)

#run app
app.mainloop()
