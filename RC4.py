#
#                             ALGORITMO RC4
# 
#     Nina López | Aitana Martínez | Patricia Da Concepción | Carlos Hermida


######## LIBRERÍAS

# Sólamente las usamos para la parte de front-end
# Es totalmente independiente a la implementación de RC4

import pandas as pd
import os
from time import sleep
import sys


######## KSA

def KSA(key, log = True):
    
    # Inicialización
    S = [bin(x)[2:] for x in range(256)]
    if log:
        print("\nInicialización de S: \n\n{}".format(' '.join(S)))
    T = [key[x % len(key)] for x in range(256)]
    
    # Permutación de S
    j = 0
    for i in range(256):
        j = (j + int(S[i],2) + int(T[i], 16)) % 256
        S[i], S[j] = S[j], S[i]
    if log:
        print("\n\nPermutación inicial de S: \n\n{}".format(' '.join(S)))
    return S


######## PRGA

def PRGA(S, keystream, i, j):
    i = (i + 1) % 256
    j = (j + int(S[i],2)) % 256
    S[i], S[j] = S[j], S[i]
    t = (int(S[i],2) + int(S[j],2)) % 256
    keystream.append(S[t])
    return S, keystream, i, j


######## CIFRADO

def cipher(key):
    
    # Introducción de la clave y KSA
    key = key.split(" ")
    S = KSA(key)

    # Inicialización del DataFrame, keystream (vacío) e i,j iniciales (0,0)
    df = pd.DataFrame(columns=["LETRA", "ASCII(10)", "ASCII(2)", "KEYSTREAM", "CIFRADO(2)", "CIFRADO(16)"])
    keystream = []
    i, j = 0, 0

    while True:

        # Introducción del texto letra por letra
        letter = input("\n> ")
        if letter == "exit":
            break
        if len(letter) != 1:
            continue

        # PRGA y XOR
        S, keystream, i, j = PRGA(S, keystream, i, j)
        cipher_letter = int(keystream[-1],2)^ord(letter)
    
        # Acualización del DataFrame
        df.loc[len(df.index)] = [letter, ord(letter), bin(ord(letter))[2:], keystream[-1], bin(cipher_letter)[2:], hex(cipher_letter)[2:]]
        print(df)
    
        # Muestra del estado de S
        print("\n\nModificación de S: \n")
        print(f"S[{i}] <-> S[{j}] | keystream -> S[{S.index(keystream[-1])}]\n")
        s_show = ""
        for element in S:
            if S.index(element) in [i,j]:
                s_show += ("\033[1;31m{}\033[00m").format(element)
            elif element == keystream[-1]:
                s_show += ("\033[1;32m{}\033[00m").format(element)
            else:
                s_show += element
            s_show += " "
        print(s_show)


######## DESCIFRADO

def decipher(cipher_text, key):

    # Introducción del texto cifrado
    cipher_text = cipher_text.split(" ")
    
    # Introducción de la clave y KSA
    key = key.split(" ")
    S = KSA(key, log = False)

    # Inicialización del keystream (vacío) e i,j iniciales (0,0)
    keystream = []
    clear_text = ""
    i, j = 0, 0

    for element in cipher_text:
        # PRGA y XOR
        S, keystream, i, j = PRGA(S, keystream, i, j)
        clear_text += chr(int(keystream[-1],2)^int(element, 16))

    return clear_text


######## FRONT-END

### CLEAR

def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux
    else:
        os.system('clear')


### MENÚ PRINCIPAL

def main_menu():
    clear()
    print("\n MENÚ PRINCIPAL\n\n 1. Cifrar\n 2. Descifrar\n 0. Salir\n")
    
    while True:
        try:
            main_choose = int(input("> "))
            break
        except:
            print(" ERROR / Opción incorrecta")
            sleep(2)
            main_menu()

    if main_choose == 1:
        job_menu(1)
    elif main_choose == 2:
        job_menu(2)
    elif main_choose == 0:
        clear()
        print("\n -- c8 65 de f2 c2 24 54 d6 78 b8 5a d2 !")
        sys.exit()   
    else:
        print(" ERROR / Opción incorrecta")
        sleep(2)
        main_menu()


### MENÚ DE CIFRADO / DESCIFRADO

def job_menu(op):
    clear()
    if op == 1:
        print("\n ALGORITMO DE CIFRADO")

    else:
        confirm_op = "n"
        while confirm_op not in ["y", "Y"]:
            print("\n ALGORITMO DE DESCIFRADO")
            cipher_text = input("\n Introduce el texto en hexadecimal a continuación.\n Pulsa [enter] para finalizar.\n\n > ")
            confirm_op = input("\n ¿Estás seguro? (y/n) \n Consejo: copia el texto en el portapapeles si quieres consevarlo o modificarlo\n > ")
            clear()

    while True:
        try:
            key = input("\n Introduce la clave: ")
            assert(len(key) != 0)
            for element in key.split(" "):
                int(element, 16)
            break
        except:
            print(" ¡Recuerda el formato de la clave!")

    if op == 1:
        print("\n Escribe 'exit' para terminar la ejecución\n")
        cipher(key)

    else:
        try:
            output = decipher(cipher_text, key)
            print(" Texto descifrado\n\n", output)
        except:
            print("\n ERROR / Texto cifrado no válido")
            sleep(3)
            main_menu()

    input("\n Pulsa [enter] para volver al menú principal.\n")
    main_menu()


### PANTALLA DE INICIO

def start():
    
    clear()
    logo =("\
  ____   ____ _  _   \n\
 |  _ \\ / ___| || |  \n\
 | |_) | |   | || |_ \n\
 |  _ <| |___|__   _|\n\
 |_| \\_\\\\____|  |_|  \n\
                     \n\n")
       
    print(logo, "\n"*2)
    sleep(2)                                                            
    main_menu()


######## EJECUCIÓN DEL SCRIPT

if __name__ == "__main__":
    start()







