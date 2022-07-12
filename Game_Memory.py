import random
def pantalla():     #Función que muestra el tablero en pantalla
    mat = []
    c=0
    lista = [" ",0,1,2,3,4,5]
    for i in range(7):
        fila = [c]
        for x in range (6):
            fila.append("*")
        mat.append(fila)
        c += 1
    for x in lista:
        print(x," ",end="",sep='\t')
    print("")
    for x in range (6):
        for y in range (7):
            print(mat[x][y]," ",end="",sep='\t')
        print("")
    return (mat)
def Tablero ():    #Función que hace el tablero con número aleatorios
    lista = []
    lista2 = []
    for x in range (1,19):
        lista.append(x)
        lista2.append(x)
    listafin = lista + lista2
    random.shuffle(listafin)
    mat = []
    li = 0
    ls = 6
    for x in range (6):
        lista = []
        for y in range (li,ls):
            if ls < 37 :
                lista.append(listafin[y])
        mat.append(lista)
        li += 6
        ls += 6
    return mat
def gamer():        #Función que controla a los jugadores
    if jugador%2 != 0:
        print("Turno jugador 1")
    else:
        print("Turno jugador 2")        
def cartas():       #Función que se encarga de pedir los valores de las cartas
    print("Carta 1")
    opt1 =-0.5
    opt2 = -0.5
    while opt1 < 0 or opt1 > 5:
        opt1 = int(input("Renglon de carta 1: "))
    while opt2 < 0 or opt2 >5:
        opt2 = int(input("Columna de carta 1: "))
    carta1 = tab[opt1][opt2]
    carta1 = int(carta1)
    print("Elegiste "+str(carta1))
    print("Carta 2")
    opt3 = -1
    opt4 = -1
    while (opt3 < 0 or opt3 >5):
        opt3 = int(input("Renglón de carta 2: "))
    while (opt4 < 0 or opt4 >5):
        opt4 = int(input("Columna de carta 2: "))
    if opt1 == opt3 and opt2 == opt4:
        print("Ya escogiste esas cartas, ingresa de nuevo los valores")
        while (opt1 == opt3):
            opt3 = int(input("Renglón de carta 2: "))
        while (opt2 == opt4):
            opt4 = int(input("Columna de carta 2: "))    
    carta2 = tab[opt3][opt4]
    carta2 = int(carta2)
    print("Elegiste "+str(carta2))
    opt2 += 1
    opt4 += 1
    return carta1, carta2, opt1, opt2, opt3, opt4
    
contador = 0
c1 = 0
c2 = 0
jugador = 1
print("""¡Bienvenido a "Memorandum"! un juego que te ayudará a mejorar tus\n tus habilidades cognitivas, reta a un amig@ y ¡¡¡que el juego comience!!!""")
tab = Tablero()
a = pantalla()          
while True:
    gamer ()
    carta1, carta2, opt1, opt2, opt3, opt4 = cartas()
    if(carta1 == carta2):
        if jugador%2 != 0:
            a[opt1][opt2] = carta1
            a[opt3][opt4] = carta2
            lista = [" ",0,1,2,3,4,5]
            for x in lista:
                print(x," ",end="",sep='\t')
            print("")
            for x in range (6):
                for y in range (7):
                    print(a[x][y]," ",end="",sep='\t')
                print("")
            print("¡¡¡Haz acertado!!!")
            c1 += 1
            contador += 1
            if contador == 18: #En caso de que todas las cartas sean descubiertas, el juego termina automaticamente
                break
            pregunta = (input("¿Desea seguir jugando? si/no: ")).lower() #Condición para seguir jugando
            while pregunta != 'si' and pregunta != 'no':
                pregunta = (input("¿Desea seguir jugando? si/no: ")).lower()    
            if pregunta == 'no':
                break
        elif jugador%2 == 0:
            a[opt1][opt2] = carta1
            a[opt3][opt4] = carta2
            lista =[" ",0,1,2,3,4,5]
            for x in lista:
                print(x," ",end="",sep='\t')
            print("")
            for x in range (6):
                for y in range (7):
                    print(a[x][y]," ",end="",sep='\t')
                print("")
            print("¡¡¡Haz acertado!!!")
            c2 += 1
            contador += 1
            if contador == 18:
                break
            pregunta = (input("¿Desea seguir jugando? si/no: ")).lower()
            while pregunta != 'si' and pregunta != 'no': #Si el usuario ingresa un valor no válido
                pregunta = (input("¿Desea seguir jugando? si/no: ")).lower()    
            if pregunta == 'no':
                break       
    else:
        lista = [" ",0,1,2,3,4,5]
        for x in lista:
            print(x," ",end="",sep='\t')
        print("")
        for x in range (6):
            for y in range (7):
                print(a[x][y]," ",end="",sep='\t')
            print("")
        if contador == 18:
            break
        pregunta = (input("¿Desea seguir jugando? si/no: ")).lower()
        while pregunta != 'si' and pregunta != 'no': #Si el usuario ingresa un valor no válido
            pregunta = (input("¿Desea seguir jugando? si/no: ")).lower()
        if pregunta == 'no':
            break
    jugador +=1   
print("El jugador uno tiene "+str(c1)+" pares destapados")
print("El jugador dos tiene "+str(c2)+" pares destapados")
if c1 > c2:
    print("¡¡El jugador uno gana!!")
elif c2 > c1:
    print("¡¡El jugador dos gana!!")
elif c2 == c1 and pregunta != 'no':
    print("¡¡Hubo un empate!!!")
