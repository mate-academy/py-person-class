class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    person_list = []

    for data in people_data:
        person = Person(data["name"], data["age"])
        person_list.append(person)

    for data in people_data:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"] is not None:
            person.wife = Person.people.get(data["wife"])
        elif "husband" in data and data["husband"] is not None:
            person.husband = Person.people.get(data["husband"])

    return person_list
