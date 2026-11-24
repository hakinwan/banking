import json
import random

# LOAD EXISTING CUSTOMER ACCOUNTS
try:
    with open("data.json", "r") as file:
        data = json.load(file)
        account = data["accounts"]

except FileNotFoundError:
    account = []


# FUNCTION TO GET CUSTOMER NAME
def get_name(prompt):
    while True:
        name = input(prompt).strip()

        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Invalid input. Please enter letters only.")


# FUNCTION TO GET DATE OF BIRTH
def get_date_of_birth():
    while True:
        dob = input("Enter your date of birth (DD/MM/YYYY): ")

        if len(dob) == 10 and dob[0:2].isdigit() and dob[3:5].isdigit() and dob[6:10].isdigit() and dob[2] == "/" and dob[5] == "/":
            return dob
        else:
            print("Invalid date. Please enter numbers in DD/MM/YYYY format.")


# FUNCTION TO GET STATE OF ORIGIN
def get_state_of_origin(prompt):
    while True:
        state_of_origin = input(prompt).strip()

        if state_of_origin.replace(" ", "").isalpha():
            return state_of_origin
        else:
            print("Invalid input. Please enter letters only.")


# FUNCTION TO GET USERNAME
def get_username():
    while True:
        username = input("Please create a username: ").strip()

        if username and username.isalnum():
            return username
        else:
            print("Invalid username. Use letters and numbers only, without spaces.")


# FUNCTION TO GET PASSWORD
def get_password():
    while True:
        password = input("Please create a password: ")

        if len(password) >= 6:
            return password
        else:
            print("Password must contain at least 6 characters.")


# FUNCTION TO GENERATE ACCOUNT NUMBER
def generate_account_number():
    return str(random.randint(1000000000, 9999999999))


# FUNCTION TO SAVE ACCOUNTS
def save_accounts():
    with open("data.json", "w") as file:
        json.dump({"accounts": account}, file, indent=4)


# DEPOSIT FUNCTION
def deposit_money(customer):

    print()
    print("=========== DEPOSIT MONEY ===========")

    while True:
        try:
            amount = float(input("Enter amount to deposit: ₦"))

            if amount <= 0:
                print("Invalid amount. Enter an amount greater than zero.")

            else:
                customer["Balance"] += amount

                save_accounts()

                print()
                print("Deposit successful!")
                print(f"Amount deposited: ₦{amount:,.2f}")
                print(f"Your new balance is: ₦{customer['Balance']:,.2f}")
                break

        except ValueError:
            print("Invalid input. Please enter numbers only.")

# WITHDRAWAL FUNCTION
def withdraw_money(customer):

    print()
    print("=========== WITHDRAW MONEY ===========")

    while True:
        try:
            amount = float(input("Enter amount to withdraw: ₦"))

            if amount <= 0:
                print("Invalid amount. Enter an amount greater than zero.")

            elif amount > customer["Balance"]:
                print("Insufficient balance.")
                print(f"Your available balance is: ₦{customer['Balance']:,.2f}")

            else:
                customer["Balance"] -= amount

                save_accounts()

                print()
                print("Withdrawal successful!")
                print(f"Amount withdrawn: ₦{amount:,.2f}")
                print(f"Your new balance is: ₦{customer['Balance']:,.2f}")
                break

        except ValueError:
            print("Invalid input. Please enter numbers only.")

# TRANSFER FUNCTION
def transfer_money(customer):

    print()
    print("=========== TRANSFER MONEY ===========")

    while True:

        recipient_account = input("Enter recipient's account number: ").strip()

        # CHECK IF RECIPIENT ACCOUNT EXISTS
        for recipient in account:

            if recipient["Account_Number"] == recipient_account:

                # PREVENT TRANSFERRING TO YOUR OWN ACCOUNT
                if recipient["Account_Number"] == customer["Account_Number"]:
                    print("You cannot transfer money to your own account.")
                    break

                print(f"Recipient name: {recipient['First_Name']} {recipient['Last_Name']}")

                while True:
                    try:
                        amount = float(input("Enter amount to transfer: ₦"))

                        if amount <= 0:
                            print("Invalid amount. Enter an amount greater than zero.")

                        elif amount > customer["Balance"]:
                            print("Insufficient balance.")
                            print(f"Your available balance is: ₦{customer['Balance']:,.2f}")

                        else:
                            customer["Balance"] -= amount
                            recipient["Balance"] += amount

                            save_accounts()

                            print()
                            print("Transfer successful!")
                            print(f"Amount transferred: ₦{amount:,.2f}")
                            print(f"Recipient: {recipient['First_Name']} {recipient['Last_Name']}")
                            print(f"Your new balance is: ₦{customer['Balance']:,.2f}")
                            return

                    except ValueError:
                        print("Invalid input. Please enter numbers only.")

                break

        else:
            print("Account number not found. Please enter the correct account number.")
            continue

        break


# CUSTOMER BANKING MENU
def bank_menu(customer):

    while True:
        print()
        print("=========== CUSTOMER BANKING MENU ===========")
        print()
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Transaction History")
        print("5. Exit")
        print()

        bank_choice = input("Please select an option: ")

        if bank_choice == "1":
            deposit_money(customer)

        elif bank_choice == "2":
            withdraw_money(customer)

        elif bank_choice == "3":
            transfer_money(customer)

        elif bank_choice == "4":
            print("Transaction history coming soon.")

        elif bank_choice == "5":
            print("You have logged out successfully.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")


# MAIN MENU LOOP
while True:
    print()
    print("=========== WELCOME TO OUR BANKING SYSTEM ===========")
    print()
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    print()

    choice = input("Please select an option: ")

# CREATE ACCOUNT
    if choice == "1":

        create_customer_account = {
            "First_Name": get_name("Enter your firstname: "),
            "Middle_Name": get_name("Enter your middlename: "),
            "Last_Name": get_name("Enter your lastname: "),
            "Date_Of_Birth": get_date_of_birth(),
            "State_Of_Origin": get_state_of_origin("Enter your state of origin: "),
            "Username": get_username(),
            "Password": get_password(),
            "Account_Number": generate_account_number(),
            "Balance": 0
        }

        account.append(create_customer_account)
        save_accounts()

        print()
        print("Account created successfully!")
        print(f"Welcome, {create_customer_account['First_Name']}!")
        print(f"Your account number is: {create_customer_account['Account_Number']}")
        print(f"Your account balance is: ₦{create_customer_account['Balance']}")

# OPEN CUSTOMER BANKING MENU
        bank_menu(create_customer_account)


    # LOGIN
    elif choice == "2":

        print()
        print("========== CUSTOMER LOGIN ==========")

        if len(account) == 0:
            print("No account found. Please create an account first.")

        else:
            username = input("Enter your username: ").strip()

# CHECK IF USERNAME EXISTS
            for customer in account:

                if customer["Username"] == username:

# KEEP ASKING FOR PASSWORD
                    while True:
                        password = input("Enter your password: ")

                        if customer["Password"] == password:
                            print()
                            print("Login Successful!")
                            print(f"Welcome back, {customer['First_Name']}!")

# OPEN CUSTOMER BANKING MENU
                            bank_menu(customer)
                            break

                        else:
                            print("Incorrect password. Please try again.")

                    break

            else:
                print("Username not found.")


# EXIT
    elif choice == "3":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
