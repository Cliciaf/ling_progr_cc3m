"""  

1. Começando pelo penúltimo dígito e indo em direção ao primeiro, multiplique cada dígito
sim, dígito não, por 2. Depois some os dígitos desses resultados (atenção: não é para somar
os resultados, é para somar os dígitos dos resultados);
2. Adicione a soma dos dígitos dos resultados obtidos no passo anterior, à soma dos dígitos que
não foram multiplicados por 2.
3. Se o último dígito do total for 0 (ou, mais formalmente, se o total obtido no passo anterior
for dividio por 10 e tiver resto 0), então o número representa um cartão de crédito válido
(sintaticamente).
"""



def entrada():
  """entrada do cartão"""
  numeroCartaoEntrada = input("Entre com o numero do cartão: ")
  return numeroCartaoEntrada


def check_user_input(input):
    """verifica se foram apenas numeros inseridos"""
    try:
        # Convert it into integer
        val = int(input)
        doingList(input)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return "INVALIDO"
            
        except ValueError:
            return "INVALIDO"
            


def doingList(entrada):
    
    """transformando o input, que está em string, em uma lista de inteiros e verificando se tem a quantidade minima de caracteres"""
    numero = entrada
    global list_of_ints
    list_of_ints = [int(x) for x in numero]
    if len(list_of_ints) < 13:
      print('porfavor, insira um numero de cartão valido.')
      entrada()
    return list_of_ints
    

def flagValidator():
    """validando a bandeira do cartão"""
    global bandeira
    bandeira = ''
    if list_of_ints[0] == 5 and len(list_of_ints) == 16:
      if list_of_ints[1] in [1,2,3,4,5]:
        bandeira = 'MASTERCARD'
    elif list_of_ints[0] == 3 and len(list_of_ints) == 15:
      if list_of_ints[1] in [4,7]:
        bandeira = 'AMEX'
    elif list_of_ints[0] == 4:
      if len(list_of_ints) in [13,16]:
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
    check = check_user_input(entrada())
    if check == 'INVALIDO':
      print('INVALIDO')
    else:
      flagValidator()
      print(cardValidator())
    


"""Interface"""

output()