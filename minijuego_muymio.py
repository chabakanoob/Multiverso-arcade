import time
import random
import os

def win(party):
    if party[0] =="x" and party[1] =="x" and party[2] =="x" or party[0] =="x" and party[3] =="x" and party[6] == "x" or party[1] =="x" and party[4] =="x" and party[7] =="x" or party[2] =="x" and party[5] =="x" and party [8] =="x" or party[3] =="x" and party[4] =="x" and party[5] == "x" or party[6] =="x" and party[7] =="x" and party[8]=="x" or party[0] =="x" and party[4] =="x" and party[8] == "x" or party[2] =="x" and party[4] =="x" and party[6] == "x":
        return "user"
    
    elif party[0] =="o" and party[1] =="o" and party[2] =="o" or party[0] =="o" and party[3] =="o" and party[6] == "o" or party[1] =="o" and party[4] =="o" and party[7] =="o" or party[2] =="o" and party[5] =="o" and party [8] =="o" or party[3] =="o" and party[4] =="o" and party[5] == "o" or party[6] =="o" and party[7] =="o" and party[8]=="o" or party[0] =="o" and party[4] =="o" and party[8] == "o" or party[2] =="o" and party[4] =="o" and party[6] == "o":
        return "IA"
    else:
        return "draw"

def watchtablero(party):
    print("---------")
    print("|",party[0],party[1],party[2],"|")
    print("|-------|")
    print("|",party[3],party[4],party[5],"|")
    print("|-------|")
    print("|",party[6],party[7],party[8],"|")
    print("---------")

def usermoves(position,party):
    position -=1
    if  party[position]==" ":
        party[position]="x"
        return True

def brothers(position,party):

    #gracias a que siempre se repiten los mismos patrones para las combinaciones podemos encontrar 
    #las diferentes combinaciones con los diferentes hermanos posibles a cada casilla,iteraremos con las ordenes 
    #en las que usemos esta gran funcion para hacer un poco menos cazurro a chalino(IA)

    #right bro
    if position != 2 and position != 5 and position != 8:
        if party[position] == "o" and party[position+1] == " ":
            party[position+1] = "o"
            return True
    #left bro
    if position != 0 and position != 3 and position != 6:
        if party[position] == "o" and party[position-1] == " ":
            party[position-1] = "o"
            return True
    #top bro
    if position != 0 and position != 1 and position != 2:
        if party[position] == "o" and party[position-3] == " ":
            party[position-3] = "o"
            return True            
    #bottom bro
    if position != 6 and position != 7 and position != 8:
        if party[position] == "o" and party[position+3] == " ":
            party[position+3] = "o"
            return True
    #left top corner
    if position != 0 and position != 1 and position != 2 and position != 3 and position != 6:
        if party[position] == "o" and position[position-4] ==" ":
            party[position -4] = "o"
            return True
    #right top corner
    if position != 0 and position != 1 and position != 2 and position != 5 and position != 8:
        if party[position] == "o" and position[position-2] == " ":
            party[position-2] = "o"
            return True 

def iamoves(level,party):
    yahatirado=False
    if level == 1:
        succes = False
        while  not succes:  
            posision=random.choice([0,1,2,3,4,5,6,7,8])
            if party[posision] == " ":
                party[posision] = "o"
                succes=True
                yahatirado=True
    
    probability=1

    if level == 2:
        probability=random.choice([1,2,3,4])
    if level == 3:
        probability =random.choice([1,2])
    if level == 4:
        probability = 4
    
    if probability != 1:
        encontrado=False
        for x in range(9):
            if encontrado:
                break
            if party[x] == " ":
                party[x] = "o"
                if win(party) == "IA":
                    encontrado=True #este encontrado como true cortara el que siga dejando "o" ya que la IA sigue ganando y solo 1 ficha x tirada
                else:
                    party[x] = " "
        
        #si no ha podido ganar ,comporbará si puede taponar
        taponencontrado=False
        if not encontrado:
            for x in range(9):
                if taponencontrado:
                    break
                if party[x] == " ":
                    party[x] = "x"
                    if win(party) == "user":
                        taponencontrado = True
                        party[x] = "o"
                    else:
                        party[x] = " "

        #funcion iterativa MACHINE LEARNING 2

        #si no puede ganar ni taponarte,buscara comnbinacion con alguna ficha suya del tablero con la funcion brothers
        hermanoencontrado=False
        if not taponencontrado and not encontrado:
            for posicion in range(9):
                if hermanoencontrado:
                    break
                if brothers(posicion,party):
                    hermanoencontrado=True

        #si todo lo de antes no es viable,pondrá una ficha al azar en una casilla libre
        if not taponencontrado and not encontrado and not hermanoencontrado:
            succes = False
            while  not succes:  
                posision=random.choice([0,1,2,3,4,5,6,7,8])
                if party[posision] == " ":
                    party[posision] = "o" 
                    succes=True
    

    elif probability == 1 and not yahatirado:
        succes = False
        while  not succes:  
            posision=random.choice([0,1,2,3,4,5,6,7,8])
            if party[posision] == " ":
                party[posision] = "o"
                succes=True
    
def fullparty(party):
    succes=False
    for y in party:
        if y == " ":
            succes=True
    if succes:
        return True
    else:
        return False

def main():
    empty=" "

    tablero=[empty for x in range(9)]

    os.system("clear")

    print("\n\nbienvenido al juego del tres en raya\n\n");time.sleep(3)
    print("vas a jugar contra una IA,su nombre es CHALINO,tu eres la cruz y el es el circulo\n\n");time.sleep(3)
    print("Buena suerte,CHALINO es el campeon de tres en raya de su casa!\n\n");time.sleep(3)

    os.system("clear")

    dificultad=int(input("en que dificultad quieres jugar (1) facil (2) medio (3) dificil (4) veterano : "))

    while True:

        watchtablero(tablero)

        accion=int(input("introduce la posicion en la que quieres poner la 'x'  :  "))

        if not fullparty(tablero):
            break

        if usermoves(accion,tablero):
            if win(tablero) == "user":
                break

            watchtablero(tablero)

            if fullparty(tablero):

                iamoves(dificultad,tablero)
                print("la IA esta jugando...\n");time.sleep(1.5)
                os.system("clear")

                if win(tablero) == "IA":
                    break
            else:
                break

        else:
            print("posicion ocupada,prueba de nuevo...")

    if win(tablero) == "user":
        print("\nenhorabuena forro!!!!! ,ganaste\n\n")
        watchtablero(tablero)
        time.sleep(4)
        return True


    elif win(tablero) == "IA":
        print("\nsos remalo waxin,te gano el robot...valiste verga!\n\n")
        watchtablero(tablero)
        time.sleep(4)
        return False
    else:
        print("\nempate,los dos malisimos...\n\n")
        time.sleep(4)
        return False

