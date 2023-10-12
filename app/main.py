class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    persons_ls = [Person(body["name"], body["age"]) for body in people]

    for man in range(len(people)):

        # if "wife" in people[person] and people[person]["wife"] is not None:
        if people[man].get("whife") is not None:
            persons_ls[man].wife = Person.people.get(people[man]["wife"])
        if people[man].get("husband") is not None:
            persons_ls[man].husband = Person.people.get(people[man]["husband"])

    return persons_ls
