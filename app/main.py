class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    person_list = [
        Person(data["name"], data["age"]) for data in people_data
    ]

    for data in people_data:
        name = data["name"]
        person = Person.people[name]

        if data.get("wife"):
            person.wife = Person.people[data["wife"]]
        if data.get("husband"):
            person.husband = Person.people[data["husband"]]

    return person_list
