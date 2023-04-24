class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if person.get("wife") is not None:
            Person.people[person.get("name")].wife\
                = Person.people[person.get("wife")]
        if person.get("husband") is not None:
            Person.people[person.get("name")].husband\
                = Person.people[person.get("husband")]
    return result
