#1.Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000. 

from audioop import mul


for n in range(5,1000):
    if n % 5 == 0:
        print(n)
#2.Contar, a la manera del Dojo: imprime números enteros del 1 al 100. 
# Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
for n in range(1,101):
    if n % 10 == 0:
        print("Coding Dojo")
        continue
    elif n % 5 == 0:
        print("Coding")
    else:
        print(n)
print("------------")
#3.Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final. 
suma_impares = 0
for n in range(0,500000):
    if n % 2 != 0:
        suma_impares =suma_impares+ n
print(suma_impares)
print("------------")
#4.Cuenta regresiva de a 4: imprime números positivos 
# comenzando desde el 2018, en cuenta regresiva de 4 en 4. 
# num = 2018
# for i in range(2018,0,-4):
#     print(i)
# print("------------")
#5.Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en 
# lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult.
#  Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas).
# lowNum = 2
# highNum = 9
# mult = 3
# for n in range(lowNum,highNum+1):
#     if n % mult==0:
#         print(n)
# print("------------")