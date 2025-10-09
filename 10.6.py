
#-----import statements-----
import turtle as trtl
import random as rand


score = 0 


spot_colors = ["lightpink","lime","lightblue","bisque"]
# square shaped turtle will use a global variable
box = trtl.Turtle()
box.shape("turtle")
box.shapesize(3)
box.penup()
box.color("lightblue")

#-----countdown variables-----
font_setup = ("Arial", 23, "normal")
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False

scoretrtl = trtl.Turtle()
scoretrtl.penup()
scoretrtl.hideturtle()
scoretrtl.goto(250,-250)

#-----countdown writer-----
counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-270,-250)


#-----game functions-----


def change_size():
  sizebox = [3,5,2,10,8]
  box.shapesize(sizebox[rand.randint(0,4)])
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up= True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def update_score_for_box():
  scoretrtl.clear()
  global score # gives this function access to the score that was created above
  score += 1
  print(score)
  scoretrtl.write("score: " + str(score), font=font_setup)


def trtl_clicked(x,y):

  if timer_up == True:
    return
  else:
    
    box.showturtle()
    new_xpos = rand.randint(-300, 300)
    new_ypos = rand.randint(-300, 300)
    box.hideturtle()
    box.goto(new_xpos,new_ypos)
    box.color(spot_colors[rand.randint(0,3)])
    change_size()
    box.showturtle()
    update_score_for_box()


#--------main----------
box.onclick(trtl_clicked)
# update_score_for_box will update the score for spot


#---------events---------




wn = trtl.Screen()
wn.bgcolor("orchid1")
wn.ontimer(countdown,counter_interval)
wn.mainloop()