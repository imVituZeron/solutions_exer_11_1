def dismiss_or_no():
    initial = 1
    people_list = []
    acumulator = 0

    for i in range(31):
        if i == 0:
            acumulator = initial * 2
        else:
            acumulator = acumulator * 2

        print(f'No dia {i}º tem {sum(people_list)} novas pessoas sabendo!')
        if i == 25:
            if sum(people_list) > 20000:
                print('Deve demitir o funcionario.')
            else:
                print('Não deve demitir o funcionario.')

        people_list.append(acumulator+1)
    
dismiss_or_no()

