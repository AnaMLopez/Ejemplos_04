# encoding: UTF-8
# Autor: Roberto Martínez Román
# Ciclos

from random import randint
import pygame, math

def invertirNumero(n):
    '''
    Invierte el parámetro
    n: int
    return: Regresa otro entero con los digitos al revés
    '''
    inverso = 0

    while n>=10:
        digitoDer = n%10
        inverso = inverso*10 + digitoDer
        n = n//10

    inverso = inverso*10 + n

    return inverso


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
NEGRO = (0,0,0)


def dibujarEjes(ventana):
    pygame.draw.line(ventana,VERDE,(0,ALTO//2),(ANCHO,ALTO//2))
    pygame.draw.line(ventana,VERDE,(ANCHO//2,0),(ANCHO//2,ALTO))

'''
def dibujarFuncion(ventana):
    for angulo in range(-360,360):
        angRad = math.radians(angulo)
        y = int(100*math.sin(angRad))
        pygame.draw.circle(ventana,ROJO,(angulo+ANCHO//2,ALTO//2-y),2)

'''


def generarColorAzar():
    return (randint(0,255), randint(0,255), randint(0,255))


def dibujarFuncion(ventana):
    angulo = 0
    while angulo<360:
    #for angulo in range(0,360):
        angRad = math.radians(angulo)
        radio = int(300*math.cos(1024*angRad))
        x = int(radio*math.cos(angRad))
        y = int(radio*math.sin(angRad))
        colorAzar = generarColorAzar()
        pygame.draw.circle(ventana,colorAzar,(x+ANCHO//2,ALTO//2-y),2)
        angulo += 0.1


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(NEGRO)

        dibujarEjes(ventana)
        dibujarFuncion(ventana)


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()