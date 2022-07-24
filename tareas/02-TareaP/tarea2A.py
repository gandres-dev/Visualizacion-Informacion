#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 13:56:06 2022
@subject: Visualización de la Información - Tarea 2
@author: Andrés Urbano Guillermo Gerardo
"""
import turtle

def drawLine(xFrom, yFrom, xTo, yTo, color):
    """Dibuja una linea"""
    global myLapiz
    # Alzar el lápiz
    myLapiz.penup()
    myLapiz.color(color)

    # Establecer el punto (x,y) de origen:
    myLapiz.goto(xFrom, yFrom)

    # Bajar el lápiz
    myLapiz.pendown()

    # Moverse al segundo punto
    myLapiz.goto(xTo, yTo)

turtle.title('Tarea 2 - Ejercicio A')
turtle.setup(900, 800)
myLapiz = turtle.Turtle()
myLapiz.shape('turtle')
myLapiz.pensize(2)
myLapiz.speed(4)

left_corner = (-350, 350)
right_corner = (350, 350)
longitud = 70
current_pos = [left_corner[0], left_corner[1] - longitud]

myLapiz.penup()
myLapiz.goto(*current_pos)
flag = True
while flag:
    myLapiz.pendown()
    drawLine(*current_pos, -current_pos[0], -current_pos[1], color='black')
    myLapiz.goto(*current_pos)  # Return place
    myLapiz.penup()
    if current_pos[1] < left_corner[1]:
        current_pos[1] += longitud
    elif current_pos[0] < right_corner[0]:
        current_pos[0] += longitud
    else:
        current_pos[1] -= longitud
        myLapiz.goto(*current_pos)
        myLapiz.pendown()
        drawLine(*current_pos, -current_pos[0], -current_pos[1], color='black')
        myLapiz.goto(*current_pos)  # Return place
        myLapiz.penup()
        break
    myLapiz.goto(*current_pos)

myLapiz.penup()
space_y = 150
space_x = 30
myLapiz.pensize(4)
drawLine(left_corner[0]+space_x , left_corner[1]-space_y,
        right_corner[0]-space_x, left_corner[1]-space_y, color="purple")

myLapiz.penup()
drawLine(left_corner[0]+space_x , -left_corner[1]+space_y,
        right_corner[0]-space_x, -left_corner[1]+space_y, color="purple")

myLapiz.hideturtle()
turtle.done()

# ¿Son ambas líneas purpura perfectamente rectas?
# A primera instancia nuestro percepción ve las lineas un poco curveadas por 
# causa de las lineas negras que intersectan entre ella. Pero
# detenidamente podemos ver que ambas si son lineas rectas y podemos corroborar
# en el código, el cual definimos que las lineas moradas sean lineas rectas.

