import time

# Greet the user 
print("Hello, welcome to Rizvi Bank")

# Function check and display the user's balance
def check_balance():
    print("Checking your balance.....")
    time.sleep(3)  # adds a delay to make it feel realistic
    print(f"Your current balance : {balance:.2f}")

# Function to handle money withdrawal
def withdraw():
    global balance  # to modify the main balance variable

    try:
        amt = int(input("Enter withdrawal amount :"))
        if amt < 0:
            print("Invalid amount")  # negative numbers don’t make sense
        else:
            if balance < amt:
                print("You don't have enough balance")  # can’t withdraw more than you have
            else:
                balance = balance - amt
                print("Withdrawing may take few minutes...")
                time.sleep(3)
                print(f"Money successfully withdrawn : {amt:.2f}")
                print(f"Balance you have : {balance:.2f}")
    except:
        print("Invalid amount")  # catches if the input isn’t a valid number

# Function to handle deposits
def deposit():
    global balance
    try:    
        amt1 = int(input("Enter the amount to be deposited:"))
        if amt1 < 0:
            print("Invalid amount")  # same logic — can’t deposit negative money
        else:
            balance = balance + amt1
            print("Depositing may take few minutes...")
            time.sleep(3)
            print(f"Money successfully deposited : {amt1:.2f}")
            print(f"Balance you have : {balance:.2f}")
    except:
        print("Invalid amount")  # catches if the input isn’t a valid number

# Initial account balance
balance = 0.0

# Main program loop
while True:
    print("\n--- Rizvi Bank Menu ---")
    print("1 --> To check the balance")
    print("2 --> To Deposit money")
    print("3 --> To Withdraw money")
    print("4 --> Quit")

    # take user's choice
    try:
        choose = int(input("Choose as per your need: "))
    except ValueError:
        print("Invalid number")
        continue

    # handle options
    if choose == 1:
        check_balance()
    elif choose == 2:
        deposit()
    elif choose == 3:
        withdraw()
    else:
        print("Thanks for trusting us!")
        break
