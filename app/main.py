class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        result.append(Person(person["name"], person["age"]))
    for index, person in enumerate(people):
        if "wife" in person.keys() and person["wife"]:
            result[index].wife = Person.people[person["wife"]]
        elif "husband" in person.keys() and person["husband"]:
            result[index].husband = Person.people[person["husband"]]
    return result
