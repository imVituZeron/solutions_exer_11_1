def hotel(floor, nroom, daily, internal_value=0):
    value_daily = rate_for_daily = total = service_rate = 0

    if floor == 1:
        value_daily = daily * 90
        rate_for_daily = 90
    elif floor == 2:
        value_daily = daily * 180
        rate_for_daily = 180
    elif floor == 3: 
        value_daily = daily * 300
        rate_for_daily = 300
    else:
        value_daily = daily * 450
        rate_for_daily = 450

    service_rate = (internal_value * 10/100) + (value_daily * 6/100)
    total = value_daily + service_rate + internal_value

    print(f'Number room: {nroom}')
    print(f'Daily: {daily}')
    print(f'Daily value: {rate_for_daily}')
    print(f'Total daily value: {value_daily}')
    print(f'Internal value: {internal_value}')
    print(f'Service rate: {service_rate}')
    print(f'Total: {total}')

hotel(3,45, 2, 100)