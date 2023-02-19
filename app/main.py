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
    peoples = Person.people
    for person in people:
        if person.get("wife"):
            wife = peoples.get(person.get("wife"))
            peoples.get(person.get("name")).wife = wife
        elif person.get("husband"):
            husband = peoples.get(person.get("husband"))
            peoples.get(person.get("name")).husband = husband

    return list_person
