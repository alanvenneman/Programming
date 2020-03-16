from BankAccount import BankAccount


# Create a new instance of BankAccount
newAccount = BankAccount()
# open a new file
bankFile = open("AccountSummary_AlanVenneman.txt", "w")
bankFile.write("### Welcome to Acme Bank ###\n")
# Ask user for initial deposit
newAccount.setBalance(eval(input("Enter opening balance: ")))
bankFile.write("Opening balance for February: ${:.2f}\n".format(newAccount.getBalance()))
# Ask user for additional deposits
deposits = 0.0
print("Enter deposits first, type the number 0 after final entry.")
while (deposits != -1):
    deposits = newAccount.setDeposit(float(input("Enter deposit: ")))
    if (deposits != -1):
        bankFile.write(str(deposits) + '\n')
    else:
        bankFile.write("Your Deposits: ${:.2f}\n".format(newAccount.getDeposit()))
# Ask user for a withdrawal
withdrawals = 0
print("Enter withdrawals second, type the number 0 after final entry.")
while withdrawals > -1:
    withdrawals = newAccount.setWithdraw(float(input("Enter withdrawal: ")))
    if withdrawals != -1:
        bankFile.write("Your Withdrawals: ${:.2f}\n".format(newAccount.getWithdraw()))
# Print closing Amount
bankFile.write("Your final balance today is: ${:.2f}\n".format(newAccount.getAmount()))
# Close file
bankFile.write("Thank you for doing business at Acme Bank.")
bankFile.close()
