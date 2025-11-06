from pakudex import Pakudex
menu = """
Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit
"""
print("Welcome to Pakudex: Tracker Extraordinaire!")
max_capacity = int(input("Enter max capacity of the Pakudex: "))
my_pakudex = Pakudex(max_capacity)
print(f"The Pakudex can hold {my_pakudex.get_capacity()} species of Pakuri.")
while True:
    print(menu)
    choice = int(input("What would you like to do? "))
    if choice == 1:
        print(my_pakudex.get_species_array())
    if choice == 2:
        pass
    if choice == 3:
        pass
    if choice == 4:
        pass
    if choice == 5:
        pass
    if choice == 6:
        break


