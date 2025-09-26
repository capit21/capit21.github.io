import turtle
import math
import time

# Configuración de la ventana
turtle.setup(width=600, height=600)
turtle.bgcolor('#ffe4ec')

# Crear la tortuga
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(3)
t.color('#ff69b4')
t.up()

def dibujar_corazon():
    t.goto(0, -100)
    t.down()
    t.begin_fill()
    t.fillcolor('#ff69b4')
    for i in range(360):
        angle = math.radians(i)
        x = 16 * math.sin(angle) ** 3
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
        t.goto(x * 10, y * 10 - 100)
        time.sleep(0.005)
    t.end_fill()
    t.up()
    t.goto(0, 120)
    t.color('#ff69b4')
    t.write('¡Un corazón rosa para ti!', align='center', font=('Arial', 18, 'bold'))

# Animación
dibujar_corazon()
turtle.done()
