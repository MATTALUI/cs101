#############################################
# W02 ASSIGNMENT: PIZZA MENU
# Matt Hummer
#############################################
class Pizza:
    def __init__(self, topping, price):
        """
        Initialize Pizza with topping
        """
        self._topping = topping
        self._price = price

    def display(self):
        """
        Displays formatted information about pizza
        """
        name = self._topping.capitalize() + " Pizza"
        price_str = "$%.2f" % self._price
        print(f"{name} - {price_str}")
        print(f"\tIngredients: {self._topping}, cheese, sauce, and crust")

# Display 5 different pizzas, their prices, and topping
pizzas = [
    Pizza("peperoni", 5),
    Pizza("mushroom", 4.02),
    Pizza("olive", 5.1),
    Pizza("anchovy", 6.21),
    Pizza("sausage", 3.67),
]
for pizza in pizzas:
    pizza.display()
