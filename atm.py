##########################################################
#                 Simulation of ATM in Python            #
# allowed papers: 100, 50, 10, 5, and rest of request    #
##########################################################

balance1 = 258
balance2 = 3000
cont = True


class ATM:

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawal_list = []

    def withdrawal(self):
        print("\n\n\n")
        request = int(input("Enter the amount you want to withdraw :"))

        if (request > 0) and (request <= self.balance):
            self.withdrawal_list.append(request)
            notes = [100, 50, 10, 5]
            for note in notes:
                while request >= note:
                    print("give " + str(note))
                    self.balance -= note
                    request -= note

            print("give " + str(request))
            self.balance -= request
            request -= request
            self.balance -= request

        else:
            print('Sorry, we can\'t proceed with your request. \nThe amount number is incorrect or you don\'t '
                  'have enough balance for your request')
        return self.balance

    def show_withdrawals(self):
        for withdrawal in self.withdrawal_list:
            print("ATM Cash withdrawal Debit :" + str(withdrawal))


atm1 = ATM(balance1, "EAST BANK")

atm2 = ATM(balance2, "WEST BANK")

while cont:
    print("\n\n")
    print("***********************************************")
    print("**                W E L C O M E              **")
    print("***********************************************")
    print("** DESIG.: " + atm1.bank_name + ". Current balance =" + str(atm1.balance) + " **")
    print("***********************************************")
    print("** DESIG.: " + atm2.bank_name + ". Current balance =" + str(atm2.balance) + " **")
    print("***********************************************")
    print("\n\n\n\n")
    answer = int(input("Please select : 1=" + atm1.bank_name + " Withdrawal, 2=" + atm2.bank_name + " Withdrawal, 3=Exit "))
    if answer == 1:
        atm1.withdrawal()
        atm1.show_withdrawals()
    if answer == 2:
        atm2.withdrawal()
        atm2.show_withdrawals()
    if answer == 3:
        cont = False

print("Thank you for your visit")
