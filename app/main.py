class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    Person.people.clear()
    persons = [Person(person["name"], person["age"]) for person in people]
    by_name = {p.name: p for p in persons}

    for dict_people in people:

        current = by_name[dict_people["name"]]
        if dict_people.get("wife"):
            current.wife = by_name[dict_people["wife"]]
        if dict_people.get("husband"):
            current.husband = by_name[dict_people["husband"]]

    return persons
