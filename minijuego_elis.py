# minijuego 
questions = {
    'La capital de Madagaskar: ':'C',
    'Quién de los siguientes trabajadores no puede sindicarse: ':'B',
    'Qué significa FAT: ':'A',
    'Qué componente es responsable del seguimiento de las variables en tiempo de ejecución: ':'D',
    'La comunicación asertiva permite:':'A',
    'Si la empresa quiere despedir a un representante de las personas trabajadoras por falta grave o muy grave, debe…':'C',
    'Los tribunales laborales de mayor rango que resuelven los conflicto que surgen entre empresarios y trabajadores:':'D',
    'Los trabajadores a tiempo parcial...':'B',
    'Los registros de control del horario laboral se deben conservar durante…':'B',
    '¿El importe de la locomoción cotiza a la Seguridad Social?':'A'
}

options = [
    ['A. Chad', 'B. Jakarta', 'C. Antananarivu', 'D. Madagaskar'],
    ['A. Un autónomo que no tiene asalariados', 'B. Un miembro de la Guardia Civil', 'C. Un funcionario', 'D. Todos tienen derecho a sindicarse'],
    ['A. File Allocation Table', 'B. File Absorption Transmission', 'C. File Attenuation Table', 'D. File Allocation Transmission'],
    ['A. Editor de textos', 'B. Intérprete', 'C. Compilador', 'D. Depurador'],
    ['A. Defenderse pasivamente', 'B. Defenderse sin agredir', 'C. Defenderse agrediendo', 'D. No defenderse'],
    ['A. Debe esperar un año', 'B. Comunicarle el despido con 60 días de antelación', 'C. Abrirle un expediente contradictorio antes de sancionarle', 'D. No se le puede despedir'],
    ['A. La Audiencia Provincial', 'B. La Audiencia Nacional', 'C. Los Tribunales Superiores de Justicia de las comunidades autónomas', 'D. El Tribunal Supremo'],
    ['A. Solo se pueden realizar horas extraordinarias si se pactan', 'B. No pueden realizar las horas extraordinarias salvo por fuerza mayor', 'C. Pueden realizar horas extraordinarias', 'D. Solo se pueden realizar horas extraordinarias voluntariamente'],
    ['A. 2 años', 'B. 4 años', 'C. No es necesario conservarlos', 'D. Seis meses'],
    ['A. Cotiza solo la cuantía que sobrepasa de 0,19 €/km', 'B. Cotiza solo cuando sobrepasa 0,19 €/km', 'C. No, independientemente de su importe', 'D. Cotiza el importe en su totalidad']
]

#el juego
def new_game():

    # # sp.mihilo_quiz_theme = sp.Songhilo()
    # # sp.mihilo_quiz_theme.set_song('./sources/Fluffing-a-Duck.mp3')
    # # sp.mihilo_quiz_theme.start()

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('-------------------------------------')
        print(key)
        
        for i in options[question_num-1]:
            print(i)
            
        print()
        player = input('Tu respuesta es (A, B, C, D): ')
        player = player.upper()
        guesses.append(player)

        correct_guesses += check_answer(questions.get(key), player)

        question_num += 1

    if display_score(correct_guesses, guesses):
        return True
    else:
        return False


#comprobar respuestas
def check_answer(answer, player):
    if answer == player:
        print()
        print('MUY BIEN')
        return 1
    else:
        print()
        print('CAGASTE')
        return 0

#demostrar los resultatos
def display_score(correct_guesses, guesses):
    
    global score
    score = int((correct_guesses/len(questions))*100)
    print('-------------------------------------')
    print('Tu resultado: '+str(score)+'%')


    if score < 50:
        print()
        print('GAME OVER! GAME OVER! GAME OVER!')
        print('NO SABES NADA DE FOL Y ASI NO PODRAS VIVIR!')
        return False
    else:
        print()
        print('FELICITACIONES! HAS GANADO!')
        print('ERES UN TRUE FOLISTA!')
        return True



