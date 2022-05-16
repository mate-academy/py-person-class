class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    output_list = []

    for person in people:
        pr = Person(name=person["name"], age=person["age"])
        output_list.append(pr)

    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person['name']].wife = Person.people[person['wife']]

        if "husband" in person and person["husband"] is not None:
            Person.people[person['name']].husband = \
                Person.people[person['husband']]

    return output_list
