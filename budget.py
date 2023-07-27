class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        title = self.category.center(30, "*") + "\n"
        items = [f"{item['description'][:23]:23}{item['amount']:7.2f}\n" for item in self.ledger]
        total = "Total: " + str(self.get_balance())
        return title + "".join(items) + total

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_cat):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + budget_cat.category)
            budget_cat.deposit(amount, "Transfer from " + self.category)
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()


def create_spend_chart(categories):
    total_spend = sum(category.get_balance() for category in categories)
    percentages = [(category.get_balance() / total_spend) * 100 for category in categories]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percentage in percentages:
            chart += " o " if percentage >= i else "   "
        chart += " \n"

    longest_name = max(len(category.category) for category in categories)
    names = [category.category.ljust(longest_name) for category in categories]

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    for i in range(longest_name):
        chart += "    "
        for name in names:
            chart += " " + name[i] + " "
        chart += " \n"

    return chart
