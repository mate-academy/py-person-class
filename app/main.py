class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_inst = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if person.get("wife") in Person.people:
            wife_inst = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife_inst
        if person.get("husband") in Person.people:
            husband_inst = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband_inst
    return person_inst
