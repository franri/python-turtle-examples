import turtle
import tkinter

def main():
    negro = turtle.Turtle()
    
    negro.shape("turtle")
    negro.color("green")
    negro.width(2)

    loop(negro)
    while True:
        s = input("Quiere dibujar otra figura?")
        if s == "S":
            loop(negro)
        else:
            break


def loop(turtle):
    
    turtle.clear()

    lado = int(input("Cantidad de lados --> "))
    largo = int(input("Largo --> "))
    cantidad = int(input("Cantidad de figuras --> "))

    drawshape(turtle, lado, largo, cantidad)



def drawshape(turtle, lado, largo, cantidad):
    alpha = 360/lado
    beta = 360/cantidad

    for x in range(cantidad):
        for y in range(0, lado):
            turtle.forward(largo)
            turtle.right(alpha)
        turtle.right(beta)
    return

if __name__=="__main__":
    main()