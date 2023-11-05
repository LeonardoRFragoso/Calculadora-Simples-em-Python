import os

while True:

    print('As opções são:\n')
    print('1 para Soma.')
    print('2 para Subtração.')
    print('3 para Multiplicação.')
    print('4 para Divisão.')
    print('5 para Potenciação.\n')

    while True:
        try:
            operacao = int(input('Qual operação deseja realizar? Tecle de acordo com as opções acima:    '))
        except ValueError:
            continue
        if operacao not in [1, 2, 3, 4, 5]:
            print('Digite apenas as opções dadas, de 1 a 5.\n')
            continue
        break

    if operacao == 1:
        nome_operação = 'soma'
    elif operacao == 2:
        nome_operação = 'Subtração'
    elif operacao == 3:
        nome_operação = 'Multiplicação'
    elif operacao == 4:
        nome_operação = 'Divisão'
    elif operacao == 5:
        nome_operação = 'Potenciação'

    print(f'A operação escolhida foi a {nome_operação}')

    while True:
        try:
            numero1 = float(input('Escolha o primeiro valor:    '))
            numero2 = float(input('Escolha o segundo valor:    '))
        except ValueError:
            print('Digite apenas números válidos.\n')
            continue
        if operacao == 4 and numero2 == 0:
            print('Divisão por zero não possível escolha novamente os dois números.\n')
            continue
        break

    if operacao == 1:
        resultado = numero1 + numero2
    elif operacao == 2:
        resultado = numero1 - numero2
    elif operacao == 3:
        resultado = numero1 * numero2
    elif operacao == 4:
        resultado = numero1 / numero2
    elif operacao == 5:
        resultado = numero1 ** numero2

    print(f'O resultado da {nome_operação} é {resultado:.2f}')

    while True:
        continuar = str.lower(input('Deseja fazer outra operação? (S ou N)'))
        if continuar not in {'s', 'n'}:
            continue
        elif continuar == 'n':
            os.system('cls')

        break
    if continuar == 's':
        os.system('cls')
        continue
    break