class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for data in people:
        person = Person(data["name"], data["age"])
        result.append(person)

    for data in people:
        person = Person.people[data["name"]]

        if "wife" in data and data["wife"] is not None:
            wife = Person.people[data["wife"]]
            setattr(person, "wife", wife)
            setattr(wife, "husband", person)

        if "husband" in data and data["husband"] is not None:
            husband = Person.people[data["husband"]]
            setattr(person, "husband", husband)
            setattr(husband, "wife", person)

    return result
