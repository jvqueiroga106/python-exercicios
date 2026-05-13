# questao4.py

def aplicar_desconto(preco_original, porcentagem_desconto):
    """Função que calcula e retorna o valor de um produto após um desconto."""
    valor_do_desconto = preco_original * (porcentagem_desconto / 100)
    preco_final = preco_original - valor_do_desconto
    return preco_final

def main():
    print("=== Questão 4: Calculadora de Descontos ===")
    
    # Leitura dos dados
    preco = float(input("Digite o preço do produto: R$ "))
    desconto = float(input("Digite a porcentagem de desconto (%): "))
    
    # Chamada da função e armazenamento do retorno
    preco_com_desconto = aplicar_desconto(preco, desconto)
    
    # Exibição do resultado formatado com duas casas decimais
    print(f"\nO preço final do produto com {desconto}% de desconto é: R$ {preco_com_desconto:.2f}")

# Executa a função principal
if __name__ == "__main__":
    main()