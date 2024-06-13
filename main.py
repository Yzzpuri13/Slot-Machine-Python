MAX_LINES = 3

def deposit():
    while(True):
        amount = input("Please the amount of deposit $$ ")
        if amount.isdigit(): 
        # // isdigit tells us if the number entered by user is a valid number or not 
            amount = int(amount)
            if amount > 0 :
                print(f'amount deposited is {amount}' )
                break
            else:
                print("not valid deposit. Please deposit more than 0")
        else:
            print("Please Enter an valid Amount")
    return amount

def number_of_lines():
    while(True):
        lines = input("Enter the amount of lines to be bet on (1-" + str(MAX_LINES) + ")?  ")
        if amount.isdigit(): 
        # // isdigit tells us if the number entered by user is a valid number or not 
            lines = int(lines)
            if lines > 0 :
                # print(f'amount deposited is {lines}' )
                break
            else:
                print("not valid deposit. Please deposit more than 0")
        else:
            print("Please Enter an valid Amount")
    return amount


def main():
    balance = deposit()

main()  

