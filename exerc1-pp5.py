# questao1.py

def exibir_dados(mensagem, numero):
    """Função que recebe uma mensagem e um número e os exibe."""
    print("\n--- Resultados ---")
    print(f"A mensagem digitada foi: {mensagem}")
    print(f"O número digitado foi: {numero}")

def main():
    print("=== Questão 1 ===")
    # Leitura dos dados digitados pelo usuário
    msg = input("Digite uma mensagem: ")
    # Convertendo para float para aceitar tanto inteiros quanto decimais
    num = float(input("Digite um número: ")) 
    
    # Chamada da função passando os argumentos lidos
    exibir_dados(msg, num)

# Executa a função principal
if __name__ == "__main__":
    main()