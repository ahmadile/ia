income = 2000
depenses=[]
categories = {}
#1. Welcome Message
print("Bienvenue dans votre analyseur de budget !")

while True:
    #2. Ask for the name
    depence_name  = input("Enter the name of the expense (or 'quit' to exit ):")
    #3. Exit condition
    if depence_name == "quit":
        break
    #4. Request the amount
    amount = float ( input("Request the amount of the expense :"))
    #5. Store
    new_depence= {"name":depence_name,"amount":amount}
    depenses.append(new_depence)
    print(new_depence)
# Initialize the total expenses to 0
total_expenses=0
#  Iterate through the list of expenses with a loop for
for depense in depenses:
    if depense:
     total_expenses +=depense["amount"]

balance = income - total_expenses
# 4. Display the summary
print("\n=== YOUR BUDGET SUMMARY ===")
print(f"Initial Income: {income}€")
print(f"Total Expenses: {total_expenses}€")
print(f"Remaining Balance: {balance}€")