##https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

valorCompra = float(input())
if valorCompra < 20: 
    print(f'Valor de venda: R$%.2f' %(valorCompra * 1.45))
else: 
    print(f'Valor de venda: R$%.2f' %(valorCompra * 1.30))