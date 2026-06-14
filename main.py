import cashier
import data
from sandwichmaker i#mport SandwichMachine
from cashier import Cashier

resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMachine(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    machine_on = True

    while machine_on:
        choose = input("What would you like? (small/ medium/ large/ off/ report): ")

        if choose == "off":  # also fix: "exit" should be "off" per the spec
            print("Goodbye!")
            machine_on = False

        elif choose == "report":
            for item in sandwich_maker_instance.machine_resources:
                print(f"{item.capitalize()}: {sandwich_maker_instance.machine_resources[item]}")

        elif choose in recipes:
            required_ingredients = recipes[choose]["ingredients"]
            required_cost = recipes[choose]["cost"]  # renamed to required_cost

            if sandwich_maker_instance.check_resources(required_ingredients):
                coins_inserted = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_inserted, required_cost):
                    sandwich_maker_instance.make_sandwich(choose, required_ingredients)

if __name__=="__main__":
    main()