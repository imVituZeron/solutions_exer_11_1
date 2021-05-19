def receive(number):
    list_result = []

    for i in range(20):
        if number % i == 0:
            list_result.append("True")
        else:
            list_result.append("False")

    for i in list_result:
        if i == "False":
            return f"O {number} não é primo"
        else:
            return f"O {number} é primo!"

number = input("Digite um numero inteiro e positovo: ")
if number.isdigit():
    print(receive(int(number)))
else:
    print("Na proxima digite algo valido!")