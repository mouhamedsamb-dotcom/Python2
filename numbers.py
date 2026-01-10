import random
def menu():
    print(" ---ADIVINA EL NÚMERO --- ")
    print("1. Jugar")
    print("2. Reglas")
    print("3. Salir")
def regles():
    print("Reglas del juego:")
    print("- El programa elegirá un número secreto")
    print("- Debes adivinarlo en el menor número de intentos")
    print("- El juego te dirá si el número es mayor o menor")
    print("- Pierdes puntos por cada fallo")
def dificultad():
    print("Elige dificultad:")
    print("1. Fácil (1-10)")
    print("2. Medio (1-50)")
    print("3. Difícil (1-100)")
    opcion = input("Opció: ")

    if opcion =="1":
        return 10, 5
    elif opcion == "2":
        return 50, 7
    elif opcion == "3":
        return 100, 10
    else:
        print("Opcion no valida.")
        return 10, 5
def numbers():
    max_num, intentos_max = dificultad()
    numero_secreto = random.randint(1, max_num)
    intentos = 0

    print("He pensado un número entre 1 y", max_num)

    while intentos < intentos_max:
        numero = int(input("Introduce un número: "))
        intentos = intentos + 1

        if numero == numero_secreto:
            print("Has acertado!")
            print("Intentos usados:", intentos)
            return
        else:
            if numero < numero_secreto:
                print("El numero es mayor")
            else:
                print("El numero es menor")
    print("Has perdido")
    print("El numero correcto era:", numero_secreto)
def juego():
    while True:
        menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            numbers()
        elif opcion == "2":
            regles()
        elif opcion == "3":
            print("Buena partida")
            break
        else: 
            print("Opcion incorrecta")
