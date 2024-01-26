'''
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 */
'''

## Creamos una cadena de ejemplo

mi_cadena1 = "Esto es una frase de ejemplo"
mi_cadena2 = "Pruebas de cadenas"

#Acceso a caracteres específicos, vamos a mostar el caracter 8 que sería la "u".
print(f"{mi_cadena1[8]}")
#Acceso a subcadenas, vamos a mostrar una subcadena que empieza en el caracter 6 y termina en el 12, se debería ver "s una".
print(f"{mi_cadena1[6:12]}")
#Calculamos la longitud de una cadena, la longitud de mi cadena es 28.
print(f"La longitud de cadena1 es: {len(mi_cadena1)}")
print(f"La longitud de cadena2 es: {len(mi_cadena2)}")
#Vamos a concatenar dos cadenas
print(f"Esto son las dos cadena concatenadas: {mi_cadena1 + mi_cadena2}")
#Ejemplo de repetición, vamos a contar el número de veces que aparece el caracter "e" en mi_cadena1
print(f"El número de veces que aparece el carácter e es: {mi_cadena1.count('e')}")
#Ejemplo de recorrido, vamos a imprimir caracter a caracter mi_cadena1
for car in mi_cadena1:
    print(f"{car}")
#Ejemplo de conversión de mayúsculas a minúsculas
print(f"Vamos a imprimir mi_cadena1 en mayúsculas: {mi_cadena1.upper()}")
print(f"Vamos a imprimir mi_cadena1 en minúsculas: {mi_cadena1.lower()}")
#Ejemplo de reemplazo, vamos a cambiar los carácteres e por E en mi_cadena1
print(f"Vamos a cambiar los caracteres e por E en mi_cadena1: {mi_cadena1.replace('e','E')}")
#Ejemplo de divisón, vamos a imprimir mi_cadena1 separado por espacios
print(f"Vamos a imprimir mi_cadena1 usando como separado el espacio: {mi_cadena1.split(' ')}")
#Ejemplo de unión, vamos a añadir el texto, con ganas de aprender y buscando tiempo.
print(f"Imprimimos mi_cadena1 y añadimso un texto {mi_cadena1}, con ganas de aprender y buscando tiempo")
#Ejemplo de interpolación, vamos a interpolar mi_cadena1 y mi_cadena2, con esto vamos a generar cadena3 y entre ellas vamos a poner unimos.
mi_cadena3 = f"{mi_cadena1} unimos {mi_cadena2}"
print(f"{mi_cadena3}")
#Ejemplo de búsqueda, vamos a buscar por la cadena frase en mi_cadena1
print(f"Existe la cadena frase en mi_string1: {mi_cadena1.find('frase')}")
#Ejemplo de verificación, podemos hacer diferentes verificaciones, para comprobar el tipo de cadenas que tenemos.
print(f"Vamos a ver si la palabra casa tiene solo caracteres alfabéticos: {'casa'.isalpha()}")
print(f"Como casa es solo alfabeto, si compruebo si es numérico va a salir false: {'casa'.isnumeric()}")
print(f"También puedo comprobar si casa123 es alfanumérico: {'casa123'.isalnum()}")
print(f"Además podemos comprobar si tienen mayúculas como Casa: {'Casa'.isupper()} o bien casa: {'casa'.islower()}")








'''  
/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
'''