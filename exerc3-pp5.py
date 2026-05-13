# questao3.py
import datetime

def calcular_idade(ano_nascimento):
    """Função que recebe o ano de nascimento e retorna a idade calculada."""
    # Obtém o ano atual do sistema
    ano_atual = datetime.date.today().year 
    idade = ano_atual - ano_nascimento
    return idade

def main():
    print("=== Questão 3 ===")
    # Lê o ano de nascimento digitado pelo usuário
    ano_nasc = int(input("Digite o ano do seu nascimento (ex: 1995): "))
    
    # Chama a função passando o ano lido
    idade_retornada = calcular_idade(ano_nasc)
    
    # Mostra o valor calculado
    print(f"\nVocê tem (ou fará neste ano) {idade_retornada} anos de idade.")

# Executa a função principal
if __name__ == "__main__":
    main()