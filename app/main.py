class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for data in people:
        new_person = Person(data["name"], data["age"])
        person_list.append(new_person)
    for data in people:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"]:
            person.wife = Person.people[data["wife"]]
        elif "husband" in data and data["husband"]:
            person.husband = Person.people[data["husband"]]

    return person_list
