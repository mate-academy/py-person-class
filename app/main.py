class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    for d_people in people:
        Person(d_people["name"], d_people["age"])
    for human in people:
        if "wife" in human and human["wife"] is not None:
            setattr(Person.people[human["name"]], "wife",
                    Person.people[human["wife"]])
        if "husband" in human and human["husband"] is not None:
            setattr(Person.people[human["name"]], "husband",
                    Person.people[human["husband"]])
    return [human for human in Person.people.values()]
