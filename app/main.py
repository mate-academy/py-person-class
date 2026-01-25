class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = [Person(data["name"], data["age"]) for data in people]

    for data in people:
        name = data["name"]

        wife = data.get("wife")
        if wife is not None:
            Person.people[name].wife = Person.people[wife]

        husband = data.get("husband")
        if husband is not None:
            Person.people[name].husband = Person.people[husband]

    return person_list

