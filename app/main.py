class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(person["name"], person["age"]) for person in people]
    for index, person in enumerate(people):
        if "wife" in person.keys() and person["wife"] is not None:
            result_list[index].wife = Person.people[person["wife"]]
        if "husband" in person.keys() and person["husband"] is not None:
            result_list[index].husband = Person.people[person["husband"]]
    return result_list
