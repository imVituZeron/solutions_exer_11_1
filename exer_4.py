def huguinho_and_luisinho(height_huguinho, height_luisinho):
    year = 2010
    while True:
        value_cm_huguinho = input(f'Quantos centimetros huguinho cresceu no ano de {year}: ')
        value_cm_luisinho = input(f'Quantos centimetros luisinho cresceu no ano de {year}: ')
        year += 1
        
        if value_cm_huguinho.isdigit and value_cm_luisinho.isdigit():
            height_huguinho += float(value_cm_huguinho) / 100
            height_luisinho += float(value_cm_luisinho) / 100

            if height_huguinho > height_luisinho:
                return f"""
                    Huiginho já é maior que Luisinho
                    Huguinho tem {height_huguinho:.2f} de altura
                    Luisinho tem {height_luisinho:.2f} de altura
                """

            if float(value_cm_luisinho) == 0 and float(value_cm_huguinho) == 0:
                return f"""
                    Huguinho e Luisinho pararam de crescer.
                """

        else:
            print('Digite somente números')
            
print(huguinho_and_luisinho(1.80, 1.90))

"""
    Uma função com dois parametro, altura_huguinho e altura_luisinho

    Um loop onde tem duas entradas de keyboard informando quanto cada um cresceu em tal ano.

    Uma validação para ver se os valores das entradas são digitos, se caso eles não forem
    o programa mostra uma mensagem "Digite somente números" e os obriga a digitar numero ou
    cancelar o programa

    Depois da validação tem os acumuladores que são as variaveis que a função recebe como parametro

    Dois if dentro da escopo de validação que retornam mensagens diferentes, um só retorna se
    a altura huguinho for maior que a de luisinho. E o outro retorna caso as entradas de keyboard forem 0

"""