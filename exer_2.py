print('Welcome association')

while True:
    bacic_value = input('Informe o valor da mensalidade da associação: ')
    if bacic_value.isdigit():
        float_basic_value = float(bacic_value)

        for i in range(12):
            
            if i == 0:
                print(f'No mes {i+1} você vai pagar {float_basic_value}')
    
            float_basic_value += float_basic_value * 0.05
            print(f'No mes {i+1} você vai pagar R${float_basic_value:.2f}')
            
        break   
    else:
        print('Digite apenas números!')

"""
    While é mais para validar se o que a pessoa vai informar é um digito mas é do type "str", caso não seja vai
    ser redirecionado para a mensagem "Digite apenas números", e ser forçado a digitar corretamente ou sair do programa

    Logo depois o valor que foi informado, faz uma troca de types de "str" para "float", para que seja possivel
    fazer o acumulo de 5% todos mês, lembrando que é juros sobre juros.

    E depois vem um for um range de 12, simbolizando os 12 meses do ano e acumulando o juros de 5% a cada mês

"""