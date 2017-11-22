# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo dibujar un elemento animado

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)

NUM_IMAGENES = 8                    # Para las monedas cambien a 10
TIEMPO_ENTRE_FRAMES = 0.1           # Tiempo entre cada imagen de la animación
TIEMPO_TOTAL = NUM_IMAGENES * TIEMPO_ENTRE_FRAMES


def crearListaSprites():
    lista = []

    for i in range(NUM_IMAGENES):
        nombre = "imagenes/anima-"+str(i)+".png"        # coin- para las monedas
        imagen = pygame.image.load(nombre)
        sprAnimacion = pygame.sprite.Sprite()
        sprAnimacion.image = imagen
        sprAnimacion.rect = imagen.get_rect()
        sprAnimacion.rect.left = ANCHO//2-sprAnimacion.rect.width//2
        sprAnimacion.rect.top = ALTO//2-sprAnimacion.rect.height//2
        lista.append(sprAnimacion)

    return lista


def obtenerFrame(timerAnimacion, listaSprites):
    indice = int(timerAnimacion/TIEMPO_ENTRE_FRAMES)
    return listaSprites[indice]


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    # Animación del puma (sprites)
    listaSprites = crearListaSprites()
    timerAnimacion = 0

    # Fondo
    imagenFondo = pygame.image.load("imagenes/fondo.jpg")
    x = 0

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)
        ventana.blit(imagenFondo, (x,0))
        ventana.blit(imagenFondo, (ANCHO+x ,0))
        x -= 1
        if x <= -ANCHO:
            x = 0

        # Dibujar, aquí haces todos los trazos que requieras
        frameActual = obtenerFrame(timerAnimacion, listaSprites)
        ventana.blit(frameActual.image, frameActual.rect)

        pygame.display.flip()   # Actualiza trazos
        timerAnimacion += reloj.tick(40)/1000          # Tiempo exacto entre frames
        if timerAnimacion>=TIEMPO_TOTAL:
            timerAnimacion = 0

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()