import turtle
turtle.speed(5)
turtle.penup()
turtle.goto(-200,100) 
turtle.setup(width=1100, height=700,startx= None , starty= None)

#orange block part
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("orange")
turtle.left(90)
turtle.fd(90)
turtle.right(90)
turtle.fd(400)
turtle.right(90)
turtle.fd(90)
turtle.right(90)
turtle.fd(400)
turtle.end_fill()

#white Block and Chakra
turtle.color("black")
turtle.left(90)
turtle.fd(90)
turtle.left(90)
turtle.fd(200)

#Chakra
turtle.circle(45)  #parameter is radius

#Spokes of the Chakra
turtle.penup()
turtle.goto(0,55)
turtle.color("blue")
for spoke in range(24):
    turtle.goto(0,55)
    turtle.right(15)
    turtle.pendown()
    turtle.fd(45)
    turtle.penup()

turtle.goto(0,10)
turtle.pendown()
turtle.color("black")
turtle.fd(200)
turtle.left(90)
turtle.fd(90)
turtle.hideturtle()

#return back for green rectangle
turtle.penup()
turtle.goto(-200,100)
turtle.right(180)

#green block
turtle.begin_fill()
turtle.fillcolor("green")
turtle.showturtle()
turtle.fd(90)
turtle.left(90)
turtle.fd(400)
turtle.pendown()
turtle.right(90)
turtle.fd(90)
turtle.right(90)
turtle.fd(400)
turtle.right(90)
turtle.fd(90)
turtle.end_fill()

turtle.right(180)
turtle.fd(90)

#stick of the flag
turtle.fd(210)
turtle.penup()

#text area
turtle.goto(-100,-180)
turtle.color("deep sky blue")
style = ("courier", 30, "italic", "bold")
turtle.write("Happy Independence Day !", font= style, align="left")

#signature
#turtle is facing downward
turtle.color("red")
style2 = ("courier", 30,"italic", "bold")
turtle.fd(70)
turtle.write("Designed By -",font="style2",align="left")

turtle.left(90)
turtle.fd(150)
turtle.right(90)
turtle.fd(30)
turtle.left(90)

#creating my name
#Letter "A"
turtle.pensize(5)
turtle.pendown()
turtle.color("green")
turtle.left(75)
turtle.fd(80)
turtle.right(150)
turtle.fd(40)
turtle.right(105)
turtle.fd(20)
turtle.right(180)
turtle.fd(20)
turtle.right(75)
turtle.fd(40)

#gap 
turtle.penup()
turtle.left(75)
turtle.fd(30)

#Letter "N"
turtle.pendown()
turtle.left(90)
turtle.fd(80)
turtle.right(160)
turtle.fd(80)
turtle.left(160)
turtle.fd(80)

#gap
turtle.penup()
turtle.right(90)
turtle.fd(30)

#Letter "I"
turtle.pendown()
turtle.fd(60)
turtle.left(180)
turtle.fd(30)
turtle.left(90)
turtle.fd(80)
turtle.right(90)
turtle.fd(30)
turtle.right(180)
turtle.fd(60)
turtle.hideturtle()



turtle.done()


