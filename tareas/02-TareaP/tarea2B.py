#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 13:56:06 2022
@subject: Visualización de la Información - Tarea 2
@author: Andrés Urbano Guillermo Gerardo
"""  
import turtle

def drawSquare(x, y, size, color):
    """Dibuja un cuadro"""
    global myLapiz
    myLapiz.setheading(0)
    
    #Alzar lápiz
    myLapiz.penup()
    myLapiz.goto(x,y)
    myLapiz.color(color)
    myLapiz.fillcolor(color)    
    
    #Bajar lápiz
    myLapiz.pendown()
    
    #Rellenar la figura del color:
    myLapiz.begin_fill()
    myLapiz.forward(size)
    myLapiz.right(90)
    myLapiz.forward(size)
    myLapiz.right(90)
    myLapiz.forward(size)
    myLapiz.right(90)
    myLapiz.forward(size)
    myLapiz.end_fill()

def drawCircle(x, y, radius, color):
    """Dibuja un circulo"""
    global myLapiz

    # Alzar Lápiz
    myLapiz.penup()

    myLapiz.color(color)
    myLapiz.fillcolor(color)

    # Moverse a pi
    myLapiz.goto(x, y - radius)

    # Dibuja el circulo
    myLapiz.begin_fill()
    myLapiz.circle(radius)
    myLapiz.end_fill()

    myLapiz.pendown()

turtle.title('Tarea 2 - Ejercicio B')
turtle.setup(800, 800)

myLapiz = turtle.Turtle()
myLapiz.shape('turtle')
myLapiz.pensize(2)
myLapiz.speed(8)

centrar = 100
left_corner = (-380+centrar, 350-centrar)
right_corner = (180+centrar, 350-centrar)

myLapiz.penup()
myLapiz.pencolor('grey')
myLapiz.fillcolor('grey')
myLapiz.begin_fill()
myLapiz.goto(*left_corner)
myLapiz.pendown()
myLapiz.goto(*right_corner)
myLapiz.goto(right_corner[0], 0-150)
myLapiz.goto(left_corner[0], 0-150)
myLapiz.goto(*left_corner)
myLapiz.end_fill()

# Colocamos el cursor al inicio
padding = 20
size = 57
radius = 10
myLapiz.penup()
initial_pos = [left_corner[0]+padding, left_corner[1]-padding]
current_pos = [initial_pos[0], initial_pos[1]]

grid = (5, 7)
for i in range(grid[0]):
    for j in range(grid[1]):
        drawSquare(*current_pos, size=size, color='black')
        if j < 6 and i < 4:
            drawCircle(current_pos[0]+size+2*radius, current_pos[1]-size,
                    radius=radius, color='white')
        current_pos[0] += size + padding
    current_pos[0] = initial_pos[0]
    current_pos[1] = initial_pos[1] - size*(i+1) - padding * (i+1) 

myLapiz.hideturtle()
turtle.done()


# ¿Todos los puntos blancos son realmente blancos?
# Nuevamente nuestra percepción nos engañan viendo los puntos cambiar de color
# de blanco a negro dandonos una iluasión que sean puntos negros. Pero viendo
# detenidamente podemos ver que son puntos blancos y corroborarando en nuestro
# codigo vemos que son precisamente definidos con un color blanco.

