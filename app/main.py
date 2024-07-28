class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        instance = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            wife = Person.people[person["wife"]]
            instance.wife = wife
            wife.husband = instance

        if "husband" in person and person["husband"] is not None:
            husband = Person.people[person["husband"]]
            instance.husband = husband
            husband.wife = instance

        result.append(instance)
    return result
