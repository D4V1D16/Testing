#Generalizacion del array
import random
 
 
arrayEjemplo = [1,2,3,4,5]

for i in range(5):
    arrayEjemplo[i] = int(random.uniform(0,50))
    print(arrayEjemplo[i+1])

varInput=int(input("Ingresa un valor"))
print(varInput)

for i in range(5):
    if arrayEjemplo[i] > varInput:
        print("El valor del arreglo es mayor")
    else :
        print("El valor del arreglo es manor")
    print(str(arrayEjemplo[i]+">"str(varInput)))






