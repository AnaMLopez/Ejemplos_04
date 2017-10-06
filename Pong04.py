# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame

# Dimensiones de la pantalla
ANCHO = 600
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

def rebotar():
    '''
    Mueve la pelota dentro de los límites de la pantalla
    '''

    # Pelota
    radio = 20
    x = ANCHO//2
    y = ALTO//2
    DX = 10
    DY = 6
    derecha = True
    abajo = True

    # Raqueta
    alturaRaqueta = ALTO//5
    anchoRaqueta = alturaRaqueta//4
    xRaqueta = 0    # No se mueve en x
    yRaqueta = ALTO//2

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
        ventana.fill(VERDE_BANDERA)

        # Dibujar. Aquí haces todos los trazos que requieras
        # Dibujar pelota
        pygame.draw.circle(ventana, ROJO, (x, y), radio)

        # Dibujar raqueta
        pygame.draw.rect(ventana,ROJO,(xRaqueta,yRaqueta,anchoRaqueta,alturaRaqueta))

        # Prueba si la pelota llega a los límites
        if derecha:
            x += DX      # x = x + 3
        else:
            x -= DX

        if abajo:
            y += DY
        else:
            y -= DY

        # ***** Falta probar colisión entre raqueta y pelota *****

        if x>=ANCHO-radio: # or x<=radio:   # 'abrimos' la pared izquierda :)
            derecha = not derecha

        if y>=ALTO-radio or y<=radio:
            abajo = not abajo

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(60)          # 60 fps

    pygame.quit()   # termina pygame


def main():
    rebotar()


main()