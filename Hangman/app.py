import random
import os

def iniciar():
    Grafico = ['''
 +---+
 |   |
     |
     |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']
    
    Palabras = [
        "RUSIA",
        "COLOMBIA",
        "JAPON",
        "CANADA",
        "NORUEGA",
    ]

    letras = random.choice(Palabras)
    espacios = ["_"] * len(letras)
    intentos = 6
    
    while True:
        os.system("clear")
        for personaje in espacios:
            print(personaje, end = " ")
        print(Grafico[intentos])
        Escribe = input("Elije una letra: ").upper()
        
        found = False
        for idx, personaje in enumerate(letras):
            if personaje == Escribe:
                espacios[idx] = Escribe
                found = True
                
        if not found:
            intentos -= 1
        
        if "_" not in espacios:
            os.system("clear")
            print("Ganaste")
            break
            input()
        
        if intentos == 0:
            os.system("clear")
            print("Perdiste")
            break
            input()
    
    
if __name__ == '__main__':
    iniciar()