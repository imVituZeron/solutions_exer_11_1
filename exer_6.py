group = []
people = []
count_miror = count_older = count = older_age = 0
older_age_name = ''

while True:
    name = input('Digite seu nome: ')
    if name == '':
        break

    age = input('Digite sua idade: ')

    if age.isdigit():
        people.append(name)
        people.append(int(age))
        group.append(people)
        people = []

        if count == 0:
            older_age_name = name
            older_age = int(age)
        elif older_age < int(age):
            older_age_name = name
            older_age = int(age)

        count += 1
    else:
        print('Informe somente numeros no campo idade!')
        

for peoples in group:
    if peoples[1] >= 18:
        count_older+= 1
            
    if peoples[1] < 11:
        count_miror += 1

if len(group) >= 5:
    if count_miror == 0:
        if len(group) / 2 < count_older:
            print('Parabens seu grupo foi aceito para excurção!')
            print(f"""
                Tem {len(group)} pessoas no grupo, sendo que o minino são 5! -> CHECK
                Tem {count_miror} pessoas com menos de 11 anos! -> CHECK
                A quantidade de pessoas maiores de idade é maior que a metade do grupo! -> CHECK
                O lider do grupo é {older_age_name}, com {older_age} anos de vida!
            """)
        else:
            print('A quantidade de maiores de idade é menor que a metade do grupo')
    else:
        print('Não pode conter pessoas menores que 11 anos')
else:
    print('grupo não aprovado para excurção!')


"""
    O While está capturado as informações de nome e idade do usuário, e dentro temos dois IFs,
    um para veficar se o nome foi digitado,e o outro validando se idade é um digito do tipo string.

    Depois de validar é adicionado o nome e idade na lista PEOPLE, e a mesma é adicionada na
    lista GROUP. E logo depois um if para pegar o nome e idade da pessoa mais velha do grupo

    O for está pegando a quantidade de pessoas mais velhas, e a quantidade de pessoas que tem
    a idade menor que 11 anos.

    E por fim temos, um if aninhado verificando se o grupo é maior que 5 integrantes, se tem
    alguma pessoa com menos de 11 anos e se a quantidade de pessoas maiores de idade é maior que
    a metade do grupo.
"""