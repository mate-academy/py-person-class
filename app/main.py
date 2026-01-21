class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(human["name"], human["age"]) for human in people]

    for human in people:
        person = Person.people[human["name"]]
        if wife_name := human.get("wife"):
            person.wife = Person.people[wife_name]
        elif husband_name := human.get("husband"):
            person.husband = Person.people[husband_name]

    return result
