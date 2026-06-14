#Kaleiah McPherson
#ITSC 3155
#This is an assignment.  We are tasked to create an automatic sandwhich maker machine.
## Resources: W3 Schools:https://www.w3schools.com/python/ref_string_capitalize.asp

### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""

        for ingredient_item in ingredients:
            if ingredients[ingredient_item] > self.machine_resources[ingredient_item]:
                print(f"Sorry, there isn't enough {ingredient_item}")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for sandwich in order_ingredients:
            self.machine_resources[sandwich] -= order_ingredients[sandwich]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


### Make an instance of SandwichMachine class and write the rest of the codes ###


    #Program should check whether there are enough resources to make the sandwich when
    # the user chooses it.
    #If there are sufficient resources to make the drink selected, then the program should
    #prompt the user to insert coins.
