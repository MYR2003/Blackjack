#Examen - Ejercicio 2

def films_actor(archivo, actor): #Funcion que recibe el nombre de un actor y devuelve una lista con las peliculas en las que este participa
    archivo.seek(0) #Se reinicia la posicion del puntero
    linea = archivo.readline() #Se lee la primera linea
    resultados = [] 
    while linea != "": #Se ingresa a un ciclo el cual se rompe en caso de que se lean todas las lineas del archivo
        linea = linea.split(";") #Se separa la linea, creando una lista
        if linea[2] == actor: #En caso de que la columna que posee al actor coincida con el nombre ingresado se guarda el nombre de la pelicula en la lista de resultados
            resultados.append(linea[0])
        linea = archivo.readline() #Se lee la siguiente linea
    return resultados #Se devuelve la lista con los resultados

def partners(archivo, actor1, actor2): #Funcion que recibe el nombre de dos actores y devuelve las peliculas en las que han trabajado
    archivo.seek(0) #Se reinicia la posicion del puntero
    respuesta = []
    pelis_actor1 = films_actor(archivo, actor1) #Se hace uso de la funcion films_actor para el primer actor
    pelis_actor2 = films_actor(archivo, actor2) #Se hace uso de la funcion films_actor para el segundo actor
    for i in pelis_actor1: #Se ingresa a un ciclo for por cada pelicula del primer actor
        for e in pelis_actor2: #Dentro de este ciclo se ingresa a otro ciclo para las peliculas del segundo actor
            if i == e: #En caso de que las peliculas sean las mismas se añade a la lista de respuestas
                respuesta.append(i)
#    for i in pelis_actor1: #Se ingresa a un ciclo for para cada actor y cada pelicula se ingresa a una lista de respuestas
#        respuesta.append(i)
#    for e in pelis_actor2:
#        respuesta.append(e)
    return respuesta #Se devuelve la lista con las respuestas

def batman_vs_superman(archivo): #Funcion que crea un diccionario de años batman y superman
    archivo.seek(0) #Se reinicia la posicion del puntero
    super_diccionario = {} 
    linea = archivo.readline() #Se lee la primera linea
    resultados = []
    while linea != "": #un ciclo que lee toda informacion del archivo por lineas
        linea = linea.split(";") #Se separa la linea creando una lista
        personaje = linea[4].lower() #Al texto que contiene al personaje se le colocan las letras en minusculas
        if "batman" == personaje or "superman" == personaje: #En caso de que la pelicula contenga a "Batman" o "Superman" entra
            tupla = (linea[4], linea[1]) #Se crea una tupla con la informacion del año y el nombre de la pelicula
            resultados.append(tupla) #Se añade la tupla a la lista de resultados
        linea = archivo.readline() #Se lee la siguiente linea y en caso de terminar de leer el archivo se rompera el ciclo
    
    años = []
    for i in range(len(resultados)): #Un ciclo el cual añade todos los años en los que aparecen los personajes
        años.append(str(resultados[i][1]))
    
    años.sort() #Se ordena la lista con los años
    a = 1
    ultimo_año = años[0]
    while a != len(años): #Un ciclo que elimina los años repetidos
        if años[a] == ultimo_año: 
            años.pop(a)
        else:
            ultimo_año = años[a]
            a += 1

    for i in range(len(años)): #Se ingresa a un ciclo el cual define por cada uno de los años quien posee mas apariciones
        S = 0 #Se define la variable S para superman 
        B = 0 #Se define la variable B para batman
        for e in range(len(resultados)): #Se ingresa a un ciclo for por cada una de las peliculas en los resultados
            if resultados[e][1] == años[i]: #En caso de que el año de la pelicula y el año en la lista sean los mismos se ingresa aqui
                personaje = resultados[e][0].lower() #Se rescata el personaje y se transforma a minusculas
                if "batman" == personaje: #En caso de que sea batman se le suma 1 a B
                    B += 1
                if "superman" == personaje: #En caso de que sea superma se le suma 1 a S
                    S += 1

        if S > B and S != 0 and B != 0: #Tras salir del ciclo que chequea los resultados se ingresa a este if o el siguiente elif
            super_diccionario[años[i]] = "Superman" #En caso de que superman tenga mas apariciones se añade el año como la key y "superman" como el value
        elif B > S and S != 0 and B != 0: 
            super_diccionario[años[i]] = "Batman" #Y en caso de que batman tenga mas apariciones se añade el año como la key y "batman" como el value
    print(super_diccionario.items()) #Se imprimen las keys y sus respectivos values del diccionario recien creado como tuplas para mostrar el resultado
    return super_diccionario #Se devuleve el diccionario

with open("cast.csv") as archivo: #Se abre el archivo para lectura
    peliculas = films_actor(archivo, input("Ingrese el actor que busca: ")) #Se define peliculas como el resultado de la funcion films_actor
    print("El actor participa en las siguientes peliculas: ", peliculas) #Se imprime el resultado de la funcion recien utilizada
    peliculas_en_conjunto = partners(archivo, #Se define peliculas_en_conjunto como el resultado de la funcion partners 
                                     input("Ingrese el primer actor que busca: "), 
                                     input("Ingrese al segun actor que busca: "))
    print("Las peliculas en las que esos actores participan juntos son: ", peliculas_en_conjunto) #Se imprimen los resultados 
    diccionario = batman_vs_superman(archivo) #Se define diccionario como el resultado de el uso de la funcion batman_vs_superman