class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    persons_ls = []
    persons_ls = [Person(body["name"], body["age"]) for body in people]

    for char in range(len(people)):

        if "wife" in people[char] and people[char]["wife"] is not None:
            persons_ls[char].wife = Person.people.get(people[char]["wife"])

        if "husband" in people[i] and people[i]["husband"] is not None:
            persons_ls[char].husband = Person.people.get(people[char]["husband"])

    return persons_ls
