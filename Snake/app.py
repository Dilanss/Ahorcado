import turtle 
import time
import random

posponer = 0.1

# Marcador
marcador = 0
Maximo_marcador = 0

# Pantalla 
wn = turtle.Screen()
wn.title("Juego de snake")
wn.bgcolor("Orange")
wn.setup(width = 600 , height = 600)
wn.tracer(0)

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("Green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

# Manzana
Manzana = turtle.Turtle()
Manzana.speed(0)
Manzana.shape("circle")
Manzana.color("Red")
Manzana.penup()
Manzana.goto(0,100)

# Segmento
Segmentos = []

# Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,260)

texto.write("Marcador: 0  Higth Score: 0 ", align = "center", font = ("Courier", 24, "normal"))
# Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"
    
    
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
    
# Mover con el teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()
    
    # Colisiones de la serpiente
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        
        # Borrar cuerpo
        for Segmento in Segmentos:
            Segmento.goto(10000,10000)
            
        # Limpiar rastro de cuerpo
        Segmentos.clear()
        
    # Comida colision
    if cabeza.distance(Manzana) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        Manzana.goto(x,y)
    
        Nuevo_Segmento = turtle.Turtle()
        Nuevo_Segmento.speed(0)
        Nuevo_Segmento.shape("square")
        Nuevo_Segmento.color("Red")
        Nuevo_Segmento.penup()
        Segmentos.append(Nuevo_Segmento)
        
        # Alimentar al marcador
        marcador += 10
        
        if marcador > Maximo_marcador:
            Maximo_marcador = marcador
        
        texto.clear()
        texto.write("Marcador: {}  Higth Score: {} ".format(marcador, Maximo_marcador), align = "center", font = ("Courier", 24, "normal"))
        
    
    # Mover el cupero de la serpiente
    totalSeg = len(Segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = Segmentos[index - 1].xcor()
        y = Segmentos[index - 1].ycor()
        Segmentos[index].goto(x,y)
    
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        Segmentos[0].goto(x,y)
        
    mov()
    
    # Colisiones del cuerpo
    for segmento in Segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
            # Esconder los segmentos
            for segmento in Segmentos:
                segmento.goto(10000,10000)
            
            Segmentos.clear()
            
            # Resetear marcador
            
            marcador = 0
            texto.clear()
            texto.write("Marcador: {}  Higth Score: {} ".format(marcador, Maximo_marcador), align = "center", font = ("Courier", 24, "normal"))
        
    time.sleep(posponer)