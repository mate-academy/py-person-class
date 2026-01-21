class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    individuals = [Person(person["name"], person["age"]) for person in people]

    for i, person in enumerate(people):
        wife, husband = person.get("wife"), person.get("husband")

        if wife:
            individuals[i].wife = Person.people[wife]
        elif husband:
            individuals[i].husband = Person.people[husband]

    return individuals
