class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = []

    for person in people:
        instance = Person(person["name"], person["age"])
        person_list.append(instance)
        if "husband" in person and person["husband"] is not None:
            instance.husband = person["husband"]
        if "wife" in person and person["wife"] is not None:
            instance.wife = person["wife"]

    for person in person_list:
        for name, inst in Person.people.items():
            if "husband" in person.__dict__:
                if person.husband == name:
                    person.husband = inst

            if "wife" in person.__dict__:
                if person.wife == name:
                    person.wife = inst

    return person_list
