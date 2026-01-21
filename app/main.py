class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(person_param.get("name"),
                   person_param.get("age")) for person_param in people]

    for person_param in people:
        if person_param.get("wife") is not None:
            person = Person.people.get(person_param.get("name"))
            person.wife = Person.people.get(person_param.get("wife"))
        if person_param.get("husband") is not None:
            person = Person.people.get(person_param.get("name"))
            person.husband = Person.people.get(person_param.get("husband"))

    return person_list
