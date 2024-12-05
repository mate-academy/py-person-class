class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __str__(self) -> str:
        return f"Person: name {self.name}, age {self.age}"


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for index, person in enumerate(people):
        if person.get("wife"):
            person_list[index].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            person_list[index].husband = Person.people[person["husband"]]

    return person_list
