'''
In creating our project, we utilized the turtle library. The url for the github page of this library is the following:
https://github.com/python/cpython/blob/3.10/Lib/turtle.py (Retrieved on 12/17/2021).
'''

#Setup
import turtle as turtle
import random as rand
import time
turtle.bgcolor("green")
wn = turtle.Screen()
wn.tracer(False)


#Variables
global health_points
global gold
health_points = 200
gold = 0


#Name
name = input("What is your name? ").upper().strip()
name = name[0:1]


#Colors
color = input("Which color do you want your player to be? ").lower().strip()

colors = ["gainsboro", "silver", "darkgray", "gray", "dimgray", "black", "lightslategray", "slategray", "lightsteelblue", "cornflowerblue", "royalblue", "blue", "mediumblue", "navy", "darkblue", "midnightblue", "lightblue", "deepskyblue", "dodgerblue", "powderblue", "skyblue", "lightskyblue", "steelblue", "cyan", "paleturquoise", "darkturquoise", "turquoise", "mediumturquoise", "lightseagreen", "cadetblue", "darkcyan", "teal", "darkslategray", "aquamarine", "mediumaquamarine", "darkseagreen", "mediumseagreen", "seagreen", "palegreen", "lightgreen", "mediumspringgreen", "springgreen", "limegreen", "green", "forestgreen", "darkgreen", "greenyellow", "chartreuse", "lawngreen", "lime", "yellowgreen", "olivedrab", "beige", "darkkhaki", "olive", "darkolivegreen", "palegoldenrod", "khaki", "yellow", "gold", "goldenrod", "darkgoldenrod", "wheat", "tan", "burlywood", "peru", "sienna", "saddlebrown", "navajowhite", "moccasin", "sandybrown", "orange", "darkorange", "chocolate", "firebrick", "brown", "darkred", "maroon", "bisque", "peachpuff", "lightsalmon", "coral", "tomato", "orangered", "red", "crimson", "darksalmon", "salmon", "lightcoral", "indianred", "rosybrown", "pink", "lightpink", "hotpink", "deeppink", "palevioletred", "mediumvioletred", "purple", "darkmagenta", "violet","magenta", "thistle", "plum", "orchid", "mediumorchid", "darkorchid", "darkviolet", "blueviolet", "mediumpurple", "rebeccapurple", "indigo","mediumslateblue", "slateblue", "darkslateblue"]

colors_index = rand.randint(0, 113)
rand_color = colors[colors_index]

white = ["white", "snow", "whitesmoke", "aliceblue", "azure", "lightcyan", "mintcream", "honeydew", "beige", "ivory", "lightyellow", "cornsilk", "floralwhite", "oldlace", "linen", "seashell", "lavenderblush", "violetred", "ghostwhite", "lightslateblue", "lightgoldenrodyellow", "lemonchiffon", "antiquewhite", "papayawhip", "blanchedalmond", "mistyrose", "lavender"]


#Setup Turtles
road = turtle.Turtle()
player = turtle.Turtle()
player.speed(1)
health = turtle.Turtle()
money = turtle.Turtle()
health_over = turtle.Turtle()
gold_over = turtle.Turtle()
over = turtle.Turtle()


#Monster Turtes
goblin = turtle.Turtle() #20 damage, 30 gold
troll = turtle.Turtle() #30 damage, 40 gold
ogre = turtle.Turtle() #40 damage, 50 gold
hydra = turtle.Turtle() #50 damage, 60 gold
monsters = [goblin, troll, ogre, hydra]


#Land Turtles
mountain = turtle.Turtle() #40 damage, 50 gold
forest = turtle.Turtle() #20 damage, 30 gold
swamp = turtle.Turtle() #50 damage, 60 gold
desert = turtle.Turtle() #30 damage, 40 gold
lands = [mountain, forest, swamp, desert]


#Boss Turtles
dragon = turtle.Turtle() #75 damage, 100 gold
cave = turtle.Turtle() #70 damage, 90 gold
bosses = [dragon, cave]


#Obstacles
obstacles = [monsters, lands]



#Functions
#Draw Road
def draw_road():
  road.fillcolor("lightgray")
  road.begin_fill()
  road.penup()
  road.goto(-50, -200)
  road.pendown()
  road.fd(100)
  road.left(90)
  road.fd(200)
  road.goto(180, 200)
  road.left(90)
  road.fd(100)
  road.goto(0,25)
  road.goto(-75, 200)
  road.fd(100)
  road.goto(-50, 0)
  road.left(90)
  road.fd(200)
  road.end_fill()


def draw_player():
  if (color in white):
    player.pencolor("black")
    player.fillcolor(color)
    player.begin_fill()
    player.penup()
    player.goto(0, -175)
    player.pendown()
    player.circle(25)
    player.end_fill()
    player.color("black")
    style = ("times new roman", 30, "bold")
    player.write(name, font = style, align = 'center')
    player.hideturtle()

  elif ((color == ("lightgray")) or (color not in colors)):
    player.pencolor("black")
    player.fillcolor(rand_color)
    player.begin_fill()
    player.penup()
    player.goto(0, -175)
    player.pendown()
    player.circle(25)
    player.end_fill()
    player.color("white")
    style = ("times new roman", 30, "bold")
    player.write(name, font = style, align = 'center')
    player.hideturtle()

  else:
    player.pencolor("black")
    player.fillcolor(color)
    player.begin_fill()
    player.penup()
    player.goto(0, -175)
    player.pendown()
    player.circle(25)
    player.end_fill()
    player.color("white")
    style = ("times new roman", 30, "bold")
    player.write(name, font = style, align = 'center')
    player.hideturtle()


#Stats
def draw_health():
  health.penup()
  health.goto(-160, -175)
  health.pendown()
  health.color("white")
  style = ("times new roman", 20, "bold")
  health.write(health_points, font = style, align = 'center')
  health.hideturtle()


def draw_gold():
  money.penup()
  money.goto(-160, -205)
  money.pendown()
  money.color("white")
  style = ("times new roman", 20, "bold")
  money.write(gold, font = style, align = 'center')
  money.hideturtle()


#Monsters
def draw_goblin():
  goblin.pencolor("black")
  goblin.fillcolor("green")
  goblin.begin_fill()
  goblin.circle(25)
  goblin.end_fill()
  goblin.color("white")
  style = ("times new roman", 30, "bold")
  goblin.write("G", font = style, align = 'center')
  goblin.hideturtle()

def goblin_attack():
  print("You encounter a gang of goblins. You manage to defeat them, but take 20 damage. You earn 30 gold.")
  global health_points
  global gold
  health_points -= 20
  gold += 30

def goblin_defeat():
  global health_points
  health_points -= 20


def draw_troll():
  troll.pencolor("black")
  troll.fillcolor("blue")
  troll.begin_fill()
  troll.circle(25)
  troll.end_fill()
  troll.color("white")
  style = ("times new roman", 30, "bold")
  troll.write("T", font = style, align = 'center')
  troll.hideturtle()

def troll_attack():
  print("You encounter a small band of menacing trolls. You manage to defeat \nthem, but take 30 damage. You earn 40 gold.")
  global health_points
  global gold
  health_points -= 30
  gold += 40

def troll_defeat():
  global health_points
  health_points -= 30


def draw_ogre():
  ogre.pencolor("black")
  ogre.fillcolor("yellow")
  ogre.begin_fill()
  ogre.circle(25)
  ogre.end_fill()
  ogre.color("white")
  style = ("times new roman", 30, "bold")
  ogre.write("O", font = style, align = 'center')
  ogre.hideturtle()

def ogre_attack():
  print("You encounter an ill-tempered ogre. You manage to defeat the ogre, but \ntake 40 damage. You earn 50 gold.")
  global health_points
  global gold
  health_points -= 40
  gold += 50

def ogre_defeat():
  global health_points
  health_points -= 40


def draw_hydra():
  hydra.pencolor("black")
  hydra.fillcolor("black")
  hydra.begin_fill()
  hydra.circle(25)
  hydra.end_fill()
  hydra.color("white")
  style = ("times new roman", 30, "bold")
  hydra.write("H", font = style, align = 'center')
  hydra.hideturtle()

def hydra_attack():
  print("You encounter a fearsome hydra. You manage to defeat the hydra, but take50 damage. You earn 60 gold.")
  global health_points
  global gold
  health_points -= 50
  gold += 60

def hydra_defeat():
  global health_points
  health_points -= 50


def draw_dragon():
  dragon.pencolor("black")
  dragon.fillcolor("orangered")
  dragon.begin_fill()
  dragon.penup()
  dragon.goto(0, 140)
  dragon.pendown()
  dragon.circle(25)
  dragon.end_fill()
  dragon.color("yellow")
  style = ("times new roman", 30, "bold")
  dragon.write("D", font = style, align = 'center')
  dragon.hideturtle()

def dragon_attack():
  print("You encounter the great dragon himself. You somehow manage to defeat thegreat dragon, but take 75 damage. You earn 100 gold.")
  global health_points
  global gold
  health_points -= 75
  gold += 100

def dragon_defeat():
  global health_points
  health_points -= 75


#Lands
def draw_mountain():
  mountain.pencolor("black")
  mountain.fillcolor("brown")
  mountain.begin_fill()
  mountain.circle(25)
  mountain.end_fill()
  mountain.color("white")
  style = ("times new roman", 30, "bold")
  mountain.write("M", font = style, align = 'center')
  mountain.hideturtle()

def mountain_pass():
  print("You attempt to climb a colossal mountain. You discover an anicent \nsettlement and find 40 gold. However, you take 30 damage due to injury \nfrom the frigid temperature.")
  global health_points
  global gold
  health_points -= 30
  gold += 40

def mountain_fail():
  global health_points
  health_points -= 30


def draw_forest():
  forest.pencolor("black")
  forest.fillcolor("darkgreen")
  forest.begin_fill()
  forest.circle(25)
  forest.end_fill()
  forest.color("white")
  style = ("times new roman", 30, "bold")
  forest.write("F", font = style, align = 'center')
  forest.hideturtle()

def forest_pass():
  print("You attempt to pass a dense forest. You discover an abandoned cabin and find 20 gold. However, you take 10 damage due to attacks from wild \nanimals.")
  global health_points
  global gold
  health_points -= 10
  gold += 20

def forest_fail():
  global health_points
  health_points -= 10


def draw_swamp():
  swamp.pencolor("black")
  swamp.fillcolor("turquoise")
  swamp.begin_fill()
  swamp.circle(25)
  swamp.end_fill()
  swamp.color("white")
  style = ("times new roman", 30, "bold")
  swamp.write("S", font = style, align = 'center')
  swamp.hideturtle()

def swamp_pass():
  print("You attempt to wade through a murky swamp. You discover an anicent ruin and find 50 gold. However, you take 40 damage due to disease.")
  global health_points
  global gold
  health_points -= 40
  gold += 50

def swamp_fail():
  global health_points
  health_points -= 40


def draw_desert():
  desert.pencolor("black")
  desert.fillcolor("khaki")
  desert.begin_fill()
  desert.circle(25)
  desert.end_fill()
  desert.color("white")
  style = ("times new roman", 30, "bold")
  desert.write("D", font = style, align = 'center')
  desert.hideturtle()

def desert_pass():
  print("You attempt to cross a vast desert. You discover an ancient desert \ntemple and find 30 gold. However, you take 20 damage due to the extreme heat.")
  global health_points
  global gold
  health_points -= 20
  gold += 30

def desert_fail():
  global health_points
  health_points -= 20


def draw_cave():
  cave.pencolor("black")
  cave.fillcolor("black")
  cave.begin_fill()
  cave.penup()
  cave.goto(0, 140)
  cave.pendown()
  cave.circle(25)
  cave.end_fill()
  cave.color("blueviolet")
  style = ("times new roman", 30, "bold")
  cave.write("C", font = style, align = 'center')
  cave.hideturtle()

def cave_pass():
  print("You attempt to navigate through a mysterious cave. You discover an \nabandoned mineshaft and find 90 gold. However, you take 70 damage due toinjury from falling rocks.")
  global health_points
  global gold
  health_points -= 70
  gold += 90

def cave_fail():
  global health_points
  health_points -= 70


#Lanes
def right_lane():

  if (right_obstacle_index == 0):
    if (right_monsters_index == 0):
      right_monster.penup()
      right_monster.goto(110, 140)
      right_monster.pendown()
      draw_goblin()
      print("There are goblins on the right lane.")

    elif (right_monsters_index == 1):
      right_monster.penup()
      right_monster.goto(110, 140)
      right_monster.pendown()
      draw_troll()
      print("There are trolls on the right lane.")

    elif (right_monsters_index == 2):
      right_monster.penup()
      right_monster.goto(110, 140)
      right_monster.pendown()
      draw_ogre()
      print("There is an ogre on the right lane.")

    else:
      right_monster.penup()
      right_monster.goto(110, 140)
      right_monster.pendown()
      draw_hydra()
      print("There is a hydra on the right lane.")

  else:
    if (right_lands_index == 0):
      right_land.penup()
      right_land.goto(110, 140)
      right_land.pendown()
      draw_mountain()
      print("There is a mountain on the right lane.")

    elif (right_lands_index == 1):
      right_land.penup()
      right_land.goto(110, 140)
      right_land.pendown()
      draw_forest()
      print("There is a forest on the right lane.")

    elif (right_lands_index == 2):
      right_land.penup()
      right_land.goto(110, 140)
      right_land.pendown()
      draw_swamp()
      print("There is a swamp on the right lane.")

    else:
      right_land.penup()
      right_land.goto(110, 140)
      right_land.pendown()
      draw_desert()
      print("There is a desert on the right lane.")


def left_lane():

  if (obstacle_index == 0):
    if (monsters_index == 0):
      monster.penup()
      monster.goto(-105, 140)
      monster.pendown()
      draw_goblin()
      print("There are goblins on the left lane.")

    elif (monsters_index == 1):
      monster.penup()
      monster.goto(-105, 140)
      monster.pendown()
      draw_troll()
      print("There are trolls on the left lane.")

    elif (monsters_index == 2):
      monster.penup()
      monster.goto(-105, 140)
      monster.pendown()
      draw_ogre()
      print("There is an ogre on the left lane.")

    else:
      monster.penup()
      monster.goto(-105, 140)
      monster.pendown()
      draw_hydra()
      print("There is a hydra on the left lane.")
      
  else:
    if (lands_index == 0):
      land.penup()
      land.goto(-105, 140)
      land.pendown()
      draw_mountain()
      print("There is a mountain on the left lane.")

    elif (lands_index == 1):
      land.penup()
      land.goto(-105, 140)
      land.pendown()
      draw_forest()
      print("There is a forest on the left lane.")

    elif (lands_index == 2):
      land.penup()
      land.goto(-105, 140)
      land.pendown()
      draw_swamp()
      print("There is a swamp on the left lane.")

    else:
      land.penup()
      land.goto(-105, 140)
      land.pendown()
      draw_desert()
      print("There is a desert on the left lane.")


#Lane Obstacles
def right_obstacle():

  if (right_obstacle_index == 0):
    if (right_monsters_index == 0):
      if (health_points > 20):
        goblin_attack()

      else:
        goblin_defeat()

    elif (right_monsters_index == 1):
      if (health_points > 30):
        troll_attack()

      else:
        troll_defeat()

    elif (right_monsters_index == 2):
      if (health_points > 40):
        ogre_attack()

      else:
        ogre_defeat()

    else:
      if (health_points > 50):
        hydra_attack()

      else:
        hydra_defeat()

  else:
    if (right_lands_index == 0):
      if (health_points > 40):
        mountain_pass()
        
      else:
        mountain_fail()

    elif (right_lands_index == 1):
      if (health_points > 20):
        forest_pass()
        
      else:
        forest_fail()

    elif (right_lands_index == 2):
      if (health_points > 50):
        swamp_pass()
        
      else:
        swamp_fail()

    else:
      if (health_points > 40):
        desert_pass()
        
      else:
        desert_fail()


def left_obstacle():

  if (obstacle_index == 0):
    if (monsters_index == 0):
      if (health_points > 20):
        goblin_attack()

      else:
        goblin_defeat()

    elif (monsters_index == 1):
      if (health_points > 30):
        troll_attack()

      else:
        troll_defeat()

    elif (monsters_index == 2):
      if (health_points > 40):
        ogre_attack()

      else:
        ogre_defeat()

    else:
      if (health_points > 50):
        hydra_attack()

      else:
        hydra_defeat()

  else:
    if (lands_index == 0):
      if (health_points > 40):
        mountain_pass()
        
      else:
        mountain_fail()

    elif (lands_index == 1):
      if (health_points > 20):
        forest_pass()
        
      else:
        forest_fail()

    elif (lands_index == 2):
      if (health_points > 50):
        swamp_pass()
        
      else:
        swamp_fail()

    else:
      if (health_points > 40):
        desert_pass()
        
      else:
        desert_fail()


#Movements
def straight():
  s = 0
  vert = 5
  for s in range(35):
    player.clear()
    if (color in white):
      player.pencolor("black")
      player.fillcolor(color)
      player.begin_fill()
      player.penup()
      player.goto(0, -175 + vert)
      player.pendown()
      player.circle(25)
      player.end_fill()
      player.color("black")
      style = ("times new roman", 30, "bold")
      player.write(name, font = style, align = 'center')
      player.hideturtle()

    elif ((color == ("lightgray")) or (color not in colors)):
      player.pencolor("black")
      player.fillcolor(rand_color)
      player.begin_fill()
      player.penup()
      player.goto(0, -175 + vert)
      player.pendown()
      player.circle(25)
      player.end_fill()
      player.color("white")
      style = ("times new roman", 30, "bold")
      player.write(name, font = style, align = 'center')
      player.hideturtle()

    else:
      player.pencolor("black")
      player.fillcolor(color)
      player.begin_fill()
      player.penup()
      player.goto(0, -175 + vert)
      player.pendown()
      player.circle(25)
      player.end_fill()
      player.color("white")
      style = ("times new roman", 30, "bold")
      player.write(name, font = style, align = 'center')
      player.hideturtle()

    vert += 5
    time.sleep(0.05)


def move_right():
  straight()

  l = 0
  vert = 5
  move = 5
  for l in range(27):
    player.clear()

    if (color in white):
      player.pencolor("black")
      player.fillcolor(color)
      player.begin_fill()
      player.penup()
      player.goto(0 + move, 0 + vert)
      player.pendown()
      player.circle(25)
      player.end_fill()
      player.color("black")
      style = ("times new roman", 30, "bold")
      player.write(name, font = style, align = 'center')
      player.hideturtle()

    elif ((color == "lightgray") or (color not in colors)):
      player.pencolor("black")
      player.fillcolor(rand_color)
      player.begin_fill()
      player.penup()
      player.goto(0 + move, 0 + vert)
      player.pendown()
      player.circle(25)
      player.end_fill()
      player.color("white")
      style = ("times new roman", 30, "bold")
      player.write(name, font = style, align = 'center')
      player.hideturtle()

    else:
      player.pencolor("black")
      player.fillcolor(color)
      player.begin_fill()
      player.penup()
      player.goto(0 + move, 0 + vert)
      player.pendown()
      player.circle(25)
      player.end_fill()
      player.color("white")
      style = ("times new roman", 30, "bold")
      player.write(name, font = style, align = 'center')
      player.hideturtle()

    vert += 3
    move += 2.8
    time.sleep(0.05)


def move_left():
  straight()

  l = 0
  vert = 5
  move = 5
  for l in range(27):
    player.clear()

    if (color in white):
      player.pencolor("black")
      player.fillcolor(color)
      player.begin_fill()
      player.penup()
      player.goto(0 - move, 0 + vert)
      player.pendown()
      player.circle(25)
      player.end_fill()
      player.color("black")
      style = ("times new roman", 30, "bold")
      player.write(name, font = style, align = 'center')
      player.hideturtle()

    elif ((color == "lightgray") or (color not in colors)):
      player.pencolor("black")
      player.fillcolor(rand_color)
      player.begin_fill()
      player.penup()
      player.goto(0 - move, 0 + vert)
      player.pendown()
      player.circle(25)
      player.end_fill()
      player.color("white")
      style = ("times new roman", 30, "bold")
      player.write(name, font = style, align = 'center')
      player.hideturtle()

    else:
      player.pencolor("black")
      player.fillcolor(color)
      player.begin_fill()
      player.penup()
      player.goto(0 - move, 0 + vert)
      player.pendown()
      player.circle(25)
      player.end_fill()
      player.color("white")
      style = ("times new roman", 30, "bold")
      player.write(name, font = style, align = 'center')
      player.hideturtle()

    vert += 3
    move += 2.6
    time.sleep(0.05)


#User checks
def check_user():
  ans = input("Which lane do you wish to select? (l/r) ").lower().strip()
  if (ans.startswith("l") == True):
    move_left()
    left_obstacle()

  elif (ans.startswith("r") == True):
    move_right()
    right_obstacle()

  else:
    while ((ans.startswith("l")) == False and (ans.startswith("r") == False)):
      print("That is not a valid input ")
      ans = input("Which lane do you wish to select? (l/r) ").lower().strip()
      if (ans.startswith("l") == True):
        move_left()
        left_obstacle()

      if (ans.startswith("r") == True):
        move_right()
        right_obstacle()


def next_road():
  cont = input("Type (n) to continue ").lower().strip()
  if (cont == "n"):
    turtle.resetscreen()
    print()
  else:
    turtle.resetscreen()
    print()


#Boss
def boss_road():
  road.fillcolor("lightgray")
  road.begin_fill()
  road.penup()
  road.goto(-50, -200)
  road.pendown()
  road.fd(100)
  road.left(90)
  road.fd(400)
  road.left(90)
  road.fd(100)
  road.left(90)
  road.fd(400)
  road.end_fill()


def boss_move():
  s = 0
  vert = 5
  for s in range(50):
    player.clear()
    if (color in white):
      player.pencolor("black")
      player.fillcolor(color)
      player.begin_fill()
      player.penup()
      player.goto(0, -175 + vert)
      player.pendown()
      player.circle(25)
      player.end_fill()
      player.color("black")
      style = ("times new roman", 30, "bold")
      player.write(name, font = style, align = 'center')
      player.hideturtle()

    elif ((color == ("lightgray")) or (color not in colors)):
      player.pencolor("black")
      player.fillcolor(rand_color)
      player.begin_fill()
      player.penup()
      player.goto(0, -175 + vert)
      player.pendown()
      player.circle(25)
      player.end_fill()
      player.color("white")
      style = ("times new roman", 30, "bold")
      player.write(name, font = style, align = 'center')
      player.hideturtle()

    else:
      player.pencolor("black")
      player.fillcolor(color)
      player.begin_fill()
      player.penup()
      player.goto(0, -175 + vert)
      player.pendown()
      player.circle(25)
      player.end_fill()
      player.color("white")
      style = ("times new roman", 30, "bold")
      player.write(name, font = style, align = 'center')
      player.hideturtle()

    vert += 5
    time.sleep(0.05)


#Game over
def victory():
  turtle.bgcolor("black")

  over.color("limegreen")
  style = ("times new roman", 30, "bold")
  over.write("Game over", font = style, align = 'center')
  over.hideturtle()

  health_over.penup()
  health_over.goto(0, -50)
  health_over.pendown()
  health_over.color("limegreen")
  style = ("times new roman", 15, "bold")
  health_over.write("Health: " + str(health_points), font = style, align = 'center')
  health_over.hideturtle()

  gold_over.penup()
  gold_over.goto(0, -100)
  gold_over.pendown()
  gold_over.color("limegreen")
  style = ("times new roman", 15, "bold")
  gold_over.write("Gold: " + str(gold), font = style, align = 'center')
  gold_over.hideturtle()


def defeat():
  turtle.bgcolor("black")

  over.color("red")
  style = ("times new roman", 30, "bold")
  over.write("Game Over", font = style, align = 'center')
  over.hideturtle()

  gold_over.penup()
  gold_over.goto(0, -50)
  gold_over.pendown()
  gold_over.color("red")
  style = ("times new roman", 15, "bold")
  gold_over.write("Gold: " + str(gold), font = style, align = 'center')
  gold_over.hideturtle()


#Reset
def reset_stats():
  health.clear()
  money.clear()
  draw_health()
  draw_gold()




#Events
#Setup stats
draw_health()
draw_gold()


#Forked road
for i in range (4):
  if (health_points > 0):
    draw_road()
    draw_player()
    draw_health()
    draw_gold()

    right_obstacle_index = rand.randint(0, 1)

    obstacle_index = rand.randint(0, 1)

    right_monsters_index = rand.randint(0, 3)
    right_lands_index = rand.randint(0, 3)

    monsters_index = rand.randint(0, 3)
    lands_index = rand.randint(0, 3)

    right_monster = monsters[right_monsters_index]
    right_land = lands[right_lands_index]

    monster = monsters[monsters_index]
    land = lands[lands_index]

    left_lane()
    right_lane()

    check_user()
    reset_stats()
    next_road()

  else:
    turtle.resetscreen()
    defeat()


#Boss attacks
if (health_points > 0):
  boss_road()
  draw_player()
  draw_health()
  draw_gold()
  boss_index = rand.randint(0, 1)

  if (boss_index == 0):
    draw_dragon()
    boss_battle = input("The lair of the great dragon is in front of you. Do you wish to enter? \n(y/n) ")

    if (boss_battle.startswith("y") == True):
      reset_stats()

      if (health_points > 75):
        boss_move()
        dragon_attack()
        reset_stats()
        next_road()
        victory()

      else:
        boss_move()
        dragon_defeat()
        reset_stats()
        next_road()
        defeat()

    else:
      turtle.resetscreen()
      victory()

  else:
    draw_cave()
    boss_battle = input("There is a dark cave in front of you. Do you wish to enter? (y/n) ")

    if (boss_battle.startswith("y") == True):
      reset_stats()

      if (health_points > 70):
        boss_move()
        cave_pass()
        reset_stats()
        next_road()
        victory()

      else:
        boss_move()
        cave_fail()
        reset_stats()
        next_road()
        defeat()

    else:
      turtle.resetscreen()
      victory()


wn.mainloop()
