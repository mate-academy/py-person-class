class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        result += {Person(person.get("name"), person.get("age"))}
    for i, person in enumerate(people):
        if "wife" in person and person.get("wife") is not None:
            result[i].wife = Person.people.get(person["wife"])
        if "husband" in person and person.get("husband") is not None:
            result[i].husband = Person.people.get(person["husband"])
    return result
