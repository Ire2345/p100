class Atm():
    def __init__(self, cardnumber, pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber

    def check_balance(self):
        print("Your balance is 50000")


    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print(" you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))

def main():
    Card_number =input("insert your card number:- ")
    pin_number = input("enter your pin number:- ")

    new_user = Atm(Card_number , pin_number)

    print|("Choose your actvity ")
    print("1.Balance Enquiry  2.withdrawl")
    activity = int(input("enter activity number :-"))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()
        