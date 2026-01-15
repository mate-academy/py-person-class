class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    Person.people.clear()

    for data in people_data:
        Person(data["name"], data["age"])

    person_list = []
    for data in people_data:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"]:
            person.wife = Person.people[data["wife"]]
        if "husband" in data and data["husband"]:
            person.husband = Person.people[data["husband"]]
        person_list.append(person)

    return person_list
