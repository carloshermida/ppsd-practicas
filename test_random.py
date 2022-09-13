
# CÁLCULO DE PROBABILIDAD DE REPETECIÓN DEL MEZCLADO ALEATORIO
# 			 RANDOM_SHUFFLE VS RANDOM.SHUFFLE
#


##### ABECEDARIO

def abcd_generator(op):
	abc = []
	vow =["A", "E", "I", "O", "U"]
	for a in range(65, 91):
		if op == "all":
			abc.append(chr(a))
		else:
			if chr(a) not in vow:
				abc.append(chr(a))
	return abc


##### TRANSFORMADOR DE ARRAY EN STRING

def merge_list(array):
	string = ""
	for item in array:
		string += item
	return string


##### MEZCLADOR DE LISTAS DEL USUARIO

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


##### TEST

vow =["A", "E", "I", "O", "U"]
cons = abcd_generator("cons")
abc = abcd_generator("all")

################# PARÁMETROS ###########################
s_rep = 1
e_rep = 20000
use = cons
########################################################

import math
rep = e_rep-s_rep+1
print("\n CÁLCULO DE PROBABILIDAD DE REPETECIÓN DEL MEZCLADO ALEATORIO\n\t       RANDOM_SHUFFLE VS RANDOM.SHUFFLE")
print(f"\nRango de semillas {s_rep}:{e_rep} ({rep} iteraciones)")
print(f"Posibles combinaciones distintas: {math.factorial(len(use))}\n")

## Mezclador creado

cnt = 0
arrays_array = []
for i in range(s_rep, e_rep+1):
	tmp = merge_list(random_shuffle(i, use))
	if tmp in arrays_array:
		cnt +=1
	arrays_array.append(tmp)

print("USUARIO:   {}  {}%".format(cnt, round(cnt/rep, 3)*100))


## Mezclador de la librería random

import random
cnt = 0
arrays_array = []
for i in range(s_rep, e_rep+1):
	tmp_abc = use.copy()
	random.seed(i)
	random.shuffle(tmp_abc)
	tmp = merge_list(tmp_abc)
	if tmp in arrays_array:
		cnt +=1
	arrays_array.append(tmp)

print("LIBRERÍA:  {}  {}%".format(cnt, round(cnt/rep, 3)*100))


######

# Esta es la probablidad (2.5% - 4%) de que se repita una combinacion cogiendo semillas secuenciales
# Sin embargo, en nuestro algoritmo utilizamos la seed, seed*3, seed*5, seed*7; lo que disminuye la probabilidad
# de que se mezclen de igual manera las listas. Además, si por ejemplo la semilla 6 y la semilla 43 mezclaran de la
# misma manera, las siguientes listas que multiplican la semilla por los numeros descritos anteriormente no serían las mismas.

######






