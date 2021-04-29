product_name = ["Base","Corretivo","Batom","Primer","Pincéis","Sombra","Rímel","Pó compacto","Blush","Água Micelar"]
product_price = [12.00,10.99,6.50,12.50,29.99,45.00,15.99,14.50,8.50,11.99]

my_car = []

def pay(caracter, lista):
    account = 0
    desc = 0
    total = 0

    for items in lista:
        account += items[1]
            
    if caracter == "d":
        desc = 20
        total = account - (account * (desc/100))
        return f"Você pagara R${total} em 1 parcela"

    elif caracter == "c":
        desc = 15
        total = account - (account * (desc/100))
        return f"Você pagara R${total} em 1 parcela"

    elif caracter == "p":
        total = account
        return f"Você pagara R${total} em 2 parcelas de {total/2} cada"

    elif caracter == "j":
        desc = 10
        total = account + (account * (desc/100))
        return f"Voce pagara R${total} e 3 parcelas de {total/3} cada."

                
while True:
    print("Lista de produtos!")
    for key, item in enumerate(product_name):
        for keys, price in enumerate(product_price):
            if keys == key:
                print(f"{key+1} {item}: {price}")

    op = input("O que deseja? (digite o numero do produto!) ")
    if op.isdigit():
        op_float = float(op)

        for key, item in enumerate(product_name):
            for keys, prices in enumerate(product_price):
                if key+1 == op_float and keys+1 == op_float:
                    my_car.append([item, prices])
    else:
        print("caracter não desejavel!")
        break

    print(my_car)
    op_output= input("deseja continuar escolhendo [s/n]: ")
    if op_output.isalpha():
        if op_output.lower() == "n":
            print("Forma de pagamento")
            break
        
print("""
    D - (dinheiro ou cheque) a vista
    C - (cartão de credito) a vista
    P - (parcelado no cartão) 2x parcelas
    J - (parcelado no cartão) 3X parcelas
""")
option = input("Escolha sua forma de pagamento [D/C/P/J]: ")
if option.lower() == "d":
    print(pay("d", my_car))
elif option.lower() == "c":
    print(pay("c", my_car))
elif option.lower() == "p":
    print(pay("p", my_car))
elif option.lower() == "j":
    print(pay("j", my_car))
