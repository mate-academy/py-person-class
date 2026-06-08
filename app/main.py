class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    res_list = []

    for peop in people:
        Person(peop["name"], peop["age"])
        res_list.append(Person(peop["name"], peop["age"]))

    for peop in people:
        if "wife" in peop:
            if peop["wife"] is not None:
                Person.people[peop["name"]].wife = Person.people[peop["wife"]]
        if "husband" in peop:
            if peop["husband"] is not None:
                Person.people[peop["name"]].husband\
                    = Person.people[peop["husband"]]

    return res_list
