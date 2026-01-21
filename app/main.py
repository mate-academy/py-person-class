class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_info = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        name = person.get("name")
        wife = person.get("wife")
        husband = person.get("husband")
        if wife is not None:
            Person.people[name].wife = Person.people[wife]
        if husband is not None:
            Person.people[name].husband = Person.people[husband]

    return person_info
