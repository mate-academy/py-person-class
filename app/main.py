class Person:
    people = {}

    def __init__(self, name : str, age : int) -> None:
        self.name = name
        self.age = age
        self.people[name] = Person


def create_person_list(people: list) -> list:
    humans = []
    wife = []
    husband = []
    for index, person in enumerate(people):
        key = person.keys()
        human = Person(person["name"], person["age"])
        humans.append(human)
        Person.people[person["name"]] = human
        if "wife" in key and person["wife"]:
            human.wife = person["wife"]
            wife.append(index)
        elif "husband" in key and person["husband"]:
            human.husband = person["husband"]
            husband.append(index)
    for index, human in enumerate(humans):
        if index in wife:
            for person in humans[index:]:
                if human.wife == person.name:
                    human.wife = person
                    person.husband = human
                    break
        elif index in husband:
            for person in humans[index:]:
                if human.husband == person.name:
                    human.husband = person
                    person.wife = human
                    break
    return humans
