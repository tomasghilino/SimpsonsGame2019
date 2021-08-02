#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *

from funcionesVACIAS import *

#Funcion principal
def main():
    #Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.init()

    #Preparar la ventana
    pygame.display.set_caption("Subtimpsons...")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    #Cargamos las imagenes de los fondos
    fondo_inicio=pygame.image.load("Imagenes/fondo_inicio.jpg")
    fondo = pygame.image.load("Imagenes/fondo.jpg")
    fondo_fin= pygame.image.load("Imagenes/fondo_final.jpg")
    ranking_fondo=pygame.image.load("Imagenes/ranking.jpg")

    #Cargamos Sonidos:
    pygame.mixer.music.load("Sonidos/SimpsonsSong.mp3")
    Correcto=pygame.mixer.Sound("Sonidos/correcto.wav")
    Incorrecto=pygame.mixer.Sound("Sonidos/incorrecto.wav")

    #Iniciamos la cancion, mas adelante ponemos para que suene correcto e incorrecto (segun si le pega o no a la respuesta)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    #Esta funcion muestra la pantalla de inicio, cuando el usuario toca ENTER, se cumple el True y se sigue con el codigo del juego.
    if inicio(screen,fondo_inicio):

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        #Variables que usaremos para las funciones basicas del juego
        puntos = 0
        palabraUsuario = ""

        subtitulo=[]
        correctas=0

        #saber si el juego termino (usado mas adelante)
        fin=False

        archivo= open("TheSimpsons.srt","r")

        #lectura del archivo y filtrado de caracteres especiales
        lectura(archivo, subtitulo, N)

        #elige unsubtitulo al azar, su siguiente y otro
        lista=seleccion(subtitulo)

        azar=random.randrange(2)

        screen.blit(fondo,[0,0])
        dibujar(screen, palabraUsuario, lista, azar, puntos, segundos,correctas)

        pygame.display.update()



        while segundos > fps/1000 :

        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3


            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        #chequea si es correcta y suma o resta puntos
                        sumar=procesar(palabraUsuario, lista[0], lista[1], lista[2],correctas)


                        if sumar<=0:
                               #Como le erro suena incorrecto
                               Incorrecto.play()
                               correctas=0
                               multiplicar=1
                               puntos+=sumar*multiplicar

                        else:
                                #Como acerto suena correcto
                                Correcto.play()
                                correctas=correctas+1
                                multiplicar=1
                                puntos+=sumar*multiplicar

                        # Cuando llega a una cantidad de aciertos, se aumenta el multiplicador

                        if correctas>3:
                            Correcto.play()
                            multiplicar=2
                            puntos+=sumar*multiplicar



                        #elige un subtitulo al azar, su siguiente y otro
                        lista=seleccion(subtitulo)
                        palabraUsuario = ""
                        #cambia el orden al azar
                        azar=random.randrange(2)

            segundos = TIEMPO_MAX - totaltime/1000
            #Fin del juego
            fin=True

            #Limpiar pantalla anterior
            screen.blit(fondo, [0, 0])


            #Dibujar de nuevo todo
            dibujar(screen, palabraUsuario, lista, azar, puntos, segundos,correctas)
            pygame.display.flip()


        #Agregamos una pantalla final al juego, donde se ingresa su nombre y muestra el score
        Ranking=False
        f=open("ranking.txt","a")
        Usuario=""
        while fin:
            #Dibujamos toda la pantalla final
            screen.blit(fondo_fin,[0,0])
            dibujar_fin(screen,puntos,Usuario)
            pygame.display.flip()
            for e in pygame.event.get():
                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    Usuario += letra
                    if e.key == K_BACKSPACE:
                        Usuario = Usuario[0:len(Usuario)-1]
                    #Si el usuario toca enter, agrega al txt su nombre de usuario y ordena el puntaje. Tambien salta a la pantalla de highscores.
                    if e.key == K_RETURN:
                        fin=False
                        #Termina esta pantalla y se activa la pantalla de "ranking"
                        Ranking=True
                        if puntos > 0:
                            f.write("\n"+Usuario+" "+str(puntos))
                            f.close()
                            ordenar_puntaje()
            dibujar_fin(screen,puntos,Usuario)
        #Lee los primeros top 5 puntajes con su nombre de usuario
        top_cinco=leerTop5()

        #Comienzo de la ultima pantalla donde se muestran los maximos puntajes:
        while Ranking:
            screen.blit(ranking_fondo,[0,0])
            dibujar_scores(screen,top_cinco)
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    #Si se presiona ENTER, se sale del juego.
                    if e.key == K_RETURN:
                        pygame.quit()
                        sys.exit()
                    #Si presiona la letra "p" , se vuelve a llamar a la funcion main(), por lo cual el juego "arranca" de nuevo.
                    if e.key == K_p:
                        main()
                if e.type == QUIT:
                    pygame.quit()
                    return
            dibujar_scores(screen,top_cinco)

        archivo.close()

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
