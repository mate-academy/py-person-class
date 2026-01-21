class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        if person.get("husband"):
            marry(
                wife=Person.people.get(person["name"]),
                husband=Person.people.get(person["husband"]),
            )

    return [*Person.people.values()]


def marry(wife: Person, husband: Person) -> None:
    wife.husband = husband
    husband.wife = wife
