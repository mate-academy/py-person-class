class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        name = person["name"]
        wife = person.get("wife")
        husband = person.get("husband")

        if wife:
            Person.people[name].wife = Person.people[wife]

        if husband:
            Person.people[name].husband = Person.people[husband]

    return person_list
