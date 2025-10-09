# CODE TO COPY
#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["circle", "square", "turtle", "triangle","circle", "square", "turtle", "triangle","circle", "square", "turtle", "triangle"]
turtle_colors = ["pink", "blue", "orange", "purple","pink", "blue", "orange", "purple","pink", "blue", "orange", "purple","pink", "blue", "orange", "purple"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#  

for k in range(3):
    startx = -50
    starty = 50
    startx2 = 50
    starty2 = 50
    i = 0

    #
    for t in my_turtles:
        if i < 2:
            t.goto(startx, starty)
            
        else:
            t.goto(startx2, starty2)
    
        t.forward(10)
        t.right(135)
        color = turtle_colors[i]
        t.color(color)   
        t.left(250)  
        if i < 2:
            startx = startx + 10
            starty = starty - 10
            
        else:
            startx2 = startx2 + 10
            starty2 = starty2 - 10
            
        i += 1
    #	

wn = trtl.Screen()
wn.mainloop()