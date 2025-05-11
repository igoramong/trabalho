
# Versão 4: Organizando o código em funções
def conversor(valor, taxa):
    return valor * taxa

def obter_valor():
    try:
        valor = float(input("Digite o valor em reais: "))
        if valor < 0:
            print("Valor não pode ser negativo")
            return None
        return valor
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
        return None

def obter_moeda():
    moeda = input("Digite a moeda para conversão (dolar/euro): ").lower()
    if moeda not in ['dolar', 'euro']:
        print("Moeda inválida")
        return None
    return moeda

def main():
    valor = obter_valor()
    if valor is None:
        return
    
    moeda = obter_moeda()
    if moeda is None:
        return
    
    taxa = 5.0 if moeda == 'dolar' else 5.5
    resultado = conversor(valor, taxa)
    print(f"Valor convertido: {resultado} {moeda}")

if __name__ == "__main__":
    main()
