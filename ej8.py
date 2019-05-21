import turtle


def main():
    largo = int(input("Largo de los cuadrados --> "))
    pisos = int(input("Cantidad de pisos --> "))

    largoDePaso = largo/2

    negro = turtle.Turtle()

    negro.penup() ##para que no dibuje cuando me muevo a (-40, 0)
    negro.setpos(0, -100)

    negro.shape("turtle")
    negro.color("green")
    negro.width(2)
    negro.speed(6)

    for i in range(pisos, 0, -1):
        if i == 1:
            dibujarPunta(negro, largo)
        else:
            ## pasos se relaciona con la cantidad de cuadrados que te quedan por hacer, ni idea porqué
            pasos = (i-1)*2-1

            irIzq(negro, pasos, largoDePaso)
            dibujarCuadradoIzq(negro, largo)
            volverDeIzq(negro, pasos, largoDePaso)

            irDer(negro, pasos, largoDePaso)
            dibujarCuadradoDer(negro, largo)
            volverDeDer(negro, pasos, largoDePaso)

            subir(negro, largo)
    turtle.done()
    return

def irIzq(turtle, pasos, largoDePaso):
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(pasos*largoDePaso)
    return

def volverDeIzq(turtle, pasos, largoDePaso):
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(pasos*largoDePaso)
    return

def irDer(turtle, pasos, largoDePaso):
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(pasos*largoDePaso)
    return

def volverDeDer(turtle, pasos, largoDePaso):
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(pasos*largoDePaso)
    return

def dibujarCuadradoIzq(turtle, largo):
    turtle.pendown()
    for lado in range(0, 4):
        turtle.forward(largo)
        turtle.right(90)
    return

def dibujarCuadradoDer(turtle, largo):
    turtle.pendown()
    for lado in range(0, 4):
        turtle.forward(largo)
        turtle.left(90)
    return

def subir(turtle, largo):
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(largo)
    return

def dibujarPunta(turtle, largo):
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(largo/2)
    turtle.right(90)
    for x in range(0,3):
        turtle.forward(largo)
        turtle.right(90)
    turtle.forward(largo/2)

if __name__=="__main__":
    main()