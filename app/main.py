class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    result = [Person(person["name"], person["age"]) for person in people]

    for data in people:
        person = Person.people[data["name"]]

        if data.get("wife") and Person.people.get(data["wife"]):
            person.wife = Person.people[data["wife"]]

        if data.get("husband") and Person.people.get(data["husband"]):
            person.husband = Person.people[data["husband"]]

    return result
