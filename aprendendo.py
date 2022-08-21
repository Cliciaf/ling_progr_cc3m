#estudo de python
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits 
_________________
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

resultado: 
Python is fantastic
Python is awesome
_____________
If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
_______________

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
____________
import random

print(random.randrange(1, 10))
resultado: 8

____________
The len() function returns the length of a string:


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
Resultado: 
apple
banana
cherry

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

 ou

 fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

Resultado:

['apple', 'banana', 'mango']
_________


receber numero do cartão
transformar em string
Pegar os numeros de index impar a partir do penultimo numero
multiplicar por dois cada item 
somar os digitos de cada resultado mais os numeros de index pares 
somar o ultimo digito  
se o numero final for divisivel por 10, então é valido

numeroCartao = input("Entre com o numero do cartão: ")
a = 0
i = 0
soma = 0
resultado = 0
for i in range(len(numeroCartao)-2, -1,-2):
  print(numeroCartao[i])
  a = int(numeroCartao[i]) * 2
  if len(str(a))> 1:
    b = str(a)
    print("entrou no if")
    soma = int(b[0]) + int(b[1])
    print(soma)
    resultado += soma 
  else:
    resultado+=a
    print(a)
print(resultado)
"""
