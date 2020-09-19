from random import randint

print("""
Monthly Budget
========================================
Item\t\tMonth\t\tYear
========================================""")

# Create a simple 6 item budget
for category in ['Tithing', 'Dates', 'House', 'Travel', 'Candy', 'Dogs']:
    # Item's name as a string ("category")
    yearly_cost = randint(100, 1000) # Yearly amount as an integer
    monthly_cost = yearly_cost / 12.0 # Monthly amount as a floating point
    print(f"%s\t\t$%.2f\t\t$%.2f" % (category, monthly_cost, yearly_cost))
