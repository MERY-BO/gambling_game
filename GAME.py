import random 

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
   "A" : 2,
   "B" : 4,
   "C" : 6,
   "D" : 8
}

symbol_value = {
  "A" : 5,
  "B" : 4,
  "C" : 3,
  "D" : 2
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  win_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
    else:
      winnings += values[symbol] * bet
      win_lines.append(line + 1)

  return winnings, win_lines                    

def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  columns = []
  for col in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for row in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)
    columns.append(column)
  return columns

def print_slot_machine(columns):
  for row in range(len(columns[0])):
      for i,column in enumerate(columns):
        if i!= len(columns) - 1 :
          print(column[row], end = "|")
        else:
          print(column[row]) 
       
def deposit():
  while True:
      amount = input('What would you like to deposit ?')
      if amount.isdigit():
        amount = int(amount)
        if amount > 0:
            break
        else:
            print('enter a valid number')
      else:
          print('please enter a number') 
  return amount

def get_bet():
  while True:
      bet = input('What would you like to bet ?')
      if bet.isdigit():
        bet = int(bet)
        if MIN_BET <= bet <= MAX_BET:
            break
        else:
            print('enter a valid number')
      else:
          print('please enter a number') 
  return bet

def num_of_lines():
  while True:
      lines = input(f'What is the number of lines between 1 and {MAX_LINES} do You want to bet on ?')
      if lines.isdigit():
        lines = int(lines)
        if 1<= lines <= MAX_LINES :
            break
        else:
            print('enter a valid number')
      else:
          print('please enter a number') 
  return lines

def game(amount):
  lines = num_of_lines()
  print(amount,lines)
  bet = get_bet()
  tot = bet * lines
  while True :
      if tot > amount:
        print('you do not have enough money to bet you need to add' + str(tot-amount))
      else:
        break
  print(f'you are betting {amount} the total is {tot}')
  slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
  print(print_slot_machine(slots))
  winnings, win_lines = check_winnings(slots,lines,bet,symbol_value)
  print("you won " + str(winnings) )
  print(f"on the lines", *win_lines )
  return winnings - tot

def main():
    amount = deposit()
    while amount > 0:
      print('current balance is: ' + str(amount) )
      spin = input("Press enter to spin (q to quit). ")
      if spin == "q":
        break
      amount += game(amount)
    print(f'you are left with {amount}')
       
main()