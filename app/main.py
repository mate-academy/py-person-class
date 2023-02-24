class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]
    for i, person in enumerate(people):
        if person.get("wife"):
            setattr(
                person_list[i],
                "wife",
                Person.people.get(person["wife"])
            )
        elif person.get("husband"):
            setattr(
                person_list[i],
                "husband",
                Person.people.get(person["husband"])
            )
    return person_list
