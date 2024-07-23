class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for someone in people:
        Person(someone["name"], someone["age"])

    for someone in people:
        someone_person = Person.people[someone["name"]]
        if someone.get("wife"):
            someone_person.wife = Person.people.get(someone["wife"])
        if someone.get("husband"):
            someone_person.husband = Person.people.get(someone["husband"])

    return list(Person.people.values())
