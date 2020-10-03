class BudgetItem:
    def __init__(self, name, monthly):
        self._name = name
        self._monthly = monthly

    def display(self):
        yearly_cost = self._monthly * 12
        print(f"%s\t\t$%.2f\t\t$%.2f" % (self._name, self._monthly, yearly_cost))

expenses = []
collecting_expenses = True
while collecting_expenses:
    expense = input("Expense Name: ")
    collecting_expenses = bool(expense) # break loop if empty name given
    if collecting_expenses:
        # could throw errors; who cares!
        monthly_cost = float(input(f"Monthly cost for {expense}: "))
        print()
        expenses.append(BudgetItem(expense, monthly_cost))


print("""
Monthly Budget
========================================
Item\t\tMonth\t\tYear
========================================""")
for expense in expenses:
    expense.display()
