### Prácticas PPSD - [[Changelog]](https://github.com/carloshermida/ppsd-practicas/blob/main/changelog.md#changelog)
##### Curso 2021/2022

Este repositorio contiene las prácticas de la asignatura _Protección, Privacidad y Seguridad de Datos_ del grado en _Ciencia e Ingeniería de Datos_ de la _Universidad de Coruña_.

---

#### Monoalfabeto
Creación e implementación de un algoritmo de cifrado simétrico por sustitución monoalfabeto
* Cipher
```
En primer lugar, generamos las listas de consonantes y vocales originales,
y a partir de la semilla obtenemos los n-gramas por los que vamos a sustituir
las letras del texto en claro. Intercambiamos las vocales por su correspondiente
trigrama y las consonantes por su respectivo digrama. Finalmente, añadimos un
espacio cada 4 posiciones para tratar de dificultar el análisis.

Ejemplo:
Texto en claro: “Este es el texto en claro”. 
Semilla: 4

El algoritmo automáticamente pone el texto como “ESTEESELTEXTOENCLARO”
(con la función auxiliar text_format), y con la semilla que le pasamos crea las
siguientes asignaciones para las letras:

Para las vocales: ['AQI', 'IPE', 'OFA', 'EBU', 'UJO']
Para las consonantes: ['QJ', 'PK', 'FL', 'BC', 'JH', 'GB', 'HQ', 'CP', 'MM', 'NF', 'TT',
'SR', 'YV', 'LD', 'KN', 'RW', 'VX', 'DS', 'XZ', 'ZG', 'WY']
 
Finalmente, sustituye en el texto en claro, pone los espacios y devuelve:
IPEK NRWI PEIP EKNI PEMM RWIP EXZR WEBU IPET TPKM MAQI LDEB U
```
* Decipher
```
Esta función comienza ignorando los espacios y, a continuación, si el elemento que
se está seleccionando es una consonante avanza dos elementos y añade un espacio
(debido a que las consonantes son digramas), mientras que si el elemento seleccionado
es una vocal se avanza 3 elementos y se añade un espacio (debido a que las vocales
son trigramas).

Una vez tengamos estos elementos separados, los cambiamos por su correspondiente
letra en claro.

Ejemplo:
Texto cifrado: “IPEK NRWI PEIP EKNI PEMM RWIP EXZR WEBU IPET TPKM MAQI LDEB U”.
Semilla: 4

El algoritmo automáticamente podría el texto como
“IPEKNRWIPEIPEKNIPEMMRWIPEXZRWEBUIPETTPKMMAQILDEBU”, y con la semilla que le pasamos,
lo que hace es crear las siguientes asignaciones para las letras:

Para las vocales: ['AQI', 'IPE', 'OFA', 'EBU', 'UJO']
Para las consonantes: ['QJ', 'PK', 'FL', 'BC', 'JH', 'GB', 'HQ', 'CP', 'MM', 'NF',
'TT', 'SR', 'YV', 'LD','KN', 'RW', 'VX', 'DS', 'XZ', 'ZG', 'WY']

Finalmente, sustituye en el texto cifrado, y devuelve: “ESTEESELTEXTOENCLARO”
```
* Random Shuffle
```
Esta función pretende sustituir a la función random.shuffle de la librería Random.

El objetivo de nuestra función es mezclar de manera aleatoria mediante una semilla
los elementos que le pasamos en forma de array, de manera que con una semilla
siempre se va a hacer de la misma forma.

Por lo tanto, a esta función se le pasan los argumentos seed, que sería un número
entero,y array, que sería la lista de elementos que queremos mezclar.

En primer lugar, se crea una lista vacía array_indexes que guardará los números
del 0 al 9 tantas veces como sean necesarias para que la longitud de array_indexes
sea mayor o igual a la longitud de “array”, que es lo que se hace en el primer bucle.
Además, se inicializa el número random_num a partir de la semilla y una serie
de cálculos.

En el bucle while se va eliminando cada cifra de random_num de array_indexes
(en el caso en el que no queden de esas cifras en el array, simplemente
se pasa a la siguiente).

Si random_num consiguió vaciar array_indexes, ese número es válido. En caso
contrario, se le aplican unos cálculos a este número para obtener otro más largo.

Se crea una lista vacía que va a guardar los índices del array pero mezclados,
shuffled_array_indexes, y la manera de mezclarlos se define en el siguiente bucle,
que lo que hace es coger cada cifra del random_num y añadir ese índice a
shuffled_array_indexes en caso de que ya esté añadido, le suma 10. En caso de que
ese número sea mayor a la longitud del “array” (el que se quiere mezclar),
ese índice se descarta.

Por último, coloca los valores de “array” en las posiciones que indica
shuffled_array_indexes y obtenemos de esta manera el array barajado.

Esta función no consigue para todas las semillas una mezcla diferente, pero lo
hace considerablemente bien. De hecho, como nosotros al crear los abecedarios
permutados utilizamos una semilla y esa misma multiplicada por 3, 5 y 7, es 
muy complicado que casualmente coincidan los abecedarios barajados resultantes.

Ejemplo:
array = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’, ‘h’, ‘i’, ‘j’, ‘k’]
seed = 43 
array_indexes=[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]

Primer random_num que crea:
random_num = 16684 
array_indexes=[0,2,3,5,7,9,0,1,2,3,4,5,7,8,9]

A continuación, haría cálculos para obtener otro “random_num”

Último random_num que crea:
random_num = 200096949731595398487625349157381203732 
array_indexes = [ ]
shuffled_array_indexes = [2, 0, 10, 9, 6, 4, 7, 3, 1, 5, 8]
array = [‘c’, ‘a’, ‘k’, ‘j’, ‘g’, ‘e’, ‘h’, ‘d’, ‘b’, ‘f’, ‘i’]

Ese sería el array barajado
```
* Abcd Generator
```
Esta función devolverá:
   clear_cons: una lista con todas las consonantes del abecedario.
   clear_vowel: una lista con todas las vocales del abecedario.
```	
* Key Generator
```
Esta función crea cuatro listas: 2 con las consonantes permutadas y 2 con las
vocales permutadas (con semillas diferentes). Posteriormente, crea trigramas para
referirse a las vocales y digramas para referirse a las consonantes.

Los trigramas de las vocales tienen la estructura de vocal-consonante-vocal 
mientras que los digramas de consonantes tiene la estructura de consonante-consonante.

Esta función devolverá:
	vowel_key: lista con los trigramas que identifican a las vocales. 
	cons_key: lista con los digramas que identifican a los consonantes.

```
* Text format
```
Elimina o cambia todos los caracteres no permitidos en la práctica del texto en
claro que se desea cifrar, como letras con tildes, signos de puntación, espacios etc.
```
* Front-end
```
Para facilitar el uso del algoritmo, creamos una interfaz para el usuario. 
Simplemente se debe introducir el número del apartado al que se quiere acceder
y seguir las instrucciones.
	
	(1) Cifrar
		(1) Escribir el texto
		(2) Importar desde un archivo 
		(0) Volver al menú principal

	(2) Descifrar
		(1) Escribir el texto
		(2) Importar desde un archivo 
		(0) Volver al menú principal

	(0) Salir
```
###### Sintaxis de uso
```
Ejecuta el fichero de Python en cualquier terminal ($python3 monoalfabeto.py).
En el menú principal, si quieres cifrar pulsa el número 1, y si quieres descifrar
el número 2. A continuación, la tecla enter.

Para importar el texto desde un fichero, selecciona la opción 2 e introduce el
nombre del archivo (en caso de que se encuentre en un directorio distinto al
del fichero de Python, se debe introducir la ruta).

Si prefieres escribir el texto, selecciona la opción 1, escribe el texto,
y al terminar confirma que el texto es correcto.

Introduce la clave, teniendo en cuenta que en este caso es numérica (la semilla).

El resultado se muestra por pantalla, y se da la opción de guardarlo en un archivo.
En caso afirmativo, se debe indicar el nombre y extensión. Finalmente, pulsa enter
para volver al menú principal.
```

---

#### Test Random
Programa para comparar el rendimiento de la función *random.shuffle* de la librería de Python _"random"_ y la función *random_shuffle* creada para el algoritmo de cifrado simétrico por sustitución monoalfabeto

---

#### Vigenère
Implementación del algoritmo de Vigenère
* Cipher
```
Esta función crea los abecedarios con desplazamiento en función de la clave introducida. 
A continuación, decide que abecedario le corresponde a cada letra según su posición en
el texto y sustituye por la letra que ocupa el lugar correspondiente a la letra original.

Ejemplo:
Texto en claro: “Este es el texto en claro”
Clave: “cable”

El algoritmo automáticamente pone el texto como “ESTEESELTEXTOENCLARO” (con la función
auxiliar text_format).

abc: [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]

abc_list [0]: [C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B] 
abc_list [1]: [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z] 
abc_list [2]: [B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A] 
abc_list [3]: [L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K] 
abc_list [4]: [E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D]

Texto cifrado: “GSUPIUEMEIZTPPRELBCS”
```
* Decipher
```
Esta función crea los abecedarios con desplazamiento en función de la clave introducida. 
A continuación, decide que abecedario le corresponde a cada letra según su posición en el
texto y sustituye por la letra real que ocupa el lugar correspondiente a la letra cifrada
en cada abecedario.

Ejemplo:
Texto cifrado: “GSUPIUEMEIZTPPRELBCS”
Clave: “cable”

abc: [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]

abc_list [0]: [C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B] 
abc_list [1]: [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
abc_list [2]: [B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A] 
abc_list [3]: [L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K] 
abc_list [4]: [E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D]

Texto en claro: “ESTEESELTEXTOENCLARO”
```
* Abcd Generator
```
Tras obtener el abecedario normal, crea diferentes abecedarios a partir de la clave
introducida (tantos como caracteres tenga la clave). Cada uno de estos abecedarios
empiezan por las letras de la clave y van hasta la letra Z, y vuelven a la A hasta
llegar a la letra anterior a la letra de la clave.
```	
* Text format
```
Elimina o cambia todos los caracteres no permitidos en la práctica del texto en claro
que se desea cifrar, como letras con tildes, signos de puntación, espacios etc.
```
* Front-end
```
Para facilitar el uso del algoritmo, creamos una interfaz para el usuario. 
Simplemente se debe introducir el número del apartado al que se quiere acceder
y seguir las instrucciones.
	
	(1) Cifrar
		(1) Escribir el texto
		(2) Importar desde un archivo 
		(0) Volver al menú principal

	(2) Descifrar
		(1) Escribir el texto
		(2) Importar desde un archivo 
		(0) Volver al menú principal

	(0) Salir
```
###### Sintaxis de uso
```
Ejecuta el fichero de Python en cualquier terminal ($python3 vigenere.py).
En el menú principal, si quieres cifrar pulsa el número 1, y si quieres descifrar
el número 2. A continuación, la tecla enter.

Para importar el texto desde un fichero, selecciona la opción 2 e introduce el
nombre del archivo (en caso de que se encuentre en un directorio distinto al del
fichero de Python, se debe introducir la ruta).

Si prefieres escribir el texto, selecciona la opción 1, escribe el texto, y al
terminar confirma que el texto es correcto.

Introduce la clave, teniendo en cuenta que en este caso está compuesta por letras.

El resultado se muestra por pantalla, y se da la opción de guardarlo en un archivo.
En caso afirmativo, se debe indicar el nombre y extensión. Finalmente, pulsa enter
para volver al menú principal.
```

---

#### RC4
Implementación del algoritmo RC4
* KSA
```
Inicializa la lista S con los números del 0:255, en binario. Genera la lista T,
donde se repite la clave en bucle hasta llegar a 256 elementos.

Finalmente, permuta el vector S.
```
* PRGA
```
Por cada carácter que se quiera cifrar, se realiza una llamada a la función PRGA. 
Esta realiza permutaciones en S y obtiene los valores del keystream. Estos números,
que se guardan en binario, se utilizarán posteriormente para la operación XOR con el
carácter que se quiera cifrar/descifrar.
```
* Cipher
```
En primer lugar, se genera la lista S y se le aplica la permutación inicial.
Creamos el DataFrame donde se guardarán los datos que se mostrarán al usuario posteriormente.
Inicializamos también el keystream, que empieza vacío, y los valores de i y j (0,0).

Procesamos cada carácter que introduzca el usuario y mostramos la codificación y los
cambios que se producen en S (en rojo los valores de S[i] y S[j] que se intercambian,
y en verde el valor que se añade al keystream y que se utilizará para el XOR).
```	
* Decipher
```
En primer lugar, se genera la lista S. Inicializamos también el keystream,
que empieza vacío, y los valores de i y j (0,0).

Automáticamente, se descifra cada carácter del texto cifrado (introducido en hexadecimal),
calculando los valores del keystream y el resultado del XOR. Una vez que tenemos el
texto descifrado completamente, se muestra por pantalla.
```
* Front-end
```
Para facilitar el uso del algoritmo, creamos una interfaz para el usuario. 
Simplemente se debe introducir el número del apartado al que se quiere acceder
y seguir las instrucciones.
	
	(1) Cifrar

	(2) Descifrar

	(0) Salir
```
###### Sintaxis de uso
```
Ejecuta el fichero de Python en cualquier terminal ($python3 RC4.py).

En el menú principal, si quieres cifrar pulsa el número 1, y si quieres
descifrar el número 2. A continuación, la tecla enter.

En el caso del cifrado, se pedirá que se introduzca la clave en hexadecimal.
Después se mostrará por pantalla el estado inicial de la lista S y su primera permutación.
Para continuar, simplemente se debe introducir un carácter y pulsar enter. Se verá una
tabla con todos los datos relevantes de la codificación y los cambios producidos en la
lista S (en rojo los valores de S[i] y S[j] que se intercambian, y en verde el valor que
se añade al keystream y que se utilizará para el XOR). Para terminar la ejecución del
cifrado, se debe introducir la palabra exit y después pulsar enter.

En el caso del descifrado, escribe el texto en hexadecimal, y al terminar confirma
que el texto es correcto. Después, se pedirá que se introduzca la clave en hexadecimal,
y ya se podrá ver en la pantalla el texto descifrado. Finalmente, pulsa enter para
volver al menú principal.
```

---

#### Recursos
Contiene dos pares de archivos cifrados y descifrados para probar los algoritmos

---

#### EasterEggs
Al cerrar cualquiera de los tres programas aparece un texto que está cifrado
según el algoritmo que corresponda. Para descifrarlos, se debe utilizar el código
usando las siguientes claves:
* Monoalfabeto: 2022
* Vigènere: PPSD
* RC4: 7e6 (hex(2022))
