import turtle

class Rabit(object):
    def __init__(self, grids, size=600):
        self.__grid_size = size / grids
        self.__left = -size / 2 - 5
        self.__top = size / 2 + 5
        self.__speed = 5
        self.__mat = [[{"text":"", "line_color":"black", "text_color":"black", "font":("Times", 24)}\
                       for _ in range(grids)] for _ in range(grids)]

        self.t = turtle.Turtle()
        self.t.pensize(2)
        self.t.hideturtle()
        self.t.speed(self.__speed)

    def speed(self, speed):
        self.__speed = speed
        self.t.speed(speed)

    def hold(self):
        turtle.done()

    def pensize(self, pensize):
       self.t.pensize(pensize) 

    def delay(self, time):
        self.begin_hide()
        turtle.delay(time)
        self.end_hide()
        
    def begin_hide(self):
        turtle.tracer(0)

    def end_hide(self):
        turtle.update()
        turtle.tracer(1)
        self.t.speed(self.__speed)

    def draw_rect(self, row, col, rows=1, cols=1, color="black"):
        self.t.pencolor(color)
        self.t.pu()
        self.t.setheading(0)
        self.t.goto(self.__left + col * self.__grid_size, self.__top - row * self.__grid_size) 
        self.t.pd()
        for i in range(2):
            self.t.fd(self.__grid_size * cols)
            self.t.rt(90)
            self.t.fd(self.__grid_size * rows)
            self.t.rt(90)

        for i in range(row, row + rows):
            for j in range(col, col + cols):
                    self.__mat[i][j]["line_color"] = color

    def paint_rect(self, row, col, rows=1, cols=1, color="black", cover=False):
        self.t.pencolor(self.__mat[row][col]["line_color"])
        self.t.fillcolor(color)
        self.t.pu()
        self.t.setheading(0)
        self.t.goto(self.__left + col * self.__grid_size, self.__top - row * self.__grid_size) 
        self.t.pd()
        self.t.begin_fill()
        for i in range(2):
            self.t.fd(self.__grid_size * cols)
            self.t.rt(90)
            self.t.fd(self.__grid_size * rows)
            self.t.rt(90)
        self.t.end_fill()
        if cover:
            for i in range(row, row + rows):
                for j in range(col, col + cols):
                    self.__mat[i][j] = [
                        {"text":"", "line_color":"black", "text_color":"black", "font":("Times", 24)}
                    ]
        else:
            for i in range(row, row + rows):
                for j in range(col, col + cols):
                    self.draw_text(row, col,
                                   self.__mat[i][j]["text"], self.__mat[i][j]["text_color"],
                                   self.__mat[i][j]["font"])

    def clear_rect(self, row, col, rows=1, cols=1, color="white"):
        self.t.pencolor(color)
        self.t.fillcolor(color)
        self.t.pu()
        self.t.setheading(0)
        self.t.goto(self.__left + col * self.__grid_size, self.__top - row * self.__grid_size) 
        self.t.pd()
        self.t.begin_fill()
        for i in range(2):
            self.t.fd(self.__grid_size * cols)
            self.t.rt(90)
            self.t.fd(self.__grid_size * rows)
            self.t.rt(90)
        self.t.end_fill()

    def draw_circle(self, row, col, color="black"):
        self.t.pencolor(color)
        self.t.pu()
        self.t.goto(self.__left + col * self.__grid_size, self.__top - row * self.__grid_size) 
        self.t.pd()
        self.t.circle(self.__grid_size / 2)

    
    def draw_text(self, row, col, text, color="black", font=("Times", 24)):
        self.__mat[row][col]["text"] = text
        self.__mat[row][col]["text_color"] = color
        self.__mat[row][col]["font"] = font
        self.t.pencolor(color)
        self.t.pu()
        text_width = len(text) * font[1] / 2
        text_height = font[1] * 1.16 

        self.t.goto(self.__left + col * self.__grid_size + (self.__grid_size - text_width) / 2,
               self.__top - row * self.__grid_size - (self.__grid_size + text_height) / 2) 
        self.t.pd()
        self.t.write(text, font=font)
        self.t.pu()

    def draw_line(self, from_row, from_col, to_row, to_col, color="black"):
        self.t.pencolor(color)
        self.t.pu()
        self.t.goto(self.__left + from_col * self.__grid_size,
                    self.__top - from_row * self.__grid_size)
        self.t.pd()
        self.t.goto(self.__left + to_col * self.__grid_size,
                    self.__top - to_row * self.__grid_size)

    def save2eps(self, file):
        turtle.getcanvas().postscript(file = file)

if __name__ == '__main__':

    rabit = Rabit(11)
    rabit.begin_hide()
    for i in range(11):
        for j in range(11):
            rabit.draw_rect(i, j, color="red")
    rabit.end_hide()

    rabit.draw_circle(1.5, 1.5)
    for i in range(11):
        rabit.draw_text(i, 1, "1")
        rabit.paint_rect(i, 1, color="red")
        rabit.paint_rect(i, 1, color="blue", cover=True)

    turtle.done()

