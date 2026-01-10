import random
def triar_mode():
    print("Benvingut al janken!")
    print("Tria el mode de joc:")
    print ("1 - Primer que arribe a 3 victòries")
    print ("2 - Millor de 5 rondes") 

    mode = input("Opció: ")
    print("Mode seleccionat:", "Primer que arribe a 3" if mode == "1" else "Al millor de 5")
    return mode

def print_marcador(marcador):
    print("---------------")
    print("    Maracdor   ")
    print("---------------")
    print(" Jugador", marcador["Jugador"])
    print("Màquina:", marcador["Màquina"])
    print("---------------")

def janken():
    opcions = ["paper", "tisora", "pedra"]
    marcador = {"Jugador": 0, "Màquina": 0}
    mode = triar_mode()
    rondes = 5 if mode== "2" else 100000
    ronda_actual = 0
    while True:
        if mode == 1 and (marcador ["Jugador"] == 3 or marcador["Maquina"] == 3)
            break
        if mode == "2" and ronda_actual == rondes:
            break
        
        print("Opcions: paper, tisora, pedra")
        opcio = input("Tria una opcio (o 's' per sortir): ")

        if opcio == 's':
            print("Sortint del joc.")
            return
        if opcio not in opcions:
            print("Opció no vàlida.")
            continue
        maquina = random.choice (opcions)
        print("La màqiuina tria:", maquina)
        if opcio == maquina:
            print("Empat!")
        elif (opcio == "paper" and maquina == "pedra") or \
             (opcio == "tisora" and maquina == "paper") or \
             (opcio == "pedra" and maquina == "tisora"):
            print("Has guanyat aquesta ronda!")
            
            marcador["Juagdor"] += 1
        else:
            print("Has perdut aquesta ronda!")
            marcador["Maquina"] += 1
                     
        ronda_actual +=1
        print_marcador(marcador)

        if marcador ["Jugador"] > marcador["Màquina"]:
            print("Has guanyat la partida!")
        elif marcador["Jugador"] < marcador["Maquina"]:
            print("La maquina ha guanyat la partida!")
        else:
            print("Empat final!")
        janken()

        


