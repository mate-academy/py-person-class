class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = [
        Person(individual["name"], individual["age"])
        for individual in people
    ]

    for individual in people:
        if individual.get("wife"):
            Person.people[individual["name"]].wife = \
                Person.people[individual["wife"]]
        if individual.get("husband"):
            Person.people[individual["name"]].husband = \
                Person.people[individual["husband"]]

    return result_list
