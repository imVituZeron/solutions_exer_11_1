def applied_balance(initial_value, rate):
    count = 0
    acumulatore = 0

    while True:
        acumulator += initial_value * (rate/100)
        count += 1

        if acumulator == (initial_value * 2):
            return f'O saldo inicial é R${initial_value}, e foi preciso de {count} anos para dobra o saldo'
        
print(applied_balance(1000, 8))

"""
    Uma função com dois valores, o saldo inicial e taxa de juros anual.

    Initial_value é o acumulador de saldo e count o contador de anos.

    O while só vai parar, caso o acumulator for do mesmo valor que initial_value * 2,
    retornando uma frase
"""