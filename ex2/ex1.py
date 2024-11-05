def calc():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    func = int(input("Digite a função[1 - soma, 2 - subtração, 3 - multiplicação, 4 - divisão] "))

    if func == 1:
        print(num1 + num2)
    elif func == 2:
        print(num1 - num2)
    elif func == 3:
        print(num1 * num2)
    elif func == 4:
        print(num1 / num2)
    else:
        print('ERROR')

calc()