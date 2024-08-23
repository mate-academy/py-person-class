class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    persons = Person.people

    for per in people:
        if per.get("wife"):
            persons[per["name"]].wife = persons[per["wife"]]

        elif per.get("husband"):
            persons[per["name"]].husband = persons[per["husband"]]

    return person_list
