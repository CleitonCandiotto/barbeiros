def formata_preco(value):
    return f'R$ {value:.2f}'.replace('.', ',')


def cart_total_qtd(carrinho):
    '''pega a quantidade de itens do carrinho e soma as as mesmas'''
    return sum([item['quantidade'] for item in carrinho.values()])


def cart_total(carrinho):
    '''soma a quantidade dos valores do carrinho'''
    return sum(
        [
            item.get('preco_quantitativo_promocional')
            if item.get('preco_quantitativo_promocional')
            else item.get('preco_quantitativo')
            for item 
            in carrinho.values()
        ]
    )