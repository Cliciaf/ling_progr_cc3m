"""
receber numero do cartão
transformar em string
Pegar os numeros de index impar a partir do penultimo numero
multiplicar por dois cada item 
somar os digitos de cada resultado mais os numeros de index pares 
somar o ultimo digito  
se o numero final for divisivel por 10, então é valido

"""

def entrada():
  """entrada do cartão"""
  numeroCartaoEntrada = input("Entre com o numero do cartão: ")
  return numeroCartaoEntrada


def doingList(entrada):
    """transformando o input, que está em string, em uma lista de inteiros e verificando se tem a quantidade minima de caracteres"""
    numero = entrada
    global list_of_ints
    list_of_ints = [int(x) for x in numero]
    #print(list_of_ints)  # 👉️ [1, 2, 3, 4, 5, 6]
    
    if len(list_of_ints) < 13:
      print('porfavor, insira um numero de cartão valido.')
      entrada()
    return list_of_ints
    

def flagValidator():
    """validando a bandeira do cartão"""
    global bandeira
    bandeira = ''
    if list_of_ints[0] == 5:
      bandeira = 'MASTERCARD'
    elif list_of_ints[0] == 3:
      bandeira = 'AMEX'
    elif list_of_ints[0] == 4:
      bandeira = 'VISA'
    else:
      bandeira = 'INVALIDO'

    return bandeira


def cardValidator():
    """validando o numero do cartao"""

    somaDigitos = 0
    somaParcial = 0
    somaTotal = 0
    """Para validar, é necessario usar o Algoritmo de Luhn. Portanto, temos a seguir a implememtação desse algoritmo:"""
    for i in (range(len(list_of_ints) - 2, -1,-2)):
      list_of_ints[i] = list_of_ints[i]*2

      if list_of_ints[i] > 10 :
        somaDigitos +=(1 + (list_of_ints[i]-10))
      else:
        somaDigitos+=(list_of_ints[i])

    for i in (range(len(list_of_ints) - 1, -1,-2)):
      somaParcial+= list_of_ints[i]
      somaTotal = somaParcial + somaDigitos

    if str(somaTotal)[1] == '0':
     return bandeira
    else:
      return 'INVALIDO'


def output():
    doingList(entrada())
    flagValidator()
    print(cardValidator())
    


"""Interface"""

output()