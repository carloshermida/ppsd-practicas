#
#                           ALGORITMO DE VIGENÈRE
# 
#     Nina López | Aitana Martínez | Patricia Da Concepción | Carlos Hermida


######## LIBRERÍAS

# Sólamente las usamos para la parte de front-end
# El algoritmo de cifrado es totalmente independiente

import os
from time import sleep
import sys


######## ABECEDARIO

def abcd_generator(key):
    abc_list = []
    abc = []
    for _ in range(2):    
        for a in range(65, 91):
            abc.append(chr(a))

    key = key.upper()
    for i in key:
        start = abc.index(i)
        tmp_abc = abc[start:start+26]
        abc_list.append(tmp_abc)  

    return (abc,abc_list)


######## CIFRADO

def cipher(text, key):
    abc, abc_list = abcd_generator(key)
    hide_text = ""
    cnt = 0
    for letter in text:
        index = abc.index(letter)
        hide_text += abc_list[cnt%len(key)][index]
        cnt += 1

    return hide_text


######## DESCIFRADO

def decipher(hide_text, key):
    abc, abc_list = abcd_generator(key)
    text = ""
    cnt = 0
    for hide_letter in hide_text:
        letter_index = abc_list[cnt%len(key)].index(hide_letter)
        text += abc[letter_index]
        cnt += 1

    return text


######## FORMATEO DE TEXTO

def text_format(text):
    text = text.upper().replace("\n", "").replace("\t", "").replace(" ", "").replace(".", "")
    text = text.replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
    text = text.replace("Ñ", "NH").replace("?", "").replace("¿", "").replace("¡", "").replace("!", "").replace("(", "")
    text = text.replace(",", "").replace(";", "").replace(":", "").replace("-", "").replace(")", "")
    for num in range(10):
        text = text.replace(str(num), "")
    return text


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
        print("\n -- WPKWPEJRCIG !")
        sys.exit()   
    else:
        print(" ERROR / Opción incorrecta")
        sleep(2)
        main_menu()


### MENÚ DE CIFRADO / DESCIFRADO

def job_menu(op):
    clear()
    if op == 1:
        print("\n ALGORITMO DE CIFRADO\n")
    else:
        print("\n ALGORITMO DE DESCIFRADO\n")

    print(" 1. Escribir texto\n 2. Importar desde un archivo\n 0. Volver al menú principal\n")

    while True:
        try:
            job_choose = int(input("> "))
            break
        except:
            print(" ERROR / Opción incorrecta")
            sleep(2)
            job_menu(op)

    if job_choose == 1:
        confirm_op = "n"
        while confirm_op not in ["y", "Y"]:
            clear()
            input_text = input("\n Introduce el texto a continuación.\n Pulsa [enter] para finalizar.\n\n> ")
            confirm_op = input("\n ¿Estás seguro? (y/n) \n Consejo: copia el texto en el portapapeles si quieres consevarlo o modificarlo\n > ")

    elif job_choose == 2:
        cnt = 3
        while True:
            try:
                file = input("\n Introduce el nombre completo del archivo: ")
                with open (file, "r") as f:
                    input_text = f.read()
                break
            except:
                cnt -= 1
                if cnt == 0:
                    job_menu(op)
                print(" El archivo no ha sido encontrado o está dañado ({} intento(s) restante(s))".format(cnt))

    elif job_choose == 0:
        main_menu()

    else:
        print(" ERROR / Opción incorrecta")
        sleep(2)
        job_menu(op)

    input_text = text_format(input_text)
    
    clear()
    while True:
        try:
            key = input("\n Introduce la clave: ")
            assert(len(key) != 0)
            for letter in key:
                assert(ord(letter.upper()) in range(65,91))
            break
        except:
            print(" ¡Recuerda el formato de la clave!")

    if op == 1:
        output = cipher(input_text, key)
        print("\n Texto cifrado\n", output)

    else:
        try:
            output = decipher(input_text, key)
            assert(len(output) != 0)
        except:
            print("\n ERROR / Texto cifrado incorrectamente")
            sleep(3)
            main_menu()
        print("\n Texto descifrado\n", output)

    save = input("\n ¿Desea guardarlo? (y/n)\n > ")
    if save in ["y", "Y"]:
        file_name = input(" Nombre del archivo: ")
        with open (file_name, "w") as f:
            f.write(output)

    input("\n Pulsa [enter] para volver al menú principal.\n")
    main_menu()


### PANTALLA DE INICIO

def start():
    
    clear()
    logo =("\
 __     _____ ____ _____ _   _  __   ____  _____ \n\
 \\ \\   / /_ _/ ___| ____| \\ | |_\\_\\_|  _ \\| ____|\n\
  \\ \\ / / | | |  _|  _| |  \\| | ____| |_) |  _|  \n\
   \\ V /  | | |_| | |___| |\\  |  _|_|  _ <| |___ \n\
    \\_/  |___\\____|_____|_| \\_|_____|_| \\_\\_____|\n\n")
       
    print(logo, "\n"*2)
    sleep(2)                                                            
    main_menu()


######## EJECUCIÓN DEL SCRIPT

if __name__ == "__main__":
    start()





