class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for human in people:
        person = Person(human["name"], human["age"])
        person_list.append(person)
    for human in people:
        for person in person_list:
            if "wife" in human:
                if human["wife"] is not None:
                    if human["name"] == person.name:
                        person.wife = Person.people[human["wife"]]
            if "husband" in human:
                if human["husband"] is not None:
                    if human["name"] == person.name:
                        person.husband = Person.people[human["husband"]]
    return person_list
