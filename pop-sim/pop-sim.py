import random
import timeit

male_names = open("male-names.txt").readlines()
female_names = open("female-names.txt").readlines()



def debugTimer(mode):
    _debug_start = 0
    _debug_end = 0
    if mode == "s":
        _debug_start = timeit.timeit()
    elif mode == "e":
        _debug_end = timeit.timeit()
        _time = _debug_end - _debug_start
        print(_time)


class Sim:
    people = []

    def __init__(self):
        self.p = None
        self.temp_person = None

    def createPerson(self):
        # These names are taken from 2 text files
        global male_names, female_names
        both_gender_names = [random.choice(male_names).replace("\n", ""),
                             random.choice(female_names).replace("\n", "")]

        self.temp_person = []

        # Gives person a gender
        # 0 is male, 1 is female
        if random.randint(0, 100) >= 50:
            gender = 0
        else:
            gender = 1

        # Gives person a name
        self.temp_person.append(both_gender_names[gender])

        # Gives person a starting age of 0 months old
        # Time in pop-sim is in months throughout
        self.temp_person.append(0)

        self.temp_person.append(gender)

        # Gives person a starting affection rating
        self.temp_person.append(100)  # 100 is a test!!!

        # Appends the person to people
        self.people.append(self.temp_person)

    def printPeople(self):
        gender = ["Male", "Female"]

        for self.p in self.people:
            age = self.p[1]

            # Calculates years and months, out of months
            age_years, age_months = divmod(age, 12)
            print(f"Name: {self.p[0]}\n"
                  f"Age: {age_years} years, {age_months} months\n"
                  f"Gender: {gender[self.p[2]]}\n")

    # def passTime(self, amount_of_time):

    def updateSim(self, amount_of_time):
        if amount_of_time == "": amount_of_time = 1
        amount_of_time = int(amount_of_time)

        # Adds age to all people
        for self.p in self.people:
            self.p[1] += amount_of_time

        for self.time in range(amount_of_time):

            # Calculates who will reproduce
            for self.p in self.people:
                # |Checks if age 16|checks affection 90|randomly decides|
                if self.p[1] > 16*12 and self.p[3] > 90 and random.randint(0, 100) > 60:
                    self.createPerson()



Sim.createPerson(Sim())
Sim.createPerson(Sim())
while True:
    Sim.printPeople(Sim())
    time_amount = input(">>> ").strip()
    debugTimer("s")
    Sim.updateSim(Sim(), time_amount)
    debugTimer("e")
    print(Sim.people)
