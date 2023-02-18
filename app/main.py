class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    list_person = [
        Person(person.get("name"), person.get("age")) for person in people
    ]
    for person in people:
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
        elif person.get("husband"):
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband

    return list_person
