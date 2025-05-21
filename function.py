# Base class
class Character:
    def __init__(self, name, power):
        self.name = name
        self._power = power  # Protected attribute (encapsulation)

    def show_power(self):
        print(f"{self.name} has the power of {self._power}.")

# Subclass inheriting from Character
class Superhero(Character):
    def __init__(self, name, power, alias):
        super().__init__(name, power)
        self.alias = alias

    def fight_crime(self):
        print(f"{self.alias} fights crime with {self._power}!")

# Subclass inheriting from Character
class Villain(Character):
    def __init__(self, name, power, evil_plan):
        super().__init__(name, power)
        self.evil_plan = evil_plan

    def execute_plan(self):
        print(f"{self.name} executes the evil plan: {self.evil_plan}")

# Create objects
hero = Superhero("Clark Kent", "Super Strength", "Superman")
villain = Villain("Lex Luthor", "Genius Intellect", "Take over the world")

# Use methods
hero.show_power()
hero.fight_crime()

villain.show_power()
villain.execute_plan()
