
# encoding: UTF-8
# Autor: Roberto Martínez Román
# Una carrera de tortugas, ¡prohibido apostar dentro del campus! :)

import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)


def dibujarPista(ventana):
    '''
    Dibuja la línea de arranque y la meta
    '''
    pygame.draw.rect(ventana,BLANCO,(64,50,10,ALTO-128))
    pygame.draw.rect(ventana, BLANCO, (ANCHO-10, 50, 10, ALTO - 128))


def dibujarCorredores(ventana,imagenLiebre, imagenTortuga, posicionLiebre, posicionTortuga):
    ventana.blit(imagenLiebre,posicionLiebre)
    ventana.blit(imagenTortuga,posicionTortuga)
    #Dibujar lineas, posición de la imagen + 64 (ancho)
    xLiebre = posicionLiebre[0]+64
    xTortuga = posicionTortuga[0]+64
    primerColor = ROJO
    segundoColor = BLANCO
    # Primer lugar siempre con línea blanca
    if xLiebre > xTortuga:
        primerColor = BLANCO
        segundoColor = ROJO

    pygame.draw.line(ventana, primerColor, (xLiebre,0), (xLiebre,ALTO))
    pygame.draw.line(ventana, segundoColor, (xTortuga, 0), (xTortuga, ALTO))


def moverCorredor(x):
    '''
    Actualiza la posición del corredor
    '''
    x += randint(0,3)
    return x


def dibujarGana(ventana,titulo):
    '''
    Muestra en la pantalla un mensaje de texto
    '''
    fuente = pygame.font.SysFont("monospace", 48)

    texto = fuente.render("¡Gana la "+titulo+"!", 1, BLANCO)
    ventana.blit(texto, (ANCHO//2-100, ALTO//2))


def dibujar():
    '''
    Simulación de una carrera de tortugas (¡20 tortugas!)
    '''
    # Imagen de fondo
    imagenFondo = pygame.image.load("pistaCarreras.jpg")
    # Imagen de tortugas
    imagenTortuga = pygame.image.load("tortuga.png")
    imagenLiebre = pygame.image.load("liebre.png")
    # Ubica a los competidores
    xTortuga = 0
    yTortuga = ALTO//3
    xLiebre = 0
    yLiebre = 2*ALTO//3

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
        ventana.blit(imagenFondo,(0,0))

        # Dibujar, aquí haces todos los trazos que requieras
        dibujarPista(ventana)
        dibujarCorredores(ventana,imagenLiebre, imagenTortuga, (xLiebre,yLiebre), (xTortuga,yTortuga),)

        if xLiebre>=ANCHO-74:
            # Gana liebre
            dibujarGana(ventana,"Liebre")
        elif xTortuga>=ANCHO-74:
            dibujarGana(ventana, "Tortuga")
        else:
            xLiebre = moverCorredor(xLiebre)
            xTortuga = moverCorredor(xTortuga)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(45)          # 45 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()
