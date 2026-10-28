"""
Calculadora Básica com 4 Operações e Porcentagem em Python
Execução: python calculadora_porcentagem.py
"""

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b

def porcentagem(valor, taxa):
    """Calcula taxa% de um valor. Exemplo: 15% de 200 = 30.0"""
    return valor * (taxa / 100.0)

def exibir_menu():
    print("\n" + "=" * 35)
    print("      CALCULADORA COM PORCENTAGEM")
    print("=" * 35)
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Porcentagem (%)")
    print("0 - Sair")
    print("=" * 35)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0 a 5): ").strip()
        
        if opcao == "0":
            print("\nPrograma encerrado. Até mais!")
            break
            
        if opcao not in ("1", "2", "3", "4", "5"):
            print("❌ Opção inválida! Escolha um número de 0 a 5.")
            continue
            
        try:
            if opcao == "5":
                valor = float(input("Digite o valor base: "))
                taxa = float(input("Digite a taxa percentual (%): "))
                resultado = porcentagem(valor, taxa)
                
                print(f"\n✅ {taxa}% de {valor} = {resultado}")
                print(f"   • Valor com acréscimo (+{taxa}%): {valor + resultado}")
                print(f"   • Valor com desconto (-{taxa}%): {valor - resultado}")
            else:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == "1":
                    print(f"\n✅ Resultado: {num1} + {num2} = {somar(num1, num2)}")
                elif opcao == "2":
                    print(f"\n✅ Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
                elif opcao == "3":
                    print(f"\n✅ Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
                elif opcao == "4":
                    print(f"\n✅ Resultado: {num1} / {num2} = {dividir(num1, num2)}")
                    
        except ValueError:
            print("❌ Erro: Digite apenas números válidos!")
        except ZeroDivisionError as err:
            print(f"❌ Erro: {err}")

if __name__ == "__main__":
    main()
