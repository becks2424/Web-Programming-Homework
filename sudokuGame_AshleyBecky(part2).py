#Sudoku Game: Ashley & Becky
# https://docs.python.org/3/library/tkinter.html
# http://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
#click then fill in squares
from pygame import *
from graphics import *
import graphics
import tkinter

win = graphics.GraphWin("Sudoku", 800, 800)

#image
##yellowJ = Image(Point(750,50),"GracelandYellowjacketsLogo.png")

#base square
rect = Rectangle(Point(50,50),Point(500,500))
rect.setWidth(4)
rect.setFill('white')
rect.draw(win)

#hint box
rect2 = Rectangle(Point(575,100),Point(700,150))
rect2.draw(win)
rect2.setFill('white')
wordHint = Text(Point(637.5,125),"Hint")
wordHint.draw(win)

#drawIn box
rect3 = Rectangle(Point(575, 175),Point(700,225))
rect3.draw(win)
rect3.setFill('white')
drawIn = Text(Point(637.5,200),"Write In")
drawIn.draw(win)

#numbers
one = Text(Point(50,600),"1")
one.draw(win)
one.setStyle("bold")
one.setSize(18)

two = Text(Point(162.5,600),"2")
two.draw(win)
two.setStyle("bold")
two.setSize(18)

three = Text(Point(275,600),"3")
three.draw(win)
three.setStyle("bold")
three.setSize(18)

four = Text(Point(387.5,600),"4")
four.draw(win)
four.setStyle("bold")
four.setSize(18)

five = Text(Point(500,600),"5")
five.draw(win)
five.setStyle("bold")
five.setSize(18)

six = Text(Point(106.25,660),"6")
six.draw(win)
six.setStyle("bold")
six.setSize(18)

seven = Text(Point(218.75,660),"7")
seven.draw(win)
seven.setStyle("bold")
seven.setSize(18)

eight = Text(Point(331.5,660),"8")
eight.draw(win)
eight.setStyle("bold")
eight.setSize(18)

nine = Text(Point(443.75,660),"9")
nine.draw(win)
nine.setStyle("bold")
nine.setSize(18)

#erase box
rect4 = Rectangle(Point(575, 250),Point(700,300))
rect4.draw(win)
rect4.setFill('white')
eraser = Text(Point(637.5,275),"Erase")
eraser.draw(win)

#undo box
rect5 = Rectangle(Point(575,325),Point(700,375))
rect5.draw(win)
rect5.setFill('white')
drawIn = Text(Point(637.5,350),"Undo")
drawIn.draw(win)

#yellow blocks
r1 = Rectangle(Point(50,50),Point(200,200))
r1.draw(win)
#r1.setFill('yellow')

r2 = Rectangle(Point(350,50),Point(500,200))
r2.draw(win)
#r2.setFill('yellow')

r3 = Rectangle(Point(200,200),Point(350,350))
r3.draw(win)
#r3.setFill('yellow')

r4= Rectangle(Point(50,500),Point(200,350))
r4.draw(win)
#r4.setFill('yellow')

r5 = Rectangle(Point(500,500),Point(350,350))
r5.draw(win)
#r5.setFill('yellow')


#vertical points
p1 = Point(100,50)
p2 = Point(100,500)

p3 = Point(150,50)
p4 = Point(150,500)

p5 = Point(200,50)
p6 = Point(200,500)

p7 = Point(250,50)
p8 = Point(250,500)

p9 = Point(300,50)
p10 = Point(300,500)

p11 = Point(350,50)
p12 = Point(350,500)

p13 = Point(400,50)
p14 = Point(400,500)

p15 = Point(450,50)
p16 = Point(450,500)

#horizontal points
p17 = Point(50,100)
p18 = Point(500,100)

p19 = Point(50,150)
p20 = Point(500,150)

p21 = Point(50,200)
p22 = Point(500,200)

p23 = Point(50,250)
p24 = Point(500,250)

p25 = Point(50,300)
p26 = Point(500,300)

p27 = Point(50,350)
p28 = Point(500,350)

p29 = Point(50,400)
p30 = Point(500,400)

p31 = Point(50,450)
p32 = Point(500,450)

#vertical lines
line1 = Line(p1, p2)
line1.draw(win)

line2 = Line(p3, p4)
line2.draw(win)

line3 = Line(p5, p6)
line3.setWidth(3)
line3.draw(win)

line4 = Line(p7, p8)
line4.draw(win)

line5 = Line(p9, p10)
line5.draw(win)

line6 = Line(p11, p12)
line6.setWidth(3)
line6.draw(win)

line7 = Line(p13, p14)
line7.draw(win)

line8 = Line(p15, p16)
line8.draw(win)

#horizontal lines
line9 = Line(p17, p18)
line9.draw(win)

line10 = Line(p19, p20)
line10.draw(win)

line11 = Line(p21, p22)
line11.setWidth(3)
line11.draw(win)

line12 = Line(p23, p24)
line12.draw(win)

line13 = Line(p25, p26)
line13.draw(win)

line14 = Line(p27, p28)
line14.setWidth(3)
line14.draw(win)

line15 = Line(p29, p30)
line15.draw(win)

line16 = Line(p31, p32)
line16.draw(win)


def board_is_valid(self):


        for i, row in enumerate(board):
            for j, col in enumerate(row):
                # This gives a temporarily unset position, because the checked value
                # will always be set in its designated row, column and box.
                _, board[i][j] = self.board[i][j], None
        
                if _ != 0:
                    is_valid = self.is_legal_move(board, i, j, _)
                    board[i][j] = _
                    if not is_valid:
                        return is_valid
                board[i][j] = _
        return is_valid


def exists_in_column(self, board, col, val):
        ''' This determines if a given value exists in the
            given column. '''
        for i in range(9):
            if board[i][col] == val:
                return True
        return False

def exists_in_row(self, board, row, val):
        ''' This determines if a given value exists in the
            given row. '''
        for i in range(9):
            if board[row][i] == val:
                return True
        return False

def exists_in_box(self, board, row, col, val):
        ''' This determines if a given value exists in the
            given 3x3 box. '''
        for i in range(3):
            for j in range(3):
                # Given row/column is not always top left of box
                # so this needs to be considered
                if board[i+(row - row % 3)][j+(col - col % 3)] == val:
                    return True
        return False

def is_legal_move(self, board, row, col, val):
        #Takes a given row, column and value and decides wheter
            #placing the value at this row/column is permitted or not.
        if (not self.exists_in_column(board, col, val) and not
                self.exists_in_row(board, row, val) and not
                self.exists_in_box(board, row, col, val) and
                1 <= val <= 9):
            return True
        return False

def next_empty_location(self, board, next_pos):
        #Determines the next empty location that is available

        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    next_pos[0] = row
                    next_pos[1] = col
                    return True
        return False
