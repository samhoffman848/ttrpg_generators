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
        self.max_value = round(self.base_value * self.variant_amount)

    def generate_gems(self):
        print("\n--------------------------")
        print("Price Range: {0}gp - {1}gp".format(self.min_value, self.max_value))
        print("\nResults:")

        while len(self.gem_list) <= self.num_to_generate:
            max_num = len(GEM_PRICES) - 1
            min_num = 0
            random_num = random.randint(min_num, max_num)
            gem = list(GEM_PRICES.keys())[random_num]
            base_gem_price = GEM_PRICES[gem]

            max_gem_price = base_gem_price * MAX_MODIFIER
            min_gem_price = base_gem_price * MIN_MODIFIER

            # if max possible gem price is too low or min possible gem price is too high then generate a new random gem
            if max_gem_price < self.min_value or min_gem_price > self.max_value:
                continue

            gem_price = -100
            while self.min_value >= gem_price or gem_price >= self.max_value:
                random_price_mod = random.uniform(MIN_MODIFIER, MAX_MODIFIER)
                gem_price = round(base_gem_price * random_price_mod)

            self.gem_list.append({gem: gem_price})

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
