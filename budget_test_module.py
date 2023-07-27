import unittest
import budget
from budget import create_spend_chart

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.food = budget.Category("Food")
        self.entertainment = budget.Category("Entertainment")
        self.business = budget.Category("Business")

    def test_deposit(self):
        self.food.deposit(900, "deposit")
        self.assertEqual(self.food.ledger[0], {"amount": 900, "description": "deposit"})

    def test_withdraw(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        self.assertEqual(self.food.ledger[1], {"amount": -45.67, "description": "milk, cereal, eggs, bacon, bread"})

    def test_balance(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        self.assertEqual(self.food.get_balance(), 854.33)

    def test_transfer(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        self.assertTrue(self.food.transfer(20, self.entertainment))
        self.assertEqual(self.food.ledger[2], {"amount": -20, "description": "Transfer to Entertainment"})
        self.assertEqual(self.entertainment.ledger[0], {"amount": 20, "description": "Transfer from Food"})

    def test_check_funds(self):
        self.food.deposit(10, "deposit")
        self.assertFalse(self.food.check_funds(20))
        self.assertTrue(self.food.check_funds(10))

    def test_withdraw_no_funds(self):
        self.food.deposit(100, "deposit")
        self.assertFalse(self.food.withdraw(100.10))

    def test_transfer_no_funds(self):
        self.food.deposit(100, "deposit")
        self.assertFalse(self.food.transfer(200, self.entertainment))

    def test_to_string(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        self.food.transfer(20, self.entertainment)
        expected = "*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
        self.assertEqual(str(self.food), expected)

    def test_create_spend_chart(self):
        self.food.deposit(900, "deposit")
        self.entertainment.deposit(900, "deposit")
        self.business.deposit(900, "deposit")
        self.food.withdraw(105.55)
        self.entertainment.withdraw(33.40)
        self.business.withdraw(10.99)
        expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
        self.assertEqual(create_spend_chart([self.business, self.food, self.entertainment]), expected)

if __name__ == "__main__":
    unittest.main()
