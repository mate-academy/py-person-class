class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    result = [
        Person(name=person["name"],
               age=person["age"])
        for person in people
    ]

    for person in people:
        if person.get("wife"):
            husband = Person.people[person["name"]]
            wife = Person.people[person["wife"]]
            husband.wife = wife
            wife.husband = husband
        return result
