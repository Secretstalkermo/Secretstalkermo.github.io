import turtle

a = turtle.Turtle()
a.pensize(4)
a.shape("turtle")
screen = turtle.Screen()
screen.bgcolor("#F8C8DC")


def go(x,y):
    a.penup()
    a.goto(x,y)
    a.pendown()
 
#Flower cover thingy ba
a.pencolor("SteelBlue")
a.fillcolor("LightBlue")

go(40.03, -167.53)
a.begin_fill()
a.seth(104.91)
a.circle(120.54, 29.94)
a.seth(49.57)
a.circle(-315.30, 15.58) 
a.seth(33.99)
a.circle(172.07, 64.94)
a.seth(185.9)
a.circle(227.51, 53.26)
a.seth(239.17)
a.circle(99.15, 72.41)
a.seth(213.64)
a.circle(74.25, 50.32)
a.seth(336.29)
a.circle(108.41, 47.43)
a.end_fill()

go(-37.02,-69.53)
a.begin_fill()
a.seth(98.75)
a.circle(-121.74, 54.75)
a.seth(131.6)
a.circle(187.54, 48.16)
a.seth(253.4)
a.circle(134.51, 95.25)
a.end_fill()

#Ribbon
a.pencolor("MediumVioletRed")
a.fillcolor("HotPink")

go(69.69, -55.52)
a.begin_fill()
a.seth(184.72)
a.circle(90.59, 53.66)
a.seth(127.63)
a.circle(111.93, 45.5)
a.seth(234.89)
a.circle(80.10, 70.23)
a.seth(9.8)
a.circle(152.91, 31.68)
a.seth(311.3)
a.circle(108.05, 42.6)
a.seth(58.45)
a.circle(88.07, 63.09)
a.end_fill()

go(16.3, -99.27)
a.begin_fill()
a.seth(99)
a.circle(19.5)
a.end_fill()

#Leaves
def leaves (angle):
    a.begin_fill()
    a.seth(angle)
    a.circle(75.61, 121.08)
    a.seth(angle+175.63)
    a.circle(72.70, 129.82)
    a.end_fill()

a.pencolor("DarkGreen")
a.fillcolor("LimeGreen")

go(-79.20, 110.03)
leaves(165.01)
go(-122.12, 151)
leaves(79.67)

a.fillcolor("LawnGreen")

go(-100.51, 123.98)
leaves(119.46)
go(-90.46, 135.14)
leaves(22.07)

#Flowers
def flor(x,y):
    go(x,y)
    a.begin_fill()
    a.seth(330.2)
    a.circle(22.66, 236.14)
    a.seth(42.2)
    a.circle(22.66, 236.14)
    a.seth(114.2)
    a.circle(22.66, 236.14)
    a.seth(186.2)
    a.circle(22.66, 236.14)
    a.seth(258.2)
    a.circle(22.66, 236.14)
    a.end_fill()

    a.pencolor("Gold")
    a.fillcolor("Gold")
    go(x-4.81, y+20.88)
    a.begin_fill()
    a.seth(99)
    a.circle(22.5)
    a.end_fill()

a.pencolor("MediumOrchid")
a.fillcolor("Violet")
flor(155.36, 115.58)
a.pencolor("DarkGray")
a.fillcolor("White")
flor(60.97, 170)
a.pencolor("IndianRed")
a.fillcolor("LightSalmon")
flor(-43.377, 120)
a.pencolor("MediumOrchid")
a.fillcolor("Violet")
flor(-11.60, 41.39)
a.pencolor("SteelBlue")
a.fillcolor("DarkTurquoise")
flor(65.71, 85.27)

#For greetings toh bieh
a.color("Chocolate")
go(-450, 300)
a.write("Happy", False, "Right", 
        ("Bradley Hand ItC", 40, "bold"))
a.color("Chocolate")
go(-225, 300)
a.write("Sweet", False, "Right", 
    ('Bradley Hand ItC', 40, "bold"))
a.color("Chocolate")
go(-92, 300)
a.write("17th", False, "Right", 
    ('Bradley Hand ItC', 40, "bold"))
a.color("Chocolate")
go(235, 300)
a.write("Birthday", False, "Right", 
    ('Bradley Hand ItC', 40, "bold"))
a.color("Chocolate")
go(470, 300)
a.write("Tangi!", False, "Right", 
    ('Bradley Hand ItC', 40, "bold"))

#For the letter
a.color("Black")
go(-650, -264)  
paragraph = (
    "Binabati kita sa iyong Kaarawan! Isa na namang\ntaon ang nakalipas. "
    "Ang bilis ng panahon noh?\nYou’re 17 years old now. Syempre, iiyakan mo "
    "Din\nyan ng ilang araw kase nakakatakot. Alam mo, para kang\n ano yung pakiramdam "
    "pag may araw sa mukha mo tas\nang lamig ng hangin? Para sakin, "
    "It's comforting. You're kind,\nmapagmahal, at warm. \n\n"
    "Pero gusto kong malaman mo na, ang saya ko na kasama kita.\n Na hanggang "
    "ngayon, andito ka pa. Kung hindi man, Okay lang.\nOkay lang. I miss your hugs."
    "I miss everything. Sometimes, I\nwould do something with Roda and I’d start "
    "thinking of what it\nwould have been if you're there too. How I’ll probably just "
    "randomly\nopen my arms and you’ll hug me, just like the old times.\n Kung "
    "nandito ka, hindi ganto gift ko beh. Wala akong pera para\nmag ship ng gift "
    "from here eh or ask one of ur friends/mom for\na huge favor. No money, so I "
    "hope you’ll like this simple gift as you also\ndeserve to have what you give "
    "that you can’t receive from the wrong person. Ingat ka palagi!\n"
)
a.write(paragraph, False, "Left", ("Times New Roman", 14, "italic"))


a.color("Chocolate")
go(500, -99)
a.write("I miss you", False, "Right",
         ("Bradley Hand ItC", 40, "bold"))

a.hideturtle()

#Mini Hearts
c = turtle.Turtle()
c.pensize(2)
c.shape("turtle")
screen = turtle.Screen()
screen.bgcolor("#F8C8DC")

def go(x, y):
    c.penup()
    c.goto(x, y)
    c.pendown()

# Function to draw a small pink heart shape
def draw_small_heart():
    c.fillcolor("Pink")
    c.begin_fill()
    c.left(140)
    c.forward(30)  # Forward length for a small heart
    c.circle(-15, 200)  # Radius for the curves
    c.left(120)
    c.circle(-15, 200)  # Radius for the curves
    c.forward(30)  # Complete the heart shape
    c.end_fill()
    c.setheading(0)  # Reset heading after drawing the heart

# Draw three aligned small pink hearts
go(340, -165)  # Starting position for the first heart
for _ in range(3):
    draw_small_heart()
    c.penup()
    c.forward(50)  # Move right for the next heart
    c.pendown()

c.hideturtle()

import webbrowser

link = "https://app.sane.fyi/s/37f2f334-a297-11ef-b4d0-c332100889a8?t=QPA72CdpElmzxaF9cZbB&utm_source=share-menu&utm_medium=web"
webbrowser.open(link)

turtle.done()



