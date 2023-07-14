import random


MAX_LINE = 3
MAX_BET = 1000
MIN_BET = 10

ROWS = 3
COLS =3

SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
SYMBOL_VALUES = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def deposit():
    while True:
        amount = input("What would you like to deposit?: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero (0)!! ")
        else:
           print("Enter an integer! ")
    return amount
def get_number_of_line():
    while True:
        lines = input("Enter the number of lines to bet on(1-"+str(MAX_LINE)+")? : " )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a digit between 1-3")
        else:
            ("Enter a digit between 1-3")
    return lines
def get_bet():
    while True:
        bet = input("Enter the Bet amount per line (Max Bet = $"+str(MAX_BET)+" & Min Bet = $"+str(MIN_BET)+" ): $") 
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please bet between ${MAX_BET} to ${MIN_BET}: $") 
        else:
            print("Please bet between $"+str(MAX_BET)+" to $"+str(MIN_BET)+": $")   
    return bet

def get_slot_machine_spin(rows,cols,symbols):
    
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
             all_symbols.append(symbol)
             
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #[:] this : means it makes a copy off all elements in the allsymbols list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)                   
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end = " | ")
            else:
                print(column[row], end = "\n")
              
def check_winnings(columns,lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol  = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)
    return winnings, winning_lines
                
def spin(balance):

    lines = get_number_of_line()
    while True:
        bet = get_bet()
        totalBet = bet*lines
        if(totalBet <= balance):
            break
        else:
            print(f"You do not have enough balance. Your betting amount should be within your balance ${balance}")          
    totalBet = bet*lines
    print("Your balance : $"+str(balance))
    print("Your number of lines : "+str(lines))
    print(f"You are betting ${bet} on {lines} lines. Your total bet = ${totalBet}")
    
    slots = get_slot_machine_spin(ROWS,COLS,SYMBOL_COUNT)
    winnings, winning_lines = check_winnings(slots, lines ,bet, SYMBOL_VALUES);
    print_slot_machine(slots)
    print(f"You won ${winnings}")
    print(f"You won this lines : ", *winning_lines)
    
    return winnings- totalBet
    #print(print_slot_machine(slots))
            
def main():
    balance = deposit()
    while True:
        print(f"You balance is : ${balance}")
        ans = input("Please enter any key to spin(n to quit) : ")
        if(ans == "n"):
            break
        else:
            balance += spin(balance)    
    print(f"You're left with ${balance}")
main()