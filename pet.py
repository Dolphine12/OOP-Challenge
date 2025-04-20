class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

        # Hidden game lists
        self.fun_games = ["fetch", "tug of war", "frisbee", "hide and seek"]
        self.boring_games = ["chess", "monopoly", "tic tac toe"]

    def eat(self):
        if self.hunger == 0:
            print(f"{self.name} is already full and doesn't want to eat.")
        else:
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} ate and is now less hungry. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a nice nap. Energy: {self.energy}")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play.")
            choice = input("Would you like your pet to sleep first? (yes/no): ").strip().lower()
            if choice == "yes":
                self.sleep()
            else:
                print(f"{self.name} remains tired.")
            return

        game = input("Which game would you like to play with your pet? 🎲: ").strip().lower()

        self.hunger = min(10, self.hunger + 1)

        if game in self.fun_games:
            self.happiness = min(10, self.happiness + 2)
            self.energy = min(10, self.energy + 2)  # Boost energy
            print(f"{self.name} had a blast playing '{game}'! 😄 Energy increased!")
        elif game in self.boring_games:
            self.happiness = max(0, self.happiness - 1)
            self.energy = max(0, self.energy - 3)
            print(f"{self.name} was bored playing '{game}'... 😐 Energy drained.")
            if self.energy < 2:
                print(f"{self.name} is exhausted. Time for a nap!")
                self.sleep()
        else:
            self.happiness = min(10, self.happiness + 1)
            self.energy = max(0, self.energy - 2)
            print(f"{self.name} played '{game}'. It was okay.")

        self.get_status()

    def train(self, trick):
        if trick in self.tricks:
            print(f"{self.name} already knows how to {trick}.")
        else:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}! 🎓")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")
            choice = input("Would you like to teach one now? (yes/no): ").strip().lower()
            if choice == "yes":
                trick = input("Enter the trick to teach: ")
                self.train(trick)

    def get_status(self):
        print("\n🔍 Pet Status")
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
