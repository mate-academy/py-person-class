class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    pass


def create_person_list(people: list) -> list:
    persons = []

    for human in people:
        person = Person(human["name"], human["age"])
        persons.append(person)

    for human in people:
        person = Person.people[human["name"]]
        key = "wife" if "wife" in human else "husband"
        relation = human.get(key)
        if relation is not None:
            spouse = Person.people.get(relation)
            if spouse:
                setattr(person, key, spouse)
    return persons

    pass
