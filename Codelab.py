
#  Define una variable de cada tipo de primitivo

Edad = int(22)
clima = float(31.5)
Estudias = bool(True)
cadena = str("Sharon Elizabeth")
#-------------------------------------------------------------------------------------------------------------------------------

# Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable

resultado = f"Me llamo {cadena} y tengo {Edad} años. Hoy el clima es de {clima} grados, y es {Estudias} que estudio actualmente."

print(resultado)

#-------------------------------------------------------------------------------------------------------------------------------

# Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo

      # Límites de los enteros en Python
# En Python, los enteros no tienen un límite fijo en su tamaño, ya que pueden crecer tanto como la memoria del sistema lo permita.
# Sin embargo, el límite práctico está determinado por la cantidad de memoria disponible en la máquina.

# Límites de los flotantes en Python
# Los flotantes en Python siguen el estándar IEEE 754 para representación de números de punto flotante.
# Para flotantes de doble precisión (float), Python utiliza 64 bits para representar un número en coma flotante.
# Esto proporciona aproximadamente 15-17 dígitos decimales de precisión.

# Valor mínimo positivo representable como flotante
# valor_min_float = 2.2250738585072014e-308

# Valor máximo representable como flotante
# valor_max_float = 1.7976931348623157e+308

# Precisión de los flotantes
# Debido a cómo se almacenan los flotantes en binario, algunos números no pueden ser representados con precisión exacta.
# Esto puede llevar a pequeños errores de redondeo en operaciones con flotantes.

# Cifras significativas en flotantes
# La cantidad de cifras significativas (dígitos que contribuyen a la precisión) en un número flotante puede variar.
# Los flotantes no pueden representar todos los números de manera precisa debido a las limitaciones del formato binario.

# Notación científica y flotantes
# Python admite notación científica para representar números en coma flotante.
# Por ejemplo, 1.23e5 representa el número 123000. 

#-------------------------------------------------------------------------------------------------------------------------------

# Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero 
    # y almacenar el resultado en una variable

n = int(input("Cantidad de primeros numeros pares: "))

# Inicializar la variable para la suma
suma = 0

# Calcular la suma de los primeros n números pares
for i in range(1, n + 1):
    numero_par = 2 * i
    suma += numero_par

# Imprimir el resultado
print(f"La suma de los primeros {n} números pares es: {suma}")
