# CS558 HW1 Billiard Ball
# Author: Jieru Hu
# ID: 9070194544
import turtle

#Get input from the user
print("Hello! Welcome to the Billiard Balls Simulation !")
Width = input("Please enter the Width of the table: ")
Height = input("Please enter the Height of the table: ")
print("Input two points to define a line and see how many times the billaball has crossed it !")
print("Please enter the coordinates of the first point of the line")
x1, y1 = [int(x) for x in raw_input().split()]
print("Please enter the coordinates of the second point of the line")
x2, y2 = [int(x) for x in raw_input().split()]
count = 0

#Object: represents a Ball
class Ball:

    def __init__(self,x,y,velx,vely):
        self.x = x #x coordinate of the ball
        self.y = y  #y coordinate of the ball
        self.velx = velx #x component of the velocity
        self.vely = vely #y component of the velocity
        #The velocity vector is represented by P(s) = P0 + s(incx + incy)

    def move(self):
        #Transform the parametric function into implicit y = a*x +b and calculate a, b

        #get value s for the next collision
        s = self.getS()
        #update the position
        self.x = self.x + s*self.velx
        self.y = self.y + s*self.vely
        #if the ball collide on x = 0 or x = width, change the x component of velocity
        if(self.x == 0 or self.x == Width):
            self.velx = self.velx*(-1)
        #if the ball collide on y = 0 or y = height, change the y component of velocity
        if(self.y == 0 or self.y == Height):
            self.vely = self.vely*(-1)

        return

    #The method checks if the ball is in hole
    def checkInHole(self):
        if(self.x == 0 and self.y==0):
            return 1
        if(self.x == Width and self.y == Height):
            return 1
        if(self.x == 0 and self.y == Height):
            return 1
        if(self.x == Width and self.y == 0):
            return 1
        return 0

    #The method returns the S for the next possible collision
    def getS(self):
        list = []
        s1 = (0 - self.x)*self.velx
        if(s1 > 0):
            list.append(s1)
        s2 = (Width - self.x)*self.velx
        if(s2 > 0):
            list.append(s2)
        s3 = (0 - self.y)*self.vely
        if(s3 > 0):
            list.append(s3)
        s4 = (Height - self.y)*self.vely
        if(s4 > 0):
            list.append(s4)

        return min(list)


    def toString(self):
        return ("(" + str(self.x) + "," + str(self.y) + ")");



# If the ball crosses the line, increases the count
def crossline(prex,prey,currx,curry):
    global count
    first = crossProduct(x2-x1, y2 - x2, prex - x1, prey - y1)
    second = crossProduct(x2-x1, y2 - x2, currx - x1, curry - y1)
    third = crossProduct(currx - prex, curry - prey, x1 - prex, y1 - prey)
    fourth = crossProduct(currx - prex, curry - prey, x2 - prex, y2 - prey)
    if(first*second < 0 and third*fourth < 0):
        count += 1

    return


# The function returns the cross product of x and y
def crossProduct(x1, y1, x2, y2):
    return (x1*y2 - x2*y1)




def main():

    global Width,Height,count
    screen = turtle.Screen()
    screen.screensize(Width,Height,"black")
    screen.title("Billiard Balls Simulation")

    t = turtle.Turtle(shape="circle")
    t.color("white")
    t.penup()
    t.setpos(-Width/2,-Height/2)
    t.pendown()
    ball = Ball(0,0,1,1)
    print("The coordinates of the collision points are: ")
    i = 1;
    while(True):
        prex = ball.x
        prey = ball.y
        ball.move()
        #print ball.x, "  ", ball.y
        print i, ": ", ball.toString()
        t.setposition(ball.x-(Width/2),ball.y-(Height/2))
        t.position()
        i+=1
        crossline(prex, prey, ball.x, ball.y)
        if ball.checkInHole():
            break


    print "The ball has crossed the line ", count, "times"
    t.home()
    screen.exitonclick()




if __name__ == "__main__":
    main()
