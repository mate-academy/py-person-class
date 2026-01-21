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
        wife = human.get("wife")
        husband = human.get("husband")

        if wife is not None:
            person.wife = Person.people.get(wife)
        elif husband is not None:
            person.husband = Person.people.get(husband)

        result.append(person)

    return result
