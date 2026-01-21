class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []

    for person in people:
        person_info = Person(person.get("name"), person.get("age"))
        person_list.append(person_info)

    for person in people:
        if person.get("wife"):
            wife = Person.people[person.get("wife")]
            Person.people[person.get("name")].wife = wife
        if person.get("husband"):
            husband = Person.people[person.get("husband")]
            Person.people[person.get("name")].husband = husband

    return person_list
