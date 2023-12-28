from models.produto import Produto
from utils.help import formata_float_str_moeda
from utils.mercado import menu

def main():
    # Seu código principal aqui
    produto = Produto(nome="Exemplo", preco=19.99)
    menu()
    print(produto)

if __name__ == "__main__":
    main()  