class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person_list.append(Person(name, age))

    for person in people:
        if "wife" in person:
            wife = person["wife"]
            if wife in Person.people:
                Person.people[person["name"]].wife = Person.people[wife]
        if "husband" in person:
            husband = person["husband"]
            if husband in Person.people:
                Person.people[person["name"]].husband = Person.people[husband]

    return person_list
