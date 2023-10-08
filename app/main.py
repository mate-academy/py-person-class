class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    persons_ls = []

    for body in people:
        person = Person(body["name"], body["age"])
        persons_ls.append(person)

    for i in range(len(people)):

        if "wife" in people[i] and people[i]["wife"] is not None:
            persons_ls[i].wife = Person.people.get(people[i]["wife"])

        if "husband" in people[i] and people[i]["husband"] is not None:
            persons_ls[i].husband = Person.people.get(people[i]["husband"])

    return persons_ls
