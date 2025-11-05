import pakuri
import pakudex
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
print(f"The Pakudex can hold {max_capacity} species of Pakuri.")

while True:
    print(menu)
    choice = int(input("What would you like to do? "))
