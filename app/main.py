class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for someone in people:
        name = someone["name"]
        age = someone["age"]
        person = Person(name, age)
        person_list.append(person)

    for someone in people:
        if someone.get("wife") is not None:
            Person.people[someone["name"]].wife = \
                Person.people[someone["wife"]]

        if someone.get("husband") is not None:
            Person.people[someone["name"]].husband = \
                Person.people[someone["husband"]]

    return person_list
