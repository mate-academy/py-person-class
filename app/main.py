class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    person_insts = [Person(person["name"], person["age"]) for person in people]

    for index, person in enumerate(people):
        if person.get("wife"):
            person_insts[index].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            person_insts[index].husband = Person.people[person["husband"]]

    return person_insts
