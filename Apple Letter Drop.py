import turtle as trtl
import random as rand
import string

#-----setup-----
apple_image = "apple.gif"  # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
wn.addshape("background.gif")
wn.bgpic("background.gif")

# create apples
apple = trtl.Turtle()
apple2 = trtl.Turtle()
apple3 = trtl.Turtle()
apple4 = trtl.Turtle()
apple5 = trtl.Turtle()
apple6 = trtl.Turtle()
apple7 = trtl.Turtle()
apple8 = trtl.Turtle()

apple_list = [apple, apple2, apple3, apple4, apple5, apple6, apple7, apple8]

#-----functions-----
# use the exact letters from "williamm"
letterlist = list("williamm")
rand.shuffle(letterlist)

# create text turtles for letters
letter_turtles = []
for i in range(8):
    t = trtl.Turtle()
    t.hideturtle()
    t.penup()
    letter_turtles.append(t)

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
    active_apple.shape(apple_image)
    active_apple.penup()

# place all apples at random positions and write letters on them
for i in range(8):
    draw_apple(apple_list[i])
    randx = rand.randint(-200, 200)
    randy = rand.randint(-200, 200)
    apple_list[i].goto(randx, randy)
    letter_turtles[i].goto(randx, randy - 10)
    letter_turtles[i].write(letterlist[i], font=("Arial", 20, "bold"))

# drop apples
def drop_apple(index):
    apple_list[index].setheading(270)
    letter_turtles[index].clear()
    apple_list[index].forward(1000)


def drop_apple1():
    drop_apple(0)
def drop_apple2():
    drop_apple(1)
def drop_apple3():
    drop_apple(2)
def drop_apple4():
    drop_apple(3)
def drop_apple5():
    drop_apple(4)
def drop_apple6():
    drop_apple(5)
def drop_apple7():
    drop_apple(6)
def drop_apple8():
    drop_apple(7)

#-----function calls-----

def drop_w():
    if "w" in letterlist:
        for i in range(8):
            if letterlist[i] == "w":
                drop_apple(i)

def drop_i():
    if "i" in letterlist:
        for i in range(8):
            if letterlist[i] == "i":
                drop_apple(i)

def drop_l():
    if "l" in letterlist:
        for i in range(8):
            if letterlist[i] == "l":
                drop_apple(i)

def drop_a():
    if "a" in letterlist:
        for i in range(8):
            if letterlist[i] == "a":
                drop_apple(i)

def drop_m():
    if "m" in letterlist:
        for i in range(8):
            if letterlist[i] == "m":
                drop_apple(i)


wn.onkeypress(drop_w, "w")
wn.onkeypress(drop_i, "i")
wn.onkeypress(drop_l, "l")
wn.onkeypress(drop_a, "a")
wn.onkeypress(drop_m, "m")

wn.listen()
wn.mainloop()
