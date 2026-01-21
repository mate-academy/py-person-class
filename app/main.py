class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for human in people:
        person = Person(human["name"], human["age"])
        person_list.append(person)

    for human in people:
        person = Person.people[human["name"]]
        if human.get("wife") is not None:
            person.wife = Person.people[human["wife"]]
        elif human.get("husband") is not None:
            person.husband = Person.people[human["husband"]]

    return person_list
