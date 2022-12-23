class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for human in people:
        person_list.append(Person(human["name"], human["age"]))

    for i, human in enumerate(people):

        if "wife" in human:
            for pair_person in person_list:
                if human["wife"] == pair_person.name:
                    person_list[i].wife = pair_person

        elif "husband" in human:
            for pair_person in person_list:
                if human["husband"] == pair_person.name:
                    person_list[i].husband = pair_person

    return person_list
