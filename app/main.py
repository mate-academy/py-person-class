class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for buddy in people:
        Person(buddy["name"], buddy["age"])

    for buddy in people:
        person_info = Person.people[buddy["name"]]
        if buddy.get("wife") is not None:
            person_info.wife = Person.people[buddy["wife"]]
        if buddy.get("husband") is not None:
            person_info.husband = Person.people[buddy["husband"]]
        person_list.append(person_info)
    return person_list
