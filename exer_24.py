from math import sqrt

## --- Function ----
# making square root 
def diag_of_toybox(A, B, C):
    root = A*A + B*B + C*C
    number = sqrt(root)    
    return float(number)

# details of program
def details(list):
    print("--- Details ---")
    for k, v in enumerate(list):
        if k == 0:
            print(f"ten: {v}")
        elif k == 1:
            print(f"fifteen: {v}")
        elif k == 2:
            print(f"twenty: {v}")
        else:
            print(f"twenty five: {v}")

## --- Variables ---
ten = 0 
fifteen = 0
twenty = 0 
twenty_five = 0   
amount_of_orbs = []

## --- Main code ---
while True:
    # input of keyboard
    toy_code = int(input("Write toy code, please: "))
    toy_height = int(input("Write height of toy box, please: "))
    toy_width = int(input("Write width of toy box, please: "))
    toy_length = int(input("Write length of toy box, please: "))

    # stop program case the code is negative
    if toy_code < 0:
        print("--- Stopped input keyboard! ---")
        amount_of_orbs = [ten, fifteen, twenty, twenty_five]
        details(amount_of_orbs) 
        break
    else:
        diag = diag_of_toybox(toy_length, toy_width, toy_height)
        
        # geranting diameter of orb
        if diag <= 10:
            ten += 1
            print("The diameter of orb that goes is ten")
        elif diag > 10 and diag <= 15:
            fifteen += 1
            print("The diameter of orb that goes is fifteen")
        elif diag > 15 and diag <= 20:
            twenty += 1
            print("The diameter of orb that goes is twenty")
        elif diag > 20 and diag <= 25:
            twenty_five += 1
            print("The diameter of orb that goes is twenty five")





    