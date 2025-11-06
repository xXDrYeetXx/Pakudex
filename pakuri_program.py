from pakudex import Pakudex

def get_input():
    try:
        choice = int(input("What would you like to do? "))
        if choice not in range(1, 7):
            raise ValueError
        return choice
    except:
        print("Unrecognized menu selection!")
        print()
        return None

menu = """Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit
"""

print("Welcome to Pakudex: Tracker Extraordinaire!")

# Get Pakudex size
while True:
    try:
        max_capacity = int(input("Enter max capacity of the Pakudex: "))
        if max_capacity <= 0:
            raise ValueError
        break
    except:
        print("Please enter a valid size.")

my_pakudex = Pakudex(max_capacity)
print(f"The Pakudex can hold {my_pakudex.get_capacity()} species of Pakuri.")

while True:
    print()
    print(menu)
    choice = get_input()

    if choice == 1:
        species_array = my_pakudex.get_species_array()
        if species_array is None:
            print("No Pakuri in Pakudex yet!")
        else:
            print("Pakuri In Pakudex:")
            for i, name in enumerate(species_array, 1):
                print(f"{i}. {name}")

    elif choice == 2:
        species_name = input("Enter the name of the species to display: ")
        stats = my_pakudex.get_stats(species_name)
        if stats is None:
            print("Error: No such Pakuri!")
        else:
            print("Species:", species_name)
            print("Attack:", stats[0])
            print("Defense:", stats[1])
            print("Speed:", stats[2])

    elif choice == 3:
        if my_pakudex.get_size() == my_pakudex.get_capacity():
            print("Error: Pakudex is full!")
            continue
        species_to_add = input("Enter the name of the species to add: ")
        if my_pakudex.add_pakuri(species_to_add):
            print(f"Pakuri species {species_to_add} successfully added!")
        else:
            print("Error: Pakuri species already exists!")

    elif choice == 4:
        species_to_evolve = input("Enter the name of the species to evolve: ")
        if my_pakudex.evolve_species(species_to_evolve):
            print(f"{species_to_evolve} has evolved!")
        else:
            print("Error: No such Pakuri!")

    elif choice == 5:
        my_pakudex.sort_pakuri()
        print("Pakuri have been sorted!")

    elif choice == 6:
        print("Thanks for using Pakudex! Bye!")
        break
