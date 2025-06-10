from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Abacaxi', 5.00, 'grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pão', 2.00, 'O melhor pão da cidade')
prato_pao.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)
# restaurante_praca.receber_avaliacao('Gui', 10)
# restaurante_praca.receber_avaliacao('Lais', 8)
# restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    Restaurante.listar_restaurantes()
    print()
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()