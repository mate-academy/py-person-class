class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []

    for human in people:
        if human["name"] not in Person.people:
            Person(human["name"], human["age"])

    for human in people:
        person = Person.people[human["name"]]

        if human.get("wife") is not None:
            person.wife = Person.people.get(human["wife"])
        elif human.get("husband") is not None:
            person.husband = Person.people.get(human["husband"])

        result.append(person)

    return result
