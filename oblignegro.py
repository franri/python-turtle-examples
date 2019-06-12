import pickle
import random

PUNTAJE_GLOBAL = 5000

def obtener_opcion():
    print('Seleccione una opción:')
    print('\t1. Jugar nueva partida.')
    print('\t2. Mostrar un ranking histórico de jugadores, ordenado por cantidad de partidas ganadas de mayor a menor.')
    print('\t3. Mostrar el "máximo puntaje de todos los tiempos".')
    print('\t4. Cambiar el puntaje para ganar las partidas')
    print('\t5. Salir')
    opcion = int(input(''))
    return opcion

def jugar_partida():
    j1 = input('Nombre del jugador 1:')
    j2 = input('Nombre del jugador 2:')

    while j1 == j2:
        print('Error, ingrese nuevamente')
        j1 = input('Nombre del jugador 1:')
        j2 = input('Nombre del jugador 2:')

    ganador = arrancar_juego(j1, j2)
    actualizar_puntaje(ganador)

def arrancar_juego(j1, j2):
    puntaje_j1 = 0
    puntaje_j2 = 0

    puntaje_objetivo = PUNTAJE_GLOBAL

    turno = 1

    while puntaje_j1 < puntaje_objetivo and puntaje_j2 < puntaje_objetivo:
        print(f'Jugador 1 tiene {puntaje_j1}')
        print(f'Jugador 2 tiene {puntaje_j2}')
        print(f'Gana el que llegue a {puntaje_objetivo}')

        if turno == 1:
            puntaje_mano = 0
            while turno == 1:
                dados = tirar_dados()
                puntos = analizar_dados(dados)
                if puntos == 0:
                    turno = 2
                else:
                    print(f'Ganaste {puntos} puntos, e ibas {puntaje_mano}.')
                    seguir = input('¿Querés seguir jugando? (s/n)')
                    if seguir == 'n':
                        puntaje_j1 = puntaje_j1 + puntaje_mano
                        turno = 2
                    elif seguir == 's':
                        turno = 1
        elif turno == 2:
            puntaje_mano = 0
            while turno == 2:
                dados = tirar_dados()
                puntos = analizar_dados(dados)
                if puntos == 0:
                    turno = 1
                else:
                    print(f'Ganaste {puntos} puntos, e ibas {puntaje_mano}.')
                    seguir = input('¿Querés seguir jugando? (s/n)')
                    if seguir == 'n':
                        puntaje_j2 = puntaje_j2 + puntaje_mano
                        turno = 1
                    elif seguir == 's':
                        turno = 2


def tirar_dados():
    dados = []
    numero1 = random.randint(1,6)
    numero2 = random.randint(1,6)
    numero3 = random.randint(1,6)
    dados.append(numero1)
    dados.append(numero2)
    dados.append(numero3)
    # dados.sort(reverse = True)
    return dados

def analizar_dados(dados):
    pass

def mostrar_ranking():
    pass

def mostrar_record():
    pass

def cambiar_puntaje():
    return int(input('Escriba puntaje máximo del juego: '))

def salir():
    pass


opcion = obtener_opcion()

if opcion == 1:
    jugar_partida()
elif opcion == 2:
    mostrar_ranking()
elif opcion == 3:
    mostrar_record()
elif opcion == 4:
    PUNTAJE_GLOBAL = cambiar_puntaje()
elif opcion == 5:
    salir()
