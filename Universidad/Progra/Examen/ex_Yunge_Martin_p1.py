#Examen - Ejercicio 1
import random

lista_palabras = []
while True: #Se crea un ciclo while el cual permite al usuario ingresar una lista personalizada de palabras para jugar
    print("Ingrese las palabras de la lista, en caso de terminar o no querer ingresar una lista personalizada presione enter")
    palabra_lista = input("Ingrese una palabra: ")
    if palabra_lista == "": #En caso de no ingresar nada se ingresa a un if el cual se rompera con la lista de palabras creada o en caso de no haber ingresado nada una lista predeterminada
        if lista_palabras == []:
            lista_palabras = ["Hacker", "Informatica", "Python", "Hackerank", 
                              "Examen", "Programacion", "Ingenieria", "Matematicas", ]
        break
    else:
        lista_palabras.append(palabra_lista)
        
letras_adivinadas = []

def palabras(lista_palabras): #Funcion la cual define una palabra de la lista de palabras de manera aleatoria como la palabra a adivinar
    n = len(lista_palabras)
    x = random.randrange(0, n) #Se define un numero aleatorio entre el 0 y la cantidad de caracteres en la lista de palabras
    return lista_palabras[x] #Se utiliza el numero obtenido como argumento de posicion para definir la palabra a adivinar de la lista

def existeletra(letra, palabra): #Funcion la cual verifica si existe una letra en la palabra a adivinar
    letra = letra.lower() #Se transforma la letra a minuscula 
    for i in palabra: #Se ingresa a un ciclo for el cual verifica para cada letra si es igual a la letra ingresada por el usuario
        if letra == i: #En caso de que la letra ingresada sea una letra de la palabra devuelve True
            return True
    return False #En caso de reviar todas las letras de la palabra y ninguna coincida devuelve False

def pantalla(palabra, letras_adivinadas): #Funcion que imprime en pantalla la palabra con las letras que se han adivinado y guiones bajos donde todavia no se adivine
    for i in palabra: #Se ingresa a un ciclo for el cual recorre cada letra de la palabra
        a = False #para cada ingreso se define una variable False
        for e in range(len(letras_adivinadas)): #Se ingresa a un ciclo for el cual recorre en rango de la cantidad de letras que se hayan adivinado
            if letras_adivinadas[e] == i:  #En caso de que alguna de las letras coincidan ase ingresa aqui
                a = True #Se redefine la variable como True
        if a: #En caso de que la variable se haya convertido a True se ingresa aqui
            print(i, end="") #Se imprime la letra
        else: #En caso de que la variable siga en False ingresa aqui
            print("_", end="") #Se imprime un guion bajo, debido a que no se ha adivinado la letra
        print(" ", end="") #Se imprime un espacio para separar cada una de las letras de la palabra
    return print(" ") #Se imprime un espacio para separar el texto de esta funcion del proximo (debido al comando end="", el cual juntaria los proximos textos)

def ganar(palabra, letras_adivinadas): #Funcion la cual define si se ha ganado o no
    a = 0 #Contador de letras coincidentes entre las letras adivinadas y la palabra a adivinar, se inicia en 0
    for i in palabra: #Se ingresa a un ciclo for el cual recorre las letras de la palabra
        b = True #Se crea una variable para evitar chequear 2 veces una misma letra
        for e in range(len(letras_adivinadas)): #Un ciclo for el cual se recorre para la cantidad de letras adivinadas
            if letras_adivinadas[e] == i and b: #En caso de que la letra no se haya contabilizado todavia se comparan las letras de la palabra y de las letras que se han adivinado
                a += 1 #En caso de que coincidan se suma uno al contador
                b = False #Y se redefine la variable como False, para no repetir el contador para esta letra
    if a == len(palabra): #En caso de que la cantidad de letras adivinadas y la cantidad de letras en la palabra sean las mismas se ingresa aqui
        return True #Se devuelve True
    else: #En caso contrario se ingresa aqui
        return False #Se devuelve False

def tresintentos(palabra): #Funcion que da tres intentos para adivinar la palabra
    a = 3 #Un contador de apoyo que ira diciendo la cantidad de intentos que le quedan al usuario
    for i in range(3):
        print("Le quedan", a, "intentos") #Se imprime un texto diciendo la cantidad de intentos que le quedan al usuario
        respuesta = input("Ingrese su intento: ") #Se ingrese el intento del usuario
        respuesta = respuesta.lower() #Se transforma a minusculas
        if respuesta == palabra: #En caso de que la respuesta y la palabra sean iguales se ingresa aqui y se da por ganado el juego
            print("HAS ACERTADO") 
            return True #Se devuelve True
        a -= 1 #Se disminuye el contador
    print("NO HAS ACERTADO") #En caso de completar los 3 intentos y no haber acertado se imprime que no acerto
    return False #Se devuelve False

palabra = palabras(lista_palabras) #Se hace uso de la funcion que selecciona una palabra a adivinar
palabra = palabra.lower() #Se convierten todas las letras a minusculas
errores = 0 #Se crea un contador de erroes, inicia en 0
win = False
while errores != 5 and not win: #Se ingresa a un ciclo while el cual se mantiene mientras la variable win sea False y mientras la cantidad de errores sea menor a 5
    letra = input("Ingrese letra: ") #Se pide la letra a adivinar
    adivinada = existeletra(letra, palabra) #Se hace uso de la funcion que verifica si se a adivinado o no
    if adivinada == False: #En caso de que no se adivine la letra se suma un error
        errores += 1
    else: #En caso contrario la letra se añade a una lista de letras adivinadas
        letras_adivinadas.append(letra)
    pantalla(palabra, letras_adivinadas) #Se hace uso de la funcion que imprime en pantalla las letras que se han adivinado y guiones bajos en caso de que la letra todavia no se haya adivinado
    win = ganar(palabra, letras_adivinadas) #Se utiliza la funcion ganar para verificar si se a adivinado la palabra
    print("Llevas", errores, "errores") #Se imprimen la cantidad de errores del usuario

if not win: #En caso de que no se haya ganado todavia se ingresa a la funcion de tresintentos
    win = tresintentos(palabra) 
else: #En caso de haber adivinado se felicita al usuario por adivinar
    print("HAS ACERTADO!!!")