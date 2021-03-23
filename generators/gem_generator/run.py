from generators.gem_generator.gem_constants import GEM_PRICES, MAX_MODIFIER, MIN_MODIFIER

import random


def run_generator():
    gem_generator = GemGenerator()
    gem_generator.define_settings()
    gem_generator.generate_gems()


class GemGenerator(object):
    def __init__(self):
        self.base_value = 0
        self.variant_amount = 0
        self.num_to_generate = 25
        self.min_value = 0
        self.max_value = 0
        self.gem_list = []

        self.variant_dict = {
            "Very High": 10,
            "High": 5,
            "Standard": 2,
            "Low": 1.5,
            "Very Low": 1.1
        }

        print("\n################")
        print(" Gem Generator!")
        print("################")

    def define_settings(self):
        self.base_value = int(input("\nAverage GP value: "))

        print("\nHow much variance in price do you want?")
        for i, (variant, _) in enumerate(self.variant_dict.items()):
            print(str(i) + ". " + variant)

        variant_choice = int(input("Enter: "))
        self.variant_amount = list(self.variant_dict.values())[variant_choice]

        self.min_value = round(self.base_value / self.variant_amount)
        if self.min_value < 1:
            self.min_value = 1
        self.max_value = round(self.base_value * self.variant_amount)

    def generate_gems(self):
        print("\n--------------------------")
        print("Price Range: {0}gp - {1}gp".format(self.min_value, self.max_value))
        print("\nResults:")

        # keep generating gems until we have the required number
        # while loop used instead of for because randomly chosen gem may not fit within valid price range set by user
        while len(self.gem_list) < self.num_to_generate:
            # create a list of weights from the weight value in the GEM_PRICES dict
            weight_list = [gem_dict["weight"] for gem_dict in GEM_PRICES]
            random_gems = random.choices(GEM_PRICES, weights=weight_list, k=self.num_to_generate)

            for random_gem in random_gems:
                # get the attributes from the randomly selected gem dict
                base_gem_price = random_gem["price"]
                gem_name = random_gem["name"]

                # keep randomly generating a gem price
                min_price_mod = self.min_value / base_gem_price
                max_price_mod = self.max_value / base_gem_price

                # if the min price modifier for the gem is greater than the max constant or
                # the max price modifier is less than the min constant skip the gem and generate a new one
                if max_price_mod < MIN_MODIFIER or min_price_mod > MAX_MODIFIER:
                    continue

                # ensure that the gem can never go outside the hard set Min and Max constant price
                # e.g. if the lowest variant price is 20 a gem with a price of 5000 should still never go below 200
                if min_price_mod < MIN_MODIFIER:
                    min_price_mod = MIN_MODIFIER
                if max_price_mod > MAX_MODIFIER:
                    max_price_mod = MAX_MODIFIER

                # generate a random price for the gem within the valid range for that gem and the variant price limit
                random_price_mod = random.uniform(min_price_mod, max_price_mod)
                gem_price = round(base_gem_price * random_price_mod)

                # add the newly generated gem and price to a list for sorting
                self.gem_list.append({gem_name: gem_price})
                if len(self.gem_list) == self.num_to_generate:
                    break

        # sort by gem name and then by gem value
        sorted_list = sorted(self.gem_list, key=lambda d: (list(d.keys()), list(d.values())))

        # print the final sorted list of generated gems and prices
        for gem_dict in sorted_list:
            key = list(gem_dict.keys())[0]
            value = list(gem_dict.values())[0]

            print("{0} - {1}gp".format(key, value))

        print("--------------------------")
        self.run_exit_menu()

    def run_exit_menu(self):
        self.gem_list = []
        print("\nWhat would you like to do? ")
        print("0. Generate another 10 with same settings")
        print("1. Generate another 10 with different settings")
        print("2. Exit")
        user_choice = int(input("Enter: "))

        if user_choice == 0:
            self.generate_gems()
        elif user_choice == 1:
            self.define_settings()
            self.generate_gems()
