class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    for human in people:
        Person(human.get("name"), human.get("age"))
    update_partners(people)
    return list(Person.people.values())


def update_partners(people: list) -> None:
    for human in people:
        person = Person.people.get(human.get("name"))
        if "wife" in human and human["wife"]:
            person.wife = Person.people.get(human["wife"])
        elif "husband" in human and human["husband"]:
            person.husband = Person.people.get(human["husband"])
