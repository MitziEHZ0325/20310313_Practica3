# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:58:44 2023

@author: Doramitzi Esmeralda Herrera Zepeda
20310343
"""

import random

personajes = ["Personaje1", "Personaje2", "Personaje3", "Personaje4", "Personaje5"]
armas = ["Arma1", "Arma2", "Arma3", "Arma4", "Arma5"]
habitaciones = ["Habitación1", "Habitación2", "Habitación3", "Habitación4", "Habitación5"]

# Copias de las listas de personajes, armas y habitaciones
personajes_disponibles = list(personajes)
armas_disponibles = list(armas)
habitaciones_disponibles = list(habitaciones)

def obtener_escenario_sin_repeticiones(personajes, armas, habitaciones):
    if not personajes:
        personajes = list(personajes_disponibles)
    if not armas:
        armas = list(armas_disponibles)
    if not habitaciones:
        habitaciones = list(habitaciones_disponibles)

    personaje = random.choice(personajes)
    arma = random.choice(armas)
    habitacion = random.choice(habitaciones)
    personajes.remove(personaje)
    armas.remove(arma)
    habitaciones.remove(habitacion)
    return personaje, arma, habitacion

escenarios = []
for i in range(5):
    personaje, arma, habitacion = obtener_escenario_sin_repeticiones(personajes, armas, habitaciones)
    escenarios.append((personaje, arma, habitacion))

escenario_culpable = None
while escenario_culpable is None or escenario_culpable in escenarios:
    escenario_culpable = obtener_escenario_sin_repeticiones(personajes, armas, habitaciones)

# Crear un diccionario para llevar un registro de las consultas realizadas
consultas_realizadas = {"personaje": [], "arma": [], "habitación": []}

def generar_pistas(escenarios, escenario_culpable, consultas_realizadas):
    pistas = []
    for escenario in escenarios:
        personaje, arma, habitacion = escenario
        pista = f"{personaje} dijo haber estado en {habitacion} y ver {arma}"
        pistas.append(pista)

    pistas_habitaciones = [f"{habitacion} es un lugar importante en la historia." for habitacion in habitaciones]
    pistas.extend(pistas_habitaciones)

    return pistas

pistas = generar_pistas(escenarios, escenario_culpable, consultas_realizadas)

def mostrar_pistas_seleccionadas(opcion, seleccion, escenario_culpable):
    pistas_mostradas = []

    for pista in pistas:
        if opcion in pista.lower() and seleccion in pista:
            pistas_mostradas.append(pista)

    registro_personaje = escenario_culpable[0]
    registro_habitacion = escenario_culpable[2]
    registro_arma = escenario_culpable[1]

    mensaje = []

    for pista in pistas_mostradas:
        elementos = pista.split()
        personaje_en_pista = elementos[0]
        habitacion_en_pista = elementos[5]
        arma_en_pista = elementos[-1]

        registro_personaje_text = "No" if personaje_en_pista == registro_personaje else "Sí"
        registro_habitacion_text = "No" if habitacion_en_pista == registro_habitacion else "Sí"
        registro_arma_text = "No" if arma_en_pista == registro_arma else "Sí"

        mensaje.append(f"Hay registros del {personaje_en_pista}: {registro_personaje_text}")
        mensaje.append(f"Hay registros de la {habitacion_en_pista}: {registro_habitacion_text}")
        mensaje.append(f"Hay registros del {arma_en_pista}: {registro_arma_text}")

    return pistas_mostradas, mensaje

# Inicio del juego
print("¡Bienvenido al juego Clue!")
print("Te encuentras en la mansión Blackwood, una imponente residencia en medio de la campiña inglesa. Es una noche de tormenta, con relámpagos iluminando la mansión y truenos retumbando en el cielo. Has sido invitado a una cena exclusiva en la mansión por el misterioso anfitrión, el Sr. Eustace Blackwood.")
print("Sin embargo, la noche toma un giro siniestro cuando, durante la cena, un estruendo rompe el silencio. Todos los invitados se levantan alarmados y descubren el cuerpo sin vida del Sr. Blackwood en el suelo. Ha sido asesinado.")
print("Las puertas de la mansión se cierran automáticamente, atrapándote junto con otros invitados en el escenario del crimen. La policía está camino, pero tienes la firme convicción de que puedes resolver este misterio antes de que lleguen.")
print("Cada invitado es considerado un sospechoso. Tienes que determinar quién cometió el crimen, con qué arma y en qué habitación. Las únicas pistas que tienes son las palabras de los testigos y las observaciones de los personajes durante la cena.")
print("En la mesa, Miss Scarlet menciona haber estado en la Biblioteca y haber visto un Revólver. El Profesor Plum afirma haber estado en el Vestíbulo y haber visto un Candelabro. Mrs. Peacock sostiene haber estado en la Sala de Billar y haber visto una Daga. Las pistas se entrelazan y te sumerges en un juego de deducción.")
print("Tienes cinco preguntas para recopilar pistas y resolver el misterio antes de que la policía llegue. ¿Quién fue el asesino? ¿Qué arma se utilizó? ¿En qué habitación ocurrió el crimen?")
print("Mientras te desplazas por la mansión en busca de respuestas, la tensión aumenta. Los invitados intercambian miradas sospechosas y alianzas secretas. Cada habitación esconde un misterio y cada personaje tiene secretos que revelar.")
print("Finalmente, llega el momento de hacer tu adivinanza final. ¿Serás capaz de descubrir la verdad detrás del asesinato del Sr. Blackwood? ¿O quedarás atrapado en esta mansión llena de secretos hasta que llegue la policía?")
print("El destino del juego Clue yace en tus manos. ¡Buena suerte en tu búsqueda de la verdad y en la resolución del misterio en la mansión Blackwood!")
preguntas_restantes = 5  # Número de preguntas permitidas

while preguntas_restantes > 0:
    print(f"\nPreguntas restantes: {preguntas_restantes}")

    opcion = input("¿Qué tipo de pista deseas (personaje, arma, habitación)?: ").strip().lower()
    if opcion not in ["personaje", "arma", "habitación"]:
        print("Opción no válida.")
        continue

    if opcion == "personaje":
        opciones_disponibles = personajes_disponibles
    elif opcion == "arma":
        opciones_disponibles = armas_disponibles
    elif opcion == "habitación":
        opciones_disponibles = habitaciones_disponibles

    if opciones_disponibles:
        print(f"Opciones disponibles de {opcion}: {', '.join(opciones_disponibles)}")
        seleccion = input(f"Selecciona el {opcion} del cual deseas información: ").strip()

        if seleccion in opciones_disponibles:
            pistas_seleccionadas, registro = mostrar_pistas_seleccionadas(opcion, seleccion, escenario_culpable)
            if pistas_seleccionadas:
                print("Pistas relacionadas:")
                for i, pista in enumerate(pistas_seleccionadas, 1):
                    print(f"Pista {i}: {pista}")
            else:
                print(f"No hay pistas disponibles para {seleccion}.")

            if registro is not None:
                print(registro)

            preguntas_restantes -= 1
            opciones_disponibles.remove(seleccion)
        else:
            print(f"La selección '{seleccion}' no es válida.")
    else:
        print(f"No hay opciones disponibles de {opcion}.")

# Adivinar a los culpables
print("\n¡Ha llegado el momento de adivinar a los culpables!")
personaje_culpable = input("¿Quién crees que es el personaje culpable?: ").strip()
arma_culpable = input("¿Qué arma crees que se utilizó?: ").strip()
habitacion_culpable = input("¿En qué habitación crees que ocurrió el crimen?: ").strip()

if (personaje_culpable == escenario_culpable[0] and
    arma_culpable == escenario_culpable[1] and
    habitacion_culpable == escenario_culpable[2]):
    print("¡Felicidades! Has adivinado a los culpables y resuelto el misterio. ¡Ganas el juego!")
else:
    print("Lo siento, no has adivinado a los culpables. El juego ha terminado.")
    print(f"Los culpables eran: {escenario_culpable[0]} con {escenario_culpable[1]} en {escenario_culpable[2]}.")
