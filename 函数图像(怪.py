import tkinter as tk
import turtle as tur
import math

title = "画布"
width = 1000
height = 600

center = [width/2,height/2]

window =  tk.Tk()
controlpanel = tk.Tk()

window.title( title )
window.geometry( str(width) + "x" + str(height) )
controlpanel.title("控制台")
controlpanel.geometry("205x65")
brush = tk.Canvas( window , width = width , height = height , bg = "#CCCC99" , confine = True )
brush.pack()

def createcroods():
    brush.create_line( 0 , height//2 , width , height//2 , width=3 , fill="#000000" , tag="axis" )
    brush.create_line( width//2 , 0 , width//2 , height  , width=3 , fill="#000000" , tag="axis" )

def showgrid(space=20):
    for i in range(0,width//2,space):
        brush.create_line( width//2-i , 0 , width//2-i  , height , width=1 , fill="#708090" , tag="grid" )
        brush.create_line( width//2+i , 0 , width//2+i  , height , width=1 , fill="#708090" , tag="grid" )
    for i in range(0,height//2,space):
        brush.create_line( 0 , height//2-i , width , height//2-i , width=1 , fill="#708090" , tag="grid" )
        brush.create_line( 0 , height//2+i , width , height//2+i , width=1 , fill="#708090" , tag="grid" )
    createcroods()

def hidegrid():
    brush.delete("grid")

def drawfunc(expression="y=x"):
    fixedexpression = expression[2:]
    for i in range(width):
        x = i-width//2
        y = eval(fixedexpression)
        brush.create_oval( x+width//2 , height//2-y , x+width//2 , height//2-y , width=1 , tag="func")

def getndraw():
    expression = inputbox.get()
    drawfunc(expression)

def reset():
    brush.delete("func")
    

createcroods()
e = tk.StringVar(controlpanel)
inputbox = tk.Entry( controlpanel , width=27 , textvariable=e )
e.set("y=3.14*x**2")
inputbox.place(x=5,y=5,anchor="nw")
startbutton = tk.Button( controlpanel , width=12 , height=1 , text="绘制" , command=getndraw )
resetbutton = tk.Button( controlpanel , width=12 , height=1 , text="重置" , command=reset )
startbutton.place( x=5 , y=30 ,anchor="nw")
resetbutton.place( x=105 , y=30 ,anchor="nw")

controlpanel.mainloop()
window.mainloop()


