# questao2.py

def somar_tres_valores(v1, v2, v3):
    """Função que recebe três valores, soma e retorna o resultado."""
    soma = v1 + v2 + v3
    return soma

def main():
    print("=== Questão 2 ===")
    print("Digite três valores inteiros para somar:")
    
    # Leitura dos três valores inteiros
    valor1 = int(input("Primeiro valor: "))
    valor2 = int(input("Segundo valor: "))
    valor3 = int(input("Terceiro valor: "))
    
    # Chama a função e armazena o retorno na variável 'resultado'
    resultado = somar_tres_valores(valor1, valor2, valor3)
    
    # Mostra o valor retornado
    print(f"\nO resultado da soma é: {resultado}")

# Executa a função principal
if __name__ == "__main__":
    main()