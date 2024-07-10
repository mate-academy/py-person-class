class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = []
    for human in people:
        person = Person(human["name"], human["age"])
        persons_list.append(person)

    for i, human in enumerate(people):
        if "wife" in human.keys() and human["wife"] is not None:
            persons_list[i].wife = Person.people[human["wife"]]

        elif "husband" in human.keys() and human["husband"] is not None:
            persons_list[i].husband = Person.people[human["husband"]]

    return persons_list
