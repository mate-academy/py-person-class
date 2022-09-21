class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for ind, person in enumerate(people):
        if person.get("wife") is not None:
            person_list[ind].wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            person_list[ind].husband = Person.people[person["husband"]]
    return person_list
