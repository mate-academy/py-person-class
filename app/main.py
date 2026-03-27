class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = [Person(person.get("name"), person.get("age"))
                   for person in people]

    for person in people:
        current_person = Person.people[person.get("name")]

        if person.get("wife") is not None:
            current_person.wife = Person.people[person.get("wife")]
        elif person.get("husband") is not None:
            current_person.husband = Person.people[person.get("husband")]

    return person_list
