class Person:
    people = dict()  # name: Person

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    all_people = [Person(human["name"], human["age"]) for human in people]
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]
    return all_people
