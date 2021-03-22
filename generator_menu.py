import os

print("\n########################################\n")
print(" Welcome to the TTRPG Generator System!")
print("\n########################################\n")
print("The available Generators are:")

generator_list = os.listdir(os.path.dirname(__file__))
print(generator_list)
