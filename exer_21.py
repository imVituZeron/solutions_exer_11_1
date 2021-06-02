
def calculating_autonomy(dG, dA, pG, pA, capacity=50):
    quantily_G = 0
    quantily_A = 0

    if capacity == 50:
        quantily_G = 50
        quantily_A = 0
    else:
        quantily_G = capacity
        quantily_A = 50 - capacity

    autonomy = dG*quantily_G + dA*quantily_A
    pay_value = quantily_G*pG + quantily_A*pA

    print(f"""Qtd Gas | Qtd Alc | Value | Autonomy
    {quantily_G} | {quantily_A} |R${pay_value:.2f}| {autonomy}
    """)
    
calculating_autonomy(10,15,5,4, 45)