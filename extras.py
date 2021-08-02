import pygame
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

#Cambiamos el tamano y colores de diferentes letras.
def dibujar(screen, palabraUsuario, lista, azar, puntos, segundos,correctas):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)
    defaultFontPalabraUser= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_PALABRA)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFontPalabraUser.render(palabraUsuario, 1, COLOR_TEXTO), (347, 550))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_PUNTOS), (680, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO)
    screen.blit(ren, (10, 10))

    #muestra el nombre de la Peli
    screen.blit(defaultFont.render("The Simpsons", 1, COLOR_PELI), (340,5))
    #Muestra la cantidad de seguidas
    screen.blit(defaultFont.render("Seguidas: " + str(correctas), 1, COLOR_SEGUIDAS), (350, 475))

    #muestra los subtitulos
    screen.blit(defaultFontGrande.render(lista[0], 1, COLOR_TEXTO), (ANCHO//2-len(lista[0])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*2))
    if azar==0:
        screen.blit(defaultFontGrande.render(lista[1], 1, COLOR_LETRAS), (ANCHO//2-len(lista[1])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*4))
        screen.blit(defaultFontGrande.render(lista[2], 1, COLOR_LETRAS), (ANCHO//2-len(lista[2])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*6))
    else:
        screen.blit(defaultFontGrande.render(lista[2], 1, COLOR_LETRAS), (ANCHO//2-len(lista[2])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*4))
        screen.blit(defaultFontGrande.render(lista[1], 1, COLOR_LETRAS), (ANCHO//2-len(lista[1])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*6))



#Esta funcion se encarga de dibujar la pantalla donde se muestra el puntaje total al finalizar el juego, ademas de que el usuario entre su nombre.
def dibujar_fin(screen,puntos,Usuario):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_FIN)
    defaultFontPalabraUser= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_PALABRA)
    screen.blit(defaultFontPalabraUser.render(Usuario, 1, COLOR_TEXTO), (347, 480))
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_PUNTOS), (230, 190))
    screen.blit(defaultFont.render("Fin del Juego",1,COLOR_TEXTO), (150,110))
    screen.blit(defaultFontPalabraUser.render("Ingrese su nombre:",1,COLOR_TEXTO), (245,400))

#un simple "esta", pero como ya usamos otro le pusimos "esta2"
def esta2(elemento,rankingnuevo):
    for e in rankingnuevo:
        if e == elemento:
            return True
    return False

#En base al puntaje ya escrito en el ranking.txt y con el nuevo input del usuario, ordena los puntajes de mayor a menor y sobreescribe el txt otra vez con estos.
def ordenar_puntaje():
    f=open("ranking.txt","r")
    ranking=f.readlines()
    nueva=[]
    ranking2=[]
    #Saber si hay una linea en el txt que empieza en blanco, si no empieza con blanco, agregamos todo a la lista ranking 2
    for i in range(len(ranking)):
        if not ranking[i].startswith(("\n")):
            ranking2.append(ranking[i])
    print(ranking2)
    #Verificamos los numeros para luego poder acomodarlos
    for linea in ranking2:
        cont=""
        for c in linea:
            if(c=="0" or c=="1" or c=="2" or c=="3" or c=="4" or c=="5" or c=="6" or c=="7" or c=="8" or c=="9"):
                cont=cont+c
        #Lista de numeros en el txt
        nueva.append(int(cont))
    f.close()
    #Ordenamos la lista de numeros
    ordenada=sorted(nueva,reverse=True)
    print(ordenada)
    ordenada.pop(len(ordenada)-1)
    #Buscamos los numeros en las lineas del archivo de texto, y si son lo mismo, agregamos la linea entera al rankingnuevo
    rankingnuevo=[]
    for n in ordenada:
        for elemento in ranking2:
            if (str(n) in elemento):
                #quitar las \n
                elemento=elemento.strip()
                if not esta2(elemento,rankingnuevo):
                    rankingnuevo.append(elemento)
    print(rankingnuevo)
    #Borramos el txt por completo, y escribimos los puntajes ordenados con su nombre y puntaje
    g=open("ranking.txt", "w")
    for elemento in rankingnuevo:
            g.write(elemento+"\n")
    g.close()

#Tuvimos un par de problemas en la funcion de ordenar puntaje, donde a veces en el txt quedaban mas de 5 lineas, pero resolvimos que siempre las primeras 5 son los mayores puntajes, por eso hicimos esta funcion.
def leerTop5():
    f=open("ranking.txt","r")
    archivo=f.readlines()[0:5]
    f.close()
    top5=[]
    for linea in archivo:
        linea=linea.strip()
        top5.append(linea.capitalize())
    return(top5)

#Se encarga de dibujar la pantalla final, donde se muestran los mayores puntajes historicos, lo hicimos mediante funciones basicas de pygame.
def dibujar_scores(screen,top_cinco):
    colorblanco=(255,255,255)
    fuente= pygame.font.Font( pygame.font.get_default_font(), 40)
    top1=top_cinco[0]
    top2=top_cinco[1]
    top3=top_cinco[2]
    top4=top_cinco[3]
    top5=top_cinco[4]
    screen.blit(fuente.render("- "+top1, 1, colorblanco), (235,200))
    screen.blit(fuente.render("- "+top2, 1, colorblanco), (235,250))
    screen.blit(fuente.render("- "+top3, 1, colorblanco), (235,300))
    screen.blit(fuente.render("- "+top4, 1, colorblanco), (235,350))
    screen.blit(fuente.render("- "+top5, 1, colorblanco), (235,400))

# Esta funcion muestra la primera pantalla que aparece al iniciar el juego, espera el enter del usuario para poner la variable "run" en
# True, y por ende arranca el juego. (el tiempo empieza a contar desde que se toca enter)
def inicio(screen,fondo_inicio):
    run=False
    while run==False:
        screen.blit(fondo_inicio,[0,0])
        pygame.display.flip()
        for e in pygame.event.get():
            #QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return()
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                if e.key == K_RETURN:
                    return True
    return False



