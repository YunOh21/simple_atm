import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from controller import Controller
from class_card import NewCard, OldCard


class TestController(TestCase):

    def setUp(self):
        self.controller = Controller()
        self.controller.card = OldCard(1)  # card number doesn't matter
        self.controller.card.change_balance = MagicMock()

        self.controller.make_card = MagicMock()
        self.controller.insert_card = MagicMock()
        self.controller.ask_for_new_card = MagicMock()
        self.controller.goodbye = MagicMock()
        self.controller.show_menu = MagicMock()
        self.controller.wrong_answer_try_again = MagicMock()
        self.controller.wrong_answer_five_times = MagicMock()
        self.controller.show_savings = MagicMock()
        self.controller.show_chequing = MagicMock()
        self.controller.go_deposit = MagicMock()
        self.controller.go_withdraw = MagicMock()
        self.controller.go_to_initial_screen = MagicMock()
        self.controller.user_input_weird = MagicMock()
        self.controller.incorrect_deposit = MagicMock()


    # test cases for switch_as_selected
    def test_swith_as_selected_0(self):
        self.controller.switch_as_selected(0)
        self.controller.make_card.assert_not_called()
        self.controller.insert_card.assert_not_called()
        self.controller.user_input_weird.assert_called_once()


    def test_swith_as_selected_1(self):
        self.controller.switch_as_selected(1)
        self.controller.make_card.assert_not_called()
        self.controller.insert_card.assert_called_once()


    def test_switch_as_selected_2(self):
        self.controller.switch_as_selected(2)
        self.controller.make_card.assert_not_called()
        self.controller.insert_card.assert_called_once()


    def test_switch_as_selected_3(self):
        self.controller.switch_as_selected(3)
        self.controller.make_card.assert_not_called()
        self.controller.insert_card.assert_called_once()


    def test_switch_as_selected_4(self):
        self.controller.switch_as_selected(4)
        self.controller.make_card.assert_called_once()
        self.controller.insert_card.assert_not_called()


    # test cases for switch_as_answer
    def test_switch_as_answer_Y(self):
        self.controller.switch_as_answer("Y")
        self.controller.ask_for_new_card.assert_called_once()


    def test_switch_as_answer_N(self):
        self.controller.switch_as_answer("N")
        self.controller.ask_for_new_card.assert_not_called()
        self.controller.goodbye.assert_called_once()

    
    def test_switch_as_answer_else(self):
        self.controller.switch_as_answer("else")
        self.controller.ask_for_new_card.assert_not_called()
        self.controller.goodbye.assert_not_called()
        self.controller.user_input_weird.assert_called_once()


    # test cases for check
    def test_check_right(self):
        result = self.controller.check("1234")
        self.assertEqual(result, True)


    def test_check_wrong(self):
        result = self.controller.check("1111")
        self.assertEqual(result, False)


    # test cases for switch_as_selected_account
    def test_switch_as_selected_account_0(self):
        self.controller.switch_as_selected_account(0)
        self.controller.show_savings.assert_not_called()
        self.controller.show_chequing.assert_not_called()
        self.controller.user_input_weird.assert_called_once()


    def test_switch_as_selected_account_1(self):
        self.controller.switch_as_selected_account(1)
        self.controller.show_savings.assert_called_once()
        self.controller.show_chequing.assert_not_called()


    def test_switch_as_selected_account_2(self):
        self.controller.switch_as_selected_account(2)
        self.controller.show_chequing.assert_called_once()
        self.controller.show_savings.assert_not_called()


    # test cases for switch_as_saving_answer
    def test_switch_as_saving_answer_Y(self):
        self.controller.switch_as_saving_answer("Y")
        self.controller.go_deposit.assert_called_once()
        self.controller.go_to_initial_screen.assert_not_called()


    def test_switch_as_saving_answer_N(self):
        self.controller.switch_as_saving_answer("N")
        self.controller.go_to_initial_screen.assert_called_once()
        self.controller.go_deposit.assert_not_called()


    def test_switch_as_saving_answer_else(self):
        self.controller.switch_as_saving_answer("else")
        self.controller.go_to_initial_screen.assert_called_once()
        self.controller.go_deposit.assert_not_called()


    # test cases for switch_as_chequing_answer
    def test_switch_as_chequing_answer_D(self):
        self.controller.switch_as_chequing_answer("D")
        self.controller.go_deposit.assert_called_once()
        self.controller.go_withdraw.assert_not_called()


    def test_switch_as_chequing_answer_W(self):
        self.controller.switch_as_chequing_answer("w")
        self.controller.go_withdraw.assert_called_once()
        self.controller.go_deposit.assert_not_called()


    def test_switch_as_chequing_answer_else(self):
        self.controller.switch_as_chequing_answer("else")
        self.controller.go_withdraw.assert_not_called()
        self.controller.go_deposit.assert_not_called()
        self.controller.user_input_weird.assert_called_once()


    # test cases for change_balance_with_deposit
    def test_change_balance_with_deposit_1000(self):
        self.controller.change_balance_with_depoist("1000")
        self.controller.card.change_balance.assert_called_with(1000)


    def test_change_balance_with_deposit_str(self):
        self.controller.change_balance_with_depoist("Hi")
        self.controller.incorrect_deposit.assert_called_once()


    # test cases for confirm_withdraw
    def test_confirm_withdraw_Y(self):
        self.controller.confirm_withdraw("Y", 1000)
        self.controller.card.change_balance.assert_called_with(-1000)


    def test_confirm_withdraw_N(self):
        self.controller.confirm_withdraw("N", 1000)
        self.controller.card.change_balance.assert_not_called()


if __name__ == '__main__':
    unittest.main()