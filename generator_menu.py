import os
import importlib

print("\n########################################\n")
print(" Welcome to the TTRPG Generator System!")
print("\n########################################\n")

# get list of generators from folder
generator_dir = ".//generators"
directory_list = os.listdir(generator_dir)
generator_list = []

for item in directory_list:
  if os.path.isdir(os.path.join(generator_dir, item)):
    generator_list.append(item)

# display list of available generators to user
print("The available Generators are:")
for i, generator in enumerate(generator_list):
  print(str(i) + ". " + generator)

# get the choice of generators from the user
generator_choice = int(input("Which generator would you like to run?"))

# run the generator the user chose
generator_to_run = generator_list[generator_choice]
module = importlib.import_module("generators.{}.run".format(generator_to_run))
module.run_generator()
