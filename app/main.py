class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.add_person(self)

    @classmethod
    def add_person(cls, person: "Person") -> None:
        cls.people[person.name] = person


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for per in people:
        if per.get("wife"):
            Person.people[per["name"]].wife = Person.people[per["wife"]]

        elif per.get("husband"):
            Person.people[per["name"]].husband = Person.people[per["husband"]]

    return person_list
