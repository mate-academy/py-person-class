class Person:
    people = dict()

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for index, person in enumerate(people):
        if person.get("wife") is not None:
            person_list[index].wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            person_list[index].husband = Person.people[person["husband"]]
    return person_list
