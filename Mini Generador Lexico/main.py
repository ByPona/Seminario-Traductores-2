from lexico import Lexico

entrada = input("Dame la cadena a analizar: ")
cadena = Lexico(entrada)

print("\nResultado del Analisis Lexico")
print("\nSimbolo               Tipo")
print("-------------------------------------")
print(cadena.evaluarcadena())
