class Person:

    people = {}

    def __init__(self, name: str, age: int, ) -> None:

        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    for human in people:
        Person(human["name"], human["age"])

    for human in people:
        person = Person.people[human["name"]]
        if "wife" in human and human["wife"]:
            person.wife = Person.people[human["wife"]]
        elif "husband" in human and human["husband"]:
            person.husband = Person.people[human["husband"]]

    return [Person.people[human["name"]] for human in people]
