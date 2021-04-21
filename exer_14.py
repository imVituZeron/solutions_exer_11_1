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

print(numbers_questions(3))
        
