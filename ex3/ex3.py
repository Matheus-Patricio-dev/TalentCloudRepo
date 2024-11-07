

def calculadora():
    while True:
        try:
            operacao = int(input("Bem-vindo(a) a calculadora! Escolha uma opção: 1 - Adição | 2 - subtração | 3 - Multiplicação | 4 - Divisão | 0 - Sair "))

            if operacao == 1 :
                num1 = int(input("Digite o primeiro numero: "))
                num2 = int(input("Digite o segundo numero: "))

                print(num1 + num2)
            elif operacao == 2 :
                num1 = int(input("Digite o primeiro numero: "))
                num2 = int(input("Digite o segundo numero: "))

                print(num1 - num2)
            elif operacao == 3 :
                num1 = int(input("Digite o primeiro numero: "))
                num2 = int(input("Digite o segundo numero: "))

                print(num1 * num2)
            elif operacao == 4 :
                num1 = int(input("Digite o primeiro numero: "))
                num2 = int(input("Digite o segundo numero: "))

                print(num1 / num2)
            elif operacao == 0 :
               break
            else:
                print("erro")
        except:
            print("Essa opção não existe!")

calculadora()