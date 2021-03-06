import clases as cl
import sonidos_pantallas as sp
import utilidades as ut
import random,time
import minijuego_anastasia,minijuego_elis,minijuego_chechu,minijuego_muymio,minijuego_joan


#Dimension C-137 

    #items

#los items de tipo sk sirven para tener 2 turnos seguidos,es decir,que el rival se pierda su tuno por alguna rzon
pistola_portales = cl.Items("Pistola de portales","sk",0,"con la pistola de portales de rick te vas a la dimension 35 en tal de esquivar el golpe y vuelve a ser tu turno !",1)
#los items de tipo ataque incrementan la fuerza
espada_bacon = cl.Items("Espada bacon","a",20,"con esta ridicula y sabrosa espada aumenta tu fuerza !",2)
#los items de tipo sanacion incrementan la vida
cuencas_de_ojos = cl.Items("Cuencas de ojos","s",15,"con estos deliciosas y asquerosas cuencas de ojos aumenta tu salud !",1)
#los items de tipo precicison incrementan la precision,obviamente
parche_de_morty = cl.Items("Parche de morty","p",30,"con este parche de morty te vuelves mas audaz y tu precision aumenta",1)
#los items

    #villanos

abradolf_lincler = cl.Mob("abradolf lincler",100,5,5,50,100)
asustadizo_terry = cl.Mob("asustadizo terry",100,5,5,50,10)
bola_de_nieve = cl.Mob("bola de nieve",100,5,5,50,10)

    #dimension

dimension_c137 = cl.Dimension("C-137",[pistola_portales,espada_bacon,cuencas_de_ojos,parche_de_morty],[abradolf_lincler,asustadizo_terry,bola_de_nieve],minijuego_muymio.main)


    #Dimension Fondo de bikini

#items

#sk
savia_gary=cl.Items("SaviGary","sk",0,"tirale savia de gary a tu rival para que no pueda atacar durante un turno!",1)

#ataque
caza_medusas = cl.Items("CazaMedusas 3000", "a", 15,"Con el nuevo modelo CazaMedusas aumenta tu daño!",2)
espatula = cl.Items("Espatula de Oro","a",30,"el arma legendaria de Bobesponja! calcina a tus rivales.",1)#legendaria

#sanacion
bote_burbujas = cl.Items("Burbujeitor","s",10,"rociate de este jabon burbujeante para recuperar salud!",1)
cangreburguer = cl.Items("BurguerCangreburguer","s",15, "comete esta delicia para quedarte como nuevo!",1)#legendaria

#precision
gafas = cl.Items("Lectometor","p",30,"ponte estas gafas de lectura para aumentar tu precision",1)



#villanos

patricio=cl.Mob("Patricio Estrella",100,5,10,50,7)
arenita=cl.Mob("Arenita Mejillas",100,10,5,70,10)
placton=cl.Mob("Placton",80,10,5,90,10)
calamardo=cl.Mob("Calamardo",100,5,5,50,10)


#dimension

dimension_fondo_de_bikini = cl.Dimension("Fondo de bikini",[savia_gary, caza_medusas, espatula, bote_burbujas, cangreburguer, gafas],[patricio, arenita, placton, calamardo],minijuego_chechu.Minijuego_carrera)



### ------------------------------------------------------------------------------------------------------
### ---------------------- El Claro de los Sueños
##
# ----------------- items
# ---------------------- ( a ) ataque
cohete_propulsor = cl.Items("Cohete Propulsor","a",20,"Con este cohete haras mucho daño", 1 )
# ---------------------- ( s ) sanacion
hada_lagrimas = cl.Items("lagrimas de Hada","s",10,"Esta bebida mejora la salud",1)
# ---------------------- ( a ) ataque
red_pot = cl.Items("Bote Hoodlum Red","a",15,"Con la tecnologia hoodlum podras golpear más fuerte",1)
# ---------------------- ( sk ) 2 turnos
yellow_pot = cl.Items("Bote Hoodlum Amarillo","sk",0,"Con la tecnologia hoodlum tienes un gorrocoptero para luchar otra vez",1)
# ---------------------- ( p ) precision
green_pot = cl.Items("Bote Hoodlum Verde","p",30,"Con la tecnologia hoodlum tienes obtendrás mayor precision",1)

# ---------------------- villanos
#                     Nombre, Vida, Ataque, Defensa, Precision, Velocidad

hoodlum = cl.Mob('Hoodlum', 100, 10, 20, 10, 20)
dark_lum = cl.Mob('Lum Oscuro', 120,10,5,20,20)
dark_rayman = cl.Mob('Rayma Oscuro',50,25,20,35,20)


# ---------------------- dimension
dimension_claro_de_los_sueños = cl.Dimension("El Claro de los Sueños", [ cohete_propulsor, hada_lagrimas, red_pot, yellow_pot, green_pot], [ hoodlum, dark_lum, dark_rayman ] ,minijuego_joan.reflux)

        # Dimension Planet Express

#items
#sk
doblador = cl.Items("Doblar objetos","sk",0,"Bender fue creado como doblador de objetos profesional. Dale golpes fuertes al enemigo!",2)

#ataque
thompson = cl.Items("Thompson 1928","a",20,"subfusil favorito, desde que Bender trabajó con la mafia. Aumenta tu fuerza!",2)

#sanacion
benderbrau = cl.Items("La cerveza 'Bendërbrau'","s",15,"con la cerveza favorita de Bender aumenta tu salud!",1)

#item de precision 
detector = cl.Items("Detector de homosexuales","p",25,"con este detector de homosexuales Bender se vuelve más activo y tu precisión aumenta",2)
faro = cl.Items("Faro incorpordo","p",30,"con el faro encendidio aumentas tu precision a la hora del golpe.",2)

#villanos( Nombre, Vida, Ataque, Defensa, Precision, Velocidad)
zapp_branningan = cl.Mob("Zapp Branningen",100,5,5,50,100)
hipnosapo = cl.Mob("Hipnosapo",100,5,5,50,10)
babosa_cerebral = cl.Mob("Babosa Cerebral",100,5,5,50,10)

#dimension

dimension_express = cl.Dimension("Planet Express",[doblador,thompson,benderbrau,detector,faro],[zapp_branningan,hipnosapo,babosa_cerebral],minijuego_anastasia.main)


# ---------------------- ( a ) ataque
bomba_explosiva = cl.Items("bomba explosiva","a",20,"Con esta bomba haras mucho daño", 1 )
# ---------------------- ( s ) sanacion
mdma = cl.Items("MDMA","s",10,"Esta droga mejora la salud",1)
# ---------------------- ( a ) ataque
gunatelete = cl.Items("guantelete","a",15,"Con este guantelete aumenta tu fuerza considerablemente",1)
# ---------------------- ( sk ) 2 turnos
cubo_perfecto = cl.Items("cubo perfecto","sk",0,"atrapa en este cubo a tu enemigo para golpear otra vez",1)
# ---------------------- ( p ) precision
lanza_chas = cl.Items("LANZA ESPIRITUAL CHASTIEFOL","p",30,"Con esta arma legendaria de el rey de las hadas Arlequin,tu precision sube",1)

        #villano 
folista = cl.Mob('true folista', 100, 40, 40, 20, 20)
Sara_t100 = cl.Mob("T-1000 SARAH",100,5,5,50,40)
nominador = cl.Mob("El nominador",50,22.4,10,30,20)


dimension_fol = cl.Dimension("Dimension FOL",[bomba_explosiva,mdma,gunatelete,cubo_perfecto,lanza_chas,],[folista,Sara_t100,nominador],minijuego_elis.new_game)

        #jugadores

    #homero

bola_demolicion = cl.Habilidades("Bola de demolicion","normal",(10,20),"golpe de tipo normal con la bola de demolicion con la que homer se queria tirar")
donut_envenenado = cl.Habilidades("Donut envenenado","veneno",(5,10),"donut de tipo veneno que quitará vida paulatinamente")
golpe_borracho = cl.Habilidades("Golpe borracho","normal",(0,50),"golpe de tipo normal que puede quitar muy poco o mucho debido a la borrachera de homer")


homero = cl.Jugador("homero",10,40,50,50,20,"Este jugador tiene habilidades muy variopintas y curiosas !","./recursos/manazas2.mp3",[bola_demolicion,donut_envenenado,golpe_borracho])

        #hacker

golpe_cargado = cl.Habilidades("Golpe Cargado","normal", (15,30), " Golpe cargado de tipo normal que hace Rayman")
golpe_envenenado = cl.Habilidades("Envenenamiento","veneno",(5,10),"Gracias a Leptys, Rayman puede envenenar a un enemigo")
golpe_ocasional = cl.Habilidades("Golpe Ocasional","normal",(0,50),"Rayman reune energias para asestar un golpe que puede ser muy potente")

hacker = cl.Jugador('Anonymus',100,45,50,50,25,"Este gran hacker es siniestro !","./recursos/La_purga.mp3", [ golpe_cargado, golpe_envenenado,  golpe_ocasional ] )

        #Bender

calentador = cl.Habilidades("Calentador de agua","veneno",(5,10),"echa agua hirrviendo al villado, dejando quemaduras, que quitarán vida. ")
estiron = cl.Habilidades("Estirón brusco","normal",(10,20),"las piernas y brazon de estiran a gran longitud bruscamente para hacer el golpe inesperado.")
canyon = cl.Habilidades("Cañon","normal",(0,50),"Bender puede utilizarse como cañon, para dispara, lo malo es que no sabe apuntar bien, asi que puede quitar mucha o nada de vida.")
 
        
bender = cl.Jugador("Bender",70,70,50,50,40,"Este jugador es muy sociopatico e impredecible !","./recursos/anastasia_Bender.mp3",[calentador,estiron,canyon])


        ## Nerd 
brainstorming = cl.Habilidades('Lavado de cerebro', 'veneno', (3,5), 'envenena el cerebro y quita vidas')
golpe_random = cl.Habilidades("FINIQUITO TOTAL","normal",(0,50),"golpe de tipo normal que puede quitar yo que se el que...")
golpe_finiquito = cl.Habilidades("Golpe de salario","normal", (15,30), " Golpe cargado de tipo normal que te quita vida y salario")

nerd = cl.Jugador('Nerd', 100, 50, 40, 40, 30,'un libro en persona', './recursos/mclovin.mp3', [brainstorming,golpe_random,golpe_finiquito])

    #bob esponja

##habilidades

golpe_cubo = cl.Habilidades("Comida Podrida","veneno",(5,10),"Envenena a tu enemigo con comida del cubo de cebo, ¡puaaaaaj!")
golpe_trucado = cl.Habilidades("¿Hay trampa?","normal",(0,50),"Ha bobesponja le ha crecido el brazo sorprendentemente, pero... no parece muy estable")
golpe_ancla = cl.Habilidades("Golpe ancla","normal",(10,20),"¡Lenate de valor y zúrrale una buena a tu rival!")
golpe_condimento = cl.Habilidades("Golpe condimento","normal",(10,20), "Disparale a tu oponente pero, con mucha salsa")

bob = cl.Jugador("Bobesponja",100,30,34,100,100,"¡Este jugador es muy escurridizo, rápido y el mejor cocinero de todas las dimensiones!","./recursos/esponja_frase.mp3",[golpe_cubo, golpe_trucado, golpe_ancla, golpe_condimento])



jugadores = [homero,hacker,bender,nerd]

dimensiones = [dimension_c137,dimension_fondo_de_bikini,dimension_claro_de_los_sueños,dimension_express,dimension_fol]

        #items totales

selec_items = [
    
    cl.Items("aceite_gines","s",random.randrange(15,20),"bebete este aceite colesterolientico para tener fuerza pa echar un ratejo mas en la batalla",3),
    cl.Items("poco_pan","a",random.randrange(5,10),"con el poder del poco pan de patica tendras un poco mas de fuerza",3),
    cl.Items("porro_perroviejo","p",random.randrange(50,80),"con este porro de perroviejo te concentraras mucho mas y tu precision sube",1),

    cohete_propulsor,hada_lagrimas,green_pot,yellow_pot,red_pot,

    savia_gary,cangreburguer,caza_medusas,espatula,gafas,bote_burbujas,

    parche_de_morty,espada_bacon,cuencas_de_ojos,pistola_portales,

    mdma,lanza_chas,cubo_perfecto,bomba_explosiva

]


#mostrar a cada jugador

def  mostrar_homero():
    print("""
---------------------------------------------------------------------------------------------
    Nombre : {}
                                                                                    &              
    Ataque : {}                                                                  .-"`"-.
                                                                                /       \\                 
    Defensa : {}                                                                |   __  _|
                                    ( 1 )                                       |  /  \/ \\             
    Precision : {}                                                             WW  \_o/_o/             
                                                                                (        _)            
    Velocidad : {}                                                              |   .----\\                
                                                                                ;  | '----'            
    Descripcion : {}   \__'--;`               ╚══════╝
                                                                                |___/\|
---------------------------------------------------------------------------------------------
        """.format(homero.nombre,homero.ataque,homero.defensa,homero.precision,homero.velocidad,homero.descripcion))
    
    mihilo_mostrar_homer = sp.Songhilo_jugadores()
    mihilo_mostrar_homer.set_song(homero.sonido)
    mihilo_mostrar_homer.start()
    del mihilo_mostrar_homer


def mostrar_hacker():
    print("""
---------------------------------------------------------------------------------------------

    Nombre : {}                                            
                                                            ▄ ▀▀ ▀▀ ▄
    Ataque : {}                                           █           █
                                                        █               █
    Defensa : {}                ( 2 )                 █                   █
                                                    █    ▄▀▀▀█    █▀▀▀▄    █
    Precision : {}                                 █                        █
                                                 ▐▌      ▄▄    ▀▀▀    ▄▄     █
                                                   █       ▀▀▀     ▀▀▀      █
    Velocidad : {}                                   █         ▀▀▀         █
                                                     ▐██                 ██
    Descripcion : {}    ▄████▄    ▀▀▀   ▄████▄
---------------------------------------------------------------------------------------------
        """.format( hacker.nombre, hacker.ataque, hacker.defensa, hacker.precision, hacker.velocidad, hacker.descripcion))


    mihilo_mostrar_hacker = sp.Songhilo_jugadores()
    mihilo_mostrar_hacker.set_song(hacker.sonido) # Archivo La_purga.mp3
    mihilo_mostrar_hacker.start()
    del mihilo_mostrar_hacker

def mostrar_bender():
    print("""
---------------------------------------------------------------------------------------------
                                                                             ( )
    Nombre : {}                                                           H
                                                                              H
    Ataque : {}                                                              _H_ 
                                                                         .-' -.-'-.
    Defensa : {}                  ( 3 )                                 /           \\
                                                                        |            |
    Precision : {}                                                      |   .-------'._
                                                                        |  / /  '.' '. \\
    Velocidad : {}                                                      |  \ \ @   @ / / 
                                                                        |   '---------'        
    Descripcion : {}      |     _______|  
                                                                        |   .'-+-+-+|  
                                                                        |   '.-+-+-+|         
                                                                        |     """"""       |
                                                                        '-._ _   __.-'
---------------------------------------------------------------------------------------------
          """.format(bender.nombre,bender.ataque, bender.defensa,bender.precision,bender.velocidad,bender.descripcion))

    mihilo_mostrar_hacker = sp.Songhilo_jugadores()
    mihilo_mostrar_hacker.set_song(bender.sonido) # Archivo La_purga.mp3
    mihilo_mostrar_hacker.start()
    del mihilo_mostrar_hacker

def mostrar_nerd():
    print('''
---------------------------------------------------------------------------------------------
                          
    Nombre : {}              
                                   
    Ataque : {}                               .'  `'.
                                             /  _    |                                      _
    Defensa : {}                             #_/.\==/.\                                    | |
                                            (, \_/ \\_/                 _ __    ___ _ __ __| |
    Precision : {}      ( 4 )                |    -' |                  | '_ \ / _ \ '__/ _` |
                                             \   '=  /                  | | | |  __/ | | (_| |
    Velocidad : {}                           /`-.__.'                   |_| |_|\___|_|  \__,_|  
                                          .-'`-.___|__ 
    Descripcion : {}    /    \       `. 
    
---------------------------------------------------------------------------------------------
    '''.format(nerd.nombre,nerd.ataque,nerd.defensa,nerd.precision,nerd.velocidad,nerd.descripcion))


    mihilo_mostrar_nerd = sp.Songhilo_jugadores()
    mihilo_mostrar_nerd.set_song(nerd.sonido)
    mihilo_mostrar_nerd.start()
    del mihilo_mostrar_nerd

def mostrar_bob():
    print("""

---------------------------------------------------------------------------------------------

        Nombre: {}                                                                                    
                                                                                            .--..--..--..--..--..--.                                                                     
        Ataque : {}                                                                  |(_.'  |    /    .-\-.  \   |
                                                                                         \     0|    |   ( O| O)   |                                                                                                            
        Defensa : {}                                                                  \ (_) | o         -` .-`   |
                                      ( 5 )                                                  |    \   |`-._ _ _ _ _ \ /
        Precision : {}                                                                  \    |   |  `. |_||_|     |
                                                                                              | o  |    \_      \      |       
        Velocidad : {}                                                                  |     \     `--..-'   O |  
                                                                                                    |     `-.-'      /-.__         
        Descripcion : {}
        
---------------------------------------------------------------------------------------------

""". format(bob.nombre, bob.ataque, bob.defensa, bob.precision, bob.velocidad, bob.descripcion))
    mihilo_mostrar_bob = sp.Songhilo_jugadores()
    mihilo_mostrar_bob.set_song(bob.sonido)
    mihilo_mostrar_bob.start()
    del mihilo_mostrar_bob



def elegir_jugador():
    ut.limpiar_pantalla()
    print()
    print()
    print()
    print("    - - > A continuacion vas a elegir un personaje para jugar...")
    time.sleep(3)

    ut.limpiar_pantalla()

    mostrar_homero()
    time.sleep(16)

    mostrar_hacker()
    time.sleep(8)

    mostrar_bender()
    time.sleep(15)

    mostrar_nerd()
    time.sleep(13)

    mostrar_bob()
    time.sleep(5)
    print();print()
    while True:
        try:
            eleccion_user = int(input("- - - - > "))
            return jugadores[eleccion_user-1]
        except IndexError:
            print("No existe ningun personaje con ese numero...")
            time.sleep(1.5)
        except ValueError:
            print("Solo numeros,no texto o otro tipo de caracteres...")
            time.sleep(1.5)



