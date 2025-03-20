import turtle
import random

screen = turtle.Screen()
screen.screensize(500, 500)
screen.bgcolor('black')

t = turtle.Turtle()

t.penup()
t.goto(0, 200)
t.pendown()
t.pencolor("White")
t.write("Background Color", font=("arial", 30, "normal"), align="center")

t.penup()
t.goto(-75, 100)
t.pendown()
t.pencolor("tan")
t.write("1. Tan", font=("arial", 20, "normal"), align="left")

t.penup()
t.goto(-75, 50)
t.pendown()
t.pencolor("Azure")
t.write("2. Azure", font=("arial", 20, "normal"), align="left")

t.penup()
t.goto(-75, 0)
t.pendown()
t.pencolor("AquaMarine")
t.write("3. Aqua Marine", font=("arial", 20, "normal"), align="left")

t.penup()
t.goto(-75, -50)
t.pendown()
t.pencolor("DarkKhaki")
t.write("4. Dark Khaki", font=("arial", 20, "normal"), align="left")

t.penup()
t.goto(0, -150)
t.pendown()
t.pencolor("White")
t.write("Choose One", font=("arial", 30, "normal"), align="Center")

choose = int(input("Enter a number :"))
if choose == 1:
    screen.bgcolor('tan')
elif choose == 2:
    screen.bgcolor('azure')
elif choose == 3:
    screen.bgcolor('aquamarine')
else:
    screen.bgcolor('darkkhaki')
t.clear()

t.penup()
t.goto(0, 0)
t.pendown()
t.pencolor("Black")
t.write("Enter your name", font=("arial", 30, "normal"), align="Center")

name = input("Enter a name: ")
t.clear()
# number1 = int(input("Enter a number: "))
# number2 = int(input("Enter another number: "))
operation = random.randint(1, 4)
operation = 4
if operation == 1:
    symbol = "+"
    number1 = random.randint(-100, 100)
    number2 = random.randint(-100, 100)
    solution = number1 + number2
elif operation == 2:
    symbol = "-"
    number1 = random.randint(-100, 100)
    number2 = random.randint(-100, 100)
    solution = number1 - number2
elif operation == 3:

    symbol = "*"
    number1 = random.randint(-10, 10)
    number2 = random.randint(-10, 10)
    solution = number1 * number2

elif operation == 4:
    symbol = "/"
    number1 = random.randint(-10, 10)
    number2 = random.randint(-10, 10)
    sign = random.randint(1, 2)
    if sign == 2:
        number2 = -1 * number2
    solution = number1 / number2

t.penup()
t.goto(0, 100)
t.pendown()
t.pencolor("purple")
t.write(name, font=("arial", 30, "normal"), align="center")

t.penup()
t.goto(-200, 0)
t.pendown()
t.pencolor("black")
t.write(number1, font=("arial", 30, "normal"), align="center")

t.penup()
t.goto(-100, 0)
t.pendown()
t.pencolor("black")
t.write(symbol, font=("arial", 30, "normal"), align="center")

t.penup()
t.goto(0, 0)
t.pendown()
t.pencolor("black")
t.write(number2, font=("arial", 30, "normal"), align="center")

t.penup()
t.goto(100, 0)
t.pendown()
t.pencolor("purple")
t.write("=", font=("arial", 30, "normal"), align="center")

answer = float(input("Enter Answer: "))

t.penup()
t.goto(200, 0)
t.pendown()
t.pencolor("black")
t.write(solution, font=("arial", 30, "normal"), align="center")

t.penup()
t.goto(0, -100)
t.pendown()
t.pencolor("black")
t.write("Your answer is: " + str(answer), font=("arial", 30, "normal"), align="center")
t.penup()
t.goto(0, 50)
t.pendown()
if solution == answer:
    screen.bgcolor('dodgerblue')
    t.pencolor("lime")
    t.write("Correct!", font=("arial", 30, "normal"), align="center")
else:
    screen.bgcolor('orange')
    t.pencolor("red")
    t.write("WRONG!", font=("arial", 30, "normal"), align="center")

    t.penup()
    t.goto(0, 0)
    t.pendown()

t.hideturtle()
turtle.done()


