class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_data = []
    for line in people:
        person_data.append(Person(line["name"], line["age"]))

    for human in people:
        if human.get("wife") is not None:
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        if human.get("husband") is not None:
            Person.people[human["name"]].husband = \
                Person.people[human["husband"]]
    return person_data
