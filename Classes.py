
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print(f"{self.species} makes a sound.")


class Pet:
    def __init__(self, name):
        self.name = name

    def show_affection(self):
        print(f"{self.name} shows affection.")


class Worker:
    def __init__(self, job):
        self.job = job

    def work(self):
        print(f"Performing job: {self.job}")


class GuideDog(Animal, Pet, Worker):
    def __init__(self, species, name, job):
        Animal.__init__(self, species)
        Pet.__init__(self, name)
        Worker.__init__(self, job)

    def guide(self):
        print(f"{self.name} is guiding as a {self.species} and performing job: {self.job}")


buddy = GuideDog("Dog", "Buddy", "Guide")
buddy.make_sound()
buddy.show_affection()
buddy.work()
buddy.guide()
