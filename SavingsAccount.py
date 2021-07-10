class SavingsAccount:
    def __init__(self,balance,rate):
        self.saving_balance=balance
        self.annual_inter_rate=rate

    def MonthlyInterest(self):
        interest = self.saving_balance * self.annual_inter_rate / 12
        self.saving_balance+= interest
    def modifyInterestRate(self,new_inter_rate):
        self.annual_inter_rate=new_inter_rate

saver1=SavingsAccount(2000,5)
saver2=SavingsAccount(3000,5)
saver1.MonthlyInterest()
saver2.MonthlyInterest()
print(f"New balance for saver 1(with rate {saver1.annual_inter_rate}): {saver1.saving_balance}")
print(f"New balance for saver 2(with rate {saver2.annual_inter_rate}): {saver2.saving_balance}")
saver1.modifyInterestRate(7)
saver2.modifyInterestRate(7)
saver1.MonthlyInterest()
saver2.MonthlyInterest()
print(f"New balance for saver 1(with rate {saver1.annual_inter_rate}): {saver1.saving_balance}")
print(f"New balance for saver 2(with rate {saver2.annual_inter_rate}): {saver2.saving_balance}")
