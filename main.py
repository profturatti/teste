# main.py

import mathBasic

def menu():
    print("\n--- Calculadora Básica ---")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Resto")
    print("6. Teste Par/Ímpar")
    print("7. Raiz Quadrada")
    print("0. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando...")
            break

        if opcao in ["1", "2", "3", "4", "5"]:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if opcao == "1":
                print("Resultado:", mathBasic.soma(a, b))
            elif opcao == "2":
                print("Resultado:", mathBasic.subtracao(a, b))
            elif opcao == "3":
                print("Resultado:", mathBasic.multiplicacao(a, b))
            elif opcao == "4":
                print("Resultado:", mathBasic.divisao(a, b))
            elif opcao == "5":
                print("Resultado:", mathBasic.resto(a, b))

        elif opcao == "6":
            valor = int(input("Digite um número inteiro: "))
            print("Resultado:", mathBasic.testePar(valor))

        elif opcao == "7":
            a = float(input("Digite um número: "))
            print("Resultado:", mathBasic.raiz(a))

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

