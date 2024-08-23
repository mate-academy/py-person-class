class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.add_person(self)

    @classmethod
    def add_person(cls, person: "Person") -> None:
        cls.people[person.name] = person

    @classmethod
    def get_person(cls) -> dict:
        return cls.people


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    persons = Person.get_person()

    for per in people:
        if per.get("wife"):
            persons[per["name"]].wife = persons[per["wife"]]

        elif per.get("husband"):
            persons[per["name"]].husband = persons[per["husband"]]

    return person_list
