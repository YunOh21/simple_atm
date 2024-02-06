import random
import itertools
from class_card import NewCard, OldCard


class Controller:
    def hello(self):
        print("Hello, what can I help you?")
        print("1. See Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Issue New Card")
        print("If you don't have a card now, you have to issue new one first")
        
        selected = input("Select the number: ")
        self.hello_selected_done = False
        
        while self.hello_selected_done != True:
            selected = int(selected)
            self.switch_as_selected(selected)


    def switch_as_selected(self, selected):
        if selected == 4:
            self.hello_selected_done = True
            self.make_card()
        elif selected in [1, 2, 3]:
            self.hello_selected_done = True
            self.insert_card()
        else:
            self.user_input_weird(selected, "[1, 2, 3, 4]")
            

    def user_input_weird(self, selected, options):
        print("You selected: " + selected)
        selected = input("Sorry, the choice has to be one of " + options + ". Try again.")


    def make_card(self):
        print("Do you want to make a new card?")
        print("Great!")
        print("We need to ask some information for that.")
        print("It would take a few minutes.")
        answer = input("Do you want to continue? [Y/N]")
        self.make_card_answer_done = False
        while self.make_card_answer_done != True:
            self.switch_as_answer(answer)
            

    def switch_as_answer(self, answer):
        answer = answer.upper()
        if answer == "Y":
            self.make_card_answer_done = True
            self.ask_for_new_card()

        elif answer == "N":
            self.make_card_answer_done = True
            self.goodbye()

        else:
            self.user_input_weird(answer, "[Y/N]")


    def ask_for_new_card(self):
        print("Certainly!")
        name = input("What is your name?: ")
        bank = input("Tell me your bank name: ")
        account = input("Please enter your bank account number: ")

        print("Thank you for answering!")
        print("I'll show your card number and PIN number.")
        print("Please write down them somewhere safe.")

        numbers = list(itertools.combinations('123456789', 4))
        num_1 = random.choice(numbers)
        num_2 = random.choice(numbers)
        num_3 = random.choice(numbers)
        num_4 = random.choice(numbers)
        num = ''.join(num_1) + "-" + ''.join(num_2) + "-" + ''.join(num_3) + "-" + ''.join(num_4)
        print("This is your new card number: " + num)
        
        PIN = ''.join(random.choice(numbers))
        
        print("This is new PIN number for the card: " + PIN)

        self.card = NewCard(num, account, bank, name, int(PIN))

        print("Now that you have a card, you can see balance, deposit, or withdraw.")
        self.show_menu()


    def goodbye(self):
        print("OK, see you later.")


    def insert_card(self):
        num = input("Please insert your card: ")

        self.card = OldCard(num)

        check_done = False
        self.check_count = 0

        while check_done == False:
            PIN = input("Please enter your PIN number :")

            checked = self.check(PIN)

            if checked:
                check_done = True
                self.show_menu()
            elif self.check_count < 5:
                self.wrong_answer_try_again()
            else:
                check_done = True
                


    def check(self, PIN):
        if PIN == self.card.PIN:
            return True
        else:
            return False
        
    
    def wrong_answer_try_again(self):
        self.check_count += 1
        print("The PIN number is not correct. Please Try again.")
        print("You can try " + (5 - self.check_count) + " times.")


    def wrong_answer_five_times(self):
        print("You cannot try more than 5 times. Please contact your bank.")
        

    def show_menu(self):
        print("==== SELECT ACCOUNT ====")
        selected = input("1. savings   2. chequing")
        self.account_selected_done = False

        while self.account_selected_done != True:
            selected = int(selected)
            self.switch_as_selected_account(selected)


    def switch_as_selected_account(self, selected):
        if selected == 1:
            self.account_selected_done = True
            self.show_savings()
        elif selected == 2:
            self.account_selected_done = True
            self.show_chequing()
        else:
            self.user_input_weird(selected, "[1, 2]")


    def show_savings(self):
        print("Current Balance: " + str(self.card.balance))
        selected = input("Would you deposit? [Y/N]")
        self.switch_as_saving_answer(selected)
    

    def switch_as_saving_answer(self, selected):
        selected = selected.upper()
        if selected == "Y":
            self.go_deposit()
        else:
            self.go_to_initial_screen()


    def go_to_initial_screen(self):
        print("OK, going back to the initial screen.")
        self.hello()


    def show_chequing(self):
        print("Current Balance: " + str(self.card.balance))
        selected = input("What would you want to do? [Deposit/Withdraw]")
        self.chequing_selected_done = False

        while self.chequing_selected_done != True:
            self.switch_as_chequing_answer(selected)



    def switch_as_chequing_answer(self, selected):
        selected = selected.upper()
        if selected == "D" or selected == "Deposit":
            self.chequing_selected_done = True
            self.go_deposit()
        elif selected == "W" or selected == "Withdraw":
            self.chequing_selected_done = True
            self.go_withdraw()
        else:
            self.user_input_weird(selected, "[D/W]")


    def go_deposit(self):
        deposit = input("How much would you want to deposit?")
        self.deposit_done = False

        while self.deposit_done != True:
            self.change_balance_with_depoist(deposit)


    def change_balance_with_depoist(self, deposit):
        if deposit.isdigit() == True:
            self.card.change_balance(int(deposit))
            self.deposit_done = True
        else:
            self.incorrect_deposit(deposit)


    def incorrect_deposit(deposit):
        print("There was incorrect input.")
        deposit = input("Please enter correct amount: ")
        

    def go_withdraw(self):
        self.withdraw_done = False

        while self.withdraw_done != True:
            withdraw = input("How much would you want to withdraw?")

            if withdraw.isdigit() == True:
                withdraw = int(withdraw)
                if self.card.balance < withdraw:
                    print("You asked: " + str(withdraw))
                    print("It exceeds your current balance: " + str(self.card.balance))
                else:
                    print("You want to withdraw: " + str(withdraw))
                    selected = input("Is it correct? [Y/N]")
                    self.confirm_withdraw(selected, withdraw)

            else:
                print("There was incorrect input.")
                print("You entered: " + withdraw)


    def confirm_withdraw(self, selected, withdraw):
        if selected == "Y":
            self.card.change_balance(withdraw*(-1))
            self.withdraw_done = True



if __name__ == "__main__":
    controller = Controller()
    controller.hello()