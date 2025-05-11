
# Versão 2: Adicionando suporte para mais moedas
def conversor(valor, taxa):
    return valor * taxa

def main():
    valor = float(input("Digite o valor em reais: "))
    moeda = input("Digite a moeda para conversão (dolar/euro): ").lower()
    
    if moeda == 'dolar':
        taxa = 5.0
    elif moeda == 'euro':
        taxa = 5.5
    else:
        print("Moeda inválida")
        return
    
    resultado = conversor(valor, taxa)
    print(f"Valor convertido: {resultado} {moeda}")

if __name__ == "__main__":
    main()
