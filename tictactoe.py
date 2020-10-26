from graphics import *

win = GraphWin('Tic-Tac-Toe 2020', 500, 500)
count=0
win.items=[]
win.setBackground('yellow')

def board():

    Title= Text(Point(250, 50), 'LA Lakers Tic-Tac-Toe Game')
    Title.setFill('purple')
    Title.setSize(20)
    Title.setStyle('bold')
    Title.draw(win)
    
    BoardLine = Rectangle(Point(100,100), Point(400,400))
    BoardLine.setFill('yellow')
    BoardLine.setOutline('yellow')
    BoardLine.setWidth(3)
    BoardLine.draw(win)

    BoardPart1 = Line(Point(200, 100), Point(200, 400))
    BoardPart1.setOutline('purple')
    BoardPart1.setWidth(3)
    BoardPart1.draw(win)

    BoardPart2 = Line(Point(300, 100), Point(300, 400))
    BoardPart2.setOutline('purple')
    BoardPart2.setWidth(3)
    BoardPart2.draw(win)

    BoardPart3 = Line(Point(100, 200), Point(400, 200))
    BoardPart3.setOutline('purple')
    BoardPart3.setWidth(3)
    BoardPart3.draw(win)

    BoardPart4 = Line(Point(100, 300), Point(400, 300))
    BoardPart4.setOutline('purple')
    BoardPart4.setWidth(3)
    BoardPart4.draw(win)

    RestartB = Rectangle(Point(100,450), Point(200,475))
    RestartB.setFill('silver')
    RestartB.setOutline('dark blue')
    RestartB.setWidth(1)
    RestartB.draw(win)

    rt = Text(Point(150,463), 'Restart')
    rt.setTextColor('purple')
    rt.setStyle('bold')
    rt.setSize(10)
    rt.draw(win)

    ExitB = Rectangle(Point(300,450), Point(400,475))
    ExitB.setFill('silver')
    ExitB.setOutline('dark blue')
    ExitB.setWidth(1)
    ExitB.draw(win)

    ex = Text(Point(350,463), 'Exit')
    ex.setTextColor('purple')
    ex.setStyle('bold')
    ex.setSize(10)
    ex.draw(win)
    
    displayBoard()


def ListBlock():
    for i in range(9):
        tile = Text(Point(150+(i%3)*100, 150+(i//3)*100), i+1)
        win.items.append(tile)
        
def Guide() :
    txt1 = Text(Point(250, 422), 'Click in one of the nine block')
    txt1.setTextColor('purple')
    txt1.setStyle('bold')
    txt1.setSize(10)
    txt1.draw(win)

def gameEnded():
    txt2 = Text(Point(250, 422), "Game tie, Press Restart to start another")
    txt2.setTextColor('black')
    txt2.setStyle('bold')
    txt2.setSize(10)
    txt2.draw(win)
    afterGame()

def Xwin():
    txt3 = Text(Point(250, 422), "Congratulations 'King James' Won")
    txt3.setTextColor('green')
    txt3.setStyle('bold')
    txt3.setSize(10)
    txt3.draw(win)
    afterGame()

def Owin():
    txt4 = Text(Point(250, 422),  "Congratulations 'The Brow' Won")
    txt4.setTextColor('green')
    txt4.setStyle('bold')
    txt4.setSize(10)
    txt4.draw(win)
    afterGame()

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()
    board()
    

def displayBoard():
    for i in range(9):
        win.items[i].setTextColor('navy')
        win.items[i].setStyle('bold')
        win.items[i].setSize(10)
        win.items[i].draw(win)

def checkWin():
    if (win.items[0].getText()==win.items[1].getText() and win.items[1].getText()==win.items[2].getText()):
        if win.items[0].getText()== 'Lebron James' :
            Xwin()
        elif win.items[0].getText()== 'Anthony Davis' :
            Owin()
        return False
    elif (win.items[3].getText()==win.items[4].getText() and win.items[4].getText()==win.items[5].getText()):
        if win.items[3].getText()== 'Lebron James' :
            Xwin()
        elif win.items[3].getText()== 'Anthony Davis' :
            Owin()
        return False
    elif (win.items[6].getText()==win.items[7].getText() and win.items[7].getText()==win.items[8].getText()):
        if win.items[6].getText()== 'Lebron James' :
            Xwin()
        elif win.items[6].getText()== 'Anthony Davis' :
            Owin()
        return False
    elif (win.items[0].getText()==win.items[3].getText() and win.items[3].getText()==win.items[6].getText()):
        if win.items[0].getText()== 'Lebron James' :
            Xwin()
        elif win.items[0].getText()== 'Anthony Davis' :
            Owin()
        return False
    elif (win.items[1].getText()==win.items[4].getText() and win.items[4].getText()==win.items[7].getText()):
        if win.items[1].getText()== 'Lebron James' :
            Xwin()
        elif win.items[1].getText()== 'Anthony Davis' :
            Owin()
        return False
    elif (win.items[2].getText()==win.items[5].getText() and win.items[5].getText()==win.items[8].getText()):
        if win.items[2].getText()== 'Lebron James' :
            Xwin()
        elif win.items[2].getText()== 'Anthony Davis' :
            Owin()
        return False
    elif (win.items[0].getText()==win.items[4].getText() and win.items[4].getText()==win.items[8].getText()):
        if win.items[0].getText()== 'Lebron James' :
            Xwin()
        elif win.items[0].getText()== 'Anthony Davis' :
            Owin()
        return False
    elif (win.items[2].getText()==win.items[4].getText() and win.items[4].getText()==win.items[6].getText()):
        if win.items[2].getText()== 'Lebron James' :
            Xwin()
        elif win.items[2].getText()== 'Anthony Davis' :
            Owin()
        return False
    else :
        for i in range(9):
            if win.items[i].getText() not in ['Lebron James','Anthony Davis'] :
                return True
        gameEnded()
        return False

def restart ():
    count=0
    for i in range(9):
        win.items[i].setText(str(i+1))
    clear(win)
    Guide()
    MouseEvents()

def WrongChoice():
    txt5 = Text(Point(250, 422), "Wrong Choice")
    txt5.setTextColor('red')
    txt5.setStyle('bold')
    txt5.setSize(10)
    txt5.draw(win)
    

def MouseEvents():
    while (checkWin()):
        p1=win.getMouse()
        if ( (p1.getX()>100 and p1.getX()<400) and (p1.getY()>100 and p1.getY()<400)):
            X=int((p1.getX()-100)//100)
            Y=int((p1.getY()-100)//100)
            global count
            if not (win.items[Y*3+X].getText()=='Lebron James') and not (win.items[Y*3+X].getText()=='Anthony Davis') :
                if count%2==0 :
                    win.items[Y*3+X].setText('Lebron James')
                else :
                    win.items[Y*3+X].setText('Anthony Davis')
                count+=1
                clear(win)
            else :
                invalid_choice()
        elif ((p1.getX()>100 and p1.getX()<200) and (p1.getY()>450 and p1.getY()<475)) :
            restart ()
        elif ((p1.getX()>300 and p1.getX()<400) and (p1.getY()>450 and p1.getY()<475)) :
            win.close()
            raise SystemExit() 
        
def afterGame():
    p1=win.getMouse()
    if ((p1.getX()>100 and p1.getX()<200) and (p1.getY()>450 and p1.getY()<475)) :
            restart ()
    elif ((p1.getX()>300 and p1.getX()<400) and (p1.getY()>450 and p1.getY()<475)) :
            win.close()
            raise SystemExit() 
    else :
        clear(win)
        txt6 = Text(Point(250, 422),  "Press 'Restart' if you wan to play again (or) Press 'Exit'")
        txt6.setTextColor('purple')
        txt6.setStyle('bold')
        txt6.setSize(10)
        txt6.draw(win)
        p1=win.getMouse()
        if ((p1.getX()>100 and p1.getX()<200) and (p1.getY()>450 and p1.getY()<475)) :
            restart ()
        elif ((p1.getX()>300 and p1.getX()<400) and (p1.getY()>450 and p1.getY()<475)) :
            win.close()
            raise SystemExit() 
        else :
            afterGame()


ListBlock()
board()
Guide()
MouseEvents()
