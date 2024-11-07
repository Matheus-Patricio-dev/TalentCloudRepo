"""

Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

"""


def idade():

    while True:
        try:
            nasc = int(input("Digite o ano de nascimento(entre 1922 e 2021): "))
            if 1922 < nasc < 2021:
                nome = input("Digite seu nome: ")
                print(f"{nome}, em 2022 voce fará {2022 - nasc} anos!")
                break
            else:
                print("Ano de nascimento invalido. Digite entre 1922 e 2021!")
                
        except ValueError:
            print("Valor inválido!")

idade()