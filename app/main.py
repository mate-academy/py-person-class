class Person:
    people = {}

    def __init__(self, name: str, age: str, *args, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    people_list = [
        Person(
            name=person["name"],
            age=person["age"],
        )
        for person in people
    ]

    for person in people:
        if person.get("wife"):
            Person.people.get(person["name"]).wife = (
                Person.people.get(person["wife"])
            )
        elif person.get("husband"):
            Person.people.get(person["name"]).husband = (
                Person.people.get(person["husband"])
            )

    return people_list
