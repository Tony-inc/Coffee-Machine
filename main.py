from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = MenuItem
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

again = "y"

while again == "y":
    choice = input(f"What would you like: {menu.get_items()}?").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        break
    elif choice in menu.get_items():
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
    else:
        print("Sorry that item is not available.")

    again = input("'y' to continue.")


