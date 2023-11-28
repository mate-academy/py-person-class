class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for human in people:
        if wife_name := human.get("wife"):
            Person(human["name"], human["age"]).wife = wife_name
        elif husband_name := human.get("husband"):
            Person(human["name"], human["age"]).husband = husband_name
        else:
            Person(human["name"], human["age"])

    for person in Person.people.values():
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        elif hasattr(person, "husband"):
            person.husband = Person.people[person.husband]

    return list(Person.people.values())
