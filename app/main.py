class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    all_people = []
    all_people = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        current = Person.people[person["name"]]
        spouse1 = person.get("wife")
        if spouse1 is not None:
            current.wife = Person.people[person["wife"]]
        spouse2 = person.get("husband")
        if spouse2 is not None:
            current.husband = Person.people[person["husband"]]

    return all_people
