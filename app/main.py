class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for human in people:
        person_list.append(Person(human["name"], human["age"]))

    for human in people:
        if human.get("husband") is not None:
            person = Person.people[human["name"]]
            person.husband = Person.people[human["husband"]]
        if human.get("wife") is not None:
            person = Person.people[human["name"]]
            person.wife = Person.people[human["wife"]]
    return person_list
