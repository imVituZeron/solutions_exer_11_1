print("with money more money")
print()

def financial(initial_value, initial_rate):
    mounth = 1
    rate = initial_rate
    value = initial_value

    while True:
        if value == initial_value * 2:
            print('End')
            break
        
        if mounth % 3 == 0:
            rate += 0.02

        if mounth % 12 == 0:
            rate += rate * 0.2

        if mounth % 13 == 0:
            value += 1000

        value += value * rate

        print(f"value: {value}")
        print(f"rate: {rate}")
        print(f"mounth: {mounth}")
        print()

        mounth += 1

financial(1000, 10)

