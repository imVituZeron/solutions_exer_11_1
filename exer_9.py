def value_unit(qtd, delivery_type):
    value = 0

    if delivery_type == 'N':
        if qtd <= 1000:
            value = 9.10
        elif qtd > 1000 and qtd <= 5000:
            value = 10 
        elif qtd > 5000 and qtd <= 10000:
            value = 6.40 
        else:
            value = 3.30
    
    if delivery_type == 'R':
        if qtd <= 1000:
            value = 11.10
        elif qtd > 1000 and qtd <= 5000:
            if qtd > 4000:
                value = 10 - (10 * 0.3)
            else:
                value = 10
        elif qtd > 5000 and qtd <= 10000:
            value = 6.40 - (6.40 * 0.3)
        else:
            value = 3.30 - (3.30 * 0.3)
           
    return value * qtd


delivery_n = []
delivery_r = []

while True:
    qtd_requests = input('Quantos pedidos quer?: ') 
    if qtd_requests.isdigit():
        discount = 0
        for i in range(int(qtd_requests)):
            print(f'{i+1}º Pedido')
            product = input('Quantos produtos deseja: ')
            delivery = input('Modo de entrega (N - normal / R - rapido): ')

            if delivery.upper() == 'N':
                retorno = value_unit(int(product), delivery.upper())
                delivery_n.append(retorno)
            elif delivery.upper() == 'R':
                if int(product) > 4000:
                    discount += 1
                
                retorno = value_unit(int(product), delivery.upper())
                delivery_r.append(retorno)

    else:
        print('Na proxima digite corretamente!')
        break

for value_r in delivery_r:
    print('Preços de pedidos com entraga radida')
    print(value_r)
print(f'Fora {discount} entregas com desconto!')

for value_n in delivery_n:
    print('Preços de pedidos com entraga normal:')
    print(value_n)
    


    
