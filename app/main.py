class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for individual in people:
        person = Person(individual["name"], individual["age"])
        person_list.append(person)

    for individual in people:
        if "wife" in individual.keys() and \
                individual["wife"] is not None:

            Person.people[individual["name"]].wife = \
                Person.people[individual["wife"]]

        elif "husband" in individual.keys() and \
                individual["husband"] is not None:

            Person.people[individual["name"]].husband = \
                Person.people[individual["husband"]]

    return person_list
