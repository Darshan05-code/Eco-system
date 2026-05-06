from abc import ABC, abstractmethod
import random

# ---------------- Base Class -----------------------
class Organism(ABC):
    def __init__(self, energy):
        self.__energy = energy

    @property
    def energy(self):
        return self.__energy

    def _change_energy(self, amount):
        self.__energy += amount

    @abstractmethod
    def act(self, world):
        pass


# ---------------- Animal ----------------
class Animal(Organism, ABC):
    def __init__(self, energy):
        super().__init__(energy)

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self, world):
        pass

    def rest(self):
        print("Animal is resting")
        self._change_energy(+1)

    def act(self, world):
        # print("\nChoose action: ")
        # print("1. Move")
        # print("2. Eat")
        # print("3. Rest")

        choice = random.randint(1,3)

        if choice == "1":
            self.move()
            self._change_energy(-1)

        elif choice == "2":
            self.eat(world)

        elif choice == "3":
            self.rest()

        else:
            print("Invalid choice")

        print("Energy:", self.energy)


# ---------------- Types ----------------
class Herbivore(Animal):
    def move(self):
        print("Herbivore moves")

    def eat(self, world):
        print("Herbivore eats plants")
        self._change_energy(+5)


class Carnivore(Animal):
    def move(self):
        print("Carnivore hunts")

    def eat(self, world):
        print("Carnivore eats animals")
        self._change_energy(+8)


class Omnivore(Animal):
    def move(self):
        print("Omnivore moves")

    def eat(self, world):
        print("Omnivore eats plants and animals")
        self._change_energy(+6)


# ---------------- Plant ----------------
class Plant(Organism):
    def act(self, world):
        print("Plant grows")
        self._change_energy(+2)
        print("Energy:", self.energy)


# ---------------- World ----------------
class World:
    def __init__(self):
        self.organisms = []

    def add(self, organism):
        self.organisms.append(organism)

    def simulate(self):
        turn = 1
    def simulate(self, turns):
        for t in range(turns):
            print(f"\n--- Turn {t+1} ---")
            for org in self.organisms:
                org.act(self)
                print("Energy:", org.energy)
            



w = World()

h = Herbivore(10)
c = Carnivore(12)
o = Omnivore(11)
p = Plant(5)

w.add(h)
w.add(c)
w.add(o)
w.add(p)

w.simulate(3)