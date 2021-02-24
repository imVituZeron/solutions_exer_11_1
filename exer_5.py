count = minor = media = 0
over_twenty = porcent = 0
list_age = []

while True:
    age = input('Digite sua idade: ')
    if age.isdigit():
        list_age.append(int(age))
        count += 1
    else:
        print('Digite somente números')

    if count == 6:
        break

for i in list_age:
    if i < 18:
        minor += 1
    
    if i >= 20:
        over_twenty += 1
        porcent += 100/len(list_age)

    media += i
    max(list_age)

if minor > 1:
    print(f'São {minor} pessoas menores de idade')
else:
    print(f'Somente {minor} é pessoa menor de idade')

print(f'A media de todas as pessoas é {media/len(list_age):.2f}')
print(f'A pessoa mais velha tem {max(list_age)} anos')
print(f'São {over_twenty} pessoas maiores de vinte anos')
print(f'a porcentagem é de {porcent:.2f}% de pessoas com mais de 20 anos')

"""
    While é para pegar as 6 idades que o problema pede, junto com uma validação
    para ver se o que a pessoa digitou é um numero do tipo string. Ainda no While
    antes de passar as idade para uma lista(array), os tipos delas são trocados de 
    string para inteiro.

    Logo depois um for passando por todas as posições da lista e dois IFs
    um pegando todos as idades que sejam menor que 18, e um outro pegando as idades que
    sejam maiores de 20, e contando as porcentagem.

    E abaixo tenho os prints com as informações.
"""
