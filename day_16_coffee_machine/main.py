from menu import Menu
from coffee_machine import CoffeeMaker
from money_machine import MoneyMachine

money_maker = MoneyMachine()
menu = Menu()
coffee_machine = CoffeeMaker()


end_order = False


while not end_order:
    choice = input("What would you like? (espresso/latte/cappuccino/americano): ")
    if choice == "report":
        coffee_machine.report()
        money_maker.report()
    elif choice == "off":
        end_order = True
    else:
        drink = menu.find_drink(choice)
        sufficient_resources = coffee_machine.is_resource_sufficient(drink)
        if sufficient_resources:
           if money_maker.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)


