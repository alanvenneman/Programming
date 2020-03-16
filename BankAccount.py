"""Write a python class to create, deposit, withdraw a bank account. 
The amount is saved in a file whenever an account is created with a initial deposit and thereafter deposit 
amount is added to the current amount, withdrawn amount is reduced from the current amount.

Create an application using the above class to ask the user with create, deposit and withdraw options and 
with relevant amounts.

With the information given operate the bank account operations.
"""


class BankAccount:
	def __init__(self):
		self.balance = 0.0
		self.deposit = 0.0
		self.withdraw = 0.0

	def setBalance(self, ba):
		self.balance = ba

	def getBalance(self):
		return float(self.balance)

	def setDeposit(self, de):
		if self.deposit > 0.0:
			self.deposit = self.deposit + de
		# else:
		# 	self.deposit = de

	def getDeposit(self):
		return float(self.deposit)

	def setWithdraw(self, wi):
		if self.withdraw > 0.0:
			self.withdraw = self.withdraw + wi
		else:
			self.withdraw = wi

	def getWithdraw(self):
		return float(self.withdraw)

	def getAmount(self):
		return float(self.balance + self.deposit - self.withdraw)
