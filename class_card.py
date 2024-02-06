class Card:
    def __init__(self, num, account, bank, name, PIN, balance):
        self.__num = num
        self.__account = account
        self.__bank = bank
        self.__name = name
        self.__PIN = PIN
        self.__balance = balance

    @property
    def num(self):
        return self.__num
    
    @num.setter
    def num(self, n):
        self.__num = n

    @property
    def account(self):
        return self.__account
    
    @account.setter
    def account(self, acc):
        self.__account = acc

    @property
    def bank(self):
        return self.__bank
    
    @bank.setter
    def bank(self, b):
        self.__bank = b

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, nm):
        self.__name = nm

    @property
    def PIN(self):
        return self.__PIN
    
    @PIN.setter
    def PIN(self, p):
        self.__PIN = p

    @property
    def balance(self):
        return self.__balance
    
    def change_balance(self, deposit):
        self.__balance += deposit
        print("Current Balance: " + str(self.__balance))
        print("Thank you for your time. Have a nice day!")


class NewCard(Card):
    def __init__(self, num, account, bank, name, PIN):
        super().__init__(num, account, bank, name, PIN, 0)


class OldCard(Card):
    # for users with cards
    # [[[WARNING]]]
    # User's balance should be maintained in database.
    # In this project, when user insert a card, the information is always as below.
    def __init__(self, num):
        super().__init__(num, "111-222-333333", "robo bank", "Yun Oh", "1234", 999999999)