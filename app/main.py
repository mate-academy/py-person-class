class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    Person.people = {}

    for data in people_data:
        Person(data["name"], data["age"])

    for data in people_data:
        person = Person.people[data["name"]]

        if data.get("wife") is not None:
            person.wife = Person.people[data["wife"]]

        if data.get("husband") is not None:
            person.husband = Person.people[data["husband"]]

    return list(Person.people.values())
