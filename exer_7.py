amount = input('Quantos numeros: ')

interval_numbers = []
out_interval = []
sum_interval = 0

if amount.isdigit():
    for i in range(int(amount)):
        number = input('Numeros? ')
        
        if number.isdigit() and int(number) > 0:
            if int(number) <= 15:
                sum_interval += int(number)
                interval_numbers.append(int(number))
            else:
                out_interval.append(int(number))
            

if len(interval_numbers) > 0:
    print(f"""
        foram {amount} números!
        INTERVALO:
            Quantidade de números que estão no intervalo de 1-15: {len(interval_numbers)}
            Soma deles é {sum_interval}, a média é {sum_interval/len(interval_numbers):.2f}
            O maior deles é {max(interval_numbers)} e o menor é {min(interval_numbers)}
    """)
else:
    print('Não foi informado nenhum numero dentro do intervalo!')

if len(out_interval) > 0:
    print(f""")
        FORA DO INTERVALO:
            Menor valor é {min(out_interval)}
    """)
else:
    print('Não foi informado nenhum numero fora do intervalo!')
            

"""
    Começa com um input pedindo infomação do keyboard, logo após variaveis instanciadas

    Um IF valida o numero informado pelo keyboard, e inicia um for com range até o numero informado
    começando a pedir números para o usuário, lembrando que não pode ser número negativo

    Dentro do um IF coleta os numeros entre um intervalo de 0 a 15, e um outro coleta o restante

    e por fim IFs para mostrar as informações que o exercicio pede.
"""




