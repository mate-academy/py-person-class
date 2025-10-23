class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for human in people:
        people_list.append(Person(human["name"], human["age"]))
    for person in people:
        if "wife" in person and person["wife"] is not None:
            for man in people_list:
                if man.name == person["name"]:
                    man.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            for woman in people_list:
                if woman.name == person["name"]:
                    woman.husband = Person.people[person["husband"]]
    return people_list
