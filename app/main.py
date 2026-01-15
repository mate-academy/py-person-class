class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    Person.people.clear()

    person_list = [Person(data["name"], data["age"]) for data in people_data]

    for data in people_data:
        person = Person.people[data["name"]]

        if data.get("wife"):
            person.wife = Person.people[data["wife"]]

        if data.get("husband"):
            person.husband = Person.people[data["husband"]]

    return person_list
