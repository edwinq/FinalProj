###
### Life
###
from Tkinter import *

def mousePressed(event):
    redrawAll()

def keyPressed(event):
    redrawAll()

def timerFired():
    redrawAll()
    delay = 250 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again

def drawPiece():
    image = PhotoImage(file = "dogmascot.ppm")
    canvas.create_image(10, 10, image = image, anchor = NW)

    pass
    #w = Label(canvas, image=photo)
    #w.photo = photo
    #w.pack()

def drawGame():
    canvas.create_image(0,0,image = canvas.data.background, anchor = 'nw')
    drawPiece()
    pass

def redrawAll():
    canvas.delete(ALL)
    canvas.create_image(canvas.data.imageLocation, image = canvas.data.image, anchor = NW)
    drawGame()

def init():
    canvas.data.image = PhotoImage(file = "dogmascot.ppm")
    canvas.data.background = PhotoImage(file = "template.ppm")
    canvas.data.imageLocation=(500,500)
    pass

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    canvas = Canvas(root,width=1000, height=800)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init()
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    redrawAll()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()


