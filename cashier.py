class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coin(s).")

        dollars = input("how many dollars?: ")
        half_dollar = input("how many half dollars?: ")
        quarters = input("how many quarters?: ")
        nickles = input("how many nickles?: ")

        half_dollar_value = int(half_dollar) * float(0.5)
        quarter_value = int(quarters) * float(0.25)
        nickle_value = int(nickles) * float(0.05)
        dollar_value = int(dollars) * float(1.0)

        total = quarter_value + nickle_value + dollar_value + half_dollar_value
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            calc_change = round(coins - cost,2)
            if calc_change >= 0:
                print(f"Here is ${calc_change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            #return False