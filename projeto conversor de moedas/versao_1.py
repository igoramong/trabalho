
# Versão 1: Esqueleto básico
def conversor(valor, taxa):
    return valor * taxa

def main():
    valor = float(input("Digite o valor em reais: "))
    taxa = float(input("Digite a taxa de conversão para dólar: "))
    resultado = conversor(valor, taxa)
    print(f"Valor convertido: {resultado} dólares")

if __name__ == "__main__":
    main()
