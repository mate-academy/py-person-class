class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for human in people:
        person = Person(human["name"], human["age"])
        if "wife" in human.keys() and human["wife"] is not None:
            person.wife = human["wife"]
        if "husband" in human.keys() and human["husband"] is not None:
            person.husband = human["husband"]
        person_list.append(person)
    for person in person_list:
        if hasattr(person, "wife"):
            # if person.wife is not None:
            for target in person_list:
                if target.name == person.wife:
                    person.wife = target
                    target.husband = person

    return person_list
