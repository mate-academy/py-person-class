class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(person.get("name"), person.get("age")))
    for person in people:
        for key, values in person.items():
            if key == "wife" and values is not None:
                Person.people[person["name"]].wife = Person.people[person["wife"]]
            elif key == "husband" and values is not None:
                Person.people[person["name"]].husband = Person.people[person["husband"]]

    return person_list
