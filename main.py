import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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
        if lines.isdigit(): 
        # // isdigit tells us if the number entered by user is a valid number or not 
            lines = int(lines) 
            if lines >= 1  and lines <= MAX_LINES :
                # print(f'amount deposited is {lines}' )
                break
            else:
                print("enter valid number of lines")
        else:
            print("Please Enter an valid Amount")
    return lines

def get_bet():
    while(True):
        bet = input('Enter the amount of the bet : ')
        if bet.isdigit:
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Enter bet in range 1 - 100")
        else:
            print("Enter a valid digit")
    return bet


def main():
    balance = deposit()
    lines = number_of_lines()
    while(True):
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You dont have enough to make this bet your current balance is ${balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} number of lines and your total bet is ${total_bet}")

main()  

