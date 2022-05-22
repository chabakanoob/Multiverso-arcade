##import clases as cl
import random, time

### ------------------------------------------------------------------------------------------------------
### ---------------------- El Claro de los Sueños
##
### ----------------- items
### ---------------------- ( a ) ataque
##cohete_propulsor = cl.Items("Cohete Propulsor","a",random.randrange(50,100),"Con este cohete haras mucho daño", 1 )
### ---------------------- ( s ) sanacion
##hada_lagrimas = cl.Items("lagrimas de Hada","s",random.randrange(15,30),"Esta bebida mejora la salud",1)
### ---------------------- ( a ) ataque
##red_pot = cl.Items("Bote Hoodlum Red","a",random.randrange(10,20),"Con la tecnologia hoodlum podras golpear más fuerte",1)
### ---------------------- ( sk ) 2 turnos
##yellow_pot = cl.Items("Bote Hoodlum Amarillo","sk",0,"Con la tecnologia hoodlum tienes un gorrocoptero para luchar otro dia",1)
### ---------------------- ( p ) precision
##green_pot = cl.Items("Bote Hoodlum Verde","p",30,"Con la tecnologia hoodlum tienes obtendrás mayor precision",1)
##
### ---------------------- villanos
###                     Nombre, Vida, Ataque, Defensa, Precision, Velocidad
##
##hoodlum = cl.Mob('Hoodlum', 100, 20, 20, 10, 20)
##dark_lum = cl.Mob('Lum Oscuro', 120,10,5,20,20)
##dark_rayman = cl.Mob('Rayma Oscuro',50,25,20,35,20)
##
### ---------------------- dimension
##dimension_claro_de_los_sueños = cl.Dimension("El Claro de los Sueños", [ cohete_propulsor, hada_lagrimas, red_pot, yellow_pot, green_pot], [ hoodlum, dark_lum, dark_rayman ] )
##
##
###homero = cl.Jugador("homero",100,40,50,50,20,[ bola_demolicion, donut_envenenado, golpe_borracho ] )
##
##
##golpe_cargado = cl.Habilidades("Golpe Cargado","normal", (15,30), " Golpe cargado de tipo normal que hace Rayman")
##golpe_envenenado = cl.Habilidades("Envenenamiento","veneno",(5,10),"Gracias a Leptys, Rayman puede envenenar a un enemigo")
##golpe_ocasional = cl.Habilidades("Golpe Ocasional","normal",(0,50),"Rayman reune energias para asestar un golpe que puede ser muy potente")
##
##rayman = cl.Jugador('Anonymus',150,45,50,50,25, [ golpe_cargado, golpe_envenenado,  golpe_ocasional ] )
##
##
##dimensiones = [ dimension_c137, dimension_fondo_de_bikini, dimension_claro_de_los_sueños ]
##

#Minijuego de Reflux

def reflux():
    
    class Codigo():
        
        def __init__(self):

            self.codigo = self.generar_codigo()
            
            self.lista_mostrar = self.mostrar_codigo()

            self.acertadas = []

        def incrementar(self,x):
            self.acertadas.append(x)
            
        def generar_codigo(self):
            dic = []
            x = random.choice( [ '1234', '1432', '3421', '4213' ] )
            y =  random.choice( [ '5678', '5876', '7865', '8657' ] )
            z =  random.choice( [ '9356', '7469', '5219', '3789' ] )

            dic = '-'.join([x,y,z])
            return dic
        
        def  mostrar_codigo(self):
            backup = ''
            backup = self.codigo
            
            backup = backup.replace('-',' ')
                    
            for j in range(0,len(backup)):
                #print( backup[ j ], type( backup[ j ] ) )

                if backup[ j ] != ' ':
                    if backup[ j ] in '123456789':
                        backup = backup.replace( str( backup[ j ] ), '-' )
                   
            #print(backup)
            return backup

    def  pide_nums ():
        ok = 0
        try:
            
            x1 = input('Dime un número del 1 -- 9 : ')
            x1 = int(x1)
            
            if x1 in range(1,10):
                ok += 1
                
            if ok == 1:
                return x1
            
            else:
                print('\n\nNumeros Invalidos ',x1,'\n\n')
                pide_nums()
            
        except Exception:
            d = '\n valor no  válido : '+' '+str(x1)+' '+'\n\n'
            print(d)
            pide_nums()
            

    def  comprovar_vida(x):
        if x <= 0:
            return False
        
    def coincidencia( num, ocul, cod, reflux):

        lista = list(ocul)
        
        for i in range(0,14):
            
            if( cod[i] != '-' and ocul[i] != ' '):  #Mientras el resultado del indice sea un caracter extraño
                                                                      # El código no se ejecuta
                if str(num) in cod:
                    
                    if cod[i] == str(num):
                        
                            lista[i] = str(num)
                            x = random.randrange(30,55)
                            print('\n\nGolpeas a Reflux con ',x,'de daño')
                            reflux -= x
            else:
                continue    # Pasa a la siguiente iteración
                            
        j = "".join(lista)

        return j, reflux
    
    def comprovar_pierdes(x,y):
        
        if str(y) not in x.acertadas:
            
            if str(y) not in x.codigo:
                return False
            
            else:
                
                x.incrementar(str(y))
                
        else:
            return False
            
    # ---------- START ---------------

        didujo_rayman= '''
            
    '''

    print('Reflux -> Preparate para tu perdición')
    print()
    print('Reflux -> Para vencerme tendrás que resolver un código o seras mi prisionero eterno')
    print('\n\n**Modo de Juego:** -> Al acertar un numero del codigo puedes quitarle vida a Reflux con un Ataque Especial\n\n')
    
    reflux_vida = 350

    intentos = 0

    objeto = Codigo( )

    ##print(objeto.codigo,type(objeto.codigo))

    oculto = objeto.lista_mostrar

    while True:
        
        if comprovar_vida( reflux_vida ) == False: # Esta funcion evalua si reflux se ha quedado sin vida
            print('\n\n Reflux -> Me has derrotado ... ,  puedes marcharte')
            return True
            #break
        
        else:
            print( '\n\nVida de Reflux : ', reflux_vida )
            
        print('\n\n')
        print('Intento : ',intentos,'    Código : ',oculto)

        n1 = pide_nums()
        if comprovar_pierdes(objeto,n1) == False:
            print('\n\n Reflux -> Jajaja El numero estava repetido')
            print('\n\n Reflux -> Jajaja No has podido vencerme has perdido')
            return False
            #break
            
        oculto, reflux_vida = coincidencia( n1 , oculto, objeto.codigo,  reflux_vida)
##    coincidencia( n1 , oculto, objeto.codigo,  reflux_vida)
    

# Prueba función del minijuego


    

    
    


