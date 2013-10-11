from graphics import *
from random import *

#Define aesthetic parameters
winw = 600  #window width
winh = 600  #window height
bgcolor = color_rgb(253,222,47)  #background color
txtcolor = color_rgb(138,49,41)  #text color
lincolor = color_rgb(228,135,67)  #board lines' color
xcolor = color_rgb(99,138,221)  #X's color
ocolor = color_rgb(64,202,79)  #O's color
if winh<167:
    txtsize = 5
elif winh>1200:
    txtsize = 36
else:
    txtsize = int(.03*winh)


################################################################################
#Determining players and difficulty
playnum = '0'
diff = 'n'
while not(playnum=='1' or playnum=='2'):
    playnum = input("1 or 2 players? ")
    if not(playnum=='1' or playnum=='2'):
        print("Please respond either 1 or 2")
if playnum=='1':
    while not(diff[0]=='e' or diff[0]=='m' or diff[0]=='h' or diff[0]=='i'):
        print("Computer difficulty")
        diff = input("easy, medium, hard, or impossible? ")
        diff += ' '
        if not(diff[0]=='e' or diff[0]=='m' or diff[0]=='h' or diff[0]=='i'):
            print("I did not understand, try again.")

objects = []
    

#Raise errors for strange dimensions
if winw!=winh:
    print("Board window is not sqare, some elements may appear distorted.")
if winw<200 or winh<200:
    print("Board window too small, some features may not appear properly.")

#Set up display
board = GraphWin("Tic-Tac-Toe", winw, winh)
board.setBackground(bgcolor)

#Draw board lines
line = Line(Point(.375*winw,.125*winh),Point(.375*winw,.875*winh))
line.setWidth(3)
line.setFill(lincolor)
line.draw(board)

line = Line(Point(.625*winw,.125*winh),Point(.625*winw,.875*winh))
line.setWidth(3)
line.setFill(lincolor)
line.draw(board)

line = Line(Point(.125*winw,.375*winh),Point(.875*winw,.375*winh))
line.setWidth(3)
line.setFill(lincolor)
line.draw(board)

line = Line(Point(.125*winw,.625*winh),Point(.875*winw,.625*winh))
line.setWidth(3)
line.setFill(lincolor)
line.draw(board)



#Checkwin- checks to see if char has three in a row in array
def checkwin(array,char):
    for i in range(3):
        if array[0][i]==array[1][i]==array[2][i]==char:
            return True
        if array[i][0]==array[i][1]==array[i][2]==char:
            return True
    if array[0][0]==array[1][1]==array[2][2]==char:
        return True
    if array[0][2]==array[1][1]==array[2][0]==char:
        return True
    return False

#Checkfull- checks to see if all the spaces in array have been filled
def checkfull(array):
    for a in range(3):
        for b in range(3):
            if array[a][b]=='E':
                return False
    return True

#Playerturn- draws on board and edits array for a human placing char in a position
def playerturn(array,char,window):
    clickx = 0
    clicky = 0
    taken = False
    while not(.125*winw<=clickx and clickx<=.875*winw and .125*winh<=clicky and clicky<=.875*winh) or taken==True:
        taken = False
        click = window.getMouse()
        clickx = click.getX()
        clicky = click.getY()
        for x in range(3):
            if .125*winw+.25*winw*x<=clickx and clickx<=.375*winw+.25*winw*x:
                break
        for y in range(3):
            if .125*winh+.25*winh*y<=clicky and clicky<=.375*winh+.25*winh*y:
                break
        if array[y][x]!='E':
            taken = True
            
    array[y][x] = char
    
    if char=='X':
        x1 = Line(Point(.15*winw+.25*winw*x,.15*winh+.25*winh*y),Point(.35*winw+.25*winw*x,.35*winh+.25*winh*y))
        x1.setWidth(2)
        x1.setFill(xcolor)
        x2 = Line(Point(.35*winw+.25*winw*x,.15*winh+.25*winh*y),Point(.15*winw+.25*winw*x,.35*winh+.25*winh*y))
        x2.setWidth(2)
        x2.setFill(xcolor)
        x1.draw(window)
        x2.draw(window)
        objects.append(x1)
        objects.append(x2)
    if char=='O':
        if winw<=winh:
            o = Circle(Point(.25*winw+.25*winw*x,.25*winh+.25*winh*y),.1*winw)
        else:
            o = Circle(Point(.25*winw+.25*winw*x,.25*winh+.25*winh*y),.1*winh)
        o.setWidth(2)
        o.setOutline(ocolor)
        o.draw(window)
        objects.append(o)
            

#Computerturn- draws on board and edits array for AI placing char in a position
def computerturn(array,char,window,full,winner,turn):
    openspaces = []
    for a in range(3):
        for b in range(3):
            if array[a][b]=='E':
                openspaces.append([a,b])

    x = -1
    y = -1

    #Medium computer checks for winning plays and blocks
    if diff[0]!='e' and x==-1 and y==-1:
        for space in openspaces:
            array[space[0]][space[1]] = 'O'
            good = checkwin(array,'O')
            array[space[0]][space[1]] = 'E'
            if good==True:
                y = space[0]
                x = space[1]

    if diff[0]!='e' and x==-1 and y==-1:
        for space in openspaces:
            array[space[0]][space[1]] = 'X'
            good = checkwin(array,'X')
            array[space[0]][space[1]] = 'E'
            if good==True:
                y = space[0]
                x = space[1]

    #Impossible computer runs on these statements
    if diff[0]=='i':
        if array[1][1]=='E':
            y = 1
            x = 1
        elif turn==1:
            remove = True
            while remove==True:
                for i in range(len(openspaces)):
                    if openspaces[i][0]==1 or openspaces[i][1]==1:
                        openspaces.pop(i)
                        break
                else:
                    remove = False

        if turn==2:
            if array[0][1]=='X':
                side = 1
            elif array[1][0]=='X':
                side = 2
            elif array[1][2]=='X':
                side = 3
            elif array[2][1]=='X':
                side = 4
            else:
                side = 0
            if side==0 and array[1][1]=='O':
                remove = True
                while remove==True:
                    for i in range(len(openspaces)):
                        if (openspaces[i][0]+openspaces[i][1])%2==0:
                            openspaces.pop(i)
                            break
                    else:
                        remove = False
            else:
                remove = True
                while remove==True:
                    for i in range(len(openspaces)):
                        if openspaces[i][0]==1 or openspaces[i][1]==1:
                            openspaces.pop(i)
                            break
                    else:
                        remove = False
                if side==1:
                    remove = True
                    while remove==True:
                        for i in range(len(openspaces)):
                            if openspaces[i][0]==2:
                                openspaces.pop(i)
                                break
                        else:
                            remove = False
                if side==2:
                    remove = True
                    while remove==True:
                        for i in range(len(openspaces)):
                            if openspaces[i][1]==2:
                                openspaces.pop(i)
                                break
                        else:
                            remove = False
                if side==3:
                    remove = True
                    while remove==True:
                        for i in range(len(openspaces)):
                            if openspaces[i][1]==0:
                                openspaces.pop(i)
                                break
                        else:
                            remove = False
                if side==4:
                    remove = True
                    while remove==True:
                        for i in range(len(openspaces)):
                            if openspaces[i][0]==0:
                                openspaces.pop(i)
                                break
                        else:
                            remove = False
                
                    
    
    #Easy computer just plays randomly
    if x==-1 and y==-1:
        rplay = choice(openspaces)
        y = rplay[0]
        x = rplay[1]

    array[y][x] = char

    if char=='X':
        x1 = Line(Point(.15*winw+.25*winw*x,.15*winh+.25*winh*y),Point(.35*winw+.25*winw*x,.35*winh+.25*winh*y))
        x1.setWidth(2)
        x1.setFill(xcolor)
        x2 = Line(Point(.35*winw+.25*winw*x,.15*winh+.25*winh*y),Point(.15*winw+.25*winw*x,.35*winh+.25*winh*y))
        x2.setWidth(2)
        x2.setFill(xcolor)
        x1.draw(window)
        x2.draw(window)
        objects.append(x1)
        objects.append(x2)
    if char=='O':
        if winw<=winh:
            o = Circle(Point(.25*winw+.25*winw*x,.25*winh+.25*winh*y),.1*winw)
        else:
            o = Circle(Point(.25*winw+.25*winw*x,.25*winh+.25*winh*y),.1*winh)
        o.setWidth(2)
        o.setOutline(ocolor)
        o.draw(window)
        objects.append(o)



#Gameplay loop
cx = winw
cy = winh
startup = True
starttext = Text(Point(.5*winw,.05*winh),"Click on a space to start")
starttext.setSize(txtsize)
starttext.setFill(txtcolor)
starttext.draw(board)
while cx>=.1*winw or cy>=.1*winh:
    if startup==False:
        for obj in objects:
            obj.undraw()
        objects = []
    winner = "Nobody"
    fullboard = False
    gameboard = [['E','E','E'],
                 ['E','E','E'],
                 ['E','E','E']]
    turn = 1
    while winner=="Nobody" and fullboard==False:
        playerturn(gameboard,'X',board)
        if startup==True:
            starttext.undraw()
            startup = False
        if checkwin(gameboard,'X')==True:
            winner = "X"
        fullboard = checkfull(gameboard)
        if playnum=='1' and fullboard==False and winner=="Nobody":
            computerturn(gameboard,'O',board,fullboard,winner,turn)
        if playnum=='2' and fullboard==False and winner=="Nobody":
            playerturn(gameboard,'O',board)
        if checkwin(gameboard,'O')==True:
            winner = "O"
        fullboard = checkfull(gameboard)
        turn += 1

    wintext = Text(Point(.5*winw,.95*winh-.6*txtsize),winner+" wins!")
    wintext.setSize(txtsize)
    wintext.setFill(txtcolor)
    endtext = Text(Point(.5*winw,.95*winh+.6*txtsize),"Click to clear the board and start a new game")
    endtext.setSize(txtsize)
    endtext.setFill(txtcolor)
    wintext.draw(board)
    endtext.draw(board)
    objects.append(wintext)
    objects.append(endtext)

    box = Rectangle(Point(0,0),Point(.1*winw,.1*winh))
    box.setFill(lincolor)
    box.setOutline(lincolor)
    quittext = Text(Point(.05*winw,.05*winh),"Quit")
    quittext.setSize(txtsize)
    quittext.setFill(txtcolor)
    box.draw(board)
    quittext.draw(board)
    objects.append(box)
    objects.append(quittext)
    
    c = board.getMouse()
    cx = c.getX()
    cy = c.getY()
    
board.close()
