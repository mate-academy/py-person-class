class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    Person.people.clear()

    for person in people_data:
        Person(person.get("name"), person.get("age"))

    for person in people_data:
        name = person.get("name")
        if person.get("wife"):
            spouse_name = person.get("wife")
            Person.people[name].wife = Person.people[spouse_name]
        elif person.get("husband"):
            spouse_name = person.get("husband")
            Person.people[name].husband = Person.people[spouse_name]

    return [Person.people[p.get("name")] for p in people_data]
