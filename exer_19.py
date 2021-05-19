# BACTERIAS

# população inicial 100

def grow_up_bacterium(init_population):
    count = 1
    times = [3, 6, 9, 12]
    init = init_population

    while True:
        if init_population * 2 == init:
            print(int(init))
            print("doubled population")
            break

        init = init + (init * 3/100)
        print(f'{int(init)} - larger population 0.3%')
        born_rate = init * 3/100

        for time in times:
            if count == time:
                init = init - (born_rate * 5/100)
                print(f'{int(init)} - smaller population 0.5%')

        if count == 12:
            count = 1
        else:
            count += 1

grow_up_bacterium(100)