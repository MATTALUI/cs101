class BudgetItem:
    def __init__(self, name, monthly):
        self._name = name
        self._monthly = monthly

    def display(self):
        yearly_cost = self._monthly * 12
        print(f"%s\t\t$%.2f\t\t$%.2f" % (self._name, self._monthly, yearly_cost))

def print_header(type="Item"):
    print("========================================")
    print(f"{type}\t\tMonth\t\tYear")
    print("========================================")

incomes = []
expenses = []

base_income_amount = float(input("How much will you make this month? "))
fast_amount = float(input("How much would you like to pay in fast offerings? "))

incomes.append(BudgetItem("", base_income_amount))
expenses.append(BudgetItem("Tithe", base_income_amount * 0.1))
expenses.append(BudgetItem("Fast", fast_amount))

collecting_expenses = True
while collecting_expenses:
    expense = input("Expense Name: ")
    collecting_expenses = bool(expense)
    if collecting_expenses:
        monthly_cost = float(input(f"Monthly cost for {expense}: "))
        print()
        expenses.append(BudgetItem(expense, monthly_cost))
savings_amount = sum([i._monthly for i in incomes]) - sum([e._monthly for e in expenses])

print("\nPERSONAL BUDGET")
print_header("Income")
for income in incomes:
    income.display()
print_header("Expense")
for expense in expenses:
    expense.display()
print_header("Savings")
BudgetItem("", savings_amount).display()
