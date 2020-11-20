from menu import MenuItem, Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_maker = CoffeeMaker()
drink_options = Menu()
money_machine = MoneyMachine()

while is_on:
    drinks = drink_options.get_items()
    choice = input(f"What would you like? ({drinks}): ")
    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink_object = drink_options.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink_object):
            payment = money_machine.make_payment(drink_object.cost)

            if payment:
                coffee_maker.make_coffee(drink_object)









