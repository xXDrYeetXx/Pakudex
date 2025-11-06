from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.species_list = []

    def get_size(self):
        return len(self.species_list)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if len(self.species_list) == 0:
            return None
        return self.species_list

    def add_pakuri(self, species):
        if len(self.species_list) >= self.capacity:
            return False
        for p in self.species_list:
            if p.get_species() == species:
                return False

        new_pakuri = Pakuri(species)
        self.species_list.append(new_pakuri)
        return True

    def get_stats(self, species):
        for p in self.species_list:
            if p.get_species() == species:
                return [p.get_attack(), p.get_defense(), p.get_speed()]
        return None

    def sort_pakuri(self):
        self.species_list.sort()

    def evolve_species(self, species):
        for p in self.species_list:
            if p.get_species() == species:
                p.evolve()
                return True
        return False
