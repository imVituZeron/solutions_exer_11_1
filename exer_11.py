def calc_value_check(value):
    calc_value_ages = []
    tot = 100
    for i in value:
        if i < 10:
            calc_value_ages.append(tot + 80)
        elif 10 <= i <= 30:
            calc_value_ages.append(tot + 50)
        elif 40 <= i <= 60:
            calc_value_ages.append(tot + 95)
        else:
            calc_value_ages.append(tot + 130)
    return calc_value_ages

names = []
ages = []

qtd_peoples = input('Digite quantas pessoas tem na sua familia: ')
if qtd_peoples.isdigit():
    for i in range(int(qtd_peoples)):
        name = input('Digite seu nome: ')
        names.append(name)
        age = input('Digite sua idade: ')

        if age.isdigit():
            ages.append(int(age))
        else:
            print('Dado incorreto!')
        print()

calc_value = calc_value_check(ages)
for k, v in enumerate(names):
    print(f"{v} tem {ages[k]} anos e vai pagar R${calc_value[k]} reais para o plano de saúde")
    

"""
    Começamos com uma def(function), com um parametro somete,que calcula o quanto você
    vai pagar pelo plano de saúde conforme for sua idade, a def retorna uma lista(array)
    com os valores já calculados.

    Logo depois temos, a declaração de duas variaveis names(lista) e ages(lista), que vão servir
    para guardar os nomes e as idades das pessoas.

    Peguntamos a quantidade de pessoas que tem na sua familia e logo depois perguntamos o nome e a
    idade de cada um, validando para ver se a pessoas digitou corretamente.

    Depois chamamos a def(fuction) e passamos a lista com as idades. Ela ira retornar ja calculado e 
    assim mostramos um print formatado as informações.

"""