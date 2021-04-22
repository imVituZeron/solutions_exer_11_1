# question A
def numbers_questions(number):
    count_yes = count_no = 0
    list_response = []
    for i in range(number):
        print('responda as questões com "s" ou "n":')
        op = input(f'digite a resposta da questão {i+1}º: ')

        if op.isnumeric():
            print('resposta errada!, fim de programa')
            break
        else:
            if op.upper() == 'S':
                count_yes = count_yes + 1
            elif op.upper() == 'N':
                count_no = count_no + 1

        list_response = [count_yes, count_no]
    return list_response

# question B
total_person_list = [] 
while True:
    print('Questões')
    name = input('digite o seu nome: ')

    returno = numbers_questions(3)
    if returno[0] > returno[1]:
        person_list = [name,'Yes Group']
    else:
        person_list = [name, 'No Group']
    
    total_person_list.append(person_list)

    continuE = input('Deseja continuar? [s/n]')
    if continuE.isalpha():
        if continuE.upper() == 'N':
            break
        else:
            print('proximo!')

print(total_person_list)
