"""
Calculadora Interativa em Python (CLI)
Execução: python calculadora_terminal.py
"""

import math

def exibir_menu():
    print("\n" + "=" * 40)
    print("        CALCULADORA EM PYTHON")
    print("=" * 40)
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potência (x^y)")
    print("6. Raiz Quadrada (√)")
    print("7. Divisão Inteira (//)")
    print("8. Resto da Divisão / Módulo (%)")
    print("9. Fatorial (n!)")
    print("10. Seno, Cosseno, Tangente")
    print("11. Ver Histórico")
    print("0. Sair")
    print("=" * 40)

def obter_numero(mensagem="Digite um número: "):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Entrada inválida! Digite um valor numérico.")

def main():
    historico = []
    
    print("Bem-vindo à Calculadora em Python!")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0-11): ").strip()
        
        if opcao == "0":
            print("\nObrigado por usar a calculadora! Encerrando...")
            break
            
        elif opcao in ("1", "2", "3", "4", "5", "7", "8"):
            num1 = obter_numero("Primeiro número: ")
            num2 = obter_numero("Segundo número: ")
            
            try:
                if opcao == "1":
                    resultado = num1 + num2
                    operacao = f"{num1} + {num2} = {resultado}"
                elif opcao == "2":
                    resultado = num1 - num2
                    operacao = f"{num1} - {num2} = {resultado}"
                elif opcao == "3":
                    resultado = num1 * num2
                    operacao = f"{num1} * {num2} = {resultado}"
                elif opcao == "4":
                    if num2 == 0:
                        raise ZeroDivisionError("Divisão por zero não é permitida.")
                    resultado = num1 / num2
                    operacao = f"{num1} / {num2} = {resultado}"
                elif opcao == "5":
                    resultado = num1 ** num2
                    operacao = f"{num1} ** {num2} = {resultado}"
                elif opcao == "7":
                    if num2 == 0:
                        raise ZeroDivisionError("Divisão por zero não é permitida.")
                    resultado = num1 // num2
                    operacao = f"{num1} // {num2} = {resultado}"
                elif opcao == "8":
                    if num2 == 0:
                        raise ZeroDivisionError("Módulo por zero não é permitido.")
                    resultado = num1 % num2
                    operacao = f"{num1} % {num2} = {resultado}"
                    
                print(f"\n✅ Resultado: {resultado}")
                historico.append(operacao)
            except ZeroDivisionError as erro:
                print(f"\n❌ Erro: {erro}")
            except OverflowError:
                print("\n❌ Erro: Número excessivamente grande para calcular!")

        elif opcao == "6":
            num = obter_numero("Digite o número para raiz: ")
            if num < 0:
                print("\n❌ Não é possível calcular raiz quadrada real de número negativo!")
            else:
                resultado = math.sqrt(num)
                operacao = f"√{num} = {resultado}"
                print(f"\n✅ Resultado: {resultado}")
                historico.append(operacao)

        elif opcao == "9":
            try:
                n = int(input("Digite um inteiro positivo para fatorial: "))
                if n < 0:
                    print("❌ Fatorial só existe para números inteiros não-negativos.")
                else:
                    resultado = math.factorial(n)
                    operacao = f"{n}! = {resultado}"
                    print(f"\n✅ Resultado: {resultado}")
                    historico.append(operacao)
            except ValueError:
                print("❌ Entrada inválida! Digite um número inteiro.")

        elif opcao == "10":
            ang = obter_numero("Digite o ângulo em graus: ")
            rad = math.radians(ang)
            seno = math.sin(rad)
            cosseno = math.cos(rad)
            tangente = math.tan(rad) if abs(cosseno) > 1e-10 else "Indefinida (90° ou 270°)"
            print(f"\nPara o ângulo de {ang}°:")
            print(f"• Seno: {seno:.5f}")
            print(f"• Cosseno: {cosseno:.5f}")
            print(f"• Tangente: {tangente if isinstance(tangente, str) else f'{tangente:.5f}'}")
            historico.append(f"Trigonometria({ang}°): sen={seno:.4f}, cos={cosseno:.4f}")

        elif opcao == "11":
            print("\n📜 Histórico de Cálculos:")
            if not historico:
                print("Nenhum cálculo realizado ainda.")
            else:
                for i, item in enumerate(historico, 1):
                    print(f"  {i}. {item}")
        else:
            print("❌ Opção inválida! Escolha um número do menu.")

if __name__ == "__main__":
    main()
