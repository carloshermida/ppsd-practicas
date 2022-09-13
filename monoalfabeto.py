#
#      		ALGORITMO DE CIFRADO SIMÉTRICO POR SUSTITUCIÓN MONOALFABETO
# 
#     Nina López | Aitana Martínez | Patricia Da Concepción | Carlos Hermida


######## LIBRERÍAS

# Sólamente las usamos para la parte de front-end
# El algoritmo de cifrado es totalmente independiente

import os
from time import sleep
import sys


######## RANDOM 

def random_shuffle(seed, array):
	array_indexes = []
	for rep in range((len(array)//10)+1):
		for i in range(10):
			array_indexes.append(str(i))

	random_num = seed * 97 * len(str(seed))**2
	while True:
		indexes = array_indexes.copy()
		for figure in str(random_num):
			if figure in indexes:
				indexes.remove(figure)
		if len(indexes) == 0:
			break
		random_num = int(str(random_num)[::-1]) * 83

	shuffled_array_indexes = []
	for num in str(random_num):
		while num in shuffled_array_indexes:
			num = str(int(num)+10)
		if int(num) < len(array):
			shuffled_array_indexes.append(num)

	shuffled_array = [0]*len(array)
	for i in range(len(array)):
		shuffled_array[int(shuffled_array_indexes[i])] = array[i]

	return shuffled_array
	

######## ABECEDARIO

def abcd_generator():
	clear_cons = []
	clear_vowel = ["A", "E", "I", "O", "U"]

	for code in range(65,91):
		letter = chr(code)
		if letter not in clear_vowel:
			clear_cons.append(letter)

	return (clear_cons, clear_vowel)


######## CLAVES

def key_generator(cons, vowel, seed):
	clear_cons, clear_vowel = abcd_generator()
	cons1 = random_shuffle(seed, clear_cons)
	cons2 = random_shuffle(seed*3, clear_cons)
	vowel1 = random_shuffle(seed*5, clear_vowel)
	vowel2 = random_shuffle(seed*7, clear_vowel)
	vowel_key = []
	cons_key = []
	
	for i in range(len(vowel)):
		vowel_key.append(vowel1[i]+cons1[i]+vowel2[i])

	for i in range(len(cons)):
		cons_key.append(cons1[i]+cons2[i])

	return (vowel_key, cons_key)


######## CIFRADO

def cipher(text, seed):
	clear_cons, clear_vowel = abcd_generator()
	vowel_key, cons_key = key_generator(clear_cons, clear_vowel, seed)
	encrypted_text = ""
	encrypted_spaced_text = ""

	for letter in text:
		if letter in clear_vowel:
			encrypted_text += vowel_key[clear_vowel.index(letter)]
		elif letter in clear_cons:
			encrypted_text += cons_key[clear_cons.index(letter)]

	cnt = 0
	for i in encrypted_text:
		encrypted_spaced_text += i
		cnt += 1
		if cnt % 4 == 0:
			encrypted_spaced_text += " "

	return encrypted_spaced_text


######## DESCIFRADO

def decipher(text, seed):
	clear_cons, clear_vowel = abcd_generator()
	vowel_key, cons_key = key_generator(clear_cons, clear_vowel, seed)
	decrypted_spaced_text = ""
	decrypted_text = ""
	text = text.replace(" ", "")
	i = 0
	
	while i < len(text):
		if text[i] in clear_cons:
			decrypted_spaced_text += text[i]+text[i+1]
			i += 2
		elif text[i] in clear_vowel:
			decrypted_spaced_text += text[i]+text[i+1]+text[i+2]
			i += 3
		decrypted_spaced_text += " "

	for code in decrypted_spaced_text.split(" "):
		if code in vowel_key:
			decrypted_text += clear_vowel[vowel_key.index(code)]
		elif code in cons_key:
			decrypted_text += clear_cons[cons_key.index(code)]

	return decrypted_text


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
		print("\n -- DBOW IQTR XOWI YPSR IKOX WRXI KO !")
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
			key = int(input("\n Introduce la clave: "))
			assert(len(str(key)) != 0)
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
			print("\n ERROR / Texto descifrado incorrectamente")
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
		                    _  __       _          _\n\
  _ __ ___   ___  _ __   ___   __ _| |/ _| __ _| |__   ___| |_ ___\n\
 | '_ ` _ \\ / _ \\| '_ \\ / _ \\ / _` | | |_ / _` | '_ \\ / _ \\ __/ _ \\\n\
 | | | | | | (_) | | | | (_) | (_| | |  _| (_| | |_) |  __/ || (_) |\n\
 |_| |_| |_|\\___/|_| |_|\\___/ \\__,_|_|_|  \\__,_|_.__/ \\___|\\__\\___/\n\n")
	   
	print(logo, "\n"*2)
	sleep(2)															
	main_menu()


######## EJECUCIÓN DEL SCRIPT

if __name__ == "__main__":
	start()




