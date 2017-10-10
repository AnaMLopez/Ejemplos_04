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
    # pelota
    radio = 20
    x = ANCHO//2
    y = ALTO//2
    DX = 5
    DY = 3
    derecha = True
    abajo = True

    # Raqueta
    alturaRaqueta = ALTO//5
    anchoRaqueta = alturaRaqueta//4
    xRaqueta = 0
    yRaqueta = ALTO//2

    dyRaqueta = 20
    moverRaqueta = False

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
            # Pregunta si se oprimió alguna tecla
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN: # flecha abajo
                    dyRaqueta = +20
                    moverRaqueta = True
                if evento.key == pygame.K_UP:   # flecha arriba
                    dyRaqueta = -20
                    moverRaqueta = True
            if evento.type == pygame.KEYUP:     # se suelta la tecla
                moverRaqueta = False

        # Borrar pantalla
        ventana.fill(VERDE_BANDERA)

        # Dibujar, aquí haces todos los trazos que requieras
        # Pelota
        pygame.draw.circle(ventana, ROJO, (x, y), radio)
        # Raqueta
        pygame.draw.rect(ventana,ROJO,(xRaqueta,yRaqueta,anchoRaqueta,alturaRaqueta))

        # Actuliza la posición de la raqueta
        if moverRaqueta:
            yRaqueta += dyRaqueta

        # Actualiza la posición de la pelota
        if derecha:
            x += DX      # x = x + 3
        else:
            x -= DX

        if abajo:
            y += DY
        else:
            y -= DY

        # Prueba límites de la pelota
        if x>=ANCHO-radio: # or x<=radio:
            derecha = not derecha

        if y>=ALTO-radio or y<=radio:
            abajo = not abajo

        # prueba colision pelota-raqueta
        xc = x
        yc = y
        xr = xRaqueta
        yr = yRaqueta
        if xc>=xr and xc<=xr+anchoRaqueta:
            # colisiona horizontal
            if yc>=yr and yc<=yr+alturaRaqueta:
                # colisiona vertical
                derecha = True


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    rebotar()


main()