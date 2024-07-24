# Haga un comando que le permita saber al usuario
# cual palabra es palidroma o no 

letra = str(input("Ingrese la palabra para conocer si palidroma: ")).lower()

letra1 = list(letra)
letra2 = list(letra1)
letra2.reverse()
if letra2==letra1:
    print("Es palidroma ")
else:
    print("No es palidroma ")
