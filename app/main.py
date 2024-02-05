class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for per in people:
        person_list.append(Person(per["name"], per["age"]))

    for per in people:
        name_person = Person.people.get(per["name"])

        if "wife" in per and per["wife"] is not None:
            # name_wife = Person.people.get(per["wife"])
            # name_person.wife = name_wife
            name_person.wife = Person.people.get(per["wife"])

        if "husband" in per and per["husband"] is not None:
            # name_husband = Person.people.get(per["husband"])
            # name_person.husband = name_husband
            name_person.husband = Person.people.get(per["husband"])

    return person_list
