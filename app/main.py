class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    persons_ls = []
    persons_ls = [Person(body["name"], body["age"]) for body in people]

    for cha in range(len(people)):

        if "wife" in people[cha] and people[cha]["wife"] is not None:
            persons_ls[cha].wife = Person.people.get(people[cha]["wife"])
        if "husband" in people[cha] and people[cha]["husband"] is not None:
            persons_ls[cha].husband = Person.people.get(people[cha]["husband"])

    return persons_ls
