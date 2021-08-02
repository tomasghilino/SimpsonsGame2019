from principal import *
from configuracion import *
import random
import math



def lectura(archivo, subtitulo,n): #se queda solo con los subtitulo de cierta longitud y filtra
    textos=[]
    lineas = archivo.readlines()
    archivo.close()
    textos2=[]
    for i in range(len(lineas)):
        #verifico que la linea no empiece con numeros o espacios (\n). Si no es, lo agrego a textos
        if not lineas[i].startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',"\n")):
            textos.append(lineas[i])
    #Reemplaza las estructuras de texto indeseadas por ""
    for cadena in textos:
        cadena=cadena.replace("<i>","")
        cadena=cadena.replace("</i>","")
        cadena=cadena.replace("\n","")
        cadena=cadena.replace("www.argenteam.net","")
        cadena=cadena.replace(".","")
        cadena=cadena.replace("Subtitulos por aRGENTeaM","")
        textos2.append(cadena)
    #Elimina los ultimos dos espacios vacios de la lista
    textos2.pop(len(textos2)-2)
    textos2.pop(len(textos2)-1)
    #Verifica que la longitud de las palabras sea mayor a 3 (que no sean conectores)
    textos3=[]
    for i in range(len(textos2)):
        cont=1
        pos=i
        for carac in textos2[i]:
            if carac == " ":
                cont=cont+1
        if not(cont<=n):
            x=textos2[pos].lower()
            textos3.append(x)
    #Agregamos los subtitulos
    for linea in textos3:
        subtitulo.append(linea)

def esta(a,b,lista):
    for i in lista:
        if(a==i) or (b==i):
            return True
    return False

def seleccion(subtitulo):
    lista=[]
    #Buscamos la posicion inicial y final para el random
    posinicio=0
    posfinal=len(subtitulo)-2
    repetidas=[]
    #El while es para que solo tome 3 subtitulos (uno al azar, el siguiente, y otro)
    while len(lista) < 3:
        x=random.randint(posinicio,posfinal)
        x1=x+1
        x2=random.randint(posinicio,posfinal)
        #Verificar que los subtitulos no se repitan con la funcion "esta"
        while esta(x,x1,repetidas):
            x=random.randint(posinicio,posfinal)
            x1=x+1
        while x2 in repetidas:
            x2=random.randint(posinicio,posfinal)
        lista.append(subtitulo[x])
        lista.append(subtitulo[x1])
        lista.append(subtitulo[x2])
        repetidas.append(subtitulo[x])
        repetidas.append(subtitulo[x1])
        repetidas.append(subtitulo[x2])
    return lista

def puntos(n):
    #devuelve el puntaje, segun seguidilla
    if n == 1:
        return 2**n
    else:
        return -1

def procesar(palabraUsuario, mostrada,siguiente, otra, correctas):
    #chequea que sea correcta, que pertenece solo a la frase siguiente. Devuelve puntaje segun seguidilla
    if len(palabraUsuario) < 3:
        return -1
    else:
        if palabraUsuario in siguiente:
            return puntos(1)
        else:
            return puntos(0)