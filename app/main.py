class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(name=person.get("name"), age=person.get("age"))
              for person in people]
    for person in people:
        person_object = Person.people[person.get("name")]
        if person.get("wife") is not None:
            person_object.wife = Person.people[person.get("wife")]
        elif person.get("husband") is not None:
            person_object.husband = Person.people[person.get("husband")]

    return result
