class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    [Person(person["name"], person["age"]) for person in people]

    for person in people:
        name = person["name"]

        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name in Person.people:
            Person.people[name].wife = Person.people[wife_name]

        if husband_name in Person.people:
            Person.people[name].husband = Person.people[husband_name]

    return list(Person.people.values())
