class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __str__(self) -> str:
        return f"Person: name {self.name}, age {self.age}"


def create_person_list(people: list) -> list:
    person_list = []

    for index, person in enumerate(people):
        person_list.append(Person(name=person["name"], age=person["age"]))

    for index, person in enumerate(people):
        if "wife" in person and person["wife"] is not None:
            person_list[index].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            person_list[index].husband = Person.people[person["husband"]]

    return person_list
