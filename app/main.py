class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_person = [Person(person["name"], person["age"]) for person in people]
    for man in people:
        if "wife" in man and man["wife"] is not None:
            wife = Person.people[man["wife"]]
            Person.people[man["name"]].wife = wife
        elif "husband" in man and man["husband"] is not None:
            husband = Person.people[man["husband"]]
            Person.people[man["name"]].husband = husband
        continue

    return list_person
