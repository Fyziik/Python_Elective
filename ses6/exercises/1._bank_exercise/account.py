class Account:
    # This class should contain the link between an account and a customer

    def __init__(self, customer, balance, acc_number):
        self.customer = customer
        self.balance = balance
        self.acc_number = acc_number

    def get_customer(self):
        return self.customer.name + " " + str(self.customer.age)

    def get_balance(self):
        return str(self.balance)

    def get_acc_number(self):
        return str(self.acc_number)


    def __str__(self):
        return str(self.customer) + '\n' + str(self.balance) + '\n' + str(self.acc_number)

        