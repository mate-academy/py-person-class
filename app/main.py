class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]
    for person in people:
        if person.get("wife"):
            setattr(
                Person.people[person["name"]],
                "wife",
                Person.people[person["wife"]])
        elif person.get("husband"):
            setattr(
                Person.people[person["name"]],
                "husband",
                Person.people[person["husband"]]
            )

    return person_list
