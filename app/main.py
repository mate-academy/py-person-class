class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    for creature in people:
        Person(creature["name"], creature["age"])

    for creature in people:
        if creature.get("wife"):
            Person.people[creature["name"]].wife\
                = Person.people[creature["wife"]]

            Person.people[creature["wife"]].husband\
                = Person.people[creature["name"]]
        else:
            del Person.people[creature["name"]].wife

    return list(Person.people.values())
