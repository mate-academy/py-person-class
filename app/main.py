class Person:

    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons_list = []
    for human in people:
        object_person = Person(human["name"], human["age"])
        persons_list.append(object_person)

    for human in people:
        name_human = Person.people[human["name"]]
        if "wife" in human and human["wife"] is not None:
            name_human.wife = Person.people[human["wife"]]
        elif "husband" in human and human["husband"] is not None:
            name_human.husband = Person.people[human["husband"]]

    return persons_list
