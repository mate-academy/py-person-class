class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    lists = []
    for pers in people:
        lists.append(Person(pers["name"], pers["age"]))
    for pers in people:
        if "wife" in pers and pers["wife"] is not None:
            Person.people[pers["name"]].wife = Person.people[pers["wife"]]
        elif "husband" in pers and pers["husband"] is not None:
            Person.people[pers["name"]].husband = \
                Person.people[pers["husband"]]
    return lists
