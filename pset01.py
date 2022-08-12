"""
receber numero do cartão
transformar em string
Pegar os numeros de index impar a partir do penultimo numero
multiplicar por dois cada item 
somar os digitos de cada resultado mais os numeros de index pares 
somar o ultimo digito  
se o numero final for divisivel por 10, então é valido
"""
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