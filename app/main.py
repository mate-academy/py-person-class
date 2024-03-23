class Person:
    people = {}

    def __init__(self,
                 name: str,
                 age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    for human in people_list:
        Person(human["name"], human["age"])

    for human in people_list:
        if "wife" in human and human["wife"] is not None:
            wife_exemplar = Person.people[human["wife"]]
            wife_exemplar.husband = Person.people[human["name"]]
        if "husband" in human and human["husband"] is not None:
            husband_exemplar = Person.people[human["husband"]]
            husband_exemplar.wife = Person.people[human["name"]]

    return [person for person in Person.people.values()]
