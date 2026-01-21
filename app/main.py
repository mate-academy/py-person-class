class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_ls = [Person(body["name"], body["age"]) for body in people]

    for person_data in people:
        if "wife" in person_data and person_data["wife"] is not None:
            persons_ls[people.index(person_data)].wife \
                = Person.people.get(person_data["wife"])

        if "husband" in person_data:
            persons_ls[people.index(person_data)].husband \
                = Person.people.get(person_data["husband"])

    return persons_ls
