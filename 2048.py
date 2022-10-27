# JUEGO 2048
import random

# Generación del tablero
def iniciar_juego():
    # Crea una matriz.
    filas=4
    columnas=4
    matriz=[]
    for f in range(filas):
        matriz.append([0]*columnas)
    return matriz

def imprimir_matriz(matriz):
    #Imprime la matriz
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%5d" %matriz[f][c], end="")
        print()

def estado_juego(matriz):
    # Esta función es la encargada de verificar que el jugador no haya perdido, caso contario, finaliza el juego
    # Si se da alguna de las 3 psobilidades que el usuario puede seguir jugando la funcion retorna False en caso contrario retorna false e imprime un mensaje
    sumador=0
    for f in range(4):
        for c in range(4):
            if (matriz[f][c]!=0):
                sumador+=1
    if(sumador!=16):
        return False
    for f in range(4):
        for c in range(3):
            if(matriz[f][c+1]==matriz[f][c]):
                 return False
    for f in range(3):
        for c in range(4):
            if(matriz[f+1][c]==matriz[f][c]): 
                return False
    
    print("El juego termino")
    print("Usted perdio :(")
    return True


def seleccionador_nuneros(matriz):
    # Posiciona un numero 2 en el tablero, siempre que este tenga el lugar(Incluye probabilidad de generar un 4)
    azarnum=random.randint(1,10)   
    if(azarnum<=8): azarnum=2
    else: azarnum=4
    k=0
    contador=0
    for f in range(4):
        for c in range(4):
            if(matriz[f][c]==0):
                contador+=1
    while(k==0 and contador!=0):
        lugar=random.randint(0,15)
        fila=int(lugar/4)
        columna=lugar%4
        if(matriz[fila][columna]==0):
            k=1
            matriz[fila][columna]=azarnum
            
# ARRIBA
def pasar_ceros_arriba(matriz):
    # Intercambia posicion entre los 0 y los numeros distintos a 0, dejando arriba los numeros distintos a 0 y abajo los 0 si es que los hay
    for f in range(1,4): #evita recorrer la primera fila 
      for c in range(4):
        aux=f
        while matriz[aux-1][c] == 0 and aux >= 1:
          box=matriz[aux-1][c]
          matriz[aux-1][c] = matriz[aux][c]
          matriz[aux][c]=box
          aux= aux - 1
    return matriz

def arriba(matriz):
    # Agrupa los numeros arriba,llamando antes a la función movimiento arriba analiza si en cada fila hay 2 iguales consecutivos, si es que hay los multiplica sino lo deja como esta y vuelve a agrupar los numeros distintos a 0 arriba
    matriz = pasar_ceros_arriba(matriz)
    for f in range(1,4): #evita recorrer la primera fila
      for c in range(4):
        if(matriz[f-1][c] == matriz[f][c]):
            matriz[f-1][c] = matriz[f-1][c] * 2      
            matriz[f][c] = 0
    matriz = pasar_ceros_arriba(matriz)
    seleccionador_nuneros(matriz)
    
    return matriz

# ABAJO
def pasar_ceros_abajo(matriz):
    # Intercambia posicion entre los 0 y los numeros distintos a 0, dejando abajo los numeros distintos a 0 y arriba los 0 si es que los hay 
    for f in range(2,-1,-1):
       for c in range(4):
        aux=f
        while(aux<=2 and matriz[aux+1][c]==0 ):
          box=matriz[aux+1][c]
          matriz[aux+1][c] = matriz[aux][c]
          matriz[aux][c]=box
          aux = aux+1
    return matriz  

def abajo(matriz):
    # hace llamado al la funcion movimiento abajo para arupar los numeros abajo, analiza si en cada fila hay 2 iguales consecutivos, si es que hay los multiplica sino lo deja como esta y vuelve a agrupar los numeros distintos a 0 abajo
    matriz = pasar_ceros_abajo(matriz)
    for f in range(2,-1,-1):
      for c in range(4):
        if(matriz[f+1][c] == matriz[f][c]):
            matriz[f+1][c]=matriz[f+1][c] * 2
            matriz[f][c]=0
    matriz = pasar_ceros_abajo(matriz)
    seleccionador_nuneros(matriz)
    return matriz

# IZQUIERDA
def pasar_ceros_izquierda(matriz):
    # Intercambia posicion entre los 0 y los numeros distintos a 0, dejando a la izquierda los numeros distintos a 0 y a la derecha los 0 si es que los hay
    for f in range(4):
      for c in range(1,4):    
        aux=c
        while matriz[f][aux-1] == 0 and aux >= 1:
          box=matriz[f][aux-1]
          matriz[f][aux-1] = matriz[f][aux]
          matriz[f][aux]=box
          aux = aux - 1
    return matriz

def izquierda(matriz):
    # Hace llamado al la funcion movimiento izquierda para arupar los numeros a la izquierda, analiza si en cada columna hay 2 iguales consecutivos, si es que hay los multiplica sino lo deja como esta y vuelve a agrupar los numeros distintos a 0 a la izquierda
    matriz = pasar_ceros_izquierda(matriz)
    for f in range(4):
      for c in range(0,3):
        if(matriz[f][c+1] == matriz[f][c]):
            matriz[f][c]=matriz[f][c] * 2
            matriz[f][c+1]=0
    matriz = pasar_ceros_izquierda(matriz)
    seleccionador_nuneros(matriz)
    return matriz
 
# DERECHA
def pasar_ceros_derecha(matriz):
    # Intercambia posicion entre los 0 y los numeros distintos a 0, dejando a la derecha los numeros distintos a 0 y a la izquierda los 0 si es que los hay
    for f in range(4):
      for c in range(2,-1,-1):    
        aux=c
        while (aux<=2 and matriz[f][aux+1]==0):
          box=matriz[f][aux+1]
          matriz[f][aux+1] = matriz[f][aux]
          matriz[f][aux] = box
          aux = aux + 1
    return matriz
  
def derecha(matriz):
    # Hace llamado al la funcion movimiento derecha para agrupar los numeros a la derecha, analiza si en cada columna hay 2 iguales consecutivos, si es que hay los multiplica sino lo deja como esta y vuelve a agrupar los numeros distintos a 0 a la derecha 
    matriz = pasar_ceros_derecha(matriz)
    for f in range(4):
      for c in range(2,-1,-1):
        if(matriz[f][c+1]==matriz[f][c]):
            matriz[f][c+1] = matriz[f][c+1] * 2
            matriz[f][c]=0 
    matriz = pasar_ceros_derecha(matriz)
    seleccionador_nuneros(matriz)
    return matriz


# VALIDACIONES   
def ganador(matriz):
    # comprueba el estado del juego, en caso de no haber llegado a 2048, nos avisa que el juego continua.
    for f in range(4):
        for c in range(4):
            if matriz[f][c] == 2048:
                p=True
                print("FELICITACIONES USTED GANO EL 2048")
                break


def validar_controles(): 
    # Verifica que el comando seleccionado corresponda con una acción en el juego. 
    jugada = input("Ingrese la jugada a realizar: ")
    jugadamayus = jugada.upper()
    while jugadamayus != "A" and jugadamayus != "W" and jugadamayus != "S" and jugadamayus != "D":
        print("Error, este control no existe, debe ser W,A,S,D")
        jugada = input("Ingrese la jugada a realizar: ")
        jugadamayus = jugada.upper()
    return jugadamayus


# PROGRAMA PRINCIPAL
print("BIENVENIDO AL JUEGO 2048:")
print("Para jugar se utilizan las teclas W, A, S, D","\n W mueve el tablero hacia arriba","\n S mueve el tablero hacia abajo", "\n A mueve el tablero hacia la izquierda", "\n D mueve el tablero hacia la derecha", "\n" )
matriz=iniciar_juego()
seleccionador_nuneros(matriz)
seleccionador_nuneros(matriz)
p=estado_juego(matriz)
imprimir_matriz(matriz)
while p != True:
    control = validar_controles()
    if control == "W":
        matriz = arriba(matriz)
        p=estado_juego(matriz)
        ganador(matriz)
        imprimir_matriz(matriz)
        
    elif control == "S":
        matriz = abajo(matriz)
        p=estado_juego(matriz)
        ganador(matriz)
        imprimir_matriz(matriz)
        
    elif control == "A":
        matriz = izquierda(matriz)
        p=estado_juego(matriz)
        ganador(matriz)
        imprimir_matriz(matriz)
        
    elif control == "D":
        matriz = derecha(matriz)
        p=estado_juego(matriz)
        ganador(matriz)
        imprimir_matriz(matriz)
    

print("-"*40)