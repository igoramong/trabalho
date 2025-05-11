
# Versão 3: Adicionando validação de entrada
def conversor(valor, taxa):
    return valor * taxa

def main():
    try:
        valor = float(input("Digite o valor em reais: "))
        moeda = input("Digite a moeda para conversão (dolar/euro): ").lower()
        
        if moeda == 'dolar':
            taxa = 5.0
        elif moeda == 'euro':
            taxa = 5.5
        else:
            print("Moeda inválida")
            return
        
        if valor < 0:
            print("Valor não pode ser negativo")
            return
        
        resultado = conversor(valor, taxa)
        print(f"Valor convertido: {resultado} {moeda}")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")

if __name__ == "__main__":
    main()
