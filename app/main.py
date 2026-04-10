class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    result = [Person(person.get("name"), person.get("age")) for person in people]

    for person in people:
        inst = Person.people[person["name"]]
        wife = person.get("wife")
        if wife is not None:
            inst.wife = Person.people.get(wife)
        husband = person.get("husband")
        if husband is not None:
            inst.husband = Person.people.get(husband)

    return result
