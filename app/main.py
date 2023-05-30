class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        new_person = Person(name, age)
        person_list.append(new_person)

    for person in people:
        name = person["name"]
        wife = person.get("wife")
        husband = person.get("husband")

        if wife is not None:
            Person.people[name].wife = Person.people[wife]

        if husband is not None:
            Person.people[name].husband = Person.people[husband]

    return person_list
