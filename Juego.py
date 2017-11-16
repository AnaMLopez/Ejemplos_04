# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)


def dibujarMenu(ventana, btnJugar):
    ventana.blit(btnJugar.image, btnJugar.rect)


def dibujarJuego(ventana, btnJugar, lista, listaBalas):
    btnJugar.rect.left = ANCHO-btnJugar.rect.width
    btnJugar.rect.top = ALTO-btnJugar.rect.height
    ventana.blit(btnJugar.image, btnJugar.rect)
    # Dibujamos TODOS los enemigos
    for enemigo in lista:
        ventana.blit(enemigo.image, enemigo.rect)
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def actualizarBalas(listaBalas, listaEnemigos):
    for bala in listaBalas:
        bala.rect.top -= 20
    for e in listaEnemigos:
        e.rect.top += 1
    # Eliminar balas fuera de la pantalla
    for k in range(-1,-len(listaBalas)-1,-1 ):
        if listaBalas[k].rect.top <= -16:
            listaBalas.remove(listaBalas[k])
    # Verificar colisiones
    for bala in listaBalas:
        borrarBala = False
        for enemigo in listaEnemigos:

            if bala.rect.colliderect(enemigo):
                # Le pegó!!!!!!!!!!
                # INCORRECTO !!!!!!!!!!!
                listaEnemigos.remove(enemigo)
                borrarBala = True
                break   # detener el CICLO for
        if borrarBala:
            listaBalas.remove(bala)


def generarEnemigos(listaEnemigos, imgBotonJugar):
    for x in range(3):
        for y in range(4):
            cx = 10 + x*260
            cy = 50 + y*100
            nuevo = pygame.sprite.Sprite()
            nuevo.image = imgBotonJugar
            nuevo.rect = imgBotonJugar.get_rect()
            nuevo.rect.left = cx
            nuevo.rect.top = cy
            listaEnemigos.append(nuevo)



def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    # Estados
    estado = "menu"     # jugando, termina

    # Botones
    imgBotonJugar = pygame.image.load("botonJugar.png")
    btnJugar = pygame.sprite.Sprite()   # SPRITE
    btnJugar.image = imgBotonJugar
    btnJugar.rect = imgBotonJugar.get_rect()
    btnJugar.rect.left = ANCHO//2 - btnJugar.rect.width//2
    btnJugar.rect.top = ALTO//2 - btnJugar.rect.height//2

    # Enemigos
    listaEnemigos = []
    generarEnemigos(listaEnemigos, imgBotonJugar)

    # Balas
    listaBalas = []
    imgBala = pygame.image.load("bala.jpg")

    timer = 0

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xb, yb, anchoB, altoB = btnJugar.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            estado = "jugando"
                elif estado == "jugando":
                    nuevo = pygame.sprite.Sprite()
                    nuevo.image = imgBotonJugar
                    nuevo.rect = imgBotonJugar.get_rect()
                    nuevo.rect.left = xm
                    nuevo.rect.top = ym
                    listaEnemigos.append(nuevo)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    # crear bala
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = ANCHO//2
                    bala.rect.top = ALTO-bala.rect.height
                    listaBalas.append(bala)

        # Borrar pantalla
        ventana.fill(BLANCO)

        timer += 1/40
        if timer > 2:
            # Acciones
            timer = 0

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            dibujarMenu(ventana, btnJugar)
        elif estado == "jugando":
            actualizarBalas(listaBalas, listaEnemigos)
            dibujarJuego(ventana, btnJugar, listaEnemigos, listaBalas)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()