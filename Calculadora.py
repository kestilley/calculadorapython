valor1 = float(input ('Informe o primeiro valor: '))
valor2 = float(input ('Informe o segundo valor: '))

print('Qual operacao deseja fazer:')
print('1- Soma')
print('2- subtracao')
print('3- Multiplicacao')
print('4- Divisao')

operacao = int(input('Escolha uma opcao: '))

if operacao  == 1:
    soma = valor1 + valor2
    print (f'A soma de {valor1:g} + {valor2:g} é igual a: {soma: .2f}')
elif operacao == 2:
    subtracao = valor1 - valor2
    print(f'A subtração de {valor1:g} - {valor2:g} é igual a: {subtracao: .2f}')
elif operacao == 3:
    multiplicacao = valor1 * valor2
    print(f'A multiplicação de {valor1:g} por {valor2:g} é igual a: {multiplicacao: .2f}')         
elif operacao == 4:
    if valor2 != 0:
      divisao = valor1 / valor2
      print(f'A divisão de {valor1:g} por {valor2:g} é igual a: {divisao: .2f}')
    else:
      print ('Não é possível dividir por 0')
else :
    print('Opção Invalida')
