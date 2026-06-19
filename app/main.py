class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for data in people:
        person = Person(data["name"], data["age"])
        person_list.append(person)

    for data in people:
        person = Person.people[data["name"]]

        if data.get("wife") is not None:
            person.wife = Person.people[data["wife"]]
        if data.get("husband") is not None:
            person.husband = Person.people[data["husband"]]

    return person_list
