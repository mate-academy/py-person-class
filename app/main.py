class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.create_people(self)

    @classmethod
    def create_people(cls, self: "Person") -> None:
        cls.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    people1 = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            Person.people[person["name"]].husband \
                = Person.people[person["husband"]]

    return people1
